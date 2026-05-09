import React from 'react';
import { Box, Paper, Typography, IconButton, Tooltip } from '@mui/material';
import { Maximize2, Download, ExternalLink } from 'lucide-react';
import { motion } from 'framer-motion';

interface DashboardCardProps {
  title: string;
  children: React.ReactNode;
  onExpand?: () => void;
  onExport?: (format: 'png' | 'svg') => void;
  onOpenPage?: () => void;
  height?: number | string;
  span?: number;
}

const DashboardCard: React.FC<DashboardCardProps> = ({
  title,
  children,
  onExpand,
  onExport,
  onOpenPage,
  height = 400,
  span = 1
}) => {
  return (
    <Box
      component={motion.div}
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      sx={{
        gridColumn: { xs: 'span 1', md: `span ${span}` },
        height: '100%'
      }}
    >
      <Paper
        elevation={0}
        sx={{
          height: '100%',
          display: 'flex',
          flexDirection: 'column',
          borderRadius: 4,
          border: '1px solid',
          borderColor: 'divider',
          overflow: 'hidden',
          transition: 'all 0.3s ease',
          '&:hover': {
            boxShadow: '0 12px 24px -10px rgba(0,0,0,0.1)',
            borderColor: 'primary.light',
          }
        }}
      >
        <Box
          sx={{
            p: 2,
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            borderBottom: '1px solid',
            borderColor: 'divider',
            background: (theme) => alpha(theme.palette.primary.main, 0.03)
          }}
        >
          <Typography variant="subtitle1" sx={{ fontWeight: 700, color: 'text.primary' }}>
            {title}
          </Typography>
          <Box sx={{ display: 'flex', gap: 0.5 }}>
            {onExport && (
              <Tooltip title="Exportar">
                <IconButton size="small" onClick={() => onExport('png')}>
                  <Download size={16} />
                </IconButton>
              </Tooltip>
            )}
            {onOpenPage && (
              <Tooltip title="Abrir en página">
                <IconButton size="small" onClick={onOpenPage}>
                  <ExternalLink size={16} />
                </IconButton>
              </Tooltip>
            )}
            {onExpand && (
              <Tooltip title="Expandir">
                <IconButton size="small" onClick={onExpand}>
                  <Maximize2 size={16} />
                </IconButton>
              </Tooltip>
            )}
          </Box>
        </Box>
        <Box sx={{ p: 2, flexGrow: 1, height }}>
          {children}
        </Box>
      </Paper>
    </Box>
  );
};

// Helper function to simulate alpha since it's not directly available in standard CSS objects here
function alpha(color: string, opacity: number) {
  return `${color}${Math.round(opacity * 255).toString(16).padStart(2, '0')}`;
}

export default DashboardCard;
