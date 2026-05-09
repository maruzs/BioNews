import React from 'react';
import { Box, Typography, Paper, useTheme } from '@mui/material';

interface DashboardTooltipProps {
  active?: boolean;
  payload?: any[];
  label?: string;
  valueFormatter?: (value: any) => string;
}

const DashboardTooltip: React.FC<DashboardTooltipProps> = ({
  active,
  payload,
  label,
  valueFormatter
}) => {
  const theme = useTheme();

  if (active && payload && payload.length) {
    return (
      <Paper
        elevation={4}
        sx={{
          p: 1.5,
          borderRadius: 2,
          border: '1px solid',
          borderColor: 'divider',
          bgcolor: 'background.paper',
          minWidth: 150
        }}
      >
        {label && (
          <Typography variant="subtitle2" sx={{ fontWeight: 800, mb: 1, borderBottom: '1px solid', borderColor: 'divider', pb: 0.5 }}>
            {label}
          </Typography>
        )}
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 0.5 }}>
          {payload.map((entry, index) => (
            <Box key={index} sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', gap: 2 }}>
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                <Box sx={{ width: 10, height: 10, borderRadius: '50%', bgcolor: entry.color || entry.fill }} />
                <Typography variant="caption" sx={{ fontWeight: 500, color: 'text.secondary' }}>
                  {entry.name}:
                </Typography>
              </Box>
              <Typography variant="caption" sx={{ fontWeight: 700, color: 'text.primary' }}>
                {valueFormatter ? valueFormatter(entry.value) : entry.value.toLocaleString()}
                {entry.payload?.percentage !== undefined ? ` (${entry.payload.percentage}%)` : ''}
              </Typography>
            </Box>
          ))}
        </Box>
      </Paper>
    );
  }

  return null;
};

export default DashboardTooltip;
