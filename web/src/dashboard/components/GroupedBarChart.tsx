import React from 'react';
import { 
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, 
  ResponsiveContainer, Cell 
} from 'recharts';
import { Box, useTheme } from '@mui/material';
import { useDashboardStore } from '../store/dashboardStore';
import { useDashboardTheme, getColorForValue } from '../utils/dashboardTheme';
import DashboardTooltip from './DashboardTooltip';
import DashboardLegend from './DashboardLegend';

interface GroupedBarChartProps {
  data: any[];
  xAxisKey: string;
  groupField?: string;
  filterKey: string;
}

const GroupedBarChart: React.FC<GroupedBarChartProps> = ({ 
  data, 
  xAxisKey, 
  groupField,
  filterKey
}) => {
  const { colors } = useDashboardTheme();
  const { filters, toggleFilter } = useDashboardStore();
  const theme = useTheme();
  
  const activeValue = filters[filterKey as keyof typeof filters];

  // Get all unique keys for the grouped bars
  const keys = React.useMemo(() => {
    if (!groupField) return ['count'];
    const keySet = new Set<string>();
    data.forEach(item => {
      Object.keys(item).forEach(k => {
        if (k !== xAxisKey && k !== 'name' && k !== 'total') {
          keySet.add(k);
        }
      });
    });
    return Array.from(keySet).sort();
  }, [data, xAxisKey, groupField]);


  return (
    <ResponsiveContainer width="100%" height="100%">
      <BarChart data={data} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
        <CartesianGrid strokeDasharray="3 3" vertical={false} stroke={theme.palette.divider} />
        <XAxis 
          dataKey={xAxisKey} 
          axisLine={false} 
          tickLine={false}
          tick={{ fontSize: 11, fill: theme.palette.text.secondary }}
        />
        <YAxis 
          axisLine={false} 
          tickLine={false}
          tick={{ fontSize: 11, fill: theme.palette.text.secondary }}
        />
        <Tooltip content={<DashboardTooltip />} cursor={{ fill: 'rgba(0,0,0,0.03)' }} />
        <Legend content={<DashboardLegend />} />
        {keys.map((key) => (
          <Bar 
            key={key} 
            dataKey={key} 
            name={key}
            fill={getColorForValue(key, colors)} 
            radius={[4, 4, 0, 0]}
            stackId={groupField ? 'a' : undefined}
            onClick={(entry: any) => toggleFilter(filterKey as any, entry[xAxisKey])}
            style={{ cursor: 'pointer' }}
          >
            {data.map((entry, index) => (
              <Cell 
                key={`cell-${index}`}
                opacity={activeValue && activeValue !== entry[xAxisKey] ? 0.3 : 1}
                style={{ transition: 'all 0.3s ease' }}
              />
            ))}
          </Bar>
        ))}
      </BarChart>
    </ResponsiveContainer>
  );
};

export default GroupedBarChart;
