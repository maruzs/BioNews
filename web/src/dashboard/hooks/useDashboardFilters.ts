import { useMemo } from 'react';
import { useDashboardStore } from '../store/dashboardStore';
import { normalizeLabel } from '../utils/normalizeLabels';

export const useDashboardFilters = (data: any[]) => {
  const filters = useDashboardStore((state) => state.filters);

  const filteredData = useMemo(() => {
    if (!data) return [];
    
    return data.filter((item) => {
      return Object.entries(filters).every(([key, value]) => {
        if (!value) return true;
        // Map filter key to data key if needed, or use directly
        return normalizeLabel(item[key], key) === value;
      });
    });
  }, [data, filters]);

  return {
    filteredData,
    activeFilters: filters,
  };
};
