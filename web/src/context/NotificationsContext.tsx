import React, { createContext, useContext, useState, useEffect, useCallback } from 'react';
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
      let timeoutId: number | undefined;

      const poll = async () => {
        try {
          const configRes = await fetch('/api/config/notifications');
          const config = await configRes.json();
          const intervalSeconds = config.interval || 15;

          await refreshStatus();

          timeoutId = setTimeout(poll, intervalSeconds * 1000);
        } catch (error) {
          console.error("Error in polling loop:", error);
          timeoutId = setTimeout(poll, 15000);
        }
      };

      poll();

      return () => {
        if (timeoutId) clearTimeout(timeoutId);
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
