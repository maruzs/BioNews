import React, { useState, useEffect, useMemo } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';
import { Heart, Calendar, FileText, Search, X, Filter, ChevronDown, ChevronUp, LayoutDashboard, BookOpen, Table, LayoutGrid } from 'lucide-react';
import { DataGrid } from '@mui/x-data-grid';
import { Autocomplete, TextField } from '@mui/material';
import { esES } from '@mui/x-data-grid/locales';
import DashboardManager from '../dashboard/DashboardManager';

interface SEAEvaluado {
  id: string;
  nombre: string;
  titular: string;
  via_ingreso: string;
  estado_proyecto: string;
  razon_ingreso: string;
  fecha_presentacion: string;
  subestado_proyecto: string;
  tipo_proyecto: string;
  categoria_economica: string;
  region: string;
  url: string;
  fecha_scraping: string;
  is_new: boolean;
}

const SEAEvaluadosPage = () => {
  const { token } = useAuth();
  const { refreshCategory, setCategoryActive } = useNotifications();
  const [data, setData] = useState<SEAEvaluado[]>([]);
  const [loading, setLoading] = useState(true);
  const [backgroundLoading, setBackgroundLoading] = useState(false);
  const [totalRecords, setTotalRecords] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [selectedItem, setSelectedItem] = useState<SEAEvaluado | null>(null);
  const [favorites, setFavorites] = useState<Set<string>>(new Set());

  // Modal state
  const [showModal, setShowModal] = useState(false);

  // Filters state
  const [searchTerm, setSearchTerm] = useState('');
  const [filterTitular, setFilterTitular] = useState('all');
  const [filterVia, setFilterVia] = useState('all');
  const [filterEstado, setFilterEstado] = useState('all');
  const [filterRegion, setFilterRegion] = useState('all');
  const [filterTipo, setFilterTipo] = useState('all');
  const [filterCategoria, setFilterCategoria] = useState('all');
  const [dateFrom, setDateFrom] = useState('');
  const [dateTo, setDateTo] = useState('');
  const [showFilters, setShowFilters] = useState(false);

  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 12;

  const [activeTab, setActiveTab] = useState('reporte');
  const [viewMode, setViewMode] = useState<'table' | 'cards'>(
    typeof window !== 'undefined' && window.innerWidth < 768 ? 'cards' : 'table'
  );

  const [appliedFilters, setAppliedFilters] = useState({
    titular: 'all',
    via: 'all',
    estado: 'all',
    region: 'all',
    tipo: 'all',
    categoria: 'all',
    dateFrom: '',
    dateTo: '',
    search: ''
  });

  const handleApplyFilters = () => {
    setAppliedFilters({
      titular: filterTitular,
      via: filterVia,
      estado: filterEstado,
      region: filterRegion,
      tipo: filterTipo,
      categoria: filterCategoria,
      dateFrom: dateFrom,
      dateTo: dateTo,
      search: searchTerm
    });
    setCurrentPage(1);
  };

  const handleClearFilters = () => {
    setSearchTerm('');
    setFilterTitular('all');
    setFilterVia('all');
    setFilterEstado('all');
    setFilterRegion('all');
    setFilterTipo('all');
    setFilterCategoria('all');
    setDateFrom('');
    setDateTo('');
    setAppliedFilters({
      titular: 'all',
      via: 'all',
      estado: 'all',
      region: 'all',
      tipo: 'all',
      categoria: 'all',
      dateFrom: '',
      dateTo: '',
      search: ''
    });
    setCurrentPage(1);
  };

  const fetchData = async () => {
    setLoading(true);
    setBackgroundLoading(true);
    setTotalRecords(null);
    try {
      // 1. Fetch total count
      try {
        const countRes = await fetch('/api/data/sea_proyectos_evaluados/count', {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        const countJson = await countRes.json();
        setTotalRecords(countJson.count || 0);
      } catch (e) {
        console.error("Error fetching count:", e);
      }

      // 2. Fetch first 100 records
      const response = await fetch('/api/data/sea_proyectos_evaluados?limit=100', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (!response.ok) throw new Error('Error al obtener los datos');
      const result = await response.json();

      // Sort by date (descending)
      const sorted = (Array.isArray(result) ? result : []).sort((a, b) => {
        const dateA = a.fecha_presentacion.split('/').reverse().join('-');
        const dateB = b.fecha_presentacion.split('/').reverse().join('-');
        return dateB.localeCompare(dateA);
      });

      setData(sorted);
      setLoading(false);

      // 3. Fetch full dataset in the background
      fetch('/api/data/sea_proyectos_evaluados?limit=-1', {
        headers: { 'Authorization': `Bearer ${token}` }
      })
        .then(r => {
          if (!r.ok) throw new Error();
          return r.json();
        })
        .then(fullResult => {
          if (Array.isArray(fullResult)) {
            const sortedFull = fullResult.sort((a, b) => {
              const dateA = a.fecha_presentacion.split('/').reverse().join('-');
              const dateB = b.fecha_presentacion.split('/').reverse().join('-');
              return dateB.localeCompare(dateA);
            });
            setData(sortedFull);
            setBackgroundLoading(false);
          }
        })
        .catch(err => {
          console.error("Error in background fetch:", err);
          setBackgroundLoading(false);
        });

      // Load favorites
      const favRes = await fetch('/api/favorites', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const favJson = await favRes.json();
      setFavorites(new Set(favJson.map((f: any) => f.id_o_link)));

      refreshCategory('sea_proyectos_evaluados');
    } catch (err: any) {
      setError(err.message);
      setLoading(false);
      setBackgroundLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    setCategoryActive('sea_proyectos_evaluados', true);
    return () => {
      setCategoryActive('sea_proyectos_evaluados', false);
    };
  }, [token]);

  const toggleFavorite = async (e: React.MouseEvent, item: SEAEvaluado) => {
    e.stopPropagation();
    const isFav = favorites.has(item.id);
    try {
      if (isFav) {
        await fetch(`/api/favorites/${encodeURIComponent(item.id)}`, {
          method: 'DELETE',
          headers: { 'Authorization': `Bearer ${token}` }
        });
        setFavorites(prev => {
          const next = new Set(prev);
          next.delete(item.id);
          return next;
        });
      } else {
        await fetch('/api/favorites', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
          body: JSON.stringify({
            id_o_link: item.id,
            fuente: 'SEA Evaluados',
            nombre: item.nombre,
            accion: item.url
          })
        });
        setFavorites(prev => new Set(prev).add(item.id));
      }
    } catch (err) {
      console.error("Error toggling favorite:", err);
    }
  };

  const handleOpenModal = (item: SEAEvaluado) => {
    setSelectedItem(item);
    setShowModal(true);
  };

  // Generate filter options
  const options = useMemo(() => {
    return {
      titulares: Array.from(new Set(data.map(i => i.titular).filter(Boolean))).sort(),
      vias: Array.from(new Set(data.map(i => i.via_ingreso).filter(Boolean))).sort(),
      estados: Array.from(new Set(data.map(i => i.estado_proyecto).filter(Boolean))).sort(),
      regiones: Array.from(new Set(data.map(i => i.region).filter(Boolean))).sort(),
      tipos: Array.from(new Set(data.map(i => i.tipo_proyecto).filter(Boolean))).sort(),
      categorias: Array.from(new Set(data.map(i => i.categoria_economica).filter(Boolean))).sort(),
    };
  }, [data]);

  const filteredData = useMemo(() => {
    return data.filter(item => {
      const matchesSearch = !appliedFilters.search ||
        item.nombre?.toLowerCase().includes(appliedFilters.search.toLowerCase()) ||
        item.titular?.toLowerCase().includes(appliedFilters.search.toLowerCase());

      const matchesTitular = appliedFilters.titular === 'all' || item.titular === appliedFilters.titular;
      const matchesVia = appliedFilters.via === 'all' || item.via_ingreso === appliedFilters.via;
      const matchesEstado = appliedFilters.estado === 'all' || item.estado_proyecto === appliedFilters.estado;
      const matchesRegion = appliedFilters.region === 'all' || item.region === appliedFilters.region;
      const matchesTipo = appliedFilters.tipo === 'all' || item.tipo_proyecto === appliedFilters.tipo;
      const matchesCategoria = appliedFilters.categoria === 'all' || item.categoria_economica === appliedFilters.categoria;

      let matchesDate = true;
      if (appliedFilters.dateFrom || appliedFilters.dateTo) {
        const itemDate = item.fecha_presentacion.split('/').reverse().join('-');
        if (appliedFilters.dateFrom && itemDate < appliedFilters.dateFrom) matchesDate = false;
        if (appliedFilters.dateTo && itemDate > appliedFilters.dateTo) matchesDate = false;
      }

      return matchesSearch && matchesTitular && matchesVia && matchesEstado && matchesRegion && matchesTipo && matchesCategoria && matchesDate;
    });
  }, [data, appliedFilters]);

  const paginatedData = filteredData.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);
  const totalPages = Math.ceil(filteredData.length / itemsPerPage);

  const columns = useMemo(() => [
    { field: 'rowNumber', headerName: 'N°', width: 60, sortable: false },
    {
      field: 'fav',
      headerName: 'Fav',
      width: 70,
      sortable: false,
      renderCell: (params: any) => (
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', height: '100%' }}>
          <button
            onClick={(e) => toggleFavorite(e, params.row)}
            style={{ background: 'none', border: 'none', cursor: 'pointer', color: favorites.has(params.row.id) ? 'var(--orange)' : 'var(--text-light)', display: 'flex', alignItems: 'center' }}
          >
            <Heart size={18} fill={favorites.has(params.row.id) ? 'var(--orange)' : 'none'} />
          </button>
        </div>
      )
    },
    { field: 'id', headerName: 'Expediente', width: 120 },
    { field: 'nombre', headerName: 'Nombre del Proyecto', flex: 1, minWidth: 250 },
    { field: 'titular', headerName: 'Titular', width: 200 },
    { field: 'via_ingreso', headerName: 'Vía Ingreso', width: 120 },
    { field: 'estado_proyecto', headerName: 'Estado', width: 140 },
    { field: 'region', headerName: 'Región', width: 140 },
    { field: 'fecha_presentacion', headerName: 'Fecha Presentación', width: 140 },
    { field: 'categoria_economica', headerName: 'Categoría Económica', width: 180 },
    { field: 'tipo_proyecto', headerName: 'Tipo Proyecto', width: 180 },
    {
      field: 'accion',
      headerName: 'Acciones',
      width: 100,
      sortable: false,
      renderCell: (params: any) => (
        <div style={{ display: 'flex', gap: '8px', alignItems: 'center', height: '100%' }}>
          <button
            onClick={(e) => { e.stopPropagation(); handleOpenModal(params.row); }}
            style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--primary)', display: 'flex', alignItems: 'center' }}
            title="Ver detalles"
          >
            <FileText size={18} />
          </button>
        </div>
      )
    }
  ], [favorites]);

  const rows = useMemo(() => {
    return filteredData.map((item, index) => ({
      ...item,
      rowNumber: index + 1
    }));
  }, [filteredData]);

  const getStatusColor = (estado: string) => {
    const estadoLower = estado?.toLowerCase() || '';
    if (estadoLower.includes('aprobado') || estadoLower.includes('calificacion favorable')) return '#10b981';
    if (estadoLower.includes('rechazado') || estadoLower.includes('desistido')) return '#ef4444';
    if (estadoLower.includes('calificación')) return '#f59e0b';
    if (estadoLower.includes('admisión')) return '#3b82f6';
    return '#64748b';
  };

  const resetFilters = () => {
    setSearchTerm('');
    setFilterTitular('all');
    setFilterVia('all');
    setFilterEstado('all');
    setFilterRegion('all');
    setFilterTipo('all');
    setFilterCategoria('all');
    setDateFrom('');
    setDateTo('');
    setCurrentPage(1);
  };

  return (
    <div style={{ padding: '20px', width: '100%' }}>
      <div style={{ marginBottom: '30px' }}>
        <h1 style={{ fontSize: '28px', fontWeight: 'bold', color: 'var(--text-dark)' }}>Proyectos Evaluados SEA</h1>
        <p style={{ color: 'var(--text-light)', marginTop: '5px' }}>Visualización y seguimiento de proyectos en el Sistema de Evaluación de Impacto Ambiental.</p>
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
            placeholder="Buscar por nombre o titular..."
            value={searchTerm}
            onChange={(e) => { setSearchTerm(e.target.value); }}
            onKeyDown={(e) => { if (e.key === 'Enter') handleApplyFilters(); }}
            style={{
              width: '100%', padding: '10px 40px 10px 40px', borderRadius: '8px',
              border: '1px solid var(--border)', outline: 'none', fontSize: '14px'
            }}
          />
          {searchTerm && (
            <button
              onClick={() => { setSearchTerm(''); handleApplyFilters(); }}
              style={{ position: 'absolute', right: '12px', top: '50%', transform: 'translateY(-50%)', background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-light)' }}
            >
              <X size={16} />
            </button>
          )}
        </div>

        <button
          onClick={() => setShowFilters(!showFilters)}
          style={{
            display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 15px',
            backgroundColor: showFilters ? 'var(--primary-light)' : 'white',
            color: showFilters ? 'var(--primary)' : 'var(--text-dark)',
            border: '1px solid ' + (showFilters ? 'var(--primary)' : 'var(--border)'),
            borderRadius: '8px', cursor: 'pointer', fontWeight: 500, fontSize: '14px',
            transition: 'all 0.2s'
          }}
        >
          <Filter size={18} />
          Filtros Avanzados
          {showFilters ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
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
              Cargando completo...
            </span>
          )}
          {totalRecords !== null ? `${totalRecords} resultados` : `${filteredData.length} resultados`}
        </div>
      </div>

      {/* Advanced Filters */}
      {showFilters && (
        <div style={{
          backgroundColor: '#f8fafc', padding: '20px', borderRadius: '12px',
          border: '1px solid var(--border)', marginBottom: '25px',
          display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '15px'
        }}>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Titular</label>
            <Autocomplete
              options={options.titulares}
              value={filterTitular === 'all' ? null : filterTitular}
              onChange={(_, newValue) => setFilterTitular(newValue || 'all')}
              renderInput={(params) => (
                <TextField
                  {...params}
                  placeholder="Todos los titulares"
                  size="small"
                  sx={{ bgcolor: 'white', '& .MuiOutlinedInput-root': { borderRadius: '6px' } }}
                />
              )}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Vía Ingreso</label>
            <Autocomplete
              options={options.vias}
              value={filterVia === 'all' ? null : filterVia}
              onChange={(_, newValue) => setFilterVia(newValue || 'all')}
              renderInput={(params) => (
                <TextField
                  {...params}
                  placeholder="Todas las vías"
                  size="small"
                  sx={{ bgcolor: 'white', '& .MuiOutlinedInput-root': { borderRadius: '6px' } }}
                />
              )}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Estado</label>
            <Autocomplete
              options={options.estados}
              value={filterEstado === 'all' ? null : filterEstado}
              onChange={(_, newValue) => setFilterEstado(newValue || 'all')}
              renderInput={(params) => (
                <TextField
                  {...params}
                  placeholder="Todos los estados"
                  size="small"
                  sx={{ bgcolor: 'white', '& .MuiOutlinedInput-root': { borderRadius: '6px' } }}
                />
              )}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Región</label>
            <Autocomplete
              options={options.regiones}
              value={filterRegion === 'all' ? null : filterRegion}
              onChange={(_, newValue) => setFilterRegion(newValue || 'all')}
              renderInput={(params) => (
                <TextField
                  {...params}
                  placeholder="Todas las regiones"
                  size="small"
                  sx={{ bgcolor: 'white', '& .MuiOutlinedInput-root': { borderRadius: '6px' } }}
                />
              )}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Tipo Proyecto</label>
            <Autocomplete
              options={options.tipos}
              value={filterTipo === 'all' ? null : filterTipo}
              onChange={(_, newValue) => setFilterTipo(newValue || 'all')}
              renderInput={(params) => (
                <TextField
                  {...params}
                  placeholder="Todos los tipos"
                  size="small"
                  sx={{ bgcolor: 'white', '& .MuiOutlinedInput-root': { borderRadius: '6px' } }}
                />
              )}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Categoría Económica</label>
            <Autocomplete
              options={options.categorias}
              value={filterCategoria === 'all' ? null : filterCategoria}
              onChange={(_, newValue) => setFilterCategoria(newValue || 'all')}
              renderInput={(params) => (
                <TextField
                  {...params}
                  placeholder="Todas las categorías"
                  size="small"
                  sx={{ bgcolor: 'white', '& .MuiOutlinedInput-root': { borderRadius: '6px' } }}
                />
              )}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Desde</label>
            <input type="date" value={dateFrom} onChange={e => setDateFrom(e.target.value)} style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)', height: '40px' }} />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Hasta</label>
            <input type="date" value={dateTo} onChange={e => setDateTo(e.target.value)} style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)', height: '40px' }} />
          </div>
          <div style={{ gridColumn: '1 / -1', display: 'flex', gap: '10px', justifyContent: 'flex-end', borderTop: '1px solid var(--border)', paddingTop: '20px', marginTop: '10px' }}>
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

      {activeTab === 'dashboard' ? (
        <DashboardManager
          data={data}
          config={{
            title: 'Proyectos Evaluados SEA',
            tableName: 'SEAEvaluados',
            dimensions: [
              { key: 'razon_ingreso', label: 'Razón de Ingreso', type: 'relative-bar' as const },
              { key: 'categoria_economica', label: 'Categoría Económica', type: 'relative-bar' as const },
              { key: 'region', label: 'Proyectos por Región', type: 'relative-bar' as const },
              { key: 'estado_proyecto', label: 'Estado de Evaluación', type: 'pie' as const },
              { key: 'fecha_presentacion', label: 'Presentaciones por Año', type: 'grouped-vertical' as const }
            ]
          }}
        />
      ) : (
        <>
          {loading ? (
            <div style={{ textAlign: 'center', padding: '100px 0' }}>
              <div className="loader" style={{ marginBottom: '20px' }}></div>
              <p style={{ color: 'var(--text-light)' }}>Cargando proyectos evaluados...</p>
            </div>
          ) : error ? (
            <div style={{ textAlign: 'center', padding: '60px', backgroundColor: '#fee2e2', borderRadius: '12px', color: '#b91c1c' }}>
              <h3 style={{ fontSize: '18px', fontWeight: 'bold', marginBottom: '10px' }}>Error al cargar los datos</h3>
              <p>{error}</p>
              <button onClick={fetchData} style={{ marginTop: '20px', padding: '10px 20px', backgroundColor: '#ef4444', color: 'white', border: 'none', borderRadius: '6px', cursor: 'pointer' }}>Reintentar</button>
            </div>
          ) : filteredData.length === 0 ? (
            <div style={{ textAlign: 'center', padding: '100px 0', backgroundColor: '#f8fafc', borderRadius: '12px', border: '1px dashed var(--border)' }}>
              <Search size={48} color="var(--text-light)" style={{ marginBottom: '20px', opacity: 0.5 }} />
              <h3 style={{ fontSize: '18px', fontWeight: 'bold', color: 'var(--text-dark)' }}>No se encontraron proyectos</h3>
              <p style={{ color: 'var(--text-light)', marginTop: '5px' }}>Intenta ajustando los términos de búsqueda o los filtros.</p>
              <button onClick={resetFilters} style={{ marginTop: '20px', color: 'var(--primary)', background: 'none', border: 'none', fontWeight: 600, cursor: 'pointer' }}>Limpiar todos los filtros</button>
            </div>
          ) : viewMode === 'table' ? (
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
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))',
                gap: '25px',
                marginBottom: '40px',
                width: '100%'
              }}>
                {paginatedData.map(item => (
                  <div key={item.id} style={{
                    backgroundColor: 'white', borderRadius: '16px', border: '1px solid var(--border)',
                    overflow: 'hidden', boxShadow: '0 4px 15px rgba(0,0,0,0.05)',
                    display: 'flex', flexDirection: 'column', transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
                    cursor: 'pointer', position: 'relative',
                    height: '100%'
                  }}
                    onClick={() => handleOpenModal(item)}
                    onMouseOver={(e) => {
                      e.currentTarget.style.transform = 'translateY(-6px)';
                      e.currentTarget.style.boxShadow = '0 10px 25px rgba(0,0,0,0.1)';
                    }}
                    onMouseOut={(e) => {
                      e.currentTarget.style.transform = 'translateY(0)';
                      e.currentTarget.style.boxShadow = '0 4px 15px rgba(0,0,0,0.05)';
                    }}
                  >
                    {/* Header with Status and Favorite */}
                    <div style={{ padding: '15px 20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid #f1f5f9' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <div style={{ width: '10px', height: '10px', borderRadius: '50%', backgroundColor: getStatusColor(item.estado_proyecto) }}></div>
                        <span style={{ fontSize: '12px', fontWeight: 700, color: 'var(--text-dark)', textTransform: 'uppercase', letterSpacing: '0.5px' }}>
                          {item.estado_proyecto}
                        </span>
                      </div>
                      <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
                        {item.is_new && <span style={{ fontSize: '10px', backgroundColor: '#3b82f6', color: 'white', padding: '2px 8px', borderRadius: '10px', fontWeight: 800 }}>NUEVO</span>}
                        <button
                          onClick={(e) => toggleFavorite(e, item)}
                          style={{ background: 'none', border: 'none', padding: 0, cursor: 'pointer', display: 'flex' }}
                        >
                          <Heart size={20} fill={favorites.has(item.id) ? "#ef4444" : "none"} color={favorites.has(item.id) ? "#ef4444" : "var(--text-light)"} />
                        </button>
                      </div>
                    </div>

                    {/* Content */}
                    <div style={{ padding: '20px', flexGrow: 1 }}>
                      <div style={{ fontSize: '11px', color: 'var(--primary)', fontWeight: 800, marginBottom: '8px', textTransform: 'uppercase' }}>
                        {item.via_ingreso} • {item.region || 'Multiregional'}
                      </div>
                      <h3 style={{
                        fontSize: '17px', fontWeight: 'bold', color: 'var(--text-dark)', lineHeight: '1.4',
                        marginBottom: '15px', display: '-webkit-box', WebkitLineClamp: 3, WebkitBoxOrient: 'vertical', overflow: 'hidden'
                      }}>
                        {item.nombre}
                      </h3>
                      <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--text-light)', fontSize: '13px' }}>
                          <Calendar size={14} />
                          <span>{item.fecha_presentacion}</span>
                        </div>
                        <div style={{ fontSize: '13px', color: 'var(--text-light)', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                          <span style={{ fontWeight: 600 }}>Titular:</span> {item.titular}
                        </div>
                      </div>
                    </div>

                    {/* Footer */}
                    <div style={{ padding: '12px 20px', backgroundColor: '#f8fafc', borderTop: '1px solid #f1f5f9', display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '5px', fontSize: '13px', fontWeight: 700, color: 'var(--primary)' }}>
                      <span>VER DETALLES COMPLETOS</span>
                    </div>
                  </div>
                ))}
              </div>

              {/* Pagination */}
              {totalPages > 1 && (
                <div style={{ display: 'flex', justifyContent: 'center', gap: '15px', alignItems: 'center' }}>
                  <button
                    onClick={() => { setCurrentPage(p => Math.max(1, p - 1)); window.scrollTo(0, 0); }}
                    disabled={currentPage === 1}
                    style={{
                      padding: '10px 20px', borderRadius: '8px', border: '1px solid var(--border)',
                      background: currentPage === 1 ? '#f1f5f9' : 'white',
                      cursor: currentPage === 1 ? 'not-allowed' : 'pointer',
                      fontWeight: 600, color: 'var(--text-dark)'
                    }}
                  >
                    Anterior
                  </button>
                  <div style={{ display: 'flex', gap: '5px' }}>
                    <span style={{ fontWeight: 'bold', color: 'var(--primary)' }}>{currentPage}</span>
                    <span style={{ color: 'var(--text-light)' }}>de {totalPages}</span>
                  </div>
                  <button
                    onClick={() => { setCurrentPage(p => Math.min(totalPages, p + 1)); window.scrollTo(0, 0); }}
                    disabled={currentPage === totalPages}
                    style={{
                      padding: '10px 20px', borderRadius: '8px', border: '1px solid var(--border)',
                      background: currentPage === totalPages ? '#f1f5f9' : 'white',
                      cursor: currentPage === totalPages ? 'not-allowed' : 'pointer',
                      fontWeight: 600, color: 'var(--text-dark)'
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

      {/* Detail Modal */}
      {showModal && selectedItem && (
        <div style={{
          position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
          backgroundColor: 'rgba(15, 23, 42, 0.6)', zIndex: 2000,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          padding: '20px', backdropFilter: 'blur(4px)'
        }} onClick={() => setShowModal(false)}>
          <div style={{
            backgroundColor: 'white', borderRadius: '20px', padding: '40px',
            maxWidth: '700px', width: '100%', maxHeight: '90vh', overflowY: 'auto',
            boxShadow: '0 25px 50px -12px rgba(0,0,0,0.25)', position: 'relative'
          }} onClick={e => e.stopPropagation()}>
            <button
              onClick={() => setShowModal(false)}
              style={{ position: 'absolute', top: '20px', right: '20px', background: '#f1f5f9', border: 'none', borderRadius: '50%', width: '36px', height: '36px', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-dark)' }}
            >
              <X size={20} />
            </button>

            <div style={{ marginBottom: '25px' }}>
              <div style={{
                display: 'inline-block', padding: '4px 12px', borderRadius: '20px', fontSize: '12px', fontWeight: 800,
                backgroundColor: getStatusColor(selectedItem.estado_proyecto), color: 'white', marginBottom: '15px'
              }}>
                {selectedItem.estado_proyecto} {selectedItem.subestado_proyecto && `(${selectedItem.subestado_proyecto})`}
              </div>
              <h2 style={{ fontSize: '24px', fontWeight: 'bold', color: 'var(--text-dark)', lineHeight: '1.3' }}>{selectedItem.nombre}</h2>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '20px', marginBottom: '30px' }}>
              <DetailField label="ID Expediente" value={selectedItem.id} />
              <DetailField label="Titular" value={selectedItem.titular} />
              <DetailField label="Fecha Presentación" value={selectedItem.fecha_presentacion} />
              <DetailField label="Vía Ingreso" value={selectedItem.via_ingreso} />
              <DetailField label="Región" value={selectedItem.region || 'Multiregional'} />
              <DetailField label="Tipo de Proyecto" value={selectedItem.tipo_proyecto} />
              <DetailField label="Categoría Económica" value={selectedItem.categoria_economica} />
              <DetailField label="Razón de Ingreso" value={selectedItem.razon_ingreso} />
            </div>

            <div style={{ paddingTop: '25px', borderTop: '1px solid #f1f5f9', display: 'flex', justifyContent: 'flex-end' }}>
              <a
                href={selectedItem.url}
                target="_blank"
                rel="noopener noreferrer"
                style={{
                  display: 'inline-flex', alignItems: 'center', gap: '10px',
                  padding: '12px 25px', backgroundColor: 'var(--primary)', color: 'white',
                  textDecoration: 'none', borderRadius: '10px', fontWeight: 700,
                  boxShadow: '0 4px 6px -1px rgba(0,0,0,0.1)'
                }}
              >
                <FileText size={20} />
                VER FICHA OFICIAL SEIA
              </a>
            </div>
          </div>
        </div>
      )}

      <style dangerouslySetInnerHTML={{
        __html: `
        .filter-select {
          appearance: none;
          background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
          background-repeat: no-repeat;
          background-position: right 8px center;
          background-size: 16px;
          padding-right: 32px !important;
        }
        .loader {
          border: 4px solid #f3f3f3;
          border-top: 4px solid var(--primary);
          border-radius: 50%;
          width: 40px;
          height: 40px;
          animation: spin 1s linear infinite;
          margin: 0 auto;
        }
        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
      ` }} />
    </div>
  );
};

const DetailField = ({ label, value }: { label: string, value: string }) => (
  <div>
    <div style={{ fontSize: '12px', fontWeight: 800, color: 'var(--primary)', textTransform: 'uppercase', marginBottom: '4px' }}>{label}</div>
    <div style={{ fontSize: '15px', color: 'var(--text-dark)', fontWeight: 500 }}>{value || 'No especificado'}</div>
  </div>
);

export default SEAEvaluadosPage;