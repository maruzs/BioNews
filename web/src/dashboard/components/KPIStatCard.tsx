import React from 'react';
import { Box, Paper, Typography } from '@mui/material';
import { alpha } from '@mui/material/styles';
import { motion } from 'framer-motion';
import type { LucideIcon } from 'lucide-react';

interface KPIStatCardProps {
  title: string;
  value: string | number;
  icon: LucideIcon;
  color?: string;
  subtitle?: string;
  trend?: {
    value: number;
    isPositive: boolean;
  };
}

const KPIStatCard: React.FC<KPIStatCardProps> = ({
  title,
  value,
  icon: Icon,
  color = 'primary.main',
  subtitle,
  trend
}) => {
  return (
    <Box
      component={motion.div}
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.3 }}
      sx={{ height: '100%' }}
    >
      <Paper
        elevation={0}
        sx={{
          p: 3,
          height: '100%',
          borderRadius: 4,
          border: '1px solid',
          borderColor: 'divider',
          display: 'flex',
          alignItems: 'center',
          gap: 3,
          position: 'relative',
          overflow: 'hidden',
          transition: 'all 0.3s ease',
          '&:hover': {
            boxShadow: '0 8px 16px -4px rgba(0,0,0,0.08)',
            transform: 'translateY(-2px)',
          }
        }}
      >
        <Box
          sx={{
            width: 56,
            height: 56,
            borderRadius: 3,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            bgcolor: (theme) => {
              const baseColor = color.includes('.') ?
                (theme.palette as any)[color.split('.')[0]][color.split('.')[1]] :
                color;
              return alpha(baseColor, 0.1);
            },
            color: color
          }}
        >
          <Icon size={28} />
        </Box>

        <Box sx={{ flexGrow: 1 }}>
          <Typography variant="caption" sx={{ fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase', letterSpacing: 1 }}>
            {title}
          </Typography>
          <Typography variant="h4" sx={{ fontWeight: 800, my: 0.5 }}>
            {value}
          </Typography>
          {subtitle && (
            <Typography variant="caption" sx={{ color: 'text.secondary', display: 'block' }}>
              {subtitle}
            </Typography>
          )}
          {trend && (
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5, mt: 0.5 }}>
              <Typography
                variant="caption"
                sx={{ fontWeight: 700, color: trend.isPositive ? 'success.main' : 'error.main' }}
              >
                {trend.isPositive ? '+' : '-'}{trend.value}%
              </Typography>
              <Typography variant="caption" sx={{ color: 'text.secondary' }}>
                vs anterior
              </Typography>
            </Box>
          )}
        </Box>

        {/* Decorative background circle */}
        <Box sx={{
          position: 'absolute',
          right: -20,
          top: -20,
          width: 100,
          height: 100,
          borderRadius: '50%',
          bgcolor: (theme) => {
            const baseColor = color.includes('.') ?
              (theme.palette as any)[color.split('.')[0]][color.split('.')[1]] :
              color;
            return alpha(baseColor, 0.03);
          }
        }} />
      </Paper>
    </Box>
  );
};

export default KPIStatCard;
