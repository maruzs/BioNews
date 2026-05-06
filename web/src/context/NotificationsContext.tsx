import React, { createContext, useContext, useState, useEffect, useCallback, useRef } from 'react';
import { useAuth } from './AuthContext';

interface NotificationsContextType {
  categoryStatus: Record<string, boolean>;
  refreshStatus: () => Promise<void>;
  markExit: (category: string) => Promise<void>;
  markItemViewed: (category: string, itemId: string) => Promise<void>;
}

const NotificationsContext = createContext<NotificationsContextType | undefined>(undefined);

export const NotificationsProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { token, user } = useAuth();
  const [categoryStatus, setCategoryStatus] = useState<Record<string, boolean>>({});
  const socketRef = useRef<WebSocket | null>(null);

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

  useEffect(() => {
    if (token && user) {
      refreshStatus();

      // Fetch polling interval and start polling
      let intervalId: any;
      
      const startPolling = async () => {
        try {
          const configRes = await fetch('/api/config/notifications');
          const config = await configRes.json();
          const intervalMs = (config.interval || 15) * 1000;
          
          intervalId = setInterval(() => {
            refreshStatus();
          }, intervalMs);
        } catch (error) {
          console.error("Error fetching notification config, falling back to 15s:", error);
          intervalId = setInterval(() => {
            refreshStatus();
          }, 15000);
        }
      };

      startPolling();

      return () => {
        if (intervalId) clearInterval(intervalId);
      };
    } else {
      setCategoryStatus({});
    }
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
        body: JSON.stringify({ category })
      });
      if (res.ok) {
        setCategoryStatus(prev => ({ ...prev, [category]: false }));
      }
    } catch (error) {
      console.error("Error marking category exit:", error);
    }
  }, [token]);

  const markItemViewed = useCallback(async (category: string, itemId: string) => {
    if (!token) return;
    try {
      await fetch('/api/notifications/view-item', {
        method: 'POST',
        headers: { 
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ category, item_id: itemId })
      });
      // No actualizamos categoryStatus aquí necesariamente, 
      // el punto rojo solo se quita al entrar/salir de la categoría según la regla.
      // O si era el último ítem, pero eso lo calcula el backend mejor en refreshStatus si queremos precisión absoluta.
    } catch (error) {
      console.error("Error marking item viewed:", error);
    }
  }, [token]);

  return (
    <NotificationsContext.Provider value={{ categoryStatus, refreshStatus, markExit, markItemViewed }}>
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
