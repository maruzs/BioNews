import React, { useState, useEffect, useMemo } from 'react';
import * as XLSX from 'xlsx';
import { Search, X, Filter, ChevronDown, ChevronUp, LayoutDashboard, Download, Heart, Eye, BookOpen, Table, LayoutGrid } from 'lucide-react';
import { DataGrid } from '@mui/x-data-grid';
import { Autocomplete, TextField } from '@mui/material';
import type { GridColDef, GridRenderCellParams } from '@mui/x-data-grid';
import { esES } from '@mui/x-data-grid/locales';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';
import type { DashboardConfig } from '../dashboard/types/dashboard';
import DashboardManager from '../dashboard/DashboardManager';

export interface LegalItem {
  [key: string]: any;
}

interface ColumnConfig {
  field: string;
  headerName: string;
  width?: number;
  flex?: number;
  minWidth?: number;
}

interface ReportLayoutProps {
  title: string;
  description: string;
  listTitle: string;
  /** Nombre de la tabla en data.db para obtener los datos */
  tableName?: string;
  /** Configuración de columnas específicas para esta tabla */
  columnConfig?: ColumnConfig[];
  /** Campo que actúa como identificador único (para link y favoritos) */
  idField?: string;
  /** Campo que contiene el link de acción */
  actionField?: string;
  /** Es la página de favoritos */
  isFavoritesPage?: boolean;
  category?: string;
  children?: React.ReactNode;
}

// Configuraciones de columnas predefinidas por tabla
const TABLE_COLUMNS: Record<string, ColumnConfig[]> = {
  fiscalizaciones: [
    { field: 'expediente', headerName: 'Expediente', width: 140 },
    { field: 'unidad_fiscalizable', headerName: 'Unidad Fiscalizable', flex: 1, minWidth: 200 },
    { field: 'nombre_razon_social', headerName: 'Razón Social', flex: 1, minWidth: 200 },
    { field: 'categoria', headerName: 'Categoría', width: 120 },
    { field: 'region', headerName: 'Región', width: 140 },
    { field: 'estado', headerName: 'Estado', width: 140 },
  ],
  sancionatorios: [
    { field: 'expediente', headerName: 'Expediente', width: 140 },
    { field: 'unidad_fiscalizable', headerName: 'Unidad Fiscalizable', flex: 1, minWidth: 200 },
    { field: 'nombre_razon_social', headerName: 'Razón Social', flex: 1, minWidth: 200 },
    { field: 'categoria', headerName: 'Categoría', width: 120 },
    { field: 'region', headerName: 'Región', width: 140 },
    { field: 'estado', headerName: 'Estado', width: 140 },
  ],
  registroSanciones: [
    { field: 'expediente', headerName: 'Expediente', width: 140 },
    { field: 'unidad_fiscalizable', headerName: 'Unidad Fiscalizable', flex: 1, minWidth: 200 },
    { field: 'nombre_razon_social', headerName: 'Razón Social', flex: 1, minWidth: 200 },
    { field: 'categoria', headerName: 'Categoría', width: 120 },
    { field: 'region', headerName: 'Región', width: 140 },
    { field: 'multa_uta', headerName: 'Multa (UTA)', width: 120 },
    { field: 'pago_multa', headerName: 'Pago Multa', width: 120 },
  ],
  medidas_provisionales: [
    { field: 'expediente', headerName: 'Expediente', width: 140 },
    { field: 'unidad_fiscalizable', headerName: 'Unidad Fiscalizable', flex: 1, minWidth: 200 },
    { field: 'nombre_razon_social', headerName: 'Razón Social', flex: 1, minWidth: 200 },
    { field: 'categoria', headerName: 'Categoría', width: 120 },
    { field: 'region', headerName: 'Región', width: 140 },
    { field: 'estado', headerName: 'Estado', width: 140 },
  ],
  requerimientos: [
    { field: 'expediente', headerName: 'Expediente', width: 140 },
    { field: 'unidad_fiscalizable', headerName: 'Unidad Fiscalizable', flex: 1, minWidth: 200 },
    { field: 'nombre_razon_social', headerName: 'Razón Social', flex: 1, minWidth: 200 },
    { field: 'categoria', headerName: 'Categoría', width: 120 },
    { field: 'region', headerName: 'Región', width: 140 },
  ],
  programasDeCumplimiento: [
    { field: 'expediente', headerName: 'Expediente', width: 140 },
    { field: 'unidad_fiscalizable', headerName: 'Unidad Fiscalizable', flex: 1, minWidth: 200 },
    { field: 'nombre_razon_social', headerName: 'Razón Social', flex: 1, minWidth: 200 },
    { field: 'categoria', headerName: 'Categoría', width: 120 },
    { field: 'region', headerName: 'Región', width: 140 },
  ],
  Tribunales: [
    { field: 'Rol', headerName: 'Rol', width: 140 },
    { field: 'Fecha', headerName: 'Fecha', width: 120 },
    { field: 'Caratula', headerName: 'Carátula', flex: 1, minWidth: 250 },
    { field: 'Tribunal', headerName: 'Tribunal', width: 120 },
    { field: 'Tipo_de_Procedimiento', headerName: 'Tipo', width: 160 },
    { field: 'Estado_Procesal', headerName: 'Estado', width: 150 },
  ],
  pertinencias: [
    { field: 'Expediente', headerName: 'Expediente', width: 140 },
    { field: 'Nombre_de_Proyecto', headerName: 'Nombre del Proyecto', flex: 1, minWidth: 250 },
    { field: 'Proponente', headerName: 'Proponente', flex: 1, minWidth: 200 },
    { field: 'tipo_proyecto', headerName: 'Tipo', width: 100 },
    { field: 'categoria_economica', headerName: 'Categoría Económica', width: 180 },
    { field: 'Fecha', headerName: 'Fecha', width: 120 },
    { field: 'Estado', headerName: 'Estado', width: 140 },
  ],
  normativas: [
    { field: 'fecha', headerName: 'Fecha', width: 120 },
    { field: 'normativa', headerName: 'Normativa', flex: 1, minWidth: 300 },
    { field: 'tipo_normativa', headerName: 'Tipo', width: 160 },
    { field: 'organismo', headerName: 'Organismo', width: 200 },
    { field: 'suborganismo', headerName: 'Suborganismo', width: 180 },
  ],
};

// Mapeo de tabla -> campo ID y campo acción
const TABLE_ID_FIELDS: Record<string, string> = {
  fiscalizaciones: 'expediente',
  sancionatorios: 'expediente',
  registroSanciones: 'expediente',
  medidas_provisionales: 'expediente',
  requerimientos: 'expediente',
  programasDeCumplimiento: 'expediente',
  Tribunales: 'Accion',
  pertinencias: 'Expediente',
  normativas: 'accion',
};

const TABLE_ACTION_FIELDS: Record<string, string> = {
  fiscalizaciones: 'detalle_link',
  sancionatorios: 'detalle_link',
  registroSanciones: 'detalle_link',
  medidas_provisionales: 'detalle_link',
  requerimientos: 'detalle_link',
  programasDeCumplimiento: 'detalle_link',
  Tribunales: 'Accion',
  pertinencias: 'Accion',
  normativas: 'accion',
};



