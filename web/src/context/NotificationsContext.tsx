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

  // Cargar estado UNA SOLA VEZ al iniciar sesión / montar el componente
  // No hay polling ni WebSocket: las notificaciones se refrescan solo
  // al navegar entre categorías (markExit actualiza el estado local)
  useEffect(() => {
    if (token && user) {
      refreshStatus();
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
      // No actualizamos categoryStatus aquí.
      // El punto rojo se quita al salir de la categoría (markExit).
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
