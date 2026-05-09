import React from 'react';
import { Box, Typography, Tooltip as MuiTooltip } from '@mui/material';
import { motion, AnimatePresence } from 'framer-motion';
import { useDashboardStore } from '../store/dashboardStore';
import { useDashboardTheme } from '../utils/dashboardTheme';
import { getColorForValue } from '../utils/dashboardTheme';

interface RelativeBarPanelProps {
  title: string;
  data: { name: string; count: number; percentage?: number }[];
  filterKey: string;
}

const RelativeBarPanel: React.FC<RelativeBarPanelProps> = ({ data, filterKey }) => {
  const { filters, toggleFilter } = useDashboardStore();
  const { colors } = useDashboardTheme();
  
  const activeValue = filters[filterKey as keyof typeof filters];
  const maxCount = Math.max(...data.map(d => d.count), 1);

  return (
    <Box sx={{ width: '100%', display: 'flex', flexDirection: 'column', gap: 1.5 }}>
      <AnimatePresence>
        {data.map((item) => {
          const isSelected = activeValue === item.name;
          const isAnySelected = activeValue !== undefined && activeValue !== null;
          const color = getColorForValue(item.name, colors);
          const relativeWidth = (item.count / maxCount) * 100;

          return (
            <Box 
              key={item.name}
              onClick={() => toggleFilter(filterKey as any, item.name)}
              sx={{ 
                cursor: 'pointer',
                opacity: isAnySelected && !isSelected ? 0.4 : 1,
                transition: 'all 0.3s ease',
                '&:hover': {
                  transform: 'translateX(4px)',
                  opacity: 1
                }
              }}
            >
              <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.5 }}>
                <Typography 
                  variant="body2" 
                  sx={{ 
                    fontWeight: isSelected ? 700 : 500,
                    fontSize: '0.85rem',
                    color: isSelected ? 'primary.main' : 'text.primary',
                    whiteSpace: 'nowrap',
                    overflow: 'hidden',
                    textOverflow: 'ellipsis',
                    maxWidth: '80%'
                  }}
                >
                  {item.name}
                </Typography>
                <Typography variant="body2" sx={{ fontWeight: 700, color: 'text.secondary', fontSize: '0.85rem' }}>
                  {item.count.toLocaleString()}
                </Typography>
              </Box>
              
              <MuiTooltip 
                title={`${item.name}: ${item.count} (${item.percentage ?? 0}%)`} 
                arrow 
                placement="top"
              >
                <Box sx={{ 
                  height: 12, 
                  width: '100%', 
                  bgcolor: (theme) => theme.palette.mode === 'dark' ? 'rgba(255,255,255,0.05)' : 'rgba(0,0,0,0.03)',
                  borderRadius: 6,
                  overflow: 'hidden',
                  position: 'relative'
                }}>
                  <motion.div
                    initial={{ width: 0 }}
                    animate={{ width: `${relativeWidth}%` }}
                    transition={{ duration: 0.8, ease: "easeOut" }}
                    style={{
                      height: '100%',
                      backgroundColor: isSelected ? color : color,
                      borderRadius: 6,
                      boxShadow: isSelected ? `0 0 12px ${color}80` : 'none'
                    }}
                  />
                </Box>
              </MuiTooltip>
            </Box>
          );
        })}
      </AnimatePresence>
    </Box>
  );
};

export default RelativeBarPanel;
