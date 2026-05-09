import React, { useState, useMemo } from 'react';
import { Box, Grid, Typography, Button, Stack } from '@mui/material';
import { useTheme, alpha } from '@mui/material/styles';
import { LayoutDashboard, FilterX, Download, ExternalLink, RefreshCcw } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

import { useDashboardStore } from './store/dashboardStore';
import { useDashboardFilters } from './hooks/useDashboardFilters';
import { aggregateData, exportToImage } from './utils/chartHelpers';
import type { DashboardConfig } from './types/dashboard';

import DashboardCard from './components/DashboardCard';
import KPIStatCard from './components/KPIStatCard';
import RelativeBarPanel from './components/RelativeBarPanel';
import PieDonutChart from './components/PieDonutChart';
import GroupedBarChart from './components/GroupedBarChart';
import DashboardModal from './components/DashboardModal';

interface DashboardManagerProps {
  data: any[];
  config: DashboardConfig;
}

const DashboardManager: React.FC<DashboardManagerProps> = ({ data, config }) => {
  const { filteredData, activeFilters } = useDashboardFilters(data);
  //const { clearFilters, toggleFilter } = useDashboardStore(); // NO BORRAR ESTA LINEA, ES UN RESPALDO POR SI LUEGO NO FUNCIONA EL CAMBIO
  const { clearFilters } = useDashboardStore(); // toggleFilter eliminado
  const [expandedChart, setExpandedChart] = useState<{ idx: number; dim: any } | null>(null);
  //const theme = useTheme(); // NO BORRAR ESTA LINEA, ES UN RESPALDO POR SI LUEGO NO FUNCIONA EL CAMBIO

  const isFiltered = Object.keys(activeFilters).length > 0;

  const renderChart = (dim: any, height: number | string = '100%') => {
    const chartData = aggregateData(filteredData, dim);

    switch (dim.type) {
      case 'relative-bar':
        return (
          <RelativeBarPanel
            title={dim.label}
            data={chartData}
            filterKey={dim.key}
          />
        );
      case 'pie':
        return (
          <PieDonutChart
            data={chartData}
            filterKey={dim.key}
          />
        );
      case 'grouped-vertical':
        return (
          <GroupedBarChart
            data={chartData}
            xAxisKey="name"
            groupField={dim.groupField}
            filterKey={dim.key}
          />
        );
      case 'bar-horizontal':
        return (
          <GroupedBarChart
            data={chartData}
            xAxisKey="name"
            filterKey={dim.key}
          />
        );
      default:
        return <Typography>Tipo de gráfico no soportado: {dim.type}</Typography>;
    }
  };

  return (
    <Box sx={{ width: '100%', py: 2 }}>
      {/* Header section with glassmorphism feel */}
      <Box
        component={motion.div}
        {...({
          initial: { opacity: 0, y: -20 },
          animate: { opacity: 1, y: 0 }
        } as any)}
        sx={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          mb: 4,
          p: 3,
          borderRadius: 4,
          bgcolor: (theme) => theme.palette.mode === 'dark' ? 'rgba(255,255,255,0.02)' : 'rgba(0,0,0,0.01)',
          border: '1px solid',
          borderColor: 'divider',
        }}
      >
        <Box>
          <Typography variant="h5" sx={{ fontWeight: 800, color: 'text.primary', mb: 0.5 }}>
            {config.title}
          </Typography>
          <Typography variant="body2" sx={{ color: 'text.secondary', fontWeight: 500 }}>
            Análisis interactivo de datos con filtros cruzados inteligentes
          </Typography>
        </Box>

        <Stack direction="row" spacing={2}>
          {isFiltered && (
            <Button
              variant="outlined"
              color="inherit"
              startIcon={<RefreshCcw size={18} />}
              onClick={clearFilters}
              sx={{
                borderRadius: 3,
                px: 3,
                textTransform: 'none',
                fontWeight: 700,
                bgcolor: 'background.paper',
                border: '1px solid',
                borderColor: 'divider',
                '&:hover': {
                  bgcolor: (theme) => alpha(theme.palette.error.main, 0.05),
                  borderColor: 'error.light',
                  color: 'error.main'
                }
              }}
            >
              Limpiar Filtros ({Object.keys(activeFilters).length})
            </Button>
          )}
        </Stack>
      </Box>

      {/* KPI Section */}
      <Grid container spacing={3} sx={{ mb: 4 }}>
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <KPIStatCard
            title="Total de Registros"
            value={filteredData.length.toLocaleString()}
            icon={LayoutDashboard}
            subtitle={isFiltered ? `De un total de ${data.length.toLocaleString()}` : 'Base de datos completa'}
            trend={isFiltered ? { value: Math.round((filteredData.length / data.length) * 100), isPositive: true } : undefined}
          />
        </Grid>
      </Grid>

      {/* Charts Grid */}
      <Grid container spacing={3}>
        <AnimatePresence mode="popLayout">
          {config.dimensions.map((dim, idx) => (
            <Grid 
              component={motion.div}
              size={{ xs: 12, md: dim.type === 'grouped-vertical' ? 12 : 6 }} 
              key={`${dim.key}-${idx}`}
              {...({
                layout: true,
                initial: { opacity: 0, scale: 0.9 },
                animate: { opacity: 1, scale: 1 },
                exit: { opacity: 0, scale: 0.9 },
                transition: { duration: 0.2 }
              } as any)}
            >
            <DashboardCard
              title={dim.label}
              span={dim.type === 'grouped-vertical' ? 2 : 1}
              onExpand={() => setExpandedChart({ idx, dim })}
              onExport={(format) => exportToImage(`chart-${idx}`, dim.label, format)}
              height={dim.type === 'relative-bar' ? 'auto' : 350}
            >
              <Box id={`chart-${idx}`} sx={{ width: '100%', height: '100%', minHeight: dim.type === 'relative-bar' ? 0 : 300 }}>
                {renderChart(dim)}
              </Box>
            </DashboardCard>
          </Grid>
        ))}
        </AnimatePresence>
      </Grid>

      {/* Expansion Modal */}
      <DashboardModal
        open={!!expandedChart}
        onClose={() => setExpandedChart(null)}
        title={expandedChart?.dim.label || ''}
        onExport={(format) => expandedChart && exportToImage('expanded-chart', expandedChart.dim.label, format)}
      >
        <Box id="expanded-chart" sx={{ width: '100%', height: 500 }}>
          {expandedChart && renderChart(expandedChart.dim, 500)}
        </Box>
      </DashboardModal>
    </Box>
  );
};

export default DashboardManager;
