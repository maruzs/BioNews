import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { Bug, Send, Image as ImageIcon, AlertCircle, CheckCircle } from 'lucide-react';

interface BugReport {
  id: number;
  user_id: number;
  user_name: string;
  titulo: string;
  descripcion: string;
  screenshot_path: string | null;
  fecha_reporte: string;
}

const BugReportPage = () => {
  const { user, token } = useAuth();
  const [titulo, setTitulo] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [screenshot, setScreenshot] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<{ type: 'success' | 'error', text: string } | null>(null);
  
  // Admin state
  const [reports, setReports] = useState<BugReport[]>([]);
  const [loadingReports, setLoadingReports] = useState(false);

  const isAdmin = user?.role === 'admin';

  useEffect(() => {
    if (isAdmin) {
      fetchReports();
    }
  }, [isAdmin]);

  const fetchReports = async () => {
    setLoadingReports(true);
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
    setLoadingReports(false);
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
        if (isAdmin) fetchReports();
      } else {
        const err = await res.json();
        setMessage({ type: 'error', text: err.detail || 'Error al enviar el reporte.' });
      }
    } catch (err) {
      setMessage({ type: 'error', text: 'Error de conexión con el servidor.' });
    }
    setLoading(false);
  };

  return (
    <div className="report-container">
      <div className="report-header-text">
        <h1 className="report-title">Reporte de Bugs</h1>
        <p className="report-description">Ayúdanos a mejorar BioNews informando sobre cualquier error o problema técnico.</p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: isAdmin ? '1fr 1fr' : '1fr', gap: '40px', marginTop: '20px' }}>
        
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
                placeholder="Explica qué sucedió y cómo podemos reproducir el error..."
                rows={5}
                style={{ width: '100%', padding: '12px 16px', borderRadius: '8px', border: '1px solid var(--border)', outline: 'none', resize: 'vertical' }}
                required
              />
            </div>

            <div style={{ marginBottom: '25px' }}>
              <label style={{ display: 'block', fontSize: '0.9rem', fontWeight: 600, marginBottom: '8px', color: '#475569' }}>Captura de pantalla (Opcional, máx 5MB)</label>
              <div style={{ position: 'relative', display: 'flex', alignItems: 'center', gap: '10px' }}>
                <input 
                  type="file" 
                  accept="image/*"
                  onChange={(e) => setScreenshot(e.target.files?.[0] || null)}
                  style={{ position: 'absolute', inset: 0, opacity: 0, cursor: 'pointer' }}
                />
                <div style={{ padding: '10px 20px', background: '#f1f5f9', borderRadius: '8px', display: 'flex', alignItems: 'center', gap: '8px', border: '1px solid var(--border)' }}>
                  <ImageIcon size={18} /> {screenshot ? screenshot.name : 'Seleccionar imagen'}
                </div>
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

        {/* Listado para administrador */}
        {isAdmin && (
          <div style={{ background: 'white', padding: '30px', borderRadius: '16px', border: '1px solid var(--border)', boxShadow: '0 4px 6px -1px rgba(0, 0, 0, 0.05)', maxHeight: '700px', overflowY: 'auto' }}>
            <h2 style={{ fontSize: '1.2rem', fontWeight: 700, marginBottom: '20px', display: 'flex', alignItems: 'center', gap: '10px' }}>
              <AlertCircle size={20} color="var(--orange)" /> Reportes Recibidos
            </h2>

            {loadingReports ? (
              <p>Cargando reportes...</p>
            ) : reports.length === 0 ? (
              <p style={{ color: 'var(--text-light)', fontStyle: 'italic' }}>No hay reportes de bugs registrados.</p>
            ) : (
              <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                {reports.map((report) => (
                  <div key={report.id} style={{ padding: '20px', borderRadius: '12px', border: '1px solid #f1f5f9', background: '#f8fafc' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '8px' }}>
                      <span style={{ fontSize: '0.8rem', fontWeight: 700, color: 'var(--primary)' }}>{report.user_name}</span>
                      <span style={{ fontSize: '0.75rem', color: '#94a3b8' }}>{report.fecha_reporte}</span>
                    </div>
                    <h3 style={{ fontSize: '1rem', fontWeight: 700, marginBottom: '8px', color: '#1e293b' }}>{report.titulo}</h3>
                    <p style={{ fontSize: '0.9rem', color: '#475569', marginBottom: '15px', lineHeight: '1.5' }}>{report.descripcion}</p>
                    {report.screenshot_path && (
                      <a 
                        href={report.screenshot_path} 
                        target="_blank" 
                        rel="noopener noreferrer"
                        style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', fontSize: '0.85rem', color: 'var(--primary)', fontWeight: 600, textDecoration: 'none' }}
                      >
                        <ImageIcon size={14} /> Ver captura de pantalla
                      </a>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

      </div>
    </div>
  );
};

export default BugReportPage;
