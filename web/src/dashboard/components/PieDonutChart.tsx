import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from 'recharts';
import { Box } from '@mui/material';
import { useTheme, alpha } from '@mui/material/styles';
import { useDashboardStore } from '../store/dashboardStore';
import { useDashboardTheme, getColorForValue } from '../utils/dashboardTheme';
import DashboardTooltip from './DashboardTooltip';
import DashboardLegend from './DashboardLegend';

interface PieDonutChartProps {
  data: { name: string; count: number; percentage?: number }[];
  filterKey: string;
}

const PieDonutChart: React.FC<PieDonutChartProps> = ({ data, filterKey }) => {
  const { filters, toggleFilter } = useDashboardStore();
  const { colors } = useDashboardTheme();
  const theme = useTheme();
  const activeValue = filters[filterKey as keyof typeof filters];

  return (
    <ResponsiveContainer width="100%" height="100%">
      <PieChart>
        <Pie
          data={data}
          cx="50%"
          cy="45%"
          innerRadius="60%"
          outerRadius="85%"
          paddingAngle={4}
          dataKey="count"
          onClick={(entry) => toggleFilter(filterKey as any, entry.name ?? null)}
          style={{ cursor: 'pointer', outline: 'none' }}
        >
          {data.map((entry, index) => {
            const color = getColorForValue(entry.name, colors);
            const isSelected = activeValue === entry.name;
            const isAnySelected = activeValue !== undefined && activeValue !== null;
            
            return (
              <Cell 
                key={`cell-${index}`} 
                fill={color} 
                stroke={isSelected ? color : 'none'}
                strokeWidth={4}
                opacity={isAnySelected && !isSelected ? 0.3 : 1}
                style={{
                  filter: isSelected ? `drop-shadow(0 0 8px ${alpha(color, 0.5)})` : 'none',
                  transition: 'all 0.3s ease'
                }}
              />
            );
          })}
        </Pie>
        <Tooltip content={<DashboardTooltip />} />
        <Legend content={<DashboardLegend />} />
      </PieChart>
    </ResponsiveContainer>
  );
};

export default PieDonutChart;
