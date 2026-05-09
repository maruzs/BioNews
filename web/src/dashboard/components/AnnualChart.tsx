import React from 'react';
import { 
  AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, 
  ResponsiveContainer 
} from 'recharts';
import { useTheme } from '@mui/material/styles';
import { useDashboardStore } from '../store/dashboardStore';
import DashboardTooltip from './DashboardTooltip';

interface AnnualChartProps {
  data: any[];
  xAxisKey: string;
  filterKey: string;
}

const AnnualChart: React.FC<AnnualChartProps> = ({ 
  data, 
  xAxisKey, 
  filterKey
}) => {
  const theme = useTheme();
  const { toggleFilter } = useDashboardStore();
  const primaryColor = theme.palette.primary.main;

  return (
    <ResponsiveContainer width="100%" height="100%">
      <AreaChart data={data} margin={{ top: 10, right: 10, left: 0, bottom: 0 }}>
        <defs>
          <linearGradient id="colorCount" x1="0" y1="0" x2="0" y2="1">
            <stop offset="5%" stopColor={primaryColor} stopOpacity={0.3}/>
            <stop offset="95%" stopColor={primaryColor} stopOpacity={0}/>
          </linearGradient>
        </defs>
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
        <Tooltip content={<DashboardTooltip />} />
        <Area 
          type="monotone" 
          dataKey="count" 
          stroke={primaryColor} 
          strokeWidth={3}
          fillOpacity={1} 
          fill="url(#colorCount)" 
          onClick={(entry: any) => toggleFilter(filterKey as any, entry[xAxisKey])}
          style={{ cursor: 'pointer' }}
          activeDot={{ r: 6, strokeWidth: 0 }}
        />
      </AreaChart>
    </ResponsiveContainer>
  );
};

export default AnnualChart;
