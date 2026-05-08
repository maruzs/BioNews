import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { ArrowLeft, Trash2, CheckCircle, Clock, Eye, X, ExternalLink } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

interface BugReport {
  id: number;
  user_id: number;
  user_name: string;
  titulo: string;
  descripcion: string;
  screenshot_path: string | null;
  fecha_reporte: string;
  status: 'pendiente' | 'resuelto';
}

const AdminBugsPage = () => {
  const { token, user } = useAuth();
  const [reports, setReports] = useState<BugReport[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedReport, setSelectedReport] = useState<BugReport | null>(null);
  const navigate = useNavigate();

  const fetchReports = async () => {
    setLoading(true);
    try {
      const res = await fetch('/api/admin/bugs', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setReports(data);
      }
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  useEffect(() => {
    if (user?.role === 'admin') {
      fetchReports();
    }
  }, [user, token]);

  const handleResolve = async (id: number) => {
    if (!window.confirm("¿Marcar como resuelto? La captura de pantalla se borrará para ahorrar espacio.")) return;
    try {
      const res = await fetch(`/api/admin/bugs/${id}/resolve`, {
        method: 'PUT',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        await fetchReports();
        // Cerramos el modal si estaba abierto para este reporte
        if (selectedReport?.id === id) setSelectedReport(null);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const handleDelete = async (id: number) => {
    if (!window.confirm("¿Eliminar este reporte permanentemente?")) return;
    try {
      const res = await fetch(`/api/admin/bugs/${id}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        fetchReports();
        if (selectedReport?.id === id) setSelectedReport(null);
      } else {
        const data = await res.json();
        alert(data.detail || "No se pudo eliminar el reporte.");
      }
    } catch (err) {
      console.error(err);
    }
  };

  if (user?.role !== 'admin') {
    return <div style={{ padding: '40px', textAlign: 'center' }}>No tienes acceso a esta página.</div>;
  }

  return (
    <div className="report-container">
      <div className="report-header-text">
        <div style={{ display: 'flex', alignItems: 'center', gap: '15px', marginBottom: '10px' }}>
          <button onClick={() => navigate('/admin')} style={{ background: 'none', border: 'none', cursor: 'pointer', display: 'flex', alignItems: 'center', color: 'var(--primary)' }}>
            <ArrowLeft size={20} />
          </button>
          <h1 className="report-title" style={{ margin: 0 }}>Gestión de Reportes de Bugs</h1>
        </div>
        <p className="report-description">Monitorea y resuelve los problemas técnicos informados por la comunidad.</p>
      </div>

      <div style={{ marginTop: '30px' }}>
        <div className="table-container" style={{ width: '100%', backgroundColor: 'white', borderRadius: '12px', padding: '0', overflow: 'auto' }}>
          <table className="data-table">
            <thead>
              <tr>
                <th>Fecha</th>
                <th>Usuario</th>
                <th>Título</th>
                <th>Estado</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              {loading ? (
                <tr><td colSpan={5} style={{ textAlign: 'center', padding: '20px' }}>Cargando reportes...</td></tr>
              ) : reports.length === 0 ? (
                <tr><td colSpan={5} style={{ textAlign: 'center', padding: '20px' }}>No hay reportes registrados.</td></tr>
              ) : (
                reports.map((r) => (
                  <tr key={r.id}>
                    <td style={{ fontSize: '0.85rem' }}>{new Date(r.fecha_reporte).toLocaleString('es-ES')}</td>
                    <td style={{ fontWeight: 600 }}>{r.user_name}</td>
                    <td>{r.titulo}</td>
                    <td>
                      <span style={{ 
                        display: 'inline-flex', 
                        alignItems: 'center', 
                        gap: '5px', 
                        padding: '4px 10px', 
                        borderRadius: '20px', 
                        fontSize: '0.75rem', 
                        fontWeight: 700,
                        background: r.status === 'resuelto' ? '#f0fdf4' : '#fff7ed',
                        color: r.status === 'resuelto' ? '#166534' : '#c2410c'
                      }}>
                        {r.status === 'resuelto' ? <CheckCircle size={12} /> : <Clock size={12} />}
                        {r.status === 'resuelto' ? 'Resuelto' : 'Pendiente'}
                      </span>
                    </td>
                    <td style={{ display: 'flex', gap: '10px' }}>
                      <button onClick={() => setSelectedReport(r)} style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--primary)' }} title="Ver detalles">
                        <Eye size={18} />
                      </button>
                      {r.status !== 'resuelto' && (
                        <button onClick={() => handleResolve(r.id)} style={{ background: 'none', border: 'none', cursor: 'pointer', color: '#10b981' }} title="Marcar como resuelto">
                          <CheckCircle size={18} />
                        </button>
                      )}
                      {r.status === 'resuelto' && (
                        <button onClick={() => handleDelete(r.id)} style={{ background: 'none', border: 'none', cursor: 'pointer', color: '#ef4444' }} title="Eliminar permanentemente">
                          <Trash2 size={18} />
                        </button>
                      )}
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>

      {/* Modal de Detalles */}
      {selectedReport && (
        <div className="modal-overlay" style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex', justifyContent: 'center', alignItems: 'center', zIndex: 1000 }} onClick={() => setSelectedReport(null)}>
          <div className="modal-content" style={{ backgroundColor: 'white', borderRadius: '16px', padding: '30px', maxWidth: '600px', width: '90%', position: 'relative' }} onClick={e => e.stopPropagation()}>
            <button onClick={() => setSelectedReport(null)} style={{ position: 'absolute', top: '15px', right: '15px', background: 'none', border: 'none', cursor: 'pointer', color: '#64748b' }}>
              <X size={24} />
            </button>
            
            <div style={{ marginBottom: '20px' }}>
              <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--primary)', textTransform: 'uppercase' }}>Reporte de Bug #{selectedReport.id}</span>
              <h2 style={{ fontSize: '1.4rem', fontWeight: 700, marginTop: '5px' }}>{selectedReport.titulo}</h2>
              <div style={{ display: 'flex', gap: '15px', marginTop: '10px', fontSize: '0.85rem', color: '#64748b' }}>
                <span><strong>De:</strong> {selectedReport.user_name}</span>
                <span><strong>Fecha:</strong> {new Date(selectedReport.fecha_reporte).toLocaleString('es-ES')}</span>
              </div>
            </div>

            <div style={{ background: '#f8fafc', padding: '20px', borderRadius: '12px', border: '1px solid #e2e8f0', marginBottom: '25px' }}>
              <h4 style={{ margin: '0 0 10px 0', fontSize: '0.9rem', color: '#475569' }}>Descripción</h4>
              <p style={{ margin: 0, lineHeight: '1.6', whiteSpace: 'pre-wrap' }}>{selectedReport.descripcion}</p>
            </div>

            <div style={{ display: 'flex', gap: '15px', flexWrap: 'wrap' }}>
              {selectedReport.screenshot_path && selectedReport.status !== 'resuelto' ? (
                <a 
                  href={selectedReport.screenshot_path} 
                  target="_blank" 
                  rel="noopener noreferrer" 
                  className="btn-secondary"
                  style={{ display: 'flex', alignItems: 'center', gap: '8px', textDecoration: 'none' }}
                >
                  <ExternalLink size={18} /> Ver Captura de Pantalla
                </a>
              ) : (
                <div style={{ fontSize: '0.85rem', color: '#94a3b8', fontStyle: 'italic', display: 'flex', alignItems: 'center', gap: '5px' }}>
                  {selectedReport.status === 'resuelto' 
                    ? 'La captura de pantalla ha sido eliminada para ahorrar espacio.' 
                    : 'No hay captura de pantalla asociada.'}
                </div>
              )}
              
              <div style={{ marginLeft: 'auto', display: 'flex', gap: '10px' }}>
                {selectedReport.status !== 'resuelto' && (
                  <button onClick={() => handleResolve(selectedReport.id)} className="btn-primary" style={{ background: '#10b981', border: 'none' }}>
                    Resolver
                  </button>
                )}
                {selectedReport.status === 'resuelto' && (
                   <button onClick={() => handleDelete(selectedReport.id)} className="btn-primary" style={{ background: '#ef4444', border: 'none' }}>
                    Eliminar
                  </button>
                )}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default AdminBugsPage;
