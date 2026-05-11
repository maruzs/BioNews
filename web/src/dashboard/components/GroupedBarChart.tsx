import React from 'react';
import { 
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, 
  ResponsiveContainer, Cell 
} from 'recharts';
import { useTheme } from '@mui/material';
import { useDashboardStore } from '../store/dashboardStore';
import { useDashboardTheme, getColorForValue } from '../utils/dashboardTheme';
import DashboardTooltip from './DashboardTooltip';
import DashboardLegend from './DashboardLegend';

interface GroupedBarChartProps {
  data: any[];
  xAxisKey: string;
  groupField?: string;
  filterKey: string;
  layout?: 'horizontal' | 'vertical';
}

const GroupedBarChart: React.FC<GroupedBarChartProps> = ({ 
  data, 
  xAxisKey, 
  groupField,
  filterKey,
  layout = 'horizontal'
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
      <BarChart data={data} layout={layout} margin={{ top: 10, right: 30, left: layout === 'vertical' ? 100 : 0, bottom: 0 }}>
        <CartesianGrid strokeDasharray="3 3" vertical={layout !== 'vertical'} horizontal={layout !== 'horizontal'} stroke={theme.palette.divider} />
        {layout === 'horizontal' ? (
          <>
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
          </>
        ) : (
          <>
            <XAxis 
              type="number"
              axisLine={false} 
              tickLine={false}
              tick={{ fontSize: 11, fill: theme.palette.text.secondary }}
              hide={true}
            />
            <YAxis 
              type="category"
              dataKey={xAxisKey} 
              axisLine={false} 
              tickLine={false}
              tick={{ fontSize: 11, fill: theme.palette.text.secondary }}
              width={150}
            />
          </>
        )}
        <Tooltip content={<DashboardTooltip />} cursor={{ fill: 'rgba(0,0,0,0.03)' }} />
        {keys.length > 1 || (keys.length === 1 && keys[0] !== 'count') ? <Legend content={<DashboardLegend />} /> : null}
        {keys.map((key) => (
          <Bar 
            key={key} 
            dataKey={key} 
            name={key === 'count' ? 'Cantidad' : key}
            fill={getColorForValue(key, colors)} 
            radius={[4, 4, 0, 0]}
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
