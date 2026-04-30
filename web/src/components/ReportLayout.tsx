import React, { useState, useEffect, useMemo } from 'react';
import { Search, ChevronDown, ChevronUp, Trash2, LayoutDashboard, Download, Star, Heart, Eye } from 'lucide-react';
import { DataGrid } from '@mui/x-data-grid';
import type { GridColDef, GridRenderCellParams } from '@mui/x-data-grid';
import { esES } from '@mui/x-data-grid/locales';

export interface LegalItem {
  link: string;
  nombre: string;
  fecha: string;
  estado: string;
  tipo: string;
  fuente: string;
  fecha_scraping: string;
}

interface ReportLayoutProps {
  title: string;
  description: string;
  listTitle: string;
  filterFn?: (item: LegalItem) => boolean;
  isFavoritesPage?: boolean;
  children?: React.ReactNode;
}

const ReportLayout: React.FC<ReportLayoutProps> = ({ title, description, listTitle, filterFn, isFavoritesPage, children }) => {
  const [filtersOpen, setFiltersOpen] = useState(false);
  const [data, setData] = useState<LegalItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [favorites, setFavorites] = useState<Set<string>>(new Set());
  const [search, setSearch] = useState('');
  const [filterEstado, setFilterEstado] = useState('');
  const [filterOrganismo, setFilterOrganismo] = useState('');
  
  // To apply filters only when "APLICAR FILTRO" is clicked
  const [appliedFilters, setAppliedFilters] = useState({ estado: '', organismo: '' });

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      try {
        const res = await fetch('/api/legal');
        const json = await res.json();
        // Don't filter here if it's favorites page, filter later using the set
        let filtered = json;
        if (filterFn && !isFavoritesPage) {
          filtered = json.filter(filterFn);
        }
        setData(filtered);
      } catch (err) {
        console.error("Error fetching data:", err);
      }
      setLoading(false);
    };

    const fetchFavorites = async () => {
      try {
        const res = await fetch('/api/favorites');
        const json = await res.json();
        setFavorites(new Set(json.map((f: any) => f.id_o_link)));
      } catch(err) {
        console.error("Error fetching favs:", err);
      }
    };

    fetchData();
    fetchFavorites();
  }, [filterFn, isFavoritesPage]);

  const toggleFavorite = async (item: LegalItem) => {
    const isFav = favorites.has(item.link);
    try {
      if (isFav) {
        await fetch(`/api/favorites/${encodeURIComponent(item.link)}`, { method: 'DELETE' });
        setFavorites(prev => {
          const next = new Set(prev);
          next.delete(item.link);
          return next;
        });
      } else {
        await fetch('/api/favorites', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ id_o_link: item.link, fuente: item.fuente, nombre: item.nombre })
        });
        setFavorites(prev => {
          const next = new Set(prev);
          next.add(item.link);
          return next;
        });
      }
    } catch(err) {
      console.error("Fav error", err);
    }
  };

  const uniqueEstados = useMemo(() => Array.from(new Set(data.map(item => item.estado).filter(Boolean))), [data]);
  const uniqueOrganismos = useMemo(() => Array.from(new Set(data.map(item => item.fuente).filter(Boolean))), [data]);

  let finalData = data;
  if (isFavoritesPage) {
    finalData = data.filter(item => favorites.has(item.link));
  }

  const filteredData = finalData.filter(item => {
    const matchesSearch = item.nombre?.toLowerCase().includes(search.toLowerCase()) || 
                          item.estado?.toLowerCase().includes(search.toLowerCase());
    const matchesEstado = appliedFilters.estado ? item.estado === appliedFilters.estado : true;
    const matchesOrganismo = appliedFilters.organismo ? item.fuente === appliedFilters.organismo : true;
    
    return matchesSearch && matchesEstado && matchesOrganismo;
  });

  const handleApplyFilters = () => {
    setAppliedFilters({ estado: filterEstado, organismo: filterOrganismo });
  };

  const handleClearFilters = () => {
    setFilterEstado('');
    setFilterOrganismo('');
    setSearch('');
    setAppliedFilters({ estado: '', organismo: '' });
  };

  const downloadCSV = () => {
    if (filteredData.length === 0) return;
    const headers = ['Nº', 'Fecha', 'Nombre', 'Estado', 'Organismo', 'Link'];
    const csvRows = [headers.join(',')];
    
    filteredData.forEach((row, idx) => {
      const escapedNombre = `"${(row.nombre || '').replace(/"/g, '""')}"`;
      csvRows.push(`${idx + 1},${row.fecha},${escapedNombre},${row.estado || ''},${row.fuente},${row.link}`);
    });
    
    const blob = new Blob([csvRows.join('\n')], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `${title.toLowerCase().replace(/\s+/g, '_')}_export.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const rows = useMemo(() => filteredData.map((item, index) => ({
    ...item,
    id: item.link || String(index),
    rowNumber: index + 1
  })), [filteredData]);

  const columns: GridColDef[] = useMemo(() => [
    { field: 'rowNumber', headerName: 'Nº', width: 60, filterable: false },
    { 
      field: 'fav', 
      headerName: 'Fav', 
      width: 60, 
      sortable: false, 
      filterable: false,
      renderCell: (params: GridRenderCellParams) => (
        <div style={{display: 'flex', alignItems: 'center', height: '100%'}}>
          <Heart 
            size={18} 
            style={{ cursor: 'pointer', fill: favorites.has(params.row.link) ? 'var(--orange)' : 'none', color: favorites.has(params.row.link) ? 'var(--orange)' : 'var(--text-light)' }} 
            onClick={() => toggleFavorite(params.row)}
          />
        </div>
      )
    },
    { field: 'fecha', headerName: 'Fecha', width: 120 },
    { field: 'nombre', headerName: listTitle, flex: 1, minWidth: 200 },
    { field: 'estado', headerName: 'Estado', width: 150 },
    { field: 'fuente', headerName: 'Organismo', width: 150 },
    { 
      field: 'accion', 
      headerName: 'Acción', 
      width: 80, 
      sortable: false, 
      filterable: false,
      renderCell: (params: GridRenderCellParams) => (
        <a href={params.row.link} target="_blank" rel="noopener noreferrer" style={{color: 'var(--primary)', display: 'flex', alignItems: 'center', height: '100%'}}>
          <Eye size={20} />
        </a>
      )
    }
  ], [favorites, listTitle]);

  return (
    <div className="report-container">
      <div className="report-header-text">
        <h1 className="report-title">Reporte de {title}</h1>
        <p className="report-description">{description}</p>
      </div>

      <div className="report-tabs">
        <div className="tab active">
          <span className="tab-icon">📖</span> Reporte de {title}
        </div>
        <div className="tab inactive">
          <LayoutDashboard size={18} /> Dashboard
        </div>
      </div>

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
            <div className="filter-grid">
              <select className="filter-select" value={filterEstado} onChange={e => setFilterEstado(e.target.value)}>
                <option value="">Todos los Estados</option>
                {uniqueEstados.map((est, i) => <option key={i} value={est}>{est}</option>)}
              </select>
              <select className="filter-select" value={filterOrganismo} onChange={e => setFilterOrganismo(e.target.value)}>
                <option value="">Todos los Organismos</option>
                {uniqueOrganismos.map((org, i) => <option key={i} value={org}>{org}</option>)}
              </select>
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

      <div className="watchlist-action">
        <button className="btn-watchlist">
          <Star size={14} style={{marginRight: 6}} /> Aplicar Watchlist
        </button>
      </div>

      <div className="list-header">
        <h2 className="list-title">Listado de {listTitle}</h2>
        <div className="list-meta" style={{display: 'flex', gap: '15px', alignItems: 'center'}}>
          <span>Total de registros: {filteredData.length}</span>
          <button onClick={downloadCSV} style={{display: 'flex', alignItems: 'center', gap: '6px', background: 'none', border: 'none', color: 'var(--primary)', cursor: 'pointer', fontWeight: 600}}>
            <Download size={16} /> Descargar CSV
          </button>
        </div>
      </div>

      <div className="table-container" style={{ height: 600, width: '100%', backgroundColor: 'white', borderRadius: '12px', padding: '10px' }}>
        <DataGrid
          rows={rows}
          columns={columns}
          localeText={esES.components.MuiDataGrid.defaultProps.localeText}
          initialState={{
            pagination: { paginationModel: { pageSize: 10 } },
          }}
          pageSizeOptions={[10, 25, 50]}
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
    </div>
  );
};

export default ReportLayout;

