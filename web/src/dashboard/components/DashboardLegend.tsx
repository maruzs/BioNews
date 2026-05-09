import React from 'react';
import { Box, Typography } from '@mui/material';

interface DashboardLegendProps {
  payload?: any[];
}

const DashboardLegend: React.FC<DashboardLegendProps> = ({ payload }) => {
  if (!payload) return null;

  return (
    <Box
      sx={{
        display: 'flex',
        flexWrap: 'wrap',
        justifyContent: 'center',
        gap: 2,
        mt: 2,
        px: 2
      }}
    >
      {payload.map((entry, index) => (
        <Box
          key={`item-${index}`}
          sx={{
            display: 'flex',
            alignItems: 'center',
            gap: 0.75,
            cursor: 'default'
          }}
        >
          <Box
            sx={{
              width: 10,
              height: 10,
              borderRadius: '50%',
              bgcolor: entry.color,
              flexShrink: 0
            }}
          />
          <Typography
            variant="caption"
            sx={{
              fontWeight: 600,
              color: 'text.secondary',
              fontSize: '0.7rem',
              whiteSpace: 'nowrap'
            }}
          >
            {entry.value}
          </Typography>
        </Box>
      ))}
    </Box>
  );
};

export default DashboardLegend;
