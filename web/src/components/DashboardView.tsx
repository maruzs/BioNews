import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import DashboardManager from '../dashboard/DashboardManager';
import type { DashboardConfig } from '../dashboard/types/dashboard';
import { Box, CircularProgress, Typography } from '@mui/material';

interface DashboardViewProps {
  tableName: string;
  title: string;
}

const DashboardView: React.FC<DashboardViewProps> = ({ tableName, title }) => {
  const [data, setData] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const { token } = useAuth();

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const res = await fetch(`/api/data/${tableName}?limit=5000`, {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        const json = await res.json();
        setData(Array.isArray(json) ? json : []);
      } catch (err) {
        console.error("Error fetching data for dashboard:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [tableName, token]);

  const getDashboardConfig = (tableName: string, title: string): DashboardConfig => {
    const baseConfig: DashboardConfig = {
      title: title,
      tableName: tableName,
      dimensions: []
    };

    switch (tableName) {
      case 'normativas':
        baseConfig.dimensions = [
          { key: 'tipo_normativa', label: 'Normativas por Tipo', type: 'relative-bar' },
          { key: 'organismo', label: 'Normativas por Organismo', type: 'bar-horizontal' },
          { key: 'fecha', label: 'Normativas por Año', type: 'grouped-vertical', groupField: 'tipo_normativa' },
          { key: 'region', label: 'Distribución por Región', type: 'bar-horizontal' }
        ];
        break;
      case 'fiscalizaciones':
      case 'sancionatorios':
      case 'medidas_provisionales':
      case 'Tribunales':
        baseConfig.dimensions = [
          { key: tableName === 'Tribunales' ? 'Tribunal' : 'categoria', label: 'Distribución Principal', type: 'bar-horizontal' },
          { key: 'region', label: 'Distribución por Región', type: 'bar-horizontal' },
          { key: tableName === 'Tribunales' ? 'Estado_Procesal' : 'estado', label: 'Estado', type: 'pie' },
          { key: tableName === 'Tribunales' ? 'Fecha' : 'expediente', label: 'Evolución Temporal', type: 'grouped-vertical' }
        ];
        break;
      default:
        baseConfig.dimensions = [
          { key: 'estado', label: 'Distribución por Estado', type: 'pie' },
          { key: 'region', label: 'Distribución por Región', type: 'bar-horizontal' },
        ];
    }
    return baseConfig;
  };

  if (loading) {
    return (
      <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', py: 8 }}>
        <CircularProgress size={40} sx={{ mb: 2 }} />
        <Typography variant="body2" color="text.secondary">Cargando datos del dashboard...</Typography>
      </Box>
    );
  }

  if (!data || data.length === 0) {
    return (
      <Box sx={{ textAlign: 'center', py: 8, border: '1px dashed', borderColor: 'divider', borderRadius: 4 }}>
        <Typography color="text.secondary">No hay datos disponibles para generar el dashboard de {title}</Typography>
      </Box>
    );
  }

  return (
    <DashboardManager
      data={data}
      config={getDashboardConfig(tableName, title)}
    />
  );
};

export default DashboardView;
