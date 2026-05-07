import React, { createContext, useContext, useState, useEffect, useCallback, useRef } from 'react';
import { useAuth } from './AuthContext';

interface NotificationsContextType {
  categoryStatus: Record<string, boolean>;
  refreshStatus: () => Promise<void>;
  refreshCategory: (category: string) => Promise<void>;
  markExit: (category: string) => Promise<void>;
  markItemViewed: (category: string, itemId: string) => Promise<void>;
  markAllRead: (category: string) => Promise<void>;
  /** Registra qué categoría está viendo el usuario actualmente */
  setCategoryActive: (category: string | null) => void;
}

const NotificationsContext = createContext<NotificationsContextType | undefined>(undefined);

export const NotificationsProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { token, user } = useAuth();
  const [categoryStatus, setCategoryStatus] = useState<Record<string, boolean>>({});
  const [activeCategory, setActiveCategory] = useState<string | null>(null);
  const eventSourceRef = useRef<EventSource | null>(null);
  const lastCategoryRef = useRef<string | null>(null);

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

  // Conectar al SSE stream para recibir eventos push cuando el scraper termina
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
        } catch { /* ignore parse errors */ }
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
  }, [token, user]);

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

  // Manejar el cambio de categoría activa con un delay para evitar falsas salidas en remounts
  useEffect(() => {
    const prev = lastCategoryRef.current;
    const current = activeCategory;

    if (prev && prev !== current) {
      // Salimos de prev. Esperamos un poco antes de marcar exit de verdad.
      const timer = setTimeout(() => {
        // Verificamos si seguimos fuera de esa categoría
        setActiveCategory(now => {
          if (now !== prev) {
            markExit(prev);
          }
          return now;
        });
      }, 1500); // 1.5s de gracia para remounts y navegación rápida
      return () => clearTimeout(timer);
    }
    
    lastCategoryRef.current = current;
  }, [activeCategory, markExit]);

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

  const setCategoryActive = useCallback((category: string | null) => {
    setActiveCategory(category);
  }, []);

  // Manejar cierre de pestaña
  useEffect(() => {
    const handleUnload = () => {
      if (activeCategory) {
        markExit(activeCategory);
      }
    };
    window.addEventListener('beforeunload', handleUnload);
    return () => window.removeEventListener('beforeunload', handleUnload);
  }, [activeCategory, markExit]);

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
