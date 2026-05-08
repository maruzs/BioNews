import React, { useState, useEffect, useMemo } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';
import { Heart, Calendar, FileText, Search, X, Filter, ChevronDown, ChevronUp, RotateCcw } from 'lucide-react';

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
  const { refreshCategory, setCategoryActive, markItemViewed } = useNotifications();
  const [data, setData] = useState<SEAEvaluado[]>([]);
  const [loading, setLoading] = useState(true);
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

  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await fetch('/api/data/sea_proyectos_evaluados?limit=5000', {
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

      // Load favorites
      const favRes = await fetch('/api/favorites', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const favJson = await favRes.json();
      setFavorites(new Set(favJson.map((f: any) => f.id_o_link)));
      
      refreshCategory('sea_proyectos_evaluados');
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
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
    if (item.is_new) {
      markItemViewed('sea_proyectos_evaluados', item.id);
      setData(prev => prev.map(n => n.id === item.id ? { ...n, is_new: false } : n));
    }
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
      const matchesSearch = !searchTerm || 
        item.nombre?.toLowerCase().includes(searchTerm.toLowerCase()) || 
        item.titular?.toLowerCase().includes(searchTerm.toLowerCase());
      
      const matchesTitular = filterTitular === 'all' || item.titular === filterTitular;
      const matchesVia = filterVia === 'all' || item.via_ingreso === filterVia;
      const matchesEstado = filterEstado === 'all' || item.estado_proyecto === filterEstado;
      const matchesRegion = filterRegion === 'all' || item.region === filterRegion;
      const matchesTipo = filterTipo === 'all' || item.tipo_proyecto === filterTipo;
      const matchesCategoria = filterCategoria === 'all' || item.categoria_economica === filterCategoria;
      
      let matchesDate = true;
      if (dateFrom || dateTo) {
        const itemDate = item.fecha_presentacion.split('/').reverse().join('-');
        if (dateFrom && itemDate < dateFrom) matchesDate = false;
        if (dateTo && itemDate > dateTo) matchesDate = false;
      }
      
      return matchesSearch && matchesTitular && matchesVia && matchesEstado && matchesRegion && matchesTipo && matchesCategoria && matchesDate;
    });
  }, [data, searchTerm, filterTitular, filterVia, filterEstado, filterRegion, filterTipo, filterCategoria, dateFrom, dateTo]);

  const paginatedData = filteredData.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);
  const totalPages = Math.ceil(filteredData.length / itemsPerPage);

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
    <div style={{ padding: '20px', maxWidth: '1400px', margin: '0 auto', width: '100%' }}>
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
            onChange={(e) => { setSearchTerm(e.target.value); setCurrentPage(1); }}
            style={{ 
              width: '100%', padding: '10px 40px 10px 40px', borderRadius: '8px', 
              border: '1px solid var(--border)', outline: 'none', fontSize: '14px' 
            }}
          />
          {searchTerm && (
            <button 
              onClick={() => setSearchTerm('')}
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

        <button 
          onClick={resetFilters}
          title="Restablecer todos los filtros"
          style={{ 
            display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 15px',
            backgroundColor: 'white', color: 'var(--text-dark)',
            border: '1px solid var(--border)',
            borderRadius: '8px', cursor: 'pointer', fontWeight: 500, fontSize: '14px'
          }}
        >
          <RotateCcw size={18} />
          Restablecer
        </button>

        <div style={{ color: 'var(--text-light)', fontSize: '14px', marginLeft: 'auto' }}>
          {filteredData.length} resultados encontrados
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
            <select value={filterTitular} onChange={e => setFilterTitular(e.target.value)} className="filter-select" style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }}>
              <option value="all">Todos los titulares</option>
              {options.titulares.map(t => <option key={t} value={t}>{t}</option>)}
            </select>
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Vía Ingreso</label>
            <select value={filterVia} onChange={e => setFilterVia(e.target.value)} className="filter-select" style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }}>
              <option value="all">Todas las vías</option>
              {options.vias.map(v => <option key={v} value={v}>{v}</option>)}
            </select>
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Estado</label>
            <select value={filterEstado} onChange={e => setFilterEstado(e.target.value)} className="filter-select" style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }}>
              <option value="all">Todos los estados</option>
              {options.estados.map(e => <option key={e} value={e}>{e}</option>)}
            </select>
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Región</label>
            <select value={filterRegion} onChange={e => setFilterRegion(e.target.value)} className="filter-select" style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }}>
              <option value="all">Todas las regiones</option>
              {options.regiones.map(r => <option key={r} value={r}>{r}</option>)}
            </select>
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Tipo Proyecto</label>
            <select value={filterTipo} onChange={e => setFilterTipo(e.target.value)} className="filter-select" style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }}>
              <option value="all">Todos los tipos</option>
              {options.tipos.map(t => <option key={t} value={t}>{t}</option>)}
            </select>
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Categoría Económica</label>
            <select value={filterCategoria} onChange={e => setFilterCategoria(e.target.value)} className="filter-select" style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }}>
              <option value="all">Todas las categorías</option>
              {options.categorias.map(c => <option key={c} value={c}>{c}</option>)}
            </select>
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Desde</label>
            <input type="date" value={dateFrom} onChange={e => setDateFrom(e.target.value)} style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }} />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Hasta</label>
            <input type="date" value={dateTo} onChange={e => setDateTo(e.target.value)} style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }} />
          </div>
        </div>
      )}

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
                onClick={() => { setCurrentPage(p => Math.max(1, p - 1)); window.scrollTo(0,0); }}
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
                onClick={() => { setCurrentPage(p => Math.min(totalPages, p + 1)); window.scrollTo(0,0); }}
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

      <style dangerouslySetInnerHTML={{ __html: `
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
