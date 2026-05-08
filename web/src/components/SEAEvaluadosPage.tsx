import React, { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';
import { Heart, Calendar, RefreshCw, FileText } from 'lucide-react';

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
  url: string;
  fecha_scraping: string;
  is_new: boolean;
}

const SEAEvaluadosPage = () => {
  const { token } = useAuth();
  const { refreshCategory, setCategoryActive } = useNotifications();
  const [data, setData] = useState<SEAEvaluado[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [selectedItem, setSelectedItem] = useState<SEAEvaluado | null>(null);
  
  // Modal state
  const [showModal, setShowModal] = useState(false);

  // Paginación y filtrado simple
  const [searchTerm, setSearchTerm] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 12;

  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await fetch('/api/data/sea_proyectos_evaluados', {
        headers: {
          'Authorization': `Bearer ${token}`
        }
      });
      if (!response.ok) throw new Error('Error al obtener los datos');
      const result = await response.json();
      setData(result);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
    // Marcar como activo para notificaciones
    setCategoryActive('sea_proyectos_evaluados', true);
    refreshCategory('sea_proyectos_evaluados');
    
    return () => {
      setCategoryActive('sea_proyectos_evaluados', false);
    };
  }, [token]);

  const toggleFavorite = async (e: React.MouseEvent, item: SEAEvaluado) => {
    e.stopPropagation();
    // Logic to toggle favorite via API would go here.
    alert(`Funcionalidad de favoritos para "${item.nombre}" a implementar`);
  };

  const filteredData = data.filter(item => 
    item.nombre?.toLowerCase().includes(searchTerm.toLowerCase()) || 
    item.titular?.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const paginatedData = filteredData.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);
  const totalPages = Math.ceil(filteredData.length / itemsPerPage);

  const getStatusColor = (estado: string) => {
    const estadoLower = estado?.toLowerCase() || '';
    if (estadoLower.includes('aprobado') || estadoLower.includes('calificacion favorable')) return '#10b981'; // Green
    if (estadoLower.includes('rechazado') || estadoLower.includes('desistido')) return '#ef4444'; // Red
    if (estadoLower.includes('calificación')) return '#f59e0b'; // Amber
    if (estadoLower.includes('admisión')) return '#3b82f6'; // Blue
    return '#64748b'; // Gray
  };

  return (
    <div style={{ padding: '20px', maxWidth: '1200px', margin: '0 auto' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
        <div>
          <h1 style={{ fontSize: '24px', fontWeight: 'bold', color: 'var(--text-dark)' }}>Proyectos Evaluados SEA</h1>
          <p style={{ color: 'var(--text-light)', marginTop: '5px' }}>Visualización de proyectos evaluados en el Sistema de Evaluación de Impacto Ambiental.</p>
        </div>
        <button 
          onClick={fetchData}
          disabled={loading}
          style={{ 
            display: 'flex', alignItems: 'center', gap: '8px', 
            padding: '10px 15px', backgroundColor: 'var(--primary)', 
            color: 'white', border: 'none', borderRadius: '6px', 
            cursor: loading ? 'not-allowed' : 'pointer',
            opacity: loading ? 0.7 : 1
          }}
        >
          <RefreshCw size={18} className={loading ? 'spin' : ''} />
          Refrescar
        </button>
      </div>

      <div style={{ marginBottom: '20px' }}>
        <input 
          type="text" 
          placeholder="Buscar por nombre o titular..." 
          value={searchTerm}
          onChange={(e) => { setSearchTerm(e.target.value); setCurrentPage(1); }}
          style={{ width: '100%', padding: '12px', borderRadius: '8px', border: '1px solid var(--border)', outline: 'none' }}
        />
      </div>

      {loading ? (
        <div style={{ textAlign: 'center', padding: '40px' }}>Cargando datos...</div>
      ) : error ? (
        <div style={{ color: '#ef4444', backgroundColor: '#fee2e2', padding: '15px', borderRadius: '8px' }}>{error}</div>
      ) : (
        <>
          <div style={{ 
            display: 'grid', 
            gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))', 
            gap: '20px',
            marginBottom: '30px'
          }}>
            {paginatedData.map(item => (
              <div key={item.id} style={{ 
                backgroundColor: 'white', 
                borderRadius: '12px', 
                border: '1px solid var(--border)',
                overflow: 'hidden',
                boxShadow: '0 2px 8px rgba(0,0,0,0.05)',
                display: 'flex',
                flexDirection: 'column',
                transition: 'transform 0.2s',
                cursor: 'pointer'
              }}
              onClick={() => { setSelectedItem(item); setShowModal(true); }}
              onMouseOver={(e) => e.currentTarget.style.transform = 'translateY(-4px)'}
              onMouseOut={(e) => e.currentTarget.style.transform = 'translateY(0)'}
              >
                <div style={{ padding: '15px', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
                    <div style={{ 
                      width: '10px', height: '10px', borderRadius: '50%', 
                      backgroundColor: getStatusColor(item.estado_proyecto) 
                    }}></div>
                    <span style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-dark)' }}>
                      {item.estado_proyecto} {item.subestado_proyecto && `(${item.subestado_proyecto})`}
                    </span>
                  </div>
                  <div style={{ display: 'flex', gap: '10px' }}>
                    {item.is_new && <span style={{ fontSize: '11px', backgroundColor: '#3b82f6', color: 'white', padding: '2px 8px', borderRadius: '12px', fontWeight: 'bold' }}>NUEVO</span>}
                    <Heart size={18} color="var(--text-light)" onClick={(e) => toggleFavorite(e, item)} style={{ cursor: 'pointer' }} />
                  </div>
                </div>
                <div style={{ padding: '15px', flexGrow: 1 }}>
                  <h3 style={{ fontSize: '16px', fontWeight: 'bold', color: 'var(--primary)', marginBottom: '10px', display: '-webkit-box', WebkitLineClamp: 3, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>
                    {item.nombre}
                  </h3>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', color: 'var(--text-light)', fontSize: '13px', marginBottom: '5px' }}>
                    <Calendar size={14} />
                    <span>{item.fecha_presentacion}</span>
                  </div>
                </div>
                <div style={{ padding: '15px', backgroundColor: '#f8fafc', borderTop: '1px solid var(--border)', textAlign: 'center', fontSize: '14px', fontWeight: 500, color: 'var(--primary)' }}>
                  Ver detalles
                </div>
              </div>
            ))}
          </div>

          {totalPages > 1 && (
            <div style={{ display: 'flex', justifyContent: 'center', gap: '10px', alignItems: 'center' }}>
              <button 
                onClick={() => setCurrentPage(p => Math.max(1, p - 1))}
                disabled={currentPage === 1}
                style={{ padding: '8px 12px', borderRadius: '6px', border: '1px solid var(--border)', background: currentPage === 1 ? '#f1f5f9' : 'white', cursor: currentPage === 1 ? 'not-allowed' : 'pointer' }}
              >
                Anterior
              </button>
              <span style={{ fontSize: '14px', color: 'var(--text-dark)' }}>Página {currentPage} de {totalPages}</span>
              <button 
                onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))}
                disabled={currentPage === totalPages}
                style={{ padding: '8px 12px', borderRadius: '6px', border: '1px solid var(--border)', background: currentPage === totalPages ? '#f1f5f9' : 'white', cursor: currentPage === totalPages ? 'not-allowed' : 'pointer' }}
              >
                Siguiente
              </button>
            </div>
          )}
        </>
      )}

      {/* Modal de Detalles */}
      {showModal && selectedItem && (
        <div style={{ 
          position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, 
          backgroundColor: 'rgba(0,0,0,0.5)', zIndex: 1000,
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          padding: '20px'
        }} onClick={() => setShowModal(false)}>
          <div style={{ 
            backgroundColor: 'white', borderRadius: '12px', padding: '30px', 
            maxWidth: '600px', width: '100%', maxHeight: '90vh', overflowY: 'auto'
          }} onClick={e => e.stopPropagation()}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '20px' }}>
              <h2 style={{ fontSize: '20px', fontWeight: 'bold', color: 'var(--primary)', paddingRight: '20px' }}>{selectedItem.nombre}</h2>
              <button onClick={() => setShowModal(false)} style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-light)' }}>✕</button>
            </div>
            
            <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
              <div style={{ display: 'grid', gridTemplateColumns: '120px 1fr', gap: '10px' }}>
                <span style={{ fontWeight: 600, color: 'var(--text-dark)' }}>ID:</span>
                <span style={{ color: 'var(--text-light)' }}>{selectedItem.id}</span>
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '120px 1fr', gap: '10px' }}>
                <span style={{ fontWeight: 600, color: 'var(--text-dark)' }}>Titular:</span>
                <span style={{ color: 'var(--text-light)' }}>{selectedItem.titular}</span>
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '120px 1fr', gap: '10px' }}>
                <span style={{ fontWeight: 600, color: 'var(--text-dark)' }}>Presentación:</span>
                <span style={{ color: 'var(--text-light)' }}>{selectedItem.fecha_presentacion}</span>
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '120px 1fr', gap: '10px' }}>
                <span style={{ fontWeight: 600, color: 'var(--text-dark)' }}>Razón Ingreso:</span>
                <span style={{ color: 'var(--text-light)' }}>{selectedItem.razon_ingreso}</span>
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '120px 1fr', gap: '10px' }}>
                <span style={{ fontWeight: 600, color: 'var(--text-dark)' }}>Estado:</span>
                <span style={{ color: 'var(--text-light)' }}>
                  <span style={{ 
                    display: 'inline-block', padding: '2px 8px', borderRadius: '12px', fontSize: '13px', fontWeight: 600,
                    backgroundColor: getStatusColor(selectedItem.estado_proyecto), color: 'white'
                  }}>
                    {selectedItem.estado_proyecto} {selectedItem.subestado_proyecto && `(${selectedItem.subestado_proyecto})`}
                  </span>
                </span>
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '120px 1fr', gap: '10px' }}>
                <span style={{ fontWeight: 600, color: 'var(--text-dark)' }}>Tipo Proyecto:</span>
                <span style={{ color: 'var(--text-light)' }}>{selectedItem.tipo_proyecto}</span>
              </div>
            </div>

            <div style={{ marginTop: '30px', display: 'flex', justifyContent: 'flex-end' }}>
              <a 
                href={selectedItem.url} 
                target="_blank" 
                rel="noopener noreferrer"
                style={{ 
                  display: 'inline-flex', alignItems: 'center', gap: '8px',
                  padding: '10px 20px', backgroundColor: 'var(--primary)', color: 'white',
                  textDecoration: 'none', borderRadius: '6px', fontWeight: 600
                }}
              >
                <FileText size={18} />
                Ver Ficha en SEA
              </a>
            </div>
          </div>
        </div>
      )}

      <style dangerouslySetInnerHTML={{ __html: `
        .spin {
          animation: spin 1s linear infinite;
        }
        @keyframes spin {
          100% { transform: rotate(360deg); }
        }
      ` }} />
    </div>
  );
};

export default SEAEvaluadosPage;
