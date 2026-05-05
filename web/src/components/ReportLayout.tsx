import React, { useState, useEffect, useMemo } from 'react';
import * as XLSX from 'xlsx';
import { Search, ChevronDown, ChevronUp, Trash2, LayoutDashboard, Download, Heart, Eye } from 'lucide-react';
import { DataGrid } from '@mui/x-data-grid';
import type { GridColDef, GridRenderCellParams } from '@mui/x-data-grid';
import { esES } from '@mui/x-data-grid/locales';

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
  Tribunales: 'Rol',
  pertinencias: 'Expediente',
  // normativas: removed to fallback to composite ID
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

import { useAuth } from '../context/AuthContext';

const ReportLayout: React.FC<ReportLayoutProps> = ({ title, description, listTitle, tableName, columnConfig, idField, actionField, isFavoritesPage, children }) => {
  const { token, user } = useAuth();
  const [filtersOpen, setFiltersOpen] = useState(false);
  const [data, setData] = useState<LegalItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [favorites, setFavorites] = useState<Set<string>>(new Set());
  const [search, setSearch] = useState('');
  const [filterEstados, setFilterEstados] = useState<Set<string>>(new Set()); // Deprecated, replaced by columnFilters
  const [columnFilters, setColumnFilters] = useState<Record<string, string>>({});
  const [dateRange, setDateRange] = useState({ start: '', end: '' });
  const [activeTab, setActiveTab] = useState('reporte');

  const toggleFilter = (setFn: React.Dispatch<React.SetStateAction<Set<string>>>, value: string) => {
    setFn(prev => {
      const next = new Set(prev);
      if (next.has(value)) next.delete(value);
      else next.add(value);
      return next;
    });
  };
  
  // Manual favorite form state
  const [manualFav, setManualFav] = useState({ id: '', nombre: '', fuente: '', accion: '' });
  
  // To apply filters only when "APLICAR FILTRO" is clicked
  const [appliedColumnFilters, setAppliedColumnFilters] = useState<Record<string, string>>({});
  const [appliedDateRange, setAppliedDateRange] = useState({ start: '', end: '' });

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

  // Determinar campos ID y acción
  const effectiveIdField = idField || (tableName ? TABLE_ID_FIELDS[tableName] : 'link') || 'link';
  const effectiveActionField = actionField || (tableName ? TABLE_ACTION_FIELDS[tableName] : 'link') || 'link';

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        // Fetch favorites list first
        const favRes = await fetch('/api/favorites', {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        const favJson = await favRes.json();
        const favSet = new Set<string>(favJson.map((f: any) => f.id_o_link));
        setFavorites(favSet);

        if (isFavoritesPage) {
          // If on favorites page, just use the fetched favorites data
          const favData = favJson.map((f: any) => ({
            _id: f.id_o_link,
            _nombre: f.nombre,
            _fuente: f.fuente,
            fecha_agregado: f.fecha_agregado,
            _action: f.accion || (f.id_o_link.startsWith('http') ? f.id_o_link : '')
          }));
          setData(favData);
        } else if (tableName) {
          const res = await fetch(`/api/data/${tableName}?limit=50000`, {
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

  let finalData = data;
  if (isFavoritesPage) {
    finalData = data;
  }

  const filteredData = finalData.filter(item => {
    // Búsqueda global en todos los campos de texto
    const matchesSearch = !search || Object.values(item).some(val => 
      typeof val === 'string' && val.toLowerCase().includes(search.toLowerCase())
    );
    
    // Filtros de columnas
    const matchesColumns = Object.entries(appliedColumnFilters).every(([field, filterValue]) => {
      if (!filterValue) return true;
      const itemVal = item[field];
      if (!itemVal) return false;
      
      const strVal = String(itemVal).toLowerCase();
      
      // For categorical fields, check for exact match if it was selected from a dropdown (space separated logic was flawed)
      const categoricalFields = ['estado', 'Estado', 'Estado_Procesal', 'organismo', 'Tribunal', 'categoria', 'region'];
      if (categoricalFields.includes(field)) {
        // If it's a multiple preference (space separated), check for any exact match
        const selectedOptions = filterValue.toLowerCase().split('  '); // Use double space or just exact match?
        // Let's use simple logic: if it's one of the unique options, check exact.
        // Actually, the leak happens because of .includes().
        // For preference terms, we should match at least one full term.
        const terms = filterValue.split(';').map(t => t.trim().toLowerCase()).filter(Boolean);
        if (terms.length > 0) {
          return terms.some(t => strVal === t || strVal.includes(t));
        }
      }

      return strVal.includes(filterValue.toLowerCase());
    });

    // Filtro de rango de fechas
    let matchesDate = true;
    if (appliedDateRange.start || appliedDateRange.end) {
      // Intentamos usar activoColumns si ya está computado, o adivinar el campo fecha
      const dateFieldNames = ['fecha', 'Fecha', 'fecha_agregado'];
      const dateField = dateFieldNames.find(f => f in item);
      if (dateField) {
        const itemDateStr = String(item[dateField] || '');
        if (itemDateStr) {
          let itemDate: Date | null = null;
          if (itemDateStr.includes('-')) {
            const datePart = itemDateStr.split(' ')[0];
            const parts = datePart.split('-');
            if (parts.length === 3) {
              if (parts[0].length === 4) {
                itemDate = new Date(parseInt(parts[0]), parseInt(parts[1]) - 1, parseInt(parts[2]));
              } else {
                itemDate = new Date(parseInt(parts[2]), parseInt(parts[1]) - 1, parseInt(parts[0]));
              }
            }
          } else {
             itemDate = new Date(itemDateStr);
          }
          
          if (itemDate && !isNaN(itemDate.getTime())) {
            if (appliedDateRange.start) {
              const start = new Date(appliedDateRange.start);
              if (itemDate < start) matchesDate = false;
            }
            if (appliedDateRange.end) {
              const end = new Date(appliedDateRange.end);
              end.setDate(end.getDate() + 1);
              if (itemDate >= end) matchesDate = false;
            }
          }
        }
      }
    }
    
    return matchesSearch && matchesColumns && matchesDate;
  });

  const handleApplyFilters = () => {
    setAppliedColumnFilters({ ...columnFilters });
    setAppliedDateRange({ ...dateRange });
  };

  const handleClearFilters = () => {
    setColumnFilters({});
    setDateRange({ start: '', end: '' });
    setSearch('');
    setAppliedColumnFilters({});
    setAppliedDateRange({ start: '', end: '' });
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
      { field: 'rowNumber', headerName: 'Nº', width: 60, filterable: false },
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
        valueGetter: isDateField ? (value: any) => {
          if (!value) return null;
          const str = String(value);
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
          <a href={link} target="_blank" rel="noopener noreferrer" style={{color: 'var(--primary)', display: 'flex', alignItems: 'center', height: '100%'}}>
            <Eye size={20} />
          </a>
        );
      }
    });

    return cols;
  }, [favorites, activeColumns, effectiveIdField, effectiveActionField, isFavoritesPage]);

  return (
    <div className="report-container">
      <div className="report-header-text">
        <h1 className="report-title">Reporte de {title}</h1>
        <p className="report-description">{description}</p>
      </div>

      <div className="report-tabs">
        <div className={`tab ${activeTab === 'reporte' ? 'active' : 'inactive'}`} onClick={() => setActiveTab('reporte')}>
          <span className="tab-icon">📖</span> Reporte de {title}
        </div>
        <div className={`tab ${activeTab === 'dashboard' ? 'active' : 'inactive'}`} onClick={() => setActiveTab('dashboard')}>
          <LayoutDashboard size={18} /> Dashboard
        </div>
      </div>

      {activeTab === 'dashboard' ? (
        <div style={{ padding: '40px', textAlign: 'center', color: 'var(--text-light)', border: '1px solid var(--border)', borderRadius: '12px', marginTop: '20px' }}>
          <h2>Dashboards en proceso</h2>
          <p>Próximamente visualizarás métricas detalladas aquí.</p>
        </div>
      ) : (
        <>
          <div className="filter-section">
        <div className="filter-top">
          <div className="search-bar">
            <Search className="search-icon" size={18} />
            <input 
              type="text" 
              placeholder="Buscar por palabra clave" 
              value={search}
              onChange={e => setSearch(e.target.value)}
            />
          </div>
          
          <div className="filter-actions">
            <button 
              className={`toggle-filter-btn ${filtersOpen ? 'open' : 'closed'}`}
              onClick={() => setFiltersOpen(!filtersOpen)}
            >
              {filtersOpen ? 'Minimizar Filtro' : 'Desplegar Filtro'} 
              {filtersOpen ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
            </button>
            <button className="trash-btn" onClick={handleClearFilters}>
              <Trash2 size={18} />
            </button>
          </div>
        </div>

        {filtersOpen && (
          <div className="filter-dropdowns">
            <div className="filter-grid" style={{ display: 'flex', gap: '20px', flexWrap: 'wrap' }}>
              {activeColumns
                .filter(c => c.field !== 'rowNumber' && c.field !== 'fav' && c.field !== 'accion' && c.field !== effectiveIdField && c.field.toLowerCase() !== 'fecha' && c.field.toLowerCase() !== 'fecha_agregado')
                .map(col => {
                  const categoricalFields = ['estado', 'Estado', 'Estado_Procesal', 'organismo', 'Tribunal', 'categoria', 'region'];
                  const isCategorical = categoricalFields.includes(col.field);
                  
                  if (isCategorical) {
                    const options = Array.from(new Set(data.map(item => item[col.field]).filter(Boolean))).sort();
                    return (
                      <div key={col.field} style={{ flex: '1 1 200px' }}>
                        <h4 style={{ marginBottom: '10px', color: 'var(--text-dark)' }}>Filtrar por {col.headerName}</h4>
                        <select 
                          className="filter-select" 
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
                    <div key={col.field} style={{ flex: '1 1 200px' }}>
                      <h4 style={{ marginBottom: '10px', color: 'var(--text-dark)' }}>Filtrar por {col.headerName}</h4>
                      <input type="text" className="filter-select" value={columnFilters[col.field] || ''} onChange={(e) => setColumnFilters({...columnFilters, [col.field]: e.target.value})} placeholder={`Buscar ${col.headerName.toLowerCase()}`} />
                    </div>
                  );
              })}
              {activeColumns.some(c => c.field.toLowerCase() === 'fecha' || c.field.toLowerCase() === 'fecha_agregado') && (
                <div style={{ flex: '1 1 300px' }}>
                  <h4 style={{ marginBottom: '10px', color: 'var(--text-dark)' }}>Rango de Fechas</h4>
                  <div style={{ display: 'flex', gap: '10px' }}>
                    <input type="date" className="filter-select" value={dateRange.start} onChange={(e) => setDateRange({...dateRange, start: e.target.value})} />
                    <span style={{ alignSelf: 'center' }}>-</span>
                    <input type="date" className="filter-select" value={dateRange.end} onChange={(e) => setDateRange({...dateRange, end: e.target.value})} />
                  </div>
                </div>
              )}
            </div>
            {children}
            <div className="filter-apply-row">
              <button className="btn-primary" onClick={handleApplyFilters}>
                <span style={{marginRight: 6}}>⚖</span> APLICAR FILTRO
              </button>
              <button className="btn-secondary" onClick={handleClearFilters}>
                <Trash2 size={14} style={{marginRight: 6}}/> LIMPIAR FILTRO
              </button>
            </div>
          </div>
        )}
      </div>

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
          localeText={esES.components.MuiDataGrid.defaultProps.localeText}
          initialState={{
            pagination: { paginationModel: { pageSize: 100 } },
          }}
          pageSizeOptions={[10, 25, 50, 100]}
          disableRowSelectionOnClick
          loading={loading}
          sx={{
            border: 'none',
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
