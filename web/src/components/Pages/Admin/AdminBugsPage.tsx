import { useState, useEffect } from 'react';
import { useAuth } from '../../../context/AuthContext';
import { ArrowLeft, Trash2, CheckCircle, Clock, Eye, X, ExternalLink } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import styles from './Admin.module.css';

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
      const res = await fetch('/api/admin/bugs', { headers: { 'Authorization': `Bearer ${token}` } });
      if (res.ok) setReports(await res.json());
    } catch (err) { console.error(err); }
    setLoading(false);
  };

  useEffect(() => {
    if (user?.role === 'admin') fetchReports();
  }, [user, token]);

  const handleResolve = async (id: number) => {
    if (!window.confirm("¿Marcar como resuelto? La captura de pantalla se borrará para ahorrar espacio.")) return;
    try {
      const res = await fetch(`/api/admin/bugs/${id}/resolve`, { method: 'PUT', headers: { 'Authorization': `Bearer ${token}` } });
      if (res.ok) {
        await fetchReports();
        if (selectedReport?.id === id) setSelectedReport(null);
      }
    } catch (err) { console.error(err); }
  };

  const handleDelete = async (id: number) => {
    if (!window.confirm("¿Eliminar este reporte permanentemente?")) return;
    try {
      const res = await fetch(`/api/admin/bugs/${id}`, { method: 'DELETE', headers: { 'Authorization': `Bearer ${token}` } });
      if (res.ok) {
        fetchReports();
        if (selectedReport?.id === id) setSelectedReport(null);
      } else {
        const data = await res.json();
        alert(data.detail || "No se pudo eliminar el reporte.");
      }
    } catch (err) { console.error(err); }
  };

  if (user?.role !== 'admin') {
    return <div className={styles.noAccess}>No tienes acceso a esta página.</div>;
  }

  return (
    <div className={styles.pageContainer}>
      <div>
        <div className={styles.backHeader}>
          <button onClick={() => navigate('/admin')} className={styles.backBtn}>
            <ArrowLeft size={20} />
          </button>
          <h1 className={styles.backPageTitle}>Gestión de Reportes de Bugs</h1>
        </div>
        <p className={styles.pageDescription}>Monitorea y resuelve los problemas técnicos informados por la comunidad.</p>
      </div>

      <div className={styles.tableWrapper}>
        <div className="table-container" style={{ width: '100%', backgroundColor: 'white', borderRadius: '12px', padding: '0', overflow: 'auto' }}>
          <table className="data-table">
            <thead>
              <tr>
                <th>Fecha</th><th>Usuario</th><th>Título</th><th>Estado</th><th>Acciones</th>
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
                    <td className={styles.tdSmallText}>{new Date(r.fecha_reporte).toLocaleString('es-ES')}</td>
                    <td className={styles.tdFontBold}>{r.user_name}</td>
                    <td>{r.titulo}</td>
                    <td>
                      <span className={`${styles.bugStatusBadge} ${r.status === 'resuelto' ? styles.bugStatusResuelto : styles.bugStatusPendiente}`}>
                        {r.status === 'resuelto' ? <CheckCircle size={12} /> : <Clock size={12} />}
                        {r.status === 'resuelto' ? 'Resuelto' : 'Pendiente'}
                      </span>
                    </td>
                    <td className={styles.tdActions}>
                      <button onClick={() => setSelectedReport(r)} className={`${styles.iconBtn} ${styles.iconBtnSuccess}`} title="Ver detalles" style={{ color: 'var(--primary)' }}>
                        <Eye size={18} />
                      </button>
                      {r.status !== 'resuelto' && (
                        <button onClick={() => handleResolve(r.id)} className={`${styles.iconBtn} ${styles.iconBtnSuccess}`} title="Marcar como resuelto">
                          <CheckCircle size={18} />
                        </button>
                      )}
                      {r.status === 'resuelto' && (
                        <button onClick={() => handleDelete(r.id)} className={`${styles.iconBtn} ${styles.iconBtnDanger}`} title="Eliminar permanentemente">
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

      {/* Modal */}
      {selectedReport && (
        <div className={styles.modalOverlay} onClick={() => setSelectedReport(null)}>
          <div className={styles.modalContent} onClick={e => e.stopPropagation()}>
            <button onClick={() => setSelectedReport(null)} className={styles.modalCloseBtn}>
              <X size={24} />
            </button>

            <div className={styles.modalHeader}>
              <span className={styles.modalBugId}>Reporte de Bug #{selectedReport.id}</span>
              <h2 className={styles.modalTitle}>{selectedReport.titulo}</h2>
              <div className={styles.modalMeta}>
                <span><strong>De:</strong> {selectedReport.user_name}</span>
                <span><strong>Fecha:</strong> {new Date(selectedReport.fecha_reporte).toLocaleString('es-ES')}</span>
              </div>
            </div>

            <div className={styles.modalDescriptionBox}>
              <h4 className={styles.modalDescriptionTitle}>Descripción</h4>
              <p className={styles.modalDescriptionText}>{selectedReport.descripcion}</p>
            </div>

            <div className={styles.modalActions}>
              {selectedReport.screenshot_path && selectedReport.status !== 'resuelto' ? (
                <a
                  href={selectedReport.screenshot_path}
                  target="_blank"
                  rel="noopener noreferrer"
                  className={styles.screenshotLink}
                >
                  <ExternalLink size={18} /> Ver Captura de Pantalla
                </a>
              ) : (
                <div className={styles.noScreenshot}>
                  {selectedReport.status === 'resuelto'
                    ? 'La captura de pantalla ha sido eliminada para ahorrar espacio.'
                    : 'No hay captura de pantalla asociada.'}
                </div>
              )}

              <div className={styles.modalActionsRight}>
                {selectedReport.status !== 'resuelto' && (
                  <button onClick={() => handleResolve(selectedReport.id)} className={styles.btnResolve}>
                    Resolver
                  </button>
                )}
                {selectedReport.status === 'resuelto' && (
                  <button onClick={() => handleDelete(selectedReport.id)} className={styles.btnDeleteRed}>
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