const getDashboardConfig = (tableName: string | undefined, title: string): DashboardConfig => {
  const baseConfig: DashboardConfig = {
    title: title,
    tableName: tableName || 'unknown',
    dimensions: []
  };

  switch (tableName) {
    case 'normativas':
      baseConfig.dimensions = [
        { key: 'tipo_normativa', label: 'Normativas por Tipo', type: 'relative-bar' },
        { key: 'organismo', label: 'Normativas por Organismo', type: 'relative-bar' },
        { key: 'fecha', label: 'Normativas por Año y Tipo', type: 'grouped-vertical' }, // Desacopladas (sin groupField)
        { key: 'region', label: 'Distribución por Región', type: 'relative-bar' }
      ];
      break;
    case 'pertinencias':
      baseConfig.dimensions = [
        { key: 'tipo_proyecto', label: 'Pertinencias por Tipo', type: 'relative-bar' },
        { key: 'categoria_economica', label: 'Categoría Económica', type: 'relative-bar' },
        // { key: 'region', label: 'Pertinencias por Región', type: 'relative-bar' }, // Actualmente no tienen region
        { key: 'Estado', label: 'Estado del Proceso', type: 'pie' },
        { key: 'Fecha', label: 'Evolución Anual por Tipo', type: 'grouped-vertical' } // Desacopladas
      ];
      break;
    case 'SEAEvaluados':
      baseConfig.dimensions = [
        { key: 'razon_ingreso', label: 'Razón de Ingreso', type: 'relative-bar' },
        { key: 'categoria_economica', label: 'Categoría Económica', type: 'relative-bar' },
        { key: 'region', label: 'Proyectos por Región', type: 'relative-bar' },
        { key: 'estado_proyecto', label: 'Estado de Evaluación', type: 'pie' },
        { key: 'fecha_presentacion', label: 'Presentaciones por Año', type: 'grouped-vertical' } // Desacopladas
      ];
      break;
    case 'Tribunales':
      baseConfig.dimensions = [
        { key: 'Tribunal', label: 'Causas por Tribunal', type: 'relative-bar' },
        { key: 'Tipo_de_Procedimiento', label: 'Tipo de Procedimiento', type: 'bar-horizontal' },
        { key: 'Estado_Procesal', label: 'Estado Procesal', type: 'pie' },
        { key: 'Fecha', label: 'Ingreso Anual de Causas', type: 'grouped-vertical' } // Desacopladas
      ];
      break;
    case 'fiscalizaciones':
    case 'sancionatorios':
      baseConfig.dimensions = [
        { key: 'categoria', label: 'Categoría Económica', type: 'relative-bar' },
        { key: 'region', label: 'Registros por Región', type: 'relative-bar' },
        { key: 'estado', label: 'Estado del Expediente', type: 'pie' },
        { key: 'expediente', label: 'Evolución Anual', type: 'grouped-vertical' }
      ];
      break;
    case 'registroSanciones':
      baseConfig.dimensions = [
        { key: 'categoria', label: 'Categoría Económica', type: 'relative-bar' },
        { key: 'region', label: 'Registros por Región', type: 'relative-bar' },
        { key: 'pago_multa', label: 'Multas', type: 'pie' },
        { key: 'expediente', label: 'Evolución Anual', type: 'grouped-vertical' }
      ];
      break;
    case 'medidas_provisionales':
    case 'requerimientos':
    case 'programasDeCumplimiento':
      baseConfig.dimensions = [
        { key: 'categoria', label: 'Categoría Económica', type: 'relative-bar' },
        { key: 'region', label: 'Registros por Región', type: 'relative-bar' },
        { key: 'expediente', label: 'Evolución Anual', type: 'grouped-vertical' }
      ];
      break;
    case 'ConsultasMMA':
      baseConfig.dimensions = [
        { key: 'estado', label: 'Estado de la Consulta', type: 'pie' },
        { key: 'materia', label: 'Materias de Interés', type: 'bar-horizontal' },
        { key: 'fecha_inicio', label: 'Consultas por Año', type: 'grouped-vertical' }
      ];
      break;
    default:
      baseConfig.dimensions = [
        { key: 'estado', label: 'Distribución por Estado', type: 'pie' },
        { key: 'region', label: 'Distribución por Región', type: 'relative-bar' },
      ];
  }
  return baseConfig;
};

