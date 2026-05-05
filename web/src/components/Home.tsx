import { useState, useEffect } from 'react';
import { Activity, AlertTriangle, CheckCircle2 } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

interface ScraperLog {
  fuente: string;
  ultimo_intento: string;
  ultimo_exito: string;
  estado: string;
  error: string;
  nuevos_registros: number;
}

const Home = () => {
  const { token } = useAuth();
  const [logs, setLogs] = useState<ScraperLog[]>([]);

  const fetchLogs = () => {
    if (!token) return;
    fetch('/api/logs', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(res => res.json())
      .then(data => {
        setLogs(data);
      })
      .catch(err => {
        console.error("Error fetching logs:", err);
      });
  };

  useEffect(() => {
    fetchLogs();
  }, []);


  return (
    <div className="report-container">
      <div className="report-header-text">
        <h1 className="report-title">Dashboard del Sistema</h1>
        <p className="report-description">Estado actual de la recolección de datos y actualización de fuentes.</p>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '20px', marginBottom: '30px' }}>
        <div style={{ background: 'white', border: '1px solid var(--border)', borderRadius: '12px', padding: '20px', display: 'flex', alignItems: 'center', gap: '15px' }}>
          <div style={{ background: 'var(--primary-light)', padding: '12px', borderRadius: '50%', color: 'var(--primary)' }}>
            <Activity size={24} />
          </div>
          <div>
            <div style={{ fontSize: '13px', color: 'var(--text-light)', fontWeight: 600 }}>Fuentes Activas</div>
            <div style={{ fontSize: '24px', fontWeight: 700, color: 'var(--text-dark)' }}>{logs.length}</div>
          </div>
        </div>

        <div style={{ background: 'white', border: '1px solid var(--border)', borderRadius: '12px', padding: '20px', display: 'flex', alignItems: 'center', gap: '15px' }}>
          <div style={{ background: '#ecfdf5', padding: '12px', borderRadius: '50%', color: '#10b981' }}>
            <CheckCircle2 size={24} />
          </div>
          <div>
            <div style={{ fontSize: '13px', color: 'var(--text-light)', fontWeight: 600 }}>Scraping Exitoso</div>
            <div style={{ fontSize: '24px', fontWeight: 700, color: 'var(--text-dark)' }}>{logs.filter(l => l.estado === 'OK').length}</div>
          </div>
        </div>

        <div style={{ background: 'white', border: '1px solid var(--border)', borderRadius: '12px', padding: '20px', display: 'flex', alignItems: 'center', gap: '15px' }}>
          <div style={{ background: '#fef2f2', padding: '12px', borderRadius: '50%', color: '#ef4444' }}>
            <AlertTriangle size={24} />
          </div>
          <div>
            <div style={{ fontSize: '13px', color: 'var(--text-light)', fontWeight: 600 }}>Con Errores</div>
            <div style={{ fontSize: '24px', fontWeight: 700, color: 'var(--text-dark)' }}>{logs.filter(l => l.estado === 'ERROR').length}</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
