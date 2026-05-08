import { useState, useEffect } from 'react';
import { Search, Calendar, FileText, X, Info, Download } from 'lucide-react';
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
  const [documents, setDocuments] = useState<Documento[]>([]);
  const [docsLoading, setDocsLoading] = useState(false);
  const [filter, setFilter] = useState<'vigentes' | 'resultados'>('vigentes');


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

  return (
    <div className="report-container">
      <div className="report-header-text">
        <h1 className="report-title">MINSAL - Consultas Públicas</h1>
        <p className="report-description">Consultas ciudadanas del Ministerio de Salud.</p>
      </div>

      <div className="news-filters" style={{ marginBottom: '20px', display: 'flex', gap: '20px', flexWrap: 'wrap', alignItems: 'center' }}>
        <div style={{ display: 'flex', background: '#f1f5f9', padding: '4px', borderRadius: '12px' }}>
          <button 
            onClick={() => setFilter('vigentes')}
            style={{ 
              padding: '8px 20px', 
              borderRadius: '8px', 
              border: 'none', 
              cursor: 'pointer',
              fontWeight: 600,
              fontSize: '0.9rem',
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
              fontSize: '0.9rem',
              backgroundColor: filter === 'resultados' ? 'white' : 'transparent',
              color: filter === 'resultados' ? 'var(--primary)' : 'var(--text-light)',
              boxShadow: filter === 'resultados' ? '0 2px 4px rgba(0,0,0,0.05)' : 'none',
              transition: 'all 0.2s'
            }}
          >
            Resultados
          </button>
        </div>

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
                       <span style={{ fontSize: '0.7rem', background: filter === 'vigentes' ? '#dcfce7' : '#e2e8f0', padding: '2px 8px', borderRadius: '4px', fontWeight: 600, color: filter === 'vigentes' ? '#166534' : '#475569' }}>
                        {filter === 'vigentes' ? 'VIGENTE' : 'RESULTADO'}
                       </span>
                    </div>
                    <div className="card-title" style={{ fontSize: '1rem', fontWeight: 600, marginBottom: '15px', minHeight: '3em', display: '-webkit-box', WebkitLineClamp: 3, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>{item.titulo}</div>
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
            
            <div style={{ marginBottom: '25px' }}>
              <span style={{ fontSize: '0.85rem', color: 'var(--primary)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em' }}>Detalle Consulta MINSAL</span>
              <h2 style={{ fontSize: '1.6rem', fontWeight: 700, marginTop: '5px', lineHeight: '1.3', color: '#1e293b' }}>{selectedItem.titulo}</h2>
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
