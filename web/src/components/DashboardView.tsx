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
          { key: 'organismo', label: 'Normativas por Organismo', type: 'relative-bar' },
          { key: 'fecha', label: 'Normativas por Año y Tipo', type: 'grouped-vertical' }, // Desacopladas
          { key: 'region', label: 'Distribución por Región', type: 'relative-bar' }
        ];
        break;
      case 'fiscalizaciones':
      case 'sancionatorios':
        baseConfig.dimensions = [
          { key: 'categoria', label: 'Distribución Principal', type: 'relative-bar' },
          { key: 'region', label: 'Distribución por Región', type: 'relative-bar' },
          { key: 'estado', label: 'Estado', type: 'pie' },
          { key: 'expediente', label: 'Evolución Temporal', type: 'grouped-vertical' }
        ];
        break;
      case 'registroSanciones':
        baseConfig.dimensions = [
          { key: 'categoria', label: 'Distribución Principal', type: 'relative-bar' },
          { key: 'region', label: 'Distribución por Región', type: 'relative-bar' },
          { key: 'pago_multa', label: 'Multas', type: 'pie' },
          { key: 'expediente', label: 'Evolución Temporal', type: 'grouped-vertical' }
        ];
        break;
      case 'medidas_provisionales':
      case 'programasDeCumplimiento':
      case 'requerimientos':
        baseConfig.dimensions = [
          { key: 'categoria', label: 'Distribución Principal', type: 'relative-bar' },
          { key: 'region', label: 'Distribución por Región', type: 'relative-bar' },
          { key: 'expediente', label: 'Evolución Temporal', type: 'grouped-vertical' }
        ];
        break;
      case 'Tribunales':
        baseConfig.dimensions = [
          { key: 'Tribunal', label: 'Distribución Principal', type: 'relative-bar' },
          { key: 'region', label: 'Distribución por Región', type: 'relative-bar' },
          { key: 'Estado_Procesal', label: 'Estado', type: 'pie' },
          { key: 'Fecha', label: 'Evolución Temporal', type: 'grouped-vertical' }
        ];
        break;
      default:
        baseConfig.dimensions = [
          { key: 'estado', label: 'Distribución por Estado', type: 'pie' },
          { key: 'region', label: 'Distribución por Región', type: 'relative-bar' },
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
