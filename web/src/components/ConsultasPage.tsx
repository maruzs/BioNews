import { useState, useEffect } from 'react';
import { Search, Calendar, FileText, Download, X } from 'lucide-react';
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
    item.titulo.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="report-container">
      <div className="report-header-text">
        <h1 className="report-title">{title}</h1>
        <p className="report-description">{description}</p>
      </div>

      <div className="news-filters" style={{ marginBottom: '20px' }}>
        <div className="search-bar" style={{ maxWidth: '400px', background: 'white', border: '1px solid var(--border)', borderRadius: '30px', padding: '10px 20px', display: 'flex', alignItems: 'center' }}>
          <Search size={18} color="var(--primary)" style={{ marginRight: '10px' }} />
          <input
            type="text"
            placeholder="Buscar consulta..."
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
