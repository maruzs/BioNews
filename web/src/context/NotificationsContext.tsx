import React, { createContext, useContext, useState, useEffect, useCallback, useRef } from 'react';
import { useAuth } from './AuthContext';

interface NotificationsContextType {
  categoryStatus: Record<string, boolean>;
  refreshStatus: () => Promise<void>;
  refreshCategory: (category: string) => Promise<void>;
  markExit: (category: string) => Promise<void>;
  markItemViewed: (category: string, itemId: string) => Promise<void>;
  markAllRead: (category: string) => Promise<void>;
  /** Notifica que el usuario entró o salió de una vista de categoría */
  setCategoryActive: (category: string, isActive: boolean) => void;
}

const NotificationsContext = createContext<NotificationsContextType | undefined>(undefined);

export const NotificationsProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { token, user } = useAuth();
  const [categoryStatus, setCategoryStatus] = useState<Record<string, boolean>>({});
  const eventSourceRef = useRef<EventSource | null>(null);
  
  // Ref para rastrear qué categorías están "vivas" en el DOM actualmente
  const mountedCategories = useRef<Set<string>>(new Set());

  const refreshStatus = useCallback(async () => {
    if (!token) return;
    try {
      const res = await fetch('/api/notifications/status', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setCategoryStatus(data);
      }
    } catch (error) {
      console.error("Error refreshing notification status:", error);
    }
  }, [token]);

  const refreshCategory = useCallback(async (category: string) => {
    if (!token) return;
    try {
      const res = await fetch(`/api/notifications/status/${category}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setCategoryStatus(prev => ({ ...prev, [category]: data.has_new }));
      }
    } catch (error) {
      console.error(`Error refreshing category ${category}:`, error);
    }
  }, [token]);

  // Conectar al SSE stream
  useEffect(() => {
    if (!token || !user) {
      if (eventSourceRef.current) {
        eventSourceRef.current.close();
        eventSourceRef.current = null;
      }
      setCategoryStatus({});
      return;
    }

    refreshStatus();

    const connectSSE = () => {
      if (eventSourceRef.current) {
        eventSourceRef.current.close();
      }
      const es = new EventSource(`/api/notifications/stream?token=${encodeURIComponent(token)}`);
      eventSourceRef.current = es;
      es.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          if (data.type === 'new_content' && data.category) {
            setCategoryStatus(prev => ({ ...prev, [data.category]: true }));
          }
        } catch { /* ignore */ }
      };
      es.onerror = () => {
        es.close();
        eventSourceRef.current = null;
        setTimeout(connectSSE, 5000);
      };
    };

    connectSSE();

    return () => {
      if (eventSourceRef.current) {
        eventSourceRef.current.close();
        eventSourceRef.current = null;
      }
    };
  }, [token, user, refreshStatus]);

  const markExit = useCallback(async (category: string) => {
    if (!token) return;
    try {
      const res = await fetch('/api/notifications/exit', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ category }),
        keepalive: true
      });
      if (res.ok) {
        setCategoryStatus(prev => ({ ...prev, [category]: false }));
      }
    } catch (error) {
      console.error("Error marking category exit:", error);
    }
  }, [token]);

  const setCategoryActive = useCallback((category: string, isActive: boolean) => {
    if (isActive) {
      mountedCategories.current.add(category);
    } else {
      mountedCategories.current.delete(category);
      // Esperar un poco para confirmar que el usuario realmente salió y no fue un re-mount de React
      setTimeout(() => {
        if (!mountedCategories.current.has(category)) {
          console.log(`[Notifications] Marcando salida genuina de ${category}`);
          markExit(category);
        }
      }, 600);
    }
  }, [markExit]);

  const markItemViewed = useCallback(async (category: string, itemId: string) => {
    if (!token) return;
    try {
      await fetch('/api/notifications/view-item', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ category, item_id: itemId }),
        keepalive: true
      });
    } catch (error) {
      console.error("Error marking item viewed:", error);
    }
  }, [token]);

  const markAllRead = useCallback(async (category: string) => {
    if (!token) return;
    try {
      const res = await fetch('/api/notifications/exit', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ category }),
        keepalive: true
      });
      if (res.ok) {
        setCategoryStatus(prev => ({ ...prev, [category]: false }));
      }
    } catch (error) {
      console.error("Error marking all as read:", error);
    }
  }, [token]);

  // Manejar cierre de pestaña/navegador para todas las categorías activas
  useEffect(() => {
    const handleUnload = () => {
      mountedCategories.current.forEach(cat => {
        markExit(cat);
      });
    };
    window.addEventListener('beforeunload', handleUnload);
    return () => window.removeEventListener('beforeunload', handleUnload);
  }, [markExit]);

  return (
    <NotificationsContext.Provider value={{ 
      categoryStatus, 
      refreshStatus, 
      refreshCategory, 
      markExit, 
      markItemViewed, 
      markAllRead,
      setCategoryActive
    }}>
      {children}
    </NotificationsContext.Provider>
  );
};

export const useNotifications = () => {
  const context = useContext(NotificationsContext);
  if (context === undefined) {
    throw new Error('useNotifications must be used within a NotificationsProvider');
  }
  return context;
};