const ReportLayout: React.FC<ReportLayoutProps> = ({
  title, description, listTitle, tableName, category, columnConfig, idField, actionField, isFavoritesPage, children
}) => {
  const { token, user } = useAuth();
  const { refreshCategory, setCategoryActive } = useNotifications();
  const [selectedCard, setSelectedCard] = useState<LegalItem | null>(null);
  const [filtersOpen, setFiltersOpen] = useState(false);
  const [data, setData] = useState<LegalItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [backgroundLoading, setBackgroundLoading] = useState(false);
  const [totalRecords, setTotalRecords] = useState<number | null>(null);
  const [favorites, setFavorites] = useState<Set<string>>(new Set());
  const [search, setSearch] = useState('');
  const [columnFilters, setColumnFilters] = useState<Record<string, string>>({});
  const [dateRange, setDateRange] = useState({ start: '', end: '' });
  const [activeTab, setActiveTab] = useState('reporte');

  const [appliedColumnFilters, setAppliedColumnFilters] = useState<Record<string, string>>({});
  const [appliedDateRange, setAppliedDateRange] = useState({ start: '', end: '' });
  const [appliedSearch, setAppliedSearch] = useState('');

  const [viewMode, setViewMode] = useState<'table' | 'cards'>(
    typeof window !== 'undefined' && window.innerWidth < 768 ? 'cards' : 'table'
  );
  const [cardPage, setCardPage] = useState(1);
  const cardsPerPage = 12;

  useEffect(() => {
    setCardPage(1);
  }, [appliedSearch, appliedColumnFilters, appliedDateRange, activeTab, tableName]);

  // Manual favorite form state
  const [manualFav, setManualFav] = useState({ id: '', nombre: '', fuente: '', accion: '' });

  const handleManualFavoriteSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!manualFav.id || !manualFav.fuente || !manualFav.nombre) return;

    try {
      await fetch('/api/favorites', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({
          id_o_link: manualFav.id,
          fuente: manualFav.fuente,
          nombre: manualFav.nombre,
          accion: manualFav.accion
        })
      });
      // Refresh the page or data
      window.location.reload();
    } catch (err) {
      console.error("Error saving manual fav", err);
    }
  };

  // On mount, apply user preferences if available
  useEffect(() => {
    if (token && user?.preferences) {
      try {
        const prefs = JSON.parse(user.preferences);
        let initialFilters: Record<string, string> = {};
        if (tableName === 'normativas' && prefs.normativas?.length > 0) {
          initialFilters['organismo'] = prefs.normativas.join('; ');
        } else if (['fiscalizaciones', 'sancionatorios', 'registroSanciones', 'programasDeCumplimiento', 'medidas_provisionales', 'requerimientos'].includes(tableName || '') && prefs.sma?.length > 0) {
          initialFilters['categoria'] = prefs.sma.join('; ');
        }

        if (Object.keys(initialFilters).length > 0) {
          setColumnFilters(initialFilters);
          setAppliedColumnFilters(initialFilters);
        }
      } catch (e) { }
    }
  }, [user, tableName, token]);

  const effectiveIdField = idField || (tableName ? TABLE_ID_FIELDS[tableName] : 'link') || 'link';
  const effectiveActionField = actionField || (tableName ? TABLE_ACTION_FIELDS[tableName] : 'link') || 'link';

  useEffect(() => {
    let active = true;
    const fetchData = async () => {
      setLoading(true);
      setBackgroundLoading(true);
      setTotalRecords(null);
      try {
        const favRes = await fetch('/api/favorites', {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        const favJson = await favRes.json();
        const favSet = new Set<string>(favJson.map((f: any) => f.id_o_link));
        if (active) {
          setFavorites(favSet);
        }

        if (isFavoritesPage) {
          const favData = favJson.map((f: any) => ({
            _id: f.id_o_link,
            _nombre: f.nombre,
            _fuente: f.fuente,
            fecha_agregado: f.fecha_agregado,
            _action: f.accion || (f.id_o_link.startsWith('http') ? f.id_o_link : '')
          }));
          if (active) {
            setData(favData);
            setLoading(false);
            setBackgroundLoading(false);
          }
        } else if (tableName) {
          // 1. Fetch total count
          try {
            const countRes = await fetch(`/api/data/${tableName}/count`, {
              headers: { 'Authorization': `Bearer ${token}` }
            });
            const countJson = await countRes.json();
            if (active) {
              setTotalRecords(countJson.count || 0);
            }
          } catch (e) {
            console.error("Error fetching count:", e);
          }

          // 2. Fetch first 100 records for fast initial load
          const res = await fetch(`/api/data/${tableName}?limit=100`, {
            headers: { 'Authorization': `Bearer ${token}` }
          });
          const json = await res.json();
          if (active) {
            setData(Array.isArray(json) ? json : []);
            setLoading(false);
          }

          // 3. Fetch full dataset in the background
          fetch(`/api/data/${tableName}?limit=-1`, {
            headers: { 'Authorization': `Bearer ${token}` }
          })
            .then(r => r.json())
            .then(fullJson => {
              if (active && Array.isArray(fullJson)) {
                setData(fullJson);
                setBackgroundLoading(false);
              }
            })
            .catch(err => {
              console.error("Error in background fetch:", err);
              if (active) setBackgroundLoading(false);
            });
        }
      } catch (err) {
        console.error("Error fetching data:", err);
        if (active) {
          setLoading(false);
          setBackgroundLoading(false);
        }
      }
    };

    fetchData();
    return () => {
      active = false;
    };
  }, [tableName, isFavoritesPage]);

  // Al cargar datos de una categoría, actualizar si tiene ítems nuevos
  // Esto actualiza el punto rojo en la sidebar sin necesidad de F5
  useEffect(() => {
    if (!loading && category && !isFavoritesPage) {
      refreshCategory(category);
    }
  }, [loading, category, isFavoritesPage]);

  // Registrar esta categoría como activa en el contexto global
  useEffect(() => {
    if (category && !isFavoritesPage) {
      setCategoryActive(category, true);
      return () => {
        setCategoryActive(category, false);
      };
    }
  }, [category, isFavoritesPage, setCategoryActive]);

  const toggleFavorite = async (item: LegalItem) => {
    const itemId = isFavoritesPage ? item._id : (item[effectiveIdField] || '');
    const isFav = favorites.has(itemId);
    try {
      if (isFav) {
        await fetch(`/api/favorites/${encodeURIComponent(itemId)}`, {
          method: 'DELETE',
          headers: { 'Authorization': `Bearer ${token}` }
        });
        setFavorites(prev => {
          const next = new Set(prev);
          next.delete(itemId);
          return next;
        });
        if (isFavoritesPage) {
          setData(prev => prev.filter(i => i._id !== itemId));
        }
      } else {
        const nombre = item['Caratula'] || item['Nombre_de_Proyecto'] || item['normativa'] || item['unidad_fiscalizable'] || item[effectiveIdField] || '';
        const fuente = tableName || item._table || 'unknown';
        const actionF = item[effectiveActionField] || item._action || '';
        await fetch('/api/favorites', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
          body: JSON.stringify({ id_o_link: itemId, fuente, nombre, accion: actionF })
        });
        setFavorites(prev => {
          const next = new Set(prev);
          next.add(itemId);
          return next;
        });
      }
    } catch (err) {
      console.error("Fav error", err);
    }
  };

  const filteredData = useMemo(() => {
    let result = data;
    if (appliedSearch) {
      const lowerSearch = appliedSearch.toLowerCase();
      result = result.filter(item =>
        Object.values(item).some(val =>
          val && String(val).toLowerCase().includes(lowerSearch)
        )
      );
    }
    Object.entries(appliedColumnFilters).forEach(([field, value]) => {
      if (value) {
        if (field === 'expediente_year') {
          result = result.filter(item => {
            const exp = String(item['expediente'] || item['Expediente'] || '');
            const parts = exp.split('-');
            // Buscar una parte que tenga 4 dígitos (el año)
            const yearPart = parts.find(p => /^\d{4}$/.test(p));
            if (yearPart) {
              return yearPart === value;
            }
            return exp.includes(value);
          });
          return;
        }

        if (field === 'expediente_tipo') {
          result = result.filter(item => {
            const exp = String(item['expediente'] || item['Expediente'] || '');
            const parts = exp.split('-');
            // El tipo suele ser la 5ta parte (index 4) o la última si es fiscalización
            // Formato: DFZ-ANO-NUMERO-REGION-TIPO
            if (parts.length >= 5) {
              // Puede tener -IA o -EI al final, tomamos solo el tipo base
              const type = parts[4];
              return type === value;
            }
            return false;
          });
          return;
        }

        const lowerValue = value.toLowerCase();
        result = result.filter(item => {
          const itemVal = item[field];
          if (!itemVal) return false;
          const strVal = String(itemVal).toLowerCase();
          const terms = value.split(';').map(t => t.trim().toLowerCase()).filter(Boolean);
          if (terms.length > 1) {
            return terms.some(t => strVal === t || strVal.includes(t));
          }
          return strVal.includes(lowerValue);
        });
      }
    });
    if (appliedDateRange.start || appliedDateRange.end) {
      const dateFieldNames = ['fecha', 'Fecha', 'fecha_agregado'];
      const dateField = dateFieldNames.find(f => data.length > 0 && f in data[0]);
      if (dateField) {
        result = result.filter(item => {
          if (!item[dateField]) return false;
          const itemDate = new Date(item[dateField]);
          if (isNaN(itemDate.getTime())) return true;
          let matchesDate = true;
          if (appliedDateRange.start) {
            const start = new Date(appliedDateRange.start);
            if (itemDate < start) matchesDate = false;
          }
          if (appliedDateRange.end) {
            const end = new Date(appliedDateRange.end);
            end.setHours(23, 59, 59, 999);
            if (itemDate > end) matchesDate = false;
          }
          return matchesDate;
        });
      }
    }
    return result;
  }, [data, appliedSearch, appliedColumnFilters, appliedDateRange]);


  const handleApplyFilters = () => {
    setAppliedColumnFilters({ ...columnFilters });
    setAppliedDateRange({ ...dateRange });
    setAppliedSearch(search);
  };

  const handleClearFilters = () => {
    setColumnFilters({});
    setDateRange({ start: '', end: '' });
    setSearch('');
    setAppliedColumnFilters({});
    setAppliedDateRange({ start: '', end: '' });
    setAppliedSearch('');
  };

  const downloadExcel = () => {
    if (filteredData.length === 0) return;

    const colFields = activeColumns.filter(c => c.field !== 'rowNumber' && c.field !== 'fav' && c.field !== 'accion');

    const excelData = filteredData.map((row) => {
      const rowData: Record<string, any> = {};
      colFields.forEach(c => {
        rowData[c.headerName] = row[c.field] || '';
      });
      return rowData;
    });

    const worksheet = XLSX.utils.json_to_sheet(excelData);
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, "Reporte");

    XLSX.writeFile(workbook, `${title.toLowerCase().replace(/\s+/g, '_')}_export.xlsx`);
  };

  // Determinar las columnas activas
  const activeColumns: ColumnConfig[] = useMemo(() => {
    if (columnConfig) return columnConfig;
    if (tableName && TABLE_COLUMNS[tableName]) return TABLE_COLUMNS[tableName];
    if (isFavoritesPage) {
      return [
        { field: '_id', headerName: 'ID', width: 140 },
        { field: '_nombre', headerName: 'Nombre', flex: 1, minWidth: 250 },
        { field: '_fuente', headerName: 'Fuente', width: 160 },
      ];
    }
    return [];
  }, [columnConfig, tableName, isFavoritesPage]);

  const rows = useMemo(() => filteredData.map((item: any, index: number) => {
    // Generar un ID único y estable para DataGrid
    const baseId = isFavoritesPage ? item._id : (item[effectiveIdField] || '');
    // Si el baseId no es suficientemente único (como en normativas), combinamos con otros campos o el índice
    const uniqueId = baseId ? `${baseId}-${item.fecha || item.Fecha || ''}-${index}` : `row-${index}`;

    return {
      ...item,
      id: uniqueId,
      rowNumber: index + 1
    };
  }), [filteredData, effectiveIdField, isFavoritesPage]);

  const totalCardPages = Math.ceil(rows.length / cardsPerPage);
  const paginatedCardRows = useMemo(() => {
    return rows.slice((cardPage - 1) * cardsPerPage, cardPage * cardsPerPage);
  }, [rows, cardPage]);

  const columns: GridColDef[] = useMemo(() => {
    const cols: GridColDef[] = [
      {
        field: 'rowNumber',
        headerName: 'Nº',
        width: 80,
        filterable: false,
        renderCell: (params: GridRenderCellParams) => {
          const isNew = params.row.is_new;
          return (
            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', height: '100%' }}>
              <span>{params.row.rowNumber}</span>
              {isNew && (
                <span style={{
                  backgroundColor: '#22c55e',
                  color: 'white',
                  fontSize: '9px',
                  padding: '2px 5px',
                  borderRadius: '10px',
                  fontWeight: 'bold',
                  textTransform: 'uppercase'
                }}>NUEVO</span>
              )}
            </div>
          );
        }
      },
      {
        field: 'fav',
        headerName: 'Fav',
        width: 60,
        sortable: false,
        filterable: false,
        renderCell: (params: GridRenderCellParams) => {
          const itemId = isFavoritesPage ? params.row._id : (params.row[effectiveIdField] || '');
          return (
            <div style={{ display: 'flex', alignItems: 'center', height: '100%' }}>
              <Heart
                size={18}
                style={{ cursor: 'pointer', fill: favorites.has(itemId) ? 'var(--orange)' : 'none', color: favorites.has(itemId) ? 'var(--orange)' : 'var(--text-light)' }}
                onClick={() => toggleFavorite(params.row)}
              />
            </div>
          );
        }
      },
    ];

    // Agregar las columnas dinámicas
    activeColumns.forEach(col => {
      const isDateField = col.field.toLowerCase() === 'fecha' || col.field.toLowerCase() === 'fecha_agregado';
      cols.push({
        field: col.field,
        headerName: col.headerName,
        width: col.width,
        flex: col.flex,
        minWidth: col.minWidth,
        type: isDateField ? 'date' : undefined,
        valueGetter: isDateField ? (value: any, row: any) => {
          let val = value;
          if (!val && row) {
            val = row.fecha || row.Fecha || row.FECHA || row.fecha_agregado;
          }
          if (!val) return null;
          const str = String(val);
          // Intentar parseo ISO directo (YYYY-MM-DD)
          if (/^\d{4}-\d{2}-\d{2}/.test(str)) {
            return new Date(str.split(' ')[0] + 'T00:00:00');
          }
          // Soporte para "/" y "-" (DD-MM-YYYY o MM-DD-YYYY)
          const separator = str.includes('-') ? '-' : (str.includes('/') ? '/' : null);
          if (separator) {
            const parts = str.split(' ')[0].split(separator);
            if (parts.length === 3) {
              const p0 = parseInt(parts[0]);
              const p1 = parseInt(parts[1]);
              const p2 = parseInt(parts[2]);
              if (p0 > 1000) { // YYYY-MM-DD
                return new Date(p0, p1 - 1, p2);
              }
              // DD-MM-YYYY (Asumimos esto por defecto para scrapers que no migraron)
              return new Date(p2, p1 - 1, p0);
            }
          }
          const d = new Date(str);
          return isNaN(d.getTime()) ? null : d;
        } : undefined
      });
    });

    // Agregar columna de acción
    cols.push({
      field: 'accion',
      headerName: 'Acción',
      width: 80,
      sortable: false,
      filterable: false,
      renderCell: (params: GridRenderCellParams) => {
        const link = isFavoritesPage ? params.row._action : (params.row[effectiveActionField] || '');
        if (!link) return null;

        return (
          <a
            href={link}
            target="_blank"
            rel="noopener noreferrer"
            style={{ color: 'var(--primary)', display: 'flex', alignItems: 'center', height: '100%' }}
          >
            <Eye size={20} />
          </a>
        );
      }
    });

    return cols;
  }, [favorites, activeColumns, effectiveIdField, effectiveActionField, isFavoritesPage]);

  // ─── Card helper: status color ───────────────────────────────────────────────
  const getCardStatusColor = (status: string | undefined, row?: LegalItem): string => {
    const s = (status || '').toLowerCase().trim();

    // pago_multa (registroSanciones)
    if (row && row.pago_multa !== undefined) {
      const pm = (row.pago_multa || '').toLowerCase();
      if (pm.includes('pagada')) return '#10b981';
      if (pm.includes('pendiente')) return '#ef4444';
      if (pm.includes('no aplica')) return '#94a3b8';
    }

    // Verdes
    if (s === 'aprobado' || s.includes('favorable') || s === 'en snifa'
        || s === 'terminado - absolucion' || s === 'terminado - pdc satisfactorio'
        || s.includes('con sancionatorio') === false && s === 'sin sancionatorio'
        || s === 'sin sancionatorio') return '#10b981';

    // Rojos
    if (s === 'rechazado' || s === 'desistido' || s === 'sancionado'
        || s === 'en análisis-suspendida' || s === 'en analisis-suspendida'
        || s === 'terminado - sanción' || s === 'terminado - sancion'
        || s === 'con sancionatorio'
        || s.includes('rechazado') || s.includes('desistido')) return '#ef4444';

    // Naranjas
    if (s.includes('formulado') || s.includes('cargos')) return '#f97316';

    // Amarillos
    if (s === 'resuelta' || s === 'suspendido' || s === 'suspendida'
        || s === 'suspendidas' || s === 'terminado' || s === 'terminada'
        || s === 'terminadas' || s === 'terminado - archivado'
        || s === 'concluido') return '#f59e0b';

    // Azules
    if (s === 'en análisis' || s === 'en analisis'
        || s === 'derivada a sma' || s === 'en curso'
        || s === 'programa de cumplimiento en ejecucion'
        || s === 'de sentencia' || s === 'en estudio'
        || s === 'en tramitacion' || s === 'tramitacion'
        || s.includes('admisi') || s.includes('calificaci')
        || s.includes('análisis') || s.includes('analisis')
        || s.includes('tramitaci')) return '#3b82f6';

    // Morado (Boletin Oficial Mineria)
    if (s.includes('boletin oficial') || s.includes('boletín oficial') || s.includes('mineria') || s.includes('minería')) return '#8b5cf6';

    // Verde lima (Normas Generales)
    if (s === 'normas generales') return '#84cc16';

    // Celeste (Normas Particulares)
    if (s === 'normas particulares') return '#06b6d4';

    // Grises
    if (s === 'archivado' || s === 'inadmitido' || s === 'sin estado'
        || s === 'sin tramitacion electronica' || s === 'sin tramitación electrónica'
        || s === 'terminado - archivado') return '#94a3b8';

    return '#64748b';
  };

  // ─── Card helper: extract semantic fields per table ───────────────────────────
  const getCardFields = (row: LegalItem) => {
    const isNormativa = !!(row.normativa || row.tipo_normativa);
    const isTribunal  = !!(row.Caratula || row.Estado_Procesal);
    const isPertinencia = !!(row.Nombre_de_Proyecto);
    const isSMA = !!(row.unidad_fiscalizable || row.expediente);

    // STATUS
    let statusVal: string;
    if (isNormativa)         statusVal = row.tipo_normativa || 'Sin tipo';
    else if (isTribunal)     statusVal = row.Estado_Procesal || 'Sin estado';
    else if (isPertinencia)  statusVal = row.Estado || 'Sin estado';
    else if (isSMA)          statusVal = row.estado || 'Sin estado';
    else                     statusVal = row.estado || row.Estado || row._fuente || 'Sin estado';

    // META LINE
    let metaParts: string[] = [];
    if (isNormativa) {
      // For normativas: organismo only (tipo_normativa already used as status)
      if (row.organismo) metaParts.push(row.organismo);
    } else if (isTribunal) {
      if (row.Tipo_de_Procedimiento) metaParts.push(row.Tipo_de_Procedimiento);
      if (row.Tribunal) metaParts.push(row.Tribunal);
    } else if (isPertinencia) {
      if (row.tipo_proyecto) metaParts.push(row.tipo_proyecto);
      if (row.categoria_economica) metaParts.push(row.categoria_economica);
    } else {
      if (row.categoria) metaParts.push(row.categoria);
      const regionVal = row.region || '';
      if (regionVal) metaParts.push(regionVal);
    }
    metaParts = Array.from(new Set(metaParts)).slice(0, 2);

    // TITLE
    const titleVal: string =
      row.Caratula || row.Nombre_de_Proyecto || row.normativa ||
      row._nombre || row.unidad_fiscalizable || row.nombre || '';

    // DATE
    const rawDate: string =
      row.fecha_presentacion || row.Fecha || row.fecha || row.fecha_inicio || '';
    const dateVal = rawDate ? String(rawDate).split(' ')[0] : '';

    // ENTITY (Titular equivalent)
    let entityVal: string;
    let entityLabel: string;
    if (isNormativa) {
      entityVal  = row.suborganismo || 'Sin suborganismo';
      entityLabel = 'Suborganismo';
    } else if (isTribunal) {
      entityVal  = row.Rol || '';
      entityLabel = 'Rol';
    } else if (isPertinencia) {
      entityVal  = row.Proponente || '';
      entityLabel = 'Proponente';
    } else if (isSMA) {
      entityVal  = row.nombre_razon_social || '';
      entityLabel = 'Razón Social';
    } else {
      entityVal  = row.titular || row.Proponente || row.nombre_razon_social || row.Rol || '';
      entityLabel = row.titular ? 'Titular' : row.Proponente ? 'Proponente' : row.nombre_razon_social ? 'Razón Social' : 'Entidad';
    }

    return { statusVal, metaParts, titleVal, dateVal, entityVal, entityLabel };
  };

  return (
    <div className="report-container">
      <div style={{ marginBottom: '30px' }}>
        <h1 style={{ fontSize: '28px', fontWeight: 'bold', color: 'var(--text-dark)' }}>Reporte de {title}</h1>
        <p style={{ color: 'var(--text-light)', marginTop: '5px' }}>{description}</p>
      </div>

      {/* Control Bar */}
      <div style={{
        backgroundColor: 'white', padding: '15px', borderRadius: '12px',
        border: '1px solid var(--border)', boxShadow: '0 2px 10px rgba(0,0,0,0.03)',
        marginBottom: '25px', display: 'flex', flexWrap: 'wrap', gap: '15px', alignItems: 'center'
      }}>
        <div style={{ flexGrow: 1, position: 'relative', minWidth: '300px' }}>
          <Search size={18} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-light)' }} />
          <input
            type="text"
            placeholder="Buscar por palabra clave..."
            value={search}
            onChange={e => setSearch(e.target.value)}
            onKeyDown={e => { if (e.key === 'Enter') { setAppliedSearch(search); } }}
            style={{
              width: '100%', padding: '10px 40px', borderRadius: '8px',
              border: '1px solid var(--border)', outline: 'none', fontSize: '14px'
            }}
          />
          {search && (
            <button
              onClick={() => { setSearch(''); setAppliedSearch(''); }}
              style={{ position: 'absolute', right: '12px', top: '50%', transform: 'translateY(-50%)', background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-light)' }}
            >
              <X size={16} />
            </button>
          )}
        </div>

        <button
          onClick={() => setFiltersOpen(!filtersOpen)}
          style={{
            display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 15px',
            backgroundColor: filtersOpen ? 'var(--primary-light)' : 'white',
            color: filtersOpen ? 'var(--primary)' : 'var(--text-dark)',
            border: '1px solid ' + (filtersOpen ? 'var(--primary)' : 'var(--border)'),
            borderRadius: '8px', cursor: 'pointer', fontWeight: 500, fontSize: '14px',
            transition: 'all 0.2s'
          }}
        >
          <Filter size={18} />
          Filtros Avanzados
          {filtersOpen ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
        </button>

        {activeTab === 'reporte' && (
          <div style={{ display: 'flex', border: '1px solid var(--border)', borderRadius: '8px', overflow: 'hidden' }}>
            <button
              onClick={() => setViewMode('table')}
              style={{
                padding: '10px 15px',
                backgroundColor: viewMode === 'table' ? 'var(--primary-light)' : 'white',
                color: viewMode === 'table' ? 'var(--primary)' : 'var(--text-dark)',
                border: 'none',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                fontWeight: 500,
                fontSize: '14px',
                transition: 'all 0.2s'
              }}
              title="Ver como tabla"
            >
              <Table size={18} />
              <span className="desktop-only">Tabla</span>
            </button>
            <button
              onClick={() => setViewMode('cards')}
              style={{
                padding: '10px 15px',
                backgroundColor: viewMode === 'cards' ? 'var(--primary-light)' : 'white',
                color: viewMode === 'cards' ? 'var(--primary)' : 'var(--text-dark)',
                border: 'none',
                borderLeft: '1px solid var(--border)',
                cursor: 'pointer',
                display: 'flex',
                alignItems: 'center',
                gap: '8px',
                fontWeight: 500,
                fontSize: '14px',
                transition: 'all 0.2s'
              }}
              title="Ver como tarjetas"
            >
              <LayoutGrid size={18} />
              <span className="desktop-only">Tarjetas</span>
            </button>
          </div>
        )}

        {!isFavoritesPage && (
          <button
            onClick={() => setActiveTab(activeTab === 'dashboard' ? 'reporte' : 'dashboard')}
            style={{
              display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 15px',
              backgroundColor: activeTab === 'dashboard' ? 'var(--primary-light)' : 'var(--primary)',
              color: activeTab === 'dashboard' ? 'var(--primary)' : 'white',
              border: activeTab === 'dashboard' ? '1px solid var(--primary)' : 'none',
              borderRadius: '8px', cursor: 'pointer', fontWeight: 500, fontSize: '14px',
              transition: '0.2s'
            }}
            onMouseOver={(e) => {
              if (activeTab !== 'dashboard') e.currentTarget.style.opacity = '0.9';
            }}
            onMouseOut={(e) => {
              if (activeTab !== 'dashboard') e.currentTarget.style.opacity = '1';
            }}
          >
            {activeTab === 'dashboard' ? (
              <>
                <BookOpen size={18} style={{ color: '#22c55e' }} />
                Registros
              </>
            ) : (
              <>
                <LayoutDashboard size={18} />
                Dashboard
              </>
            )}
          </button>
        )}

        <div style={{ color: 'var(--text-light)', fontSize: '14px', marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: '8px' }}>
          <style>{`
            @keyframes spin-mini {
              0% { transform: rotate(0deg); }
              100% { transform: rotate(360deg); }
            }
          `}</style>
          {backgroundLoading && (
            <span style={{ fontSize: '12px', color: 'var(--primary)', display: 'inline-flex', alignItems: 'center', gap: '4px' }}>
              <span className="spinner-mini" style={{
                width: '12px',
                height: '12px',
                border: '2px solid var(--primary)',
                borderTopColor: 'transparent',
                borderRadius: '50%',
                display: 'inline-block',
                animation: 'spin-mini 1s linear infinite'
              }}></span>
              Cargando historial completo...
            </span>
          )}
          {totalRecords !== null ? `${totalRecords} resultados` : `${filteredData.length} resultados`}
        </div>
      </div>

      {activeTab === 'dashboard' && !isFavoritesPage ? (
        <div style={{ marginTop: '20px' }}>
          <DashboardManager
            data={data}
            config={getDashboardConfig(tableName, title)}
          />
        </div>
      ) : (
        <>
          {/* Advanced Filters */}
          {filtersOpen && (
            <div style={{
              backgroundColor: '#f8fafc', padding: '20px', borderRadius: '12px',
              border: '1px solid var(--border)', marginBottom: '25px'
            }}>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '15px', marginBottom: '20px' }}>
                {activeColumns
                  .filter(c => c.field !== 'rowNumber' && c.field !== 'fav' && c.field !== 'accion' && c.field !== effectiveIdField && c.field.toLowerCase() !== 'fecha' && c.field.toLowerCase() !== 'fecha_agregado')
                  .map(col => {
                    const categoricalFields = [
                      'estado', 'Estado', 'Estado_Procesal',
                      'organismo', 'Tribunal', 'categoria',
                      'region', 'tipo_normativa', 'suborganismo',
                      'Tipo_de_Procedimiento', 'materia', 'resultado',
                      'pago_multa'
                    ];

                    // Specific requirement for pertinencias dropdowns
                    const isPertinenciasSpecial = tableName === 'pertinencias' && (col.field === 'categoria_economica' || col.field === 'tipo_proyecto');

                    const isCategorical = categoricalFields.includes(col.field) || isPertinenciasSpecial;

                    if (isCategorical) {
                      const options = Array.from(new Set(data.map(item => item[col.field]).filter(Boolean))).sort();
                      return (
                        <div key={col.field}>
                          <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>{col.headerName}</label>
                          <Autocomplete
                            options={options}
                            value={columnFilters[col.field] || null}
                            onChange={(_, newValue) => setColumnFilters({ ...columnFilters, [col.field]: newValue || '' })}
                            renderInput={(params) => (
                              <TextField
                                {...params}
                                placeholder="Todos"
                                size="small"
                                sx={{
                                  bgcolor: 'white',
                                  '& .MuiOutlinedInput-root': { borderRadius: '6px' }
                                }}
                              />
                            )}
                          />
                        </div>
                      );
                    }

                    return (
                      <div key={col.field}>
                        <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>{col.headerName}</label>
                        <input
                          type="text"
                          style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)', fontSize: '14px' }}
                          value={columnFilters[col.field] || ''}
                          onChange={(e) => setColumnFilters({ ...columnFilters, [col.field]: e.target.value })}
                          placeholder={`Buscar ${col.headerName.toLowerCase()}`}
                        />
                      </div>
                    );
                  })}
                {activeColumns.some(c => ['expediente', 'Expediente'].includes(c.field)) && (
                  <>
                    <div>
                      <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Año (Expediente)</label>
                      <select
                        style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)', fontSize: '14px' }}
                        value={columnFilters['expediente_year'] || ''}
                        onChange={(e) => setColumnFilters({ ...columnFilters, 'expediente_year': e.target.value })}
                      >
                        <option value="">Todos los Años</option>
                        {Array.from(new Set(
                          data.map(item => {
                            const exp = String(item['expediente'] || item['Expediente'] || '');
                            const parts = exp.split('-');
                            const yearPart = parts.find(p => /^\d{4}$/.test(p));
                            return yearPart || null;
                          }).filter((y): y is string => Boolean(y))
                        )).sort((a, b) => Number(b) - Number(a)).map(year => (
                          <option key={year} value={year}>{year}</option>
                        ))}
                      </select>
                    </div>

                    {tableName === 'fiscalizaciones' && (
                      <div>
                        <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Tipo de Documento</label>
                        <select
                          style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)', fontSize: '14px' }}
                          value={columnFilters['expediente_tipo'] || ''}
                          onChange={(e) => setColumnFilters({ ...columnFilters, 'expediente_tipo': e.target.value })}
                        >
                          <option value="">Todos los Tipos</option>
                          {['RCA', 'PC', 'PPDA', 'NE', 'LEY', 'MP', 'NC', 'SRCA'].map(tipo => (
                            <option key={tipo} value={tipo}>{tipo}</option>
                          ))}
                        </select>
                      </div>
                    )}
                  </>
                )}
                {activeColumns.some(c => c.field.toLowerCase() === 'fecha' || c.field.toLowerCase() === 'fecha_agregado') && (
                  <div style={{ gridColumn: 'span 2' }}>
                    <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Rango de Fechas</label>
                    <div style={{ display: 'flex', gap: '10px' }}>
                      <input type="date" style={{ flex: 1, padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }} value={dateRange.start} onChange={(e) => setDateRange({ ...dateRange, start: e.target.value })} />
                      <span style={{ alignSelf: 'center' }}>-</span>
                      <input type="date" style={{ flex: 1, padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }} value={dateRange.end} onChange={(e) => setDateRange({ ...dateRange, end: e.target.value })} />
                    </div>
                  </div>
                )}
              </div>
              {children}
              <div style={{ display: 'flex', gap: '10px', justifyContent: 'flex-end', borderTop: '1px solid var(--border)', paddingTop: '20px' }}>
                <button
                  onClick={handleClearFilters}
                  style={{
                    padding: '10px 20px', borderRadius: '8px', border: '1px solid var(--border)',
                    background: 'white', color: 'var(--text-dark)', fontWeight: 600, cursor: 'pointer'
                  }}
                >
                  LIMPIAR FILTROS
                </button>
                <button
                  onClick={handleApplyFilters}
                  style={{
                    padding: '10px 20px', borderRadius: '8px', border: 'none',
                    background: 'var(--primary)', color: 'white', fontWeight: 600, cursor: 'pointer'
                  }}
                >
                  APLICAR FILTROS
                </button>
              </div>
            </div>
          )}

          {isFavoritesPage && (
            <div className="manual-favorite-section" style={{ background: '#f8fafc', padding: '20px', borderRadius: '12px', border: '1px solid var(--border)', marginTop: '10px' }}>
              <h3 style={{ fontSize: '15px', marginBottom: '15px', color: 'var(--text-dark)' }}>Agregar Favorito Manualmente</h3>
              <form onSubmit={handleManualFavoriteSubmit} style={{ display: 'flex', gap: '15px', flexWrap: 'wrap', alignItems: 'flex-end' }}>
                <div style={{ flex: '1 1 120px' }}>
                  <label style={{ display: 'block', fontSize: '12px', marginBottom: '5px', color: 'var(--text-light)', fontWeight: 600 }}>ID del Registro</label>
                  <input type="text" className="filter-select" required placeholder="Ej: R-157-2026" value={manualFav.id} onChange={e => setManualFav({ ...manualFav, id: e.target.value })} />
                </div>
                <div style={{ flex: '2 1 200px' }}>
                  <label style={{ display: 'block', fontSize: '12px', marginBottom: '5px', color: 'var(--text-light)', fontWeight: 600 }}>Nombre / Descripción</label>
                  <input type="text" className="filter-select" required placeholder="Ej: Proyecto Hidroeléctrico..." value={manualFav.nombre} onChange={e => setManualFav({ ...manualFav, nombre: e.target.value })} />
                </div>
                <div style={{ flex: '1 1 150px' }}>
                  <label style={{ display: 'block', fontSize: '12px', marginBottom: '5px', color: 'var(--text-light)', fontWeight: 600 }}>Fuente</label>
                  <select className="filter-select" required value={manualFav.fuente} onChange={e => setManualFav({ ...manualFav, fuente: e.target.value })}>
                    <option value="">Seleccione...</option>
                    <option value="SNIFA">SNIFA</option>
                    <option value="SEA">SEA</option>
                    <option value="Tribunales">Tribunales</option>
                    <option value="Diario Oficial">Diario Oficial</option>
                    <option value="Noticias">Noticias Generales</option>
                  </select>
                </div>
                <div style={{ flex: '2 1 250px' }}>
                  <label style={{ display: 'block', fontSize: '12px', marginBottom: '5px', color: 'var(--text-light)', fontWeight: 600 }}>URL de Acción (Opcional)</label>
                  <input type="url" className="filter-select" placeholder="https://..." value={manualFav.accion} onChange={e => setManualFav({ ...manualFav, accion: e.target.value })} />
                </div>
                <button type="submit" className="btn-primary" style={{ height: '42px', borderRadius: '6px' }}>
                  + Agregar
                </button>
              </form>
            </div>
          )}

          <div className="list-header">
            <h2 className="list-title">Listado de {listTitle}</h2>
            <div className="list-meta" style={{ display: 'flex', gap: '15px', alignItems: 'center' }}>
              <span>Total de registros: {filteredData.length}</span>
              <button onClick={downloadExcel} style={{ display: 'flex', alignItems: 'center', gap: '6px', background: 'none', border: 'none', color: 'var(--primary)', cursor: 'pointer', fontWeight: 600 }}>
                <Download size={16} /> Descargar XLSX
              </button>
            </div>
          </div>

          {viewMode === 'table' ? (
            <div className="table-container" style={{ height: 600, width: '100%', backgroundColor: 'white', borderRadius: '12px', padding: '10px' }}>
              <DataGrid
                rows={rows}
                columns={columns}
                loading={loading}
                initialState={{
                  pagination: { paginationModel: { pageSize: 10 } },
                }}
                pageSizeOptions={[10, 25, 50]}
                disableRowSelectionOnClick
                localeText={esES.components.MuiDataGrid.defaultProps.localeText}
                getRowClassName={(params) => {
                  return params.row.is_new ? 'new-record-highlight' : '';
                }}
                sx={{
                  border: 'none',
                  '& .MuiDataGrid-cell:focus': { outline: 'none' },
                  '& .new-record-highlight': {
                    backgroundColor: 'rgba(34, 197, 94, 0.12)',
                    fontWeight: '500',
                    borderLeft: '5px solid var(--primary)',
                  },
                  '& .MuiDataGrid-row.new-record-highlight:hover': {
                    backgroundColor: 'rgba(34, 197, 94, 0.18)',
                  },
                  '& .MuiDataGrid-cell': {
                    borderBottom: '1px solid #f0f0f0',
                  },
                  '& .MuiDataGrid-columnHeaders': {
                    backgroundColor: '#f8f9fa',
                    borderBottom: '2px solid #e0e0e0',
                    fontWeight: 'bold',
                  },
                }}
              />
            </div>
          ) : (
            <>
              {loading ? (
                <div style={{ textAlign: 'center', padding: '100px 0' }}>
                  <div className="loader" style={{ marginBottom: '20px' }}></div>
                  <p style={{ color: 'var(--text-light)' }}>Cargando registros...</p>
                </div>
              ) : rows.length === 0 ? (
                <div style={{ textAlign: 'center', padding: '100px 0', backgroundColor: '#f8fafc', borderRadius: '12px', border: '1px dashed var(--border)' }}>
                  <Search size={48} color="var(--text-light)" style={{ marginBottom: '20px', opacity: 0.5 }} />
                  <h3 style={{ fontSize: '18px', fontWeight: 'bold', color: 'var(--text-dark)' }}>No se encontraron registros</h3>
                  <p style={{ color: 'var(--text-light)', marginTop: '5px' }}>Intenta ajustando los términos de búsqueda o los filtros.</p>
                </div>
              ) : (
                <>
                  <div style={{
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))',
                    gap: '25px',
                    marginBottom: '40px',
                    marginTop: '20px',
                    width: '100%'
                  }}>
                    {paginatedCardRows.map((row) => {
                      const idValue = isFavoritesPage ? row._id : (row[effectiveIdField] || '');
                      const { statusVal, metaParts, titleVal, dateVal, entityVal, entityLabel } = getCardFields(row);
                      const dotColor = getCardStatusColor(statusVal, row);

                      return (
                        <div key={row.id} style={{
                          backgroundColor: 'white', borderRadius: '16px', border: '1px solid var(--border)',
                          overflow: 'hidden', boxShadow: '0 4px 15px rgba(0,0,0,0.05)',
                          display: 'flex', flexDirection: 'column',
                          transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
                          cursor: 'pointer', position: 'relative', height: '100%',
                        }}
                          onClick={() => setSelectedCard(row)}
                          onMouseOver={(e) => {
                            e.currentTarget.style.transform = 'translateY(-6px)';
                            e.currentTarget.style.boxShadow = '0 10px 25px rgba(0,0,0,0.1)';
                          }}
                          onMouseOut={(e) => {
                            e.currentTarget.style.transform = 'translateY(0)';
                            e.currentTarget.style.boxShadow = '0 4px 15px rgba(0,0,0,0.05)';
                          }}
                        >
                          {/* Header: status dot + label + is_new badge + fav */}
                          <div style={{ padding: '15px 20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #f1f5f9' }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: '8px', overflow: 'hidden' }}>
                              <div style={{ width: '10px', height: '10px', borderRadius: '50%', backgroundColor: dotColor, flexShrink: 0 }} />
                              <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-dark)', textTransform: 'uppercase', letterSpacing: '0.5px', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                                {statusVal}
                              </span>
                              {row.is_new && <span style={{ fontSize: '10px', backgroundColor: '#22c55e', color: 'white', padding: '2px 8px', borderRadius: '10px', fontWeight: 800, flexShrink: 0 }}>NUEVO</span>}
                            </div>
                            <button
                              onClick={(e) => { e.stopPropagation(); toggleFavorite(row); }}
                              style={{ background: 'none', border: 'none', padding: 0, cursor: 'pointer', display: 'flex', flexShrink: 0, marginLeft: '10px' }}
                            >
                              <Heart size={18} fill={favorites.has(idValue) ? 'var(--orange)' : 'none'} color={favorites.has(idValue) ? 'var(--orange)' : 'var(--text-light)'} />
                            </button>
                          </div>

                          {/* Content */}
                          <div style={{ padding: '20px', flexGrow: 1, display: 'flex', flexDirection: 'column' }}>
                            {/* Meta subtitle (type • region) */}
                            {metaParts.length > 0 && (
                              <div style={{ fontSize: '11px', color: 'var(--primary)', fontWeight: 800, marginBottom: '10px', textTransform: 'uppercase', letterSpacing: '0.3px', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                                {metaParts.join(' • ')}
                              </div>
                            )}

                            {/* Title */}
                            <h3 style={{
                              fontSize: '16px', fontWeight: 'bold', color: 'var(--text-dark)', lineHeight: '1.4',
                              marginBottom: '15px', display: '-webkit-box', WebkitLineClamp: 3,
                              WebkitBoxOrient: 'vertical', overflow: 'hidden', margin: '0 0 15px 0'
                            }}>
                              {titleVal || idValue}
                            </h3>

                            {/* Date and entity at the bottom */}
                            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', marginTop: 'auto' }}>
                              {dateVal && (
                                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--text-light)', fontSize: '13px' }}>
                                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                                  <span>{dateVal}</span>
                                </div>
                              )}
                              {entityVal && (
                                <div style={{ fontSize: '13px', color: 'var(--text-light)', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                                  <span style={{ fontWeight: 600 }}>{entityLabel}:</span>{' '}{entityVal}
                                </div>
                              )}
                            </div>
                          </div>

                          {/* Footer */}
                          <div style={{
                            padding: '12px 20px', backgroundColor: '#f8fafc', borderTop: '1px solid #f1f5f9',
                            display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '6px',
                            fontSize: '13px', fontWeight: 700, color: 'var(--primary)'
                          }}>
                            <Eye size={15} />
                            <span>VER DETALLES COMPLETOS</span>
                          </div>
                        </div>
                      );
                    })}
                  </div>

                  {/* Pagination */}
                  {totalCardPages > 1 && (
                    <div style={{ display: 'flex', justifyContent: 'center', gap: '15px', alignItems: 'center', marginTop: '20px' }}>
                      <button
                        onClick={() => { setCardPage(p => Math.max(1, p - 1)); window.scrollTo({ top: 0, behavior: 'smooth' }); }}
                        disabled={cardPage === 1}
                        style={{
                          padding: '8px 16px', borderRadius: '8px', border: '1px solid var(--border)',
                          background: cardPage === 1 ? '#f1f5f9' : 'white',
                          cursor: cardPage === 1 ? 'not-allowed' : 'pointer',
                          fontWeight: 600, color: 'var(--text-dark)', fontSize: '13px'
                        }}
                      >
                        Anterior
                      </button>
                      <div style={{ display: 'flex', gap: '5px', fontSize: '14px' }}>
                        <span style={{ fontWeight: 'bold', color: 'var(--primary)' }}>{cardPage}</span>
                        <span style={{ color: 'var(--text-light)' }}>de {totalCardPages}</span>
                      </div>
                      <button
                        onClick={() => { setCardPage(p => Math.min(totalCardPages, p + 1)); window.scrollTo({ top: 0, behavior: 'smooth' }); }}
                        disabled={cardPage === totalCardPages}
                        style={{
                          padding: '8px 16px', borderRadius: '8px', border: '1px solid var(--border)',
                          background: cardPage === totalCardPages ? '#f1f5f9' : 'white',
                          cursor: cardPage === totalCardPages ? 'not-allowed' : 'pointer',
                          fontWeight: 600, color: 'var(--text-dark)', fontSize: '13px'
                        }}
                      >
                        Siguiente
                      </button>
                    </div>
                  )}
                </>
              )}
            </>
          )}
        </>
      )}

      {/* Card Detail Modal */}
      {selectedCard && (
        <div style={{
          position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
          backgroundColor: 'rgba(15, 23, 42, 0.6)', zIndex: 2000,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          padding: '20px', backdropFilter: 'blur(4px)'
        }} onClick={() => setSelectedCard(null)}>
          <div style={{
            backgroundColor: 'white', borderRadius: '20px', padding: '40px',
            maxWidth: '700px', width: '100%', maxHeight: '90vh', overflowY: 'auto',
            boxShadow: '0 25px 50px -12px rgba(0,0,0,0.25)', position: 'relative'
          }} onClick={e => e.stopPropagation()}>
            <button
              onClick={() => setSelectedCard(null)}
              style={{ position: 'absolute', top: '20px', right: '20px', background: '#f1f5f9', border: 'none', borderRadius: '50%', width: '36px', height: '36px', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-dark)' }}
            >
              <X size={20} />
            </button>

            {selectedCard.is_new && (
              <div style={{ marginBottom: '15px' }}>
                <span style={{ fontSize: '11px', backgroundColor: '#22c55e', color: 'white', padding: '3px 10px', borderRadius: '10px', fontWeight: 800 }}>NUEVO</span>
              </div>
            )}

            <h2 style={{ fontSize: '22px', fontWeight: 'bold', color: 'var(--text-dark)', lineHeight: '1.3', marginBottom: '25px', paddingRight: '40px' }}>
              {selectedCard[
                selectedCard.Caratula ? 'Caratula' :
                selectedCard.Nombre_de_Proyecto ? 'Nombre_de_Proyecto' :
                selectedCard.normativa ? 'normativa' :
                selectedCard._nombre ? '_nombre' :
                selectedCard.unidad_fiscalizable ? 'unidad_fiscalizable' :
                activeColumns[0]?.field || ''
              ] || '—'}
            </h2>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '20px', marginBottom: '30px' }}>
              {activeColumns
                .filter(c => c.field !== 'rowNumber' && c.field !== 'fav' && c.field !== 'accion')
                .map(col => {
                  let val = selectedCard[col.field];
                  if (!val) return null;
                  if (col.field.toLowerCase() === 'fecha' || col.field.toLowerCase() === 'fecha_agregado') {
                    val = String(val).split(' ')[0];
                  }
                  return (
                    <div key={col.field}>
                      <div style={{ fontSize: '11px', fontWeight: 800, color: 'var(--primary)', textTransform: 'uppercase', marginBottom: '4px' }}>{col.headerName}</div>
                      <div style={{ fontSize: '14px', color: 'var(--text-dark)', fontWeight: 500, wordBreak: 'break-word' }}>{val}</div>
                    </div>
                  );
                })}
            </div>

            {(isFavoritesPage ? selectedCard._action : selectedCard[effectiveActionField]) && (
              <div style={{ paddingTop: '25px', borderTop: '1px solid #f1f5f9', display: 'flex', justifyContent: 'flex-end' }}>
                <a
                  href={isFavoritesPage ? selectedCard._action : selectedCard[effectiveActionField]}
                  target="_blank"
                  rel="noopener noreferrer"
                  style={{
                    display: 'inline-flex', alignItems: 'center', gap: '10px',
                    padding: '12px 25px', backgroundColor: 'var(--primary)', color: 'white',
                    textDecoration: 'none', borderRadius: '10px', fontWeight: 700,
                    boxShadow: '0 4px 6px -1px rgba(0,0,0,0.1)'
                  }}
                >
                  <Eye size={18} />
                  VER FICHA OFICIAL
                </a>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};

export default ReportLayout;
