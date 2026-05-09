import { create } from 'zustand';
import type { DashboardFilters } from '../types/dashboard';

interface DashboardState {
  filters: DashboardFilters;
  setFilter: (key: keyof DashboardFilters, value: string | null) => void;
  toggleFilter: (key: keyof DashboardFilters, value: string | null) => void;
  clearFilters: () => void;
  resetFilters: () => void;
}

export const useDashboardStore = create<DashboardState>((set) => ({
  filters: {},
  
  setFilter: (key, value) => set((state) => ({
    filters: { ...state.filters, [key]: value }
  })),

  toggleFilter: (key, value) => set((state) => {
    const current = state.filters[key];
    if (current === value) {
      const newFilters = { ...state.filters };
      delete newFilters[key];
      return { filters: newFilters };
    }
    return { filters: { ...state.filters, [key]: value } };
  }),

  clearFilters: () => set({ filters: {} }),
  
  resetFilters: () => set({ filters: {} }),
}));
