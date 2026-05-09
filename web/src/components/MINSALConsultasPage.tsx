import { useState, useEffect } from 'react';
import { Search, Calendar, FileText, X, Info, Download, Heart, Filter, ChevronDown, ChevronUp, RotateCcw, LayoutDashboard } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';

interface MINSALConsulta {
  id: string;
  titulo: string;
  fecha_inicio?: string;
  periodo_consulta?: string;
  fecha_scraping: string;
  is_new: boolean;
}

interface Documento {
  nombre: string;
  link: string;
}

const MINSALConsultasPage = () => {
  const { token } = useAuth();
  const { markItemViewed, refreshCategory, setCategoryActive } = useNotifications();
  const [data, setData] = useState<MINSALConsulta[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [selectedItem, setSelectedItem] = useState<MINSALConsulta | null>(null);
  const [favorites, setFavorites] = useState<Set<string>>(new Set());
  const [documents, setDocuments] = useState<Documento[]>([]);
  const [docsLoading, setDocsLoading] = useState(false);
  const [filter, setFilter] = useState<'vigentes' | 'resultados'>('vigentes');
  const [showFilters, setShowFilters] = useState(false);

  const resetFilters = () => {
    setSearch('');
    setFilter('vigentes');
  };


  useEffect(() => {
    // Para notificaciones, MINSAL usa dos slugs actualmente en manager.py
    // Pero el usuario quiere unificar la vista.
    const activeCategory = filter === 'vigentes' ? 'minsal_vigentes' : 'minsal_resultados';
    setCategoryActive(activeCategory, true);
    return () => {
      setCategoryActive(activeCategory, false);
    };
  }, [setCategoryActive, filter]);

  const fetchData = async () => {
    setLoading(true);
    const tableName = filter === 'vigentes' ? 'minsal_vigentes' : 'minsal_resultados';
    try {
      const res = await fetch(`/api/data/${tableName}?limit=5000`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const json = await res.json();
      setData(Array.isArray(json) ? json : []);
      refreshCategory(tableName);

      // Cargar favoritos
      const favRes = await fetch('/api/favorites', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const favJson = await favRes.json();
      setFavorites(new Set(favJson.map((f: any) => f.id_o_link)));
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, [filter]);

  const handleOpenModal = async (item: MINSALConsulta) => {
    setSelectedItem(item);
    setDocuments([]);
    setDocsLoading(true);
    
    const activeCategory = filter === 'vigentes' ? 'minsal_vigentes' : 'minsal_resultados';
    if (item.is_new) {
      markItemViewed(activeCategory, item.id);
      setData(prev => prev.map(n => n.id === item.id ? { ...n, is_new: false } : n));
    }

    try {
      const type = filter === 'vigentes' ? 'vigente' : 'resultado';
      const res = await fetch(`/api/minsal/documents/${item.id}?type=${type}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const docs = await res.json();
        setDocuments(docs);
      }
    } catch (err) {
      console.error("Error fetching docs:", err);
    } finally {
      setDocsLoading(false);
    }
  };

  const filteredData = data.filter(item => 
    item.titulo.toLowerCase().includes(search.toLowerCase())
  );

  const toggleFavorite = async (e: React.MouseEvent, item: MINSALConsulta) => {
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
            fuente: 'MINSAL',
            nombre: item.titulo,
            accion: '' // MINSAL doesn't have a direct external link for the item, it's modal based
          })
        });
        setFavorites(prev => {
          const next = new Set(prev);
          next.add(item.id);
          return next;
        });
      }
    } catch (err) {
      console.error("Error toggling favorite:", err);
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '1400px', margin: '0 auto', width: '100%' }}>
      <div style={{ marginBottom: '30px' }}>
        <h1 style={{ fontSize: '28px', fontWeight: 'bold', color: 'var(--text-dark)' }}>MINSAL - Consultas Públicas</h1>
        <p style={{ color: 'var(--text-light)', marginTop: '5px' }}>Consultas ciudadanas del Ministerio de Salud.</p>
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
            placeholder="Buscar por título..." 
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            style={{ 
              width: '100%', padding: '10px 40px', borderRadius: '8px', 
              border: '1px solid var(--border)', outline: 'none', fontSize: '14px' 
            }}
          />
          {search && (
            <button 
              onClick={() => setSearch('')}
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

        <button 
          style={{ 
            display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 15px',
            backgroundColor: 'var(--primary)', color: 'white',
            border: 'none',
            borderRadius: '8px', cursor: 'pointer', fontWeight: 500, fontSize: '14px',
            transition: '0.2s'
          }}
          onMouseOver={(e) => e.currentTarget.style.opacity = '0.9'}
          onMouseOut={(e) => e.currentTarget.style.opacity = '1'}
        >
          <LayoutDashboard size={18} />
          Dashboard
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
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '10px' }}>Tipo de Consulta</label>
            <div style={{ display: 'flex', background: '#f1f5f9', padding: '4px', borderRadius: '12px', width: 'fit-content' }}>
              <button 
                onClick={() => setFilter('vigentes')}
                style={{ 
                  padding: '8px 20px', 
                  borderRadius: '8px', 
                  border: 'none', 
                  cursor: 'pointer',
                  fontWeight: 600,
                  fontSize: '13px',
                  backgroundColor: filter === 'vigentes' ? 'white' : 'transparent',
                  color: filter === 'vigentes' ? 'var(--primary)' : 'var(--text-light)',
                  boxShadow: filter === 'vigentes' ? '0 2px 4px rgba(0,0,0,0.05)' : 'none',
                  transition: 'all 0.2s'
                }}
              >
                Vigentes
              </button>
              <button 
                onClick={() => setFilter('resultados')}
                style={{ 
                  padding: '8px 20px', 
                  borderRadius: '8px', 
                  border: 'none', 
                  cursor: 'pointer',
                  fontWeight: 600,
                  fontSize: '13px',
                  backgroundColor: filter === 'resultados' ? 'white' : 'transparent',
                  color: filter === 'resultados' ? 'var(--primary)' : 'var(--text-light)',
                  boxShadow: filter === 'resultados' ? '0 2px 4px rgba(0,0,0,0.05)' : 'none',
                  transition: 'all 0.2s'
                }}
              >
                Resultados
              </button>
            </div>
          </div>
        </div>
      )}

      <div className="content-wrapper">
        {loading ? (
          <p>Cargando consultas...</p>
        ) : (
          <div className="news-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(350px, 1fr))', gap: '20px' }}>
            {filteredData.length === 0 ? (
              <p style={{ gridColumn: '1 / -1', textAlign: 'center' }}>No hay consultas para mostrar.</p>
            ) : (
              filteredData.map((item) => (
                <div key={item.id} className={`card ${item.is_new ? 'new-highlight' : ''}`} style={{ cursor: 'pointer', position: 'relative' }} onClick={() => handleOpenModal(item)}>
                  {item.is_new && (
                    <div style={{ position: 'absolute', top: '10px', right: '10px', background: 'var(--primary)', color: 'white', padding: '2px 10px', borderRadius: '10px', fontSize: '0.7rem', fontWeight: 'bold', zIndex: 5 }}>
                      NUEVO
                    </div>
                  )}
                  <div className="card-content">
                    <div style={{ display: 'flex', gap: '10px', marginBottom: '10px' }}>
                       <span style={{ fontSize: '0.7rem', background: filter === 'vigentes' ? '#dcfce7' : '#e2e8f0', padding: '2px 8px', borderRadius: '4px', fontWeight: 600, color: filter === 'vigentes' ? '#166534' : '#475569' }}>
                        {filter === 'vigentes' ? 'VIGENTE' : 'RESULTADO'}
                       </span>
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '10px', marginBottom: '15px' }}>
                      <div className="card-title" style={{ fontSize: '1rem', fontWeight: 600, margin: 0, display: '-webkit-box', WebkitLineClamp: 3, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>{item.titulo}</div>
                      <Heart 
                        size={20} 
                        onClick={(e) => toggleFavorite(e, item)}
                        style={{ 
                          cursor: 'pointer', 
                          flexShrink: 0,
                          fill: favorites.has(item.id) ? 'var(--orange)' : 'none', 
                          color: favorites.has(item.id) ? 'var(--orange)' : 'var(--text-light)',
                          transition: 'all 0.2s'
                        }} 
                      />
                    </div>
                    <div className="card-meta">
                      {item.fecha_inicio && (
                        <div style={{ display: 'flex', alignItems: 'center', gap: '5px', fontSize: '0.8rem', color: 'var(--text-light)', marginBottom: '5px' }}>
                          <Calendar size={14} /> <span style={{fontWeight: 500}}>Inicio:</span> {item.fecha_inicio}
                        </div>
                      )}
                      {item.periodo_consulta && (
                        <div style={{ display: 'flex', alignItems: 'center', gap: '5px', fontSize: '0.8rem', color: 'var(--text-light)' }}>
                          <Info size={14} /> <span style={{fontWeight: 500}}>Periodo:</span> {item.periodo_consulta}
                        </div>
                      )}
                    </div>
                    <div className="card-action" style={{ marginTop: '20px', borderTop: '1px solid #f1f5f9', paddingTop: '15px', display: 'flex', alignItems: 'center', gap: '5px', color: 'var(--primary)', fontWeight: 600 }}>
                      <FileText size={16} /> Ver detalles y documentos
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>
        )}
      </div>

      {selectedItem && (
        <div className="modal-overlay" style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex', justifyContent: 'center', alignItems: 'center', zIndex: 1000, padding: '20px' }} onClick={() => setSelectedItem(null)}>
          <div className="modal-content" style={{ backgroundColor: 'white', borderRadius: '16px', padding: '40px', maxWidth: '850px', width: '100%', maxHeight: '90vh', overflowY: 'auto', position: 'relative', boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.1)' }} onClick={e => e.stopPropagation()}>
            <button onClick={() => setSelectedItem(null)} style={{ position: 'absolute', top: '20px', right: '20px', background: '#f1f5f9', border: 'none', cursor: 'pointer', width: '36px', height: '36px', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#64748b' }}>
              <X size={20} />
            </button>
            
            <div style={{ marginBottom: '25px', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <div>
                <span style={{ fontSize: '0.85rem', color: 'var(--primary)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em' }}>Detalle Consulta MINSAL</span>
                <h2 style={{ fontSize: '1.6rem', fontWeight: 700, marginTop: '5px', lineHeight: '1.3', color: '#1e293b' }}>{selectedItem.titulo}</h2>
              </div>
              <Heart 
                size={28} 
                onClick={(e) => toggleFavorite(e, selectedItem)}
                style={{ 
                  cursor: 'pointer', 
                  fill: favorites.has(selectedItem.id) ? 'var(--orange)' : 'none', 
                  color: favorites.has(selectedItem.id) ? 'var(--orange)' : 'var(--text-light)',
                  transition: 'all 0.2s'
                }} 
              />
            </div>
            
            <div style={{ marginBottom: '30px' }}>
              <h3 style={{ fontSize: '1.1rem', fontWeight: 600, marginBottom: '15px', display: 'flex', alignItems: 'center', gap: '10px' }}>
                <Download size={20} color="var(--primary)" /> Documentos Adjuntos
              </h3>
              {docsLoading ? (
                <p>Cargando documentos...</p>
              ) : documents.length === 0 ? (
                <p style={{ color: 'var(--text-light)', fontStyle: 'italic' }}>No hay documentos disponibles para esta consulta.</p>
              ) : (
                <div style={{ display: 'grid', gridTemplateColumns: '1fr', gap: '10px' }}>
                  {documents.map((doc, idx) => (
                    <a 
                      key={idx}
                      href={doc.link} 
                      target="_blank" 
                      rel="noopener noreferrer"
                      style={{ 
                        display: 'flex', 
                        alignItems: 'center', 
                        justifyContent: 'space-between',
                        padding: '12px 20px', 
                        background: '#f8fafc', 
                        borderRadius: '10px', 
                        textDecoration: 'none', 
                        color: '#1e293b',
                        border: '1px solid #e2e8f0',
                        transition: 'all 0.2s'
                      }}
                      onMouseOver={(e) => {
                        e.currentTarget.style.background = 'white';
                        e.currentTarget.style.borderColor = 'var(--primary)';
                      }}
                      onMouseOut={(e) => {
                        e.currentTarget.style.background = '#f8fafc';
                        e.currentTarget.style.borderColor = '#e2e8f0';
                      }}
                    >
                      <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                        <FileText size={18} color="#64748b" />
                        <span style={{ fontSize: '0.95rem', fontWeight: 500 }}>{doc.nombre}</span>
                      </div>
                      <Download size={18} color="var(--primary)" />
                    </a>
                  ))}
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default MINSALConsultasPage;
