import { useState, useEffect } from 'react';
import { Search, Calendar, ExternalLink, X, Info } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';

interface MMAConsulta {
  id: string;
  nombre_instrumento: string;
  fecha_inicio: string;
  fecha_termino: string;
  tipo_instrumento: string;
  tipo_proceso?: string;
  ambito_territorial: string;
  link_detalle: string;
  fecha_scraping: string;
  is_new: boolean;
}

const MMAConsultasPage = () => {
  const { token } = useAuth();
  const { markItemViewed, refreshCategory, setCategoryActive } = useNotifications();
  const [data, setData] = useState<MMAConsulta[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [selectedItem, setSelectedItem] = useState<MMAConsulta | null>(null);
  const [filter, setFilter] = useState<'abiertas' | 'cerradas'>('abiertas');
  const [tipoFilter, setTipoFilter] = useState<string>('all');

  const category = 'mma';

  useEffect(() => {
    setCategoryActive(category, true);
    return () => {
      setCategoryActive(category, false);
    };
  }, [setCategoryActive]);

  const fetchData = async () => {
    setLoading(true);
    const tableName = filter === 'abiertas' ? 'mma_abiertas' : 'mma_cerradas';
    try {
      const res = await fetch(`/api/data/${tableName}?limit=5000`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const json = await res.json();
      setData(Array.isArray(json) ? json : []);
      refreshCategory(category);
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, [filter]);

  const handleOpenModal = (item: MMAConsulta) => {
    setSelectedItem(item);
    if (item.is_new) {
      markItemViewed(category, item.id);
      setData(prev => prev.map(n => n.id === item.id ? { ...n, is_new: false } : n));
    }
  };

  const filteredData = data.filter(item => {
    const matchesSearch = item.nombre_instrumento.toLowerCase().includes(search.toLowerCase());
    const matchesTipo = tipoFilter === 'all' || item.tipo_instrumento.toLowerCase().includes(tipoFilter.toLowerCase());
    return matchesSearch && matchesTipo;
  });

  return (
    <div className="report-container">
      <div className="report-header-text">
        <h1 className="report-title">MMA - Consultas Ciudadanas</h1>
        <p className="report-description">Consultas públicas del Ministerio del Medio Ambiente.</p>
      </div>

      <div className="news-filters" style={{ marginBottom: '20px', display: 'flex', gap: '20px', flexWrap: 'wrap', alignItems: 'center' }}>
        <div style={{ display: 'flex', background: '#f1f5f9', padding: '4px', borderRadius: '12px' }}>
          <button 
            onClick={() => setFilter('abiertas')}
            style={{ 
              padding: '8px 20px', 
              borderRadius: '8px', 
              border: 'none', 
              cursor: 'pointer',
              fontWeight: 600,
              fontSize: '0.9rem',
              backgroundColor: filter === 'abiertas' ? 'white' : 'transparent',
              color: filter === 'abiertas' ? 'var(--primary)' : 'var(--text-light)',
              boxShadow: filter === 'abiertas' ? '0 2px 4px rgba(0,0,0,0.05)' : 'none',
              transition: 'all 0.2s'
            }}
          >
            Abiertas
          </button>
          <button 
            onClick={() => setFilter('cerradas')}
            style={{ 
              padding: '8px 20px', 
              borderRadius: '8px', 
              border: 'none', 
              cursor: 'pointer',
              fontWeight: 600,
              fontSize: '0.9rem',
              backgroundColor: filter === 'cerradas' ? 'white' : 'transparent',
              color: filter === 'cerradas' ? 'var(--primary)' : 'var(--text-light)',
              boxShadow: filter === 'cerradas' ? '0 2px 4px rgba(0,0,0,0.05)' : 'none',
              transition: 'all 0.2s'
            }}
          >
            Cerradas
          </button>
        </div>

        <select 
          value={tipoFilter} 
          onChange={(e) => setTipoFilter(e.target.value)}
          className="filter-select"
          style={{ 
            padding: '8px 15px', 
            borderRadius: '12px', 
            border: '1px solid var(--border)',
            background: 'white',
            fontWeight: 500,
            fontSize: '0.9rem',
            outline: 'none',
            minWidth: '180px'
          }}
        >
          <option value="all">Todos los Instrumentos</option>
          <option value="Planes">Planes</option>
          <option value="Normas">Normas</option>
          <option value="Otros">Otros Instrumentos</option>
          <option value="Especies">Clasificación de Especies</option>
        </select>

        <div className="search-bar" style={{ maxWidth: '400px', background: 'white', border: '1px solid var(--border)', borderRadius: '30px', padding: '10px 20px', display: 'flex', alignItems: 'center', flex: 1 }}>
          <Search size={18} color="var(--primary)" style={{ marginRight: '10px' }} />
          <input
            type="text"
            placeholder="Buscar por título..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            style={{ border: 'none', outline: 'none', width: '100%' }}
          />
        </div>
      </div>

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
                       <span style={{ fontSize: '0.7rem', background: '#e2e8f0', padding: '2px 8px', borderRadius: '4px', fontWeight: 600, color: '#475569' }}>
                        {item.tipo_instrumento}
                       </span>
                       {filter === 'abiertas' && (
                         <span style={{ fontSize: '0.7rem', background: '#dcfce7', padding: '2px 8px', borderRadius: '4px', fontWeight: 600, color: '#166534' }}>
                           ACTIVA
                         </span>
                       )}
                       {filter === 'cerradas' && (
                         <span style={{ fontSize: '0.7rem', background: '#fee2e2', padding: '2px 8px', borderRadius: '4px', fontWeight: 600, color: '#991b1b' }}>
                           CERRADA
                         </span>
                       )}
                    </div>
                    <div className="card-title" style={{ fontSize: '1rem', fontWeight: 600, marginBottom: '15px', minHeight: '3em', display: '-webkit-box', WebkitLineClamp: 3, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>{item.nombre_instrumento}</div>
                    <div className="card-meta" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px' }}>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '5px', fontSize: '0.8rem', color: 'var(--text-light)' }}>
                        <Calendar size={14} /> <span style={{fontWeight: 500}}>Inicio:</span> {item.fecha_inicio}
                      </div>
                      <div style={{ display: 'flex', alignItems: 'center', gap: '5px', fontSize: '0.8rem', color: 'var(--text-light)' }}>
                        <Calendar size={14} /> <span style={{fontWeight: 500}}>Fin:</span> {item.fecha_termino}
                      </div>
                    </div>
                    <div className="card-action" style={{ marginTop: '20px', borderTop: '1px solid #f1f5f9', paddingTop: '15px', display: 'flex', alignItems: 'center', gap: '5px', color: 'var(--primary)', fontWeight: 600 }}>
                      <Info size={16} /> Ver detalles y expediente
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
            
            <div style={{ marginBottom: '25px' }}>
              <span style={{ fontSize: '0.85rem', color: 'var(--primary)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em' }}>Detalle Consulta MMA</span>
              <h2 style={{ fontSize: '1.6rem', fontWeight: 700, marginTop: '5px', lineHeight: '1.3', color: '#1e293b' }}>{selectedItem.nombre_instrumento}</h2>
            </div>
            
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '25px', marginBottom: '35px', padding: '25px', background: '#f8fafc', borderRadius: '12px' }}>
              <div>
                <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#64748b', textTransform: 'uppercase', marginBottom: '4px' }}>Estado</div>
                <div style={{ fontSize: '1rem', fontWeight: 600, color: filter === 'abiertas' ? '#16a34a' : '#dc2626' }}>{filter === 'abiertas' ? 'Activa' : 'Cerrada'}</div>
              </div>
              <div>
                <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#64748b', textTransform: 'uppercase', marginBottom: '4px' }}>Tipo de Instrumento</div>
                <div style={{ fontSize: '1rem', fontWeight: 600 }}>{selectedItem.tipo_instrumento}</div>
              </div>
              <div>
                <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#64748b', textTransform: 'uppercase', marginBottom: '4px' }}>Ámbito Territorial</div>
                <div style={{ fontSize: '1rem', fontWeight: 600 }}>{selectedItem.ambito_territorial}</div>
              </div>
              {selectedItem.tipo_proceso && (
                <div>
                  <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#64748b', textTransform: 'uppercase', marginBottom: '4px' }}>Tipo de Proceso</div>
                  <div style={{ fontSize: '1rem', fontWeight: 600 }}>{selectedItem.tipo_proceso}</div>
                </div>
              )}
               <div>
                <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#64748b', textTransform: 'uppercase', marginBottom: '4px' }}>Fecha Inicio</div>
                <div style={{ fontSize: '1rem', fontWeight: 600 }}>{selectedItem.fecha_inicio}</div>
              </div>
               <div>
                <div style={{ fontSize: '0.75rem', fontWeight: 700, color: '#64748b', textTransform: 'uppercase', marginBottom: '4px' }}>Fecha Término</div>
                <div style={{ fontSize: '1rem', fontWeight: 600 }}>{selectedItem.fecha_termino}</div>
              </div>
            </div>

            <div style={{ display: 'flex', gap: '15px' }}>
               <a 
                href={selectedItem.link_detalle} 
                target="_blank" 
                rel="noopener noreferrer" 
                style={{ 
                  flex: 1,
                  display: 'flex', 
                  alignItems: 'center', 
                  justifyContent: 'center',
                  gap: '10px', 
                  padding: '14px 25px', 
                  backgroundColor: 'var(--primary)', 
                  borderRadius: '10px', 
                  textDecoration: 'none', 
                  color: 'white', 
                  fontWeight: 600,
                  boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.1)',
                  transition: 'transform 0.2s'
                }}
                onMouseOver={(e) => e.currentTarget.style.transform = 'translateY(-2px)'}
                onMouseOut={(e) => e.currentTarget.style.transform = 'translateY(0)'}
              >
                <ExternalLink size={20} />
                <span>Ver consulta completa en MMA</span>
              </a>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default MMAConsultasPage;
