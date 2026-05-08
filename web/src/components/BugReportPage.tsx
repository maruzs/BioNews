import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { Bug, Send, Image as ImageIcon, AlertCircle, CheckCircle, Clock, Trash2, X } from 'lucide-react';

interface BugReport {
  id: number;
  user_id: number;
  titulo: string;
  descripcion: string;
  screenshot_path: string | null;
  fecha_reporte: string;
  status: 'pendiente' | 'resuelto';
}

const BugReportPage = () => {
  const { token } = useAuth();
  const [titulo, setTitulo] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [screenshot, setScreenshot] = useState<File | null>(null);
  const [screenshotPreview, setScreenshotPreview] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<{ type: 'success' | 'error', text: string } | null>(null);
  
  const [myReports, setMyReports] = useState<BugReport[]>([]);
  const [loadingHistory, setLoadingHistory] = useState(false);
  const [selectedReportId, setSelectedReportId] = useState<number | null>(null);

  const fetchMyReports = async () => {
    setLoadingHistory(true);
    try {
      const res = await fetch('/api/bugs/my', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setMyReports(data);
      }
    } catch (err) {
      console.error(err);
    }
    setLoadingHistory(false);
  };

  useEffect(() => {
    fetchMyReports();
  }, [token]);

  useEffect(() => {
    if (screenshot) {
      const reader = new FileReader();
      reader.onloadend = () => {
        setScreenshotPreview(reader.result as string);
      };
      reader.readAsDataURL(screenshot);
    } else {
      setScreenshotPreview(null);
    }
  }, [screenshot]);

  const handlePaste = (e: React.ClipboardEvent) => {
    const items = e.clipboardData.items;
    for (let i = 0; i < items.length; i++) {
      if (items[i].type.indexOf('image') !== -1) {
        const file = items[i].getAsFile();
        if (file) {
          setScreenshot(file);
        }
      }
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setMessage(null);

    if (!titulo || !descripcion) {
      setMessage({ type: 'error', text: 'Por favor completa todos los campos requeridos.' });
      setLoading(false);
      return;
    }

    const formData = new FormData();
    formData.append('titulo', titulo);
    formData.append('descripcion', descripcion);
    if (screenshot) {
      if (screenshot.size > 5 * 1024 * 1024) {
        setMessage({ type: 'error', text: 'La imagen excede los 5MB permitidos.' });
        setLoading(false);
        return;
      }
      formData.append('screenshot', screenshot);
    }

    try {
      const res = await fetch('/api/bugs', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`
        },
        body: formData
      });

      if (res.ok) {
        setMessage({ type: 'success', text: 'Reporte enviado con éxito. ¡Gracias por ayudarnos a mejorar!' });
        setTitulo('');
        setDescripcion('');
        setScreenshot(null);
        fetchMyReports();
      } else {
        const err = await res.json();
        setMessage({ type: 'error', text: err.detail || 'Error al enviar el reporte.' });
      }
    } catch (err) {
      setMessage({ type: 'error', text: 'Error de conexión con el servidor.' });
    }
    setLoading(false);
  };

  const handleDelete = async (id: number) => {
    if (!window.confirm("¿Deseas eliminar este reporte permanentemente de tu historial?")) return;
    try {
      const res = await fetch(`/api/bugs/${id}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        fetchMyReports();
        if (selectedReportId === id) setSelectedReportId(null);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const toggleModal = (id: number) => {
    if (selectedReportId === id) {
      setSelectedReportId(null);
    } else {
      setSelectedReportId(id);
    }
  };

  return (
    <div className="report-container">
      <div className="report-header-text">
        <h1 className="report-title">Reporte de Bugs</h1>
        <p className="report-description">Ayúdanos a mejorar BioNews informando sobre cualquier error o problema técnico.</p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))', gap: '40px', marginTop: '20px' }}>
        
        {/* Formulario de reporte */}
        <div style={{ background: 'white', padding: '30px', borderRadius: '16px', border: '1px solid var(--border)', boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.05)' }}>
          <h2 style={{ fontSize: '1.2rem', fontWeight: 700, marginBottom: '20px', display: 'flex', alignItems: 'center', gap: '10px' }}>
            <Bug size={20} color="var(--primary)" /> Nuevo Reporte
          </h2>

          <form onSubmit={handleSubmit}>
            <div style={{ marginBottom: '20px' }}>
              <label style={{ display: 'block', fontSize: '0.9rem', fontWeight: 600, marginBottom: '8px', color: '#475569' }}>Título del Bug *</label>
              <input 
                type="text" 
                value={titulo}
                onChange={(e) => setTitulo(e.target.value)}
                placeholder="Ej: El botón de favoritos no funciona en MMA"
                style={{ width: '100%', padding: '12px 16px', borderRadius: '8px', border: '1px solid var(--border)', outline: 'none' }}
                required
              />
            </div>

            <div style={{ marginBottom: '20px' }}>
              <label style={{ display: 'block', fontSize: '0.9rem', fontWeight: 600, marginBottom: '8px', color: '#475569' }}>Descripción detallada *</label>
              <textarea 
                value={descripcion}
                onChange={(e) => setDescripcion(e.target.value)}
                onPaste={handlePaste}
                placeholder="Explica qué sucedió y cómo podemos reproducir el error... (Puedes pegar una captura de pantalla aquí)"
                rows={5}
                style={{ width: '100%', padding: '12px 16px', borderRadius: '8px', border: '1px solid var(--border)', outline: 'none', resize: 'vertical' }}
                required
              />
            </div>

            <div style={{ marginBottom: '25px' }}>
              <label style={{ display: 'block', fontSize: '0.9rem', fontWeight: 600, marginBottom: '8px', color: '#475569' }}>Captura de pantalla (Opcional, máx 5MB)</label>
              <div style={{ position: 'relative', display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <div style={{ position: 'relative', display: 'flex', alignItems: 'center', gap: '10px' }}>
                  <input 
                    type="file" 
                    accept="image/*"
                    onChange={(e) => setScreenshot(e.target.files?.[0] || null)}
                    style={{ position: 'absolute', inset: 0, opacity: 0, cursor: 'pointer' }}
                  />
                  <div style={{ padding: '10px 20px', background: '#f1f5f9', borderRadius: '8px', display: 'flex', alignItems: 'center', gap: '8px', border: '1px solid var(--border)' }}>
                    <ImageIcon size={18} /> {screenshot ? (screenshot.name || 'Imagen pegada') : 'Seleccionar imagen'}
                  </div>
                  {screenshot && (
                    <button 
                      type="button"
                      onClick={() => setScreenshot(null)}
                      style={{ background: 'none', border: 'none', color: '#ef4444', fontSize: '0.8rem', cursor: 'pointer', fontWeight: 600 }}
                    >
                      Eliminar
                    </button>
                  )}
                </div>
                {screenshotPreview && (
                  <div style={{ marginTop: '10px', borderRadius: '8px', overflow: 'hidden', border: '1px solid var(--border)', maxWidth: '100%' }}>
                    <img src={screenshotPreview} alt="Preview" style={{ width: '100%', display: 'block' }} />
                  </div>
                )}
              </div>
            </div>

            {message && (
              <div style={{ 
                padding: '12px 16px', 
                borderRadius: '8px', 
                marginBottom: '20px', 
                display: 'flex', 
                alignItems: 'center', 
                gap: '10px',
                background: message.type === 'success' ? '#f0fdf4' : '#fef2f2',
                color: message.type === 'success' ? '#166534' : '#991b1b',
                border: `1px solid ${message.type === 'success' ? '#bbf7d0' : '#fecaca'}`
              }}>
                {message.type === 'success' ? <CheckCircle size={18} /> : <AlertCircle size={18} />}
                <span style={{ fontSize: '0.9rem' }}>{message.text}</span>
              </div>
            )}

            <button 
              type="submit" 
              disabled={loading}
              className="btn-primary"
              style={{ width: '100%', justifyContent: 'center', padding: '14px', gap: '10px' }}
            >
              {loading ? 'Enviando...' : <><Send size={18} /> Enviar Reporte</>}
            </button>
          </form>
        </div>

        {/* Historial personal */}
        <div style={{ background: 'white', padding: '30px', borderRadius: '16px', border: '1px solid var(--border)', boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.05)', maxHeight: '700px', overflowY: 'auto' }}>
          <h2 style={{ fontSize: '1.2rem', fontWeight: 700, marginBottom: '20px', display: 'flex', alignItems: 'center', gap: '10px' }}>
            <Clock size={20} color="var(--primary)" /> Mis Reportes
          </h2>

          {loadingHistory ? (
            <p>Cargando historial...</p>
          ) : myReports.length === 0 ? (
            <p style={{ color: 'var(--text-light)', fontStyle: 'italic' }}>No has enviado reportes aún.</p>
          ) : (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
              {myReports.map((report) => (
                <div key={report.id} style={{ border: '1px solid #f1f5f9', borderRadius: '12px', overflow: 'hidden' }}>
                  <div 
                    onClick={() => toggleModal(report.id)}
                    style={{ 
                      padding: '15px 20px', 
                      background: '#f8fafc', 
                      cursor: 'pointer', 
                      display: 'flex', 
                      justifyContent: 'space-between', 
                      alignItems: 'center',
                      borderBottom: selectedReportId === report.id ? '1px solid #f1f5f9' : 'none'
                    }}
                  >
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '4px' }}>
                      <span style={{ fontSize: '0.95rem', fontWeight: 600, color: '#1e293b' }}>{report.titulo}</span>
                      <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>{new Date(report.fecha_reporte).toLocaleDateString('es-ES')}</span>
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '15px' }}>
                      <span style={{ 
                        fontSize: '0.7rem', 
                        fontWeight: 700, 
                        padding: '3px 8px', 
                        borderRadius: '12px',
                        background: report.status === 'resuelto' ? '#f0fdf4' : '#fff7ed',
                        color: report.status === 'resuelto' ? '#166534' : '#c2410c',
                        textTransform: 'uppercase'
                      }}>
                        {report.status}
                      </span>
                      <Trash2 
                        size={16} 
                        color="#ef4444" 
                        style={{ cursor: 'pointer' }} 
                        onClick={(e) => { e.stopPropagation(); handleDelete(report.id); }} 
                      />
                    </div>
                  </div>
                  
                  {selectedReportId === report.id && (
                    <div style={{ padding: '20px', background: 'white', borderTop: '1px solid #f1f5f9' }}>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '10px' }}>
                        <h4 style={{ margin: 0, fontSize: '0.85rem', color: '#64748b', textTransform: 'uppercase' }}>Descripción del problema</h4>
                        <button onClick={() => setSelectedReportId(null)} style={{ background: 'none', border: 'none', cursor: 'pointer', color: '#94a3b8' }}><X size={16} /></button>
                      </div>
                      <p style={{ margin: 0, fontSize: '0.95rem', color: '#475569', lineHeight: '1.6', whiteSpace: 'pre-wrap' }}>{report.descripcion}</p>
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>

      </div>
    </div>
  );
};

export default BugReportPage;
