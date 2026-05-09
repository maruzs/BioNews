import { useState, useEffect } from 'react';
import { Search, Calendar, FileText, Download, X, Filter, ChevronDown, ChevronUp, LayoutDashboard, BookOpen } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';

interface Documento {
  nombre: string;
  link: string;
}

interface Consulta {
  id: string;
  titulo: string;
  fecha_inicio?: string;
  periodo_consulta?: string;
  indicaciones?: string;
  fecha_scraping: string;
  is_new: boolean;
}

interface ConsultasPageProps {
  title: string;
  description: string;
  tableName: string;
  category: string;
  type: 'vigente' | 'resultado';
}

const ConsultasPage = ({ title, description, tableName, category, type }: ConsultasPageProps) => {
  const { token } = useAuth();
  const { markItemViewed, refreshCategory, setCategoryActive } = useNotifications();
  const [data, setData] = useState<Consulta[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [selectedItem, setSelectedItem] = useState<Consulta | null>(null);
  const [documents, setDocuments] = useState<Documento[]>([]);
  const [docsLoading, setDocsLoading] = useState(false);
  const [showFilters, setShowFilters] = useState(false);
  const [activeTab, setActiveTab] = useState('reporte');

  const [appliedSearch, setAppliedSearch] = useState('');

  const handleApplyFilters = () => {
    setAppliedSearch(search);
  };

  const resetFilters = () => {
    setSearch('');
    setAppliedSearch('');
  };

  useEffect(() => {
    setCategoryActive(category, true);
    return () => {
      setCategoryActive(category, false);
    };
  }, [category, setCategoryActive]);

  const fetchData = async () => {
    setLoading(true);
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
  }, [tableName]);

  const fetchDocuments = async (id: string) => {
    setDocsLoading(true);
    try {
      const res = await fetch(`/api/consultas/documentos/${encodeURIComponent(id)}?tipo=minsal_${type}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const json = await res.json();
      setDocuments(json);
    } catch (err) {
      console.error(err);
    }
    setDocsLoading(false);
  };

  const handleOpenModal = (item: Consulta) => {
    setSelectedItem(item);
    fetchDocuments(item.id);
    if (item.is_new) {
      markItemViewed(category, item.id);
      setData(prev => prev.map(n => n.id === item.id ? { ...n, is_new: false } : n));
    }
  };

  const filteredData = data.filter(item => 
    item.titulo.toLowerCase().includes(appliedSearch.toLowerCase())
  );

  return (
    <div style={{ padding: '20px', maxWidth: '1400px', margin: '0 auto', width: '100%' }}>
      <div style={{ marginBottom: '30px' }}>
        <h1 style={{ fontSize: '28px', fontWeight: 'bold', color: 'var(--text-dark)' }}>{title}</h1>
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
            placeholder="Buscar consulta..." 
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            onKeyDown={(e) => { if (e.key === 'Enter') handleApplyFilters(); }}
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
      {/* Advanced Filters */}
      {showFilters && (
        <div style={{ 
          backgroundColor: '#f8fafc', padding: '20px', borderRadius: '12px', 
          border: '1px solid var(--border)', marginBottom: '25px',
          display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '15px'
        }}>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Título</label>
            <input 
              type="text" 
              value={search} 
              onChange={(e) => setSearch(e.target.value)} 
              placeholder="Buscar..."
              style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }} 
            />
          </div>
          <div style={{ gridColumn: '1 / -1', display: 'flex', gap: '10px', justifyContent: 'flex-end', borderTop: '1px solid var(--border)', paddingTop: '20px', marginTop: '10px' }}>
            <button 
              onClick={resetFilters}
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
        <div style={{ textAlign: 'center', padding: '100px 0', backgroundColor: '#f8fafc', borderRadius: '12px', border: '1px dashed var(--border)' }}>
          <LayoutDashboard size={48} color="var(--primary)" style={{ marginBottom: '20px', opacity: 0.5 }} />
          <h3 style={{ fontSize: '18px', fontWeight: 'bold', color: 'var(--text-dark)' }}>Dashboard de Consultas</h3>
          <p style={{ color: 'var(--text-light)', marginTop: '5px' }}>Vista de estadísticas y gráficos en desarrollo.</p>
        </div>
      ) : (
        <div className="content-wrapper" style={{ padding: '0' }}>
          {loading ? (
          <p>Cargando consultas...</p>
        ) : (
          <div className="news-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', gap: '20px' }}>
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
                    <div className="card-title" style={{ fontSize: '1rem', fontWeight: 600, marginBottom: '10px', minHeight: '3em' }}>{item.titulo}</div>
                    <div className="card-meta">
                      {item.fecha_inicio && (
                        <div style={{ display: 'flex', alignItems: 'center', gap: '5px', fontSize: '0.85rem' }}>
                          <Calendar size={14} /> {item.fecha_inicio}
                        </div>
                      )}
                    </div>
                    <div className="card-action" style={{ marginTop: '15px' }}>Ver detalles</div>
                  </div>
                </div>
              ))
            )}
          </div>
        )}
      </div>
      )}

      {selectedItem && (
        <div className="modal-overlay" style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex', justifyContent: 'center', alignItems: 'center', zIndex: 1000, padding: '20px' }} onClick={() => setSelectedItem(null)}>
          <div className="modal-content" style={{ backgroundColor: 'white', borderRadius: '12px', padding: '30px', maxWidth: '800px', width: '100%', maxHeight: '90vh', overflowY: 'auto', position: 'relative' }} onClick={e => e.stopPropagation()}>
            <button onClick={() => setSelectedItem(null)} style={{ position: 'absolute', top: '15px', right: '15px', background: 'none', border: 'none', cursor: 'pointer' }}>
              <X size={24} />
            </button>
            
            <h2 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: '20px', color: 'var(--primary)' }}>{selectedItem.titulo}</h2>
            
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '20px', marginBottom: '30px' }}>
              {selectedItem.fecha_inicio && (
                <div>
                  <div style={{ fontSize: '0.75rem', fontWeight: 600, color: 'var(--text-light)', textTransform: 'uppercase' }}>Fecha de Publicación</div>
                  <div style={{ fontSize: '1rem' }}>{selectedItem.fecha_inicio}</div>
                </div>
              )}
              {selectedItem.periodo_consulta && (
                <div>
                  <div style={{ fontSize: '0.75rem', fontWeight: 600, color: 'var(--text-light)', textTransform: 'uppercase' }}>Periodo de Consulta</div>
                  <div style={{ fontSize: '1rem' }}>{selectedItem.periodo_consulta}</div>
                </div>
              )}
            </div>

            {selectedItem.indicaciones && (
              <div style={{ marginBottom: '30px' }}>
                <div style={{ fontSize: '0.75rem', fontWeight: 600, color: 'var(--text-light)', textTransform: 'uppercase', marginBottom: '5px' }}>Indicaciones</div>
                <div style={{ fontSize: '0.95rem', lineHeight: '1.5' }}>{selectedItem.indicaciones}</div>
              </div>
            )}

            <div>
              <h3 style={{ fontSize: '1.1rem', fontWeight: 600, marginBottom: '15px' }}>Documentos Adjuntos</h3>
              {docsLoading ? (
                <p>Cargando documentos...</p>
              ) : documents.length === 0 ? (
                <p style={{ color: 'var(--text-light)' }}>No hay documentos adjuntos.</p>
              ) : (
                <div style={{ display: 'grid', gap: '10px' }}>
                  {documents.map((doc, idx) => (
                    <a key={idx} href={doc.link} target="_blank" rel="noopener noreferrer" style={{ display: 'flex', alignItems: 'center', gap: '10px', padding: '12px 20px', backgroundColor: '#f8fafc', borderRadius: '8px', textDecoration: 'none', color: 'var(--text-dark)', border: '1px solid var(--border)', transition: 'background 0.2s' }}>
                      <FileText size={20} color="var(--primary)" />
                      <span style={{ flex: 1, fontWeight: 500 }}>{doc.nombre}</span>
                      <Download size={18} color="var(--text-light)" />
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

export default ConsultasPage;
