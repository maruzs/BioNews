import { useTheme, alpha } from '@mui/material/styles';

export const useDashboardTheme = () => {
  const theme = useTheme();
  const isDark = theme.palette.mode === 'dark';

  const chartColors = [
    theme.palette.primary.main,
    theme.palette.secondary.main,
    '#f59e0b', // Amber
    '#10b981', // Emerald
    '#ec4899', // Pink
    '#8b5cf6', // Violet
    '#f97316', // Orange
    '#06b6d4', // Cyan
    '#ef4444', // Red
    '#84cc16', // Lime
  ];

  const getAlphaColor = (color: string, opacity: number) => alpha(color, opacity);

  return {
    colors: chartColors,
    text: theme.palette.text.primary,
    secondaryText: theme.palette.text.secondary,
    background: theme.palette.background.paper,
    border: theme.palette.divider,
    isDark,
    getAlphaColor,
    muiTheme: theme,
  };
};

// Global color cache to keep categories consistent across different charts
const colorCache: Record<string, string> = {};
let colorIndex = 0;

export const getColorForValue = (value: string, palette: string[]) => {
  if (colorCache[value]) return colorCache[value];
  const color = palette[colorIndex % palette.length];
  colorCache[value] = color;
  colorIndex++;
  return color;
};
