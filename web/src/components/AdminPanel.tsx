import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { ShieldAlert, Trash2, ShieldOff, Play, Save } from 'lucide-react';

const AdminPanel = () => {
  const { token, user } = useAuth();
  const [users, setUsers] = useState<any[]>([]);
  const [logs, setLogs] = useState<any[]>([]);
  const [scraping, setScraping] = useState<string | null>(null);
  const [schedulerConfig, setSchedulerConfig] = useState<any>({
    snifa_time_1: "07:00",
    snifa_time_2: "14:00",
    pertinencias_interval: 1,
    noticias_interval: 1,
    tribunales_interval: 1,
    hora_inicio: "07:00",
    hora_fin: "19:00"
  });

  const fetchUsers = async () => {
    try {
      const res = await fetch('/api/admin/users', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setUsers(data);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const fetchLogs = async () => {
    try {
      const res = await fetch('/api/logs', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setLogs(data);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const fetchSchedulerConfig = async () => {
    try {
      const res = await fetch('/api/admin/scheduler', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (res.ok) {
        setSchedulerConfig(await res.json());
      }
    } catch (err) {}
  };

  useEffect(() => {
    if (user?.role === 'admin') {
      fetchUsers();
      fetchLogs();
      fetchSchedulerConfig();
    }
  }, [user, token]);

  const saveSchedulerConfig = async () => {
    try {
      await fetch('/api/admin/scheduler', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify(schedulerConfig)
      });
      alert('Configuración del scheduler guardada. Los cambios aplicarán en un máximo de 30 segundos.');
    } catch(err) {
      console.error(err);
    }
  };

  const toggleBlock = async (userId: number, currentBlocked: number) => {
    try {
      await fetch(`/api/admin/users/${userId}/block`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ blocked: currentBlocked ? 0 : 1 })
      });
      fetchUsers();
    } catch (err) {
      console.error(err);
    }
  };

  const deleteUser = async (userId: number) => {
    if (!window.confirm("¿Seguro que deseas eliminar este usuario?")) return;
    try {
      await fetch(`/api/admin/users/${userId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      fetchUsers();
    } catch (err) {
      console.error(err);
    }
  };

  const handleManualScrape = async (type: string) => {
    setScraping(type);
    let url = '';
    if (type === 'news') url = '/api/scrape/news';
    if (type === 'sea') url = '/api/scrape/sea';
    if (type === 'snifa') url = '/api/scrape/snifa';
    if (type === 'normativas') url = '/api/scrape/normativas';
    if (type === 'tribunales') url = '/api/scrape/tribunales';
    
    if (!url) {
      setScraping(null);
      return;
    }

    try {
      await fetch(url, { 
        method: 'POST',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      alert('Scraping iniciado en segundo plano. Los logs se actualizarán cuando finalice.');
    } catch(err) {
      console.error(err);
    }
    setScraping(null);
  };

  if (user?.role !== 'admin') {
    return <div style={{ padding: '40px', textAlign: 'center' }}>No tienes acceso a esta página.</div>;
  }

  const formatDate = (dateString: string) => {
    if (!dateString) return 'Nunca';
    const date = new Date(dateString);
    return date.toLocaleString('es-ES', { 
      day: '2-digit', month: '2-digit', year: 'numeric', 
      hour: '2-digit', minute: '2-digit'
    });
  };

  return (
    <div className="report-container">
      <div className="report-header-text">
        <h1 className="report-title">Panel de Administrador</h1>
        <p className="report-description">Gestión de usuarios y monitoreo avanzado del sistema.</p>
      </div>

      <div style={{ marginTop: '30px' }}>
        <h2 style={{ fontSize: '20px', marginBottom: '15px', color: 'var(--text-dark)' }}>Usuarios Registrados</h2>
        <div className="table-container" style={{ width: '100%', backgroundColor: 'white', borderRadius: '12px', padding: '0', overflow: 'auto' }}>
          <table className="data-table">
            <thead>
              <tr>
                <th>Nº</th>
                <th>Nombre</th>
                <th>Correo</th>
                <th>Rol</th>
                <th>Estado</th>
                <th>Último Ingreso</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              {users.map((u, index) => (
                <tr key={u.id}>
                  <td>{index + 1}</td>
                  <td>{u.name}</td>
                  <td>{u.email}</td>
                  <td>{u.role === 'admin' ? 'Administrador' : 'Usuario'}</td>
                  <td>
                    {u.blocked ? <span style={{color: '#ef4444', fontWeight: 600}}>Bloqueado</span> : <span style={{color: '#10b981', fontWeight: 600}}>Activo</span>}
                  </td>
                  <td>{formatDate(u.last_login)}</td>
                  <td style={{ display: 'flex', gap: '10px' }}>
                    {u.role !== 'admin' && (
                      <>
                        <button onClick={() => toggleBlock(u.id, u.blocked)} style={{ background: 'none', border: 'none', cursor: 'pointer', color: u.blocked ? '#10b981' : '#f59e0b' }} title={u.blocked ? 'Desbloquear' : 'Bloquear'}>
                          {u.blocked ? <ShieldOff size={18} /> : <ShieldAlert size={18} />}
                        </button>
                        <button onClick={() => deleteUser(u.id)} style={{ background: 'none', border: 'none', cursor: 'pointer', color: '#ef4444' }} title="Eliminar">
                          <Trash2 size={18} />
                        </button>
                      </>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      <div style={{ marginTop: '50px' }}>
        <h2 style={{ fontSize: '20px', color: 'var(--text-dark)', marginBottom: '15px' }}>Configuración del Scheduler</h2>
        <div style={{ background: 'white', padding: '20px', borderRadius: '12px', border: '1px solid var(--border)' }}>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '15px', marginBottom: '20px' }}>
            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>SNIFA Horario 1</label>
              <input type="time" value={schedulerConfig.snifa_time_1} onChange={(e) => setSchedulerConfig({...schedulerConfig, snifa_time_1: e.target.value})} className="filter-select" />
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>SNIFA Horario 2</label>
              <input type="time" value={schedulerConfig.snifa_time_2} onChange={(e) => setSchedulerConfig({...schedulerConfig, snifa_time_2: e.target.value})} className="filter-select" />
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>Pertinencias (Cada X horas)</label>
              <input type="number" min="1" max="24" value={schedulerConfig.pertinencias_interval} onChange={(e) => setSchedulerConfig({...schedulerConfig, pertinencias_interval: e.target.value})} className="filter-select" />
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>Noticias (Cada X horas)</label>
              <input type="number" min="1" max="24" value={schedulerConfig.noticias_interval} onChange={(e) => setSchedulerConfig({...schedulerConfig, noticias_interval: e.target.value})} className="filter-select" />
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>Tribunales (Cada X horas)</label>
              <input type="number" min="1" max="24" value={schedulerConfig.tribunales_interval} onChange={(e) => setSchedulerConfig({...schedulerConfig, tribunales_interval: e.target.value})} className="filter-select" />
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>Hora de Inicio (Diario)</label>
              <input type="time" value={schedulerConfig.hora_inicio} onChange={(e) => setSchedulerConfig({...schedulerConfig, hora_inicio: e.target.value})} className="filter-select" />
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>Hora de Fin (Diario)</label>
              <input type="time" value={schedulerConfig.hora_fin} onChange={(e) => setSchedulerConfig({...schedulerConfig, hora_fin: e.target.value})} className="filter-select" />
            </div>
          </div>
          <button onClick={saveSchedulerConfig} className="btn-primary" style={{ display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 20px', borderRadius: '8px' }}>
            <Save size={18} /> Guardar Configuración
          </button>
        </div>
      </div>

      <div style={{ marginTop: '50px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
        <h2 style={{ fontSize: '20px', color: 'var(--text-dark)' }}>Logs de Scrapers</h2>
        <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <button onClick={() => handleManualScrape('news')} disabled={!!scraping} className="btn-secondary" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Play size={16} /> {scraping === 'news' ? '...' : 'Noticias'}
          </button>
          <button onClick={() => handleManualScrape('sea')} disabled={!!scraping} className="btn-secondary" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Play size={16} /> {scraping === 'sea' ? '...' : 'SEA'}
          </button>
          <button onClick={() => handleManualScrape('snifa')} disabled={!!scraping} className="btn-secondary" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Play size={16} /> {scraping === 'snifa' ? '...' : 'SNIFA'}
          </button>
          <button onClick={() => handleManualScrape('normativas')} disabled={!!scraping} className="btn-secondary" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Play size={16} /> {scraping === 'normativas' ? '...' : 'Normativas'}
          </button>
          <button onClick={() => handleManualScrape('tribunales')} disabled={!!scraping} className="btn-secondary" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
            <Play size={16} /> {scraping === 'tribunales' ? '...' : 'Tribunales'}
          </button>
          <button onClick={() => fetchLogs()} className="btn-primary" style={{ padding: '6px 15px' }}>
            Refrescar Logs
          </button>
        </div>
      </div>
      
      <div className="table-container" style={{ width: '100%', backgroundColor: 'white', borderRadius: '12px', padding: '0', overflow: 'auto', marginTop: '15px' }}>
        <table className="data-table">
          <thead>
            <tr>
              <th>Fuente</th>
              <th>Último Intento</th>
              <th>Último Éxito</th>
              <th>Nuevos Reg.</th>
              <th>Estado / Error</th>
            </tr>
          </thead>
          <tbody>
            {logs.map((log, idx) => (
              <tr key={idx} style={{ background: log.estado === 'ERROR' ? '#fef2f2' : 'transparent' }}>
                <td style={{ fontWeight: 600 }}>{log.fuente}</td>
                <td>{formatDate(log.ultimo_intento)}</td>
                <td>{formatDate(log.ultimo_exito)}</td>
                <td>
                  {log.nuevos_registros > 0 ? (
                    <span style={{ background: 'var(--primary-light)', color: 'var(--primary)', padding: '2px 8px', borderRadius: '12px', fontSize: '12px', fontWeight: 'bold' }}>
                      +{log.nuevos_registros}
                    </span>
                  ) : (
                    <span style={{ color: 'var(--text-light)' }}>0</span>
                  )}
                </td>
                <td>
                  {log.estado === 'OK' ? (
                    <span style={{ color: '#10b981', fontWeight: 600 }}>OK</span>
                  ) : (
                    <span style={{ color: '#ef4444', fontSize: '12px' }}>{log.error}</span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default AdminPanel;
