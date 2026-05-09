import React, { useState, useEffect, useMemo } from 'react';
import * as XLSX from 'xlsx';
import { Search, X, Filter, ChevronDown, ChevronUp, LayoutDashboard, Download, Heart, Eye, BookOpen } from 'lucide-react';
import { DataGrid } from '@mui/x-data-grid';
import type { GridColDef, GridRenderCellParams } from '@mui/x-data-grid';
import { esES } from '@mui/x-data-grid/locales';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';
import DashboardView from './DashboardView';

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


const ReportLayout: React.FC<ReportLayoutProps> = ({ 
  title, description, listTitle, tableName, category, columnConfig, idField, actionField, isFavoritesPage, children 
}) => {
  const { token, user } = useAuth();
  const { markItemViewed, refreshCategory, markAllRead, setCategoryActive } = useNotifications();
  const [filtersOpen, setFiltersOpen] = useState(false);
  const [data, setData] = useState<LegalItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [favorites, setFavorites] = useState<Set<string>>(new Set());
  const [search, setSearch] = useState('');
  const [columnFilters, setColumnFilters] = useState<Record<string, string>>({});
  const [dateRange, setDateRange] = useState({ start: '', end: '' });
  const [activeTab, setActiveTab] = useState('reporte');

  const [appliedColumnFilters, setAppliedColumnFilters] = useState<Record<string, string>>({});
  const [appliedDateRange, setAppliedDateRange] = useState({ start: '', end: '' });
  const [appliedSearch, setAppliedSearch] = useState('');

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
    } catch(err) {
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
      } catch (e) {}
    }
  }, [user, tableName, token]);

  const effectiveIdField = idField || (tableName ? TABLE_ID_FIELDS[tableName] : 'link') || 'link';
  const effectiveActionField = actionField || (tableName ? TABLE_ACTION_FIELDS[tableName] : 'link') || 'link';

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const favRes = await fetch('/api/favorites', {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        const favJson = await favRes.json();
        const favSet = new Set<string>(favJson.map((f: any) => f.id_o_link));
        setFavorites(favSet);

        if (isFavoritesPage) {
          const favData = favJson.map((f: any) => ({
            _id: f.id_o_link,
            _nombre: f.nombre,
            _fuente: f.fuente,
            fecha_agregado: f.fecha_agregado,
            _action: f.accion || (f.id_o_link.startsWith('http') ? f.id_o_link : '')
          }));
          setData(favData);
        } else if (tableName) {
          const res = await fetch(`/api/data/${tableName}?limit=5000`, {
            headers: { 'Authorization': `Bearer ${token}` }
          });
          const json = await res.json();
          setData(Array.isArray(json) ? json : []);
        }
      } catch (err) {
        console.error("Error fetching data:", err);
      }
      setLoading(false);
    };

    fetchData();
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
    } catch(err) {
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

  const rows = useMemo(() => filteredData.map((item, index) => {
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
            <div style={{display: 'flex', alignItems: 'center', gap: '8px', height: '100%'}}>
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
            <div style={{display: 'flex', alignItems: 'center', height: '100%'}}>
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
        
        const handleActionClick = () => {
          if (category && !isFavoritesPage) {
            const itemId = params.row[effectiveIdField] || '';
            markItemViewed(category, String(itemId));
            
            // Actualizar estado local para quitar etiqueta "Nuevo" inmediatamente
            setData(prev => prev.map(item => {
              const currentId = item[effectiveIdField] || '';
              if (String(currentId) === String(itemId)) {
                return { ...item, is_new: false };
              }
              return item;
            }));
          }
        };

        return (
          <a 
            href={link} 
            target="_blank" 
            rel="noopener noreferrer" 
            style={{color: 'var(--primary)', display: 'flex', alignItems: 'center', height: '100%'}}
            onClick={handleActionClick}
          >
            <Eye size={20} />
          </a>
        );
      }
    });

    return cols;
  }, [favorites, activeColumns, effectiveIdField, effectiveActionField, isFavoritesPage]);

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

        <div style={{ color: 'var(--text-light)', fontSize: '14px', marginLeft: 'auto' }}>
          {filteredData.length} resultados encontrados
        </div>
      </div>

      {activeTab === 'dashboard' ? (
        <DashboardView tableName={tableName || ''} title={title} />
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
                          <select 
                            style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)', fontSize: '14px' }}
                            value={columnFilters[col.field] || ''} 
                            onChange={(e) => setColumnFilters({...columnFilters, [col.field]: e.target.value})}
                          >
                            <option value="">Todos</option>
                            {options.map(opt => <option key={opt} value={opt}>{opt}</option>)}
                          </select>
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
                          onChange={(e) => setColumnFilters({...columnFilters, [col.field]: e.target.value})} 
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
                        onChange={(e) => setColumnFilters({...columnFilters, 'expediente_year': e.target.value})}
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
                          onChange={(e) => setColumnFilters({...columnFilters, 'expediente_tipo': e.target.value})}
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
                      <input type="date" style={{ flex: 1, padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }} value={dateRange.start} onChange={(e) => setDateRange({...dateRange, start: e.target.value})} />
                      <span style={{ alignSelf: 'center' }}>-</span>
                      <input type="date" style={{ flex: 1, padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }} value={dateRange.end} onChange={(e) => setDateRange({...dateRange, end: e.target.value})} />
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
              <input type="text" className="filter-select" required placeholder="Ej: R-157-2026" value={manualFav.id} onChange={e => setManualFav({...manualFav, id: e.target.value})} />
            </div>
            <div style={{ flex: '2 1 200px' }}>
              <label style={{ display: 'block', fontSize: '12px', marginBottom: '5px', color: 'var(--text-light)', fontWeight: 600 }}>Nombre / Descripción</label>
              <input type="text" className="filter-select" required placeholder="Ej: Proyecto Hidroeléctrico..." value={manualFav.nombre} onChange={e => setManualFav({...manualFav, nombre: e.target.value})} />
            </div>
            <div style={{ flex: '1 1 150px' }}>
              <label style={{ display: 'block', fontSize: '12px', marginBottom: '5px', color: 'var(--text-light)', fontWeight: 600 }}>Fuente</label>
              <select className="filter-select" required value={manualFav.fuente} onChange={e => setManualFav({...manualFav, fuente: e.target.value})}>
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
              <input type="url" className="filter-select" placeholder="https://..." value={manualFav.accion} onChange={e => setManualFav({...manualFav, accion: e.target.value})} />
            </div>
            <button type="submit" className="btn-primary" style={{ height: '42px', borderRadius: '6px' }}>
              + Agregar
            </button>
          </form>
        </div>
      )}

      <div className="list-header">
        <h2 className="list-title">Listado de {listTitle}</h2>
        <div className="list-meta" style={{display: 'flex', gap: '15px', alignItems: 'center'}}>
          {!isFavoritesPage && category && (
            <button 
              onClick={async () => {
                await markAllRead(category);
                setData(prev => prev.map(item => ({ ...item, is_new: false })));
              }}
              className="btn-mark-read"
              style={{
                fontSize: '12px',
                padding: '4px 8px',
                borderRadius: '4px',
                border: '1px solid var(--primary)',
                color: 'var(--primary)',
                background: 'white',
                cursor: 'pointer'
              }}
            >
              Marcar todo como leído
            </button>
          )}
          <span>Total de registros: {filteredData.length}</span>
          <button onClick={downloadExcel} style={{display: 'flex', alignItems: 'center', gap: '6px', background: 'none', border: 'none', color: 'var(--primary)', cursor: 'pointer', fontWeight: 600}}>
            <Download size={16} /> Descargar XLSX
          </button>
        </div>
      </div>

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
        </>
      )}
    </div>
  );
};

export default ReportLayout;
