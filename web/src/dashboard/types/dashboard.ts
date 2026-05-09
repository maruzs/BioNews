export type DashboardFilters = {
  tipo?: string | null;
  region?: string | null;
  estado?: string | null;
  categoriaEconomica?: string | null;
  anio?: string | null;
  organismo?: string | null;
  tribunal?: string | null;
};

export interface ChartDataPoint {
  name: string;
  count: number;
  percentage?: number;
  [key: string]: any;
}

export interface DimensionConfig {
  key: string;
  label: string;
  type: 'bar-horizontal' | 'bar-vertical' | 'pie' | 'relative-bar' | 'grouped-vertical' | 'annual';
  groupField?: string;
}

export interface DashboardConfig {
  title: string;
  tableName: string;
  kpiField?: string;
  dimensions: DimensionConfig[];
}
