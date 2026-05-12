import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';
import { ShieldAlert, Trash2, ShieldOff, Play, Save, Bug, Trash, RefreshCw, Terminal } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

const AdminPanel = () => {
  const navigate = useNavigate();
  const { token, user } = useAuth();
  const [activeTab, setActiveTab] = useState<'general' | 'debug'>('general');
  const [users, setUsers] = useState<any[]>([]);
  const [logs, setLogs] = useState<any[]>([]);
  const [scraping, setScraping] = useState<string | null>(null);
  const [debugLogs, setDebugLogs] = useState<string[]>([]);
  const [seaStartDate, setSeaStartDate] = useState<string>('');
  const [seaEndDate, setSeaEndDate] = useState<string>('');
  const [normativasStartDate, setNormativasStartDate] = useState<string>('');
  const [normativasEndDate, setNormativasEndDate] = useState<string>('');
  const [schedulerConfig, setSchedulerConfig] = useState<any>({
    snifa_time_1: "07:00",
    snifa_time_2: "14:00",
    pertinencias_interval: 1,
    noticias_interval: 1,
    tribunales_interval: 1,
    consultas_time_1: "08:30",
    consultas_time_2: "15:30",
    hora_inicio: "07:00",
    hora_fin: "19:00",
    notification_interval: 15,
    test_time: ""
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
    if (type === 'consultas') url = '/api/scrape/consultas';
    
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

  const handleSeaManualScrape = async () => {
    if (!seaStartDate || !seaEndDate) {
      alert("Por favor selecciona una fecha de inicio y una fecha de fin.");
      return;
    }
    setScraping('sea-manual');
    try {
      const res = await fetch('/api/scrape/sea/manual', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ start_date: seaStartDate, end_date: seaEndDate })
      });
      const data = await res.json();
      if (res.ok) {
        alert(data.message);
      } else {
        alert('Error: ' + data.detail);
      }
    } catch (err) {
      console.error(err);
      alert('Error de conexión');
    }
    setScraping(null);
  };

  const handleNormativasManualScrape = async () => {
    if (!normativasStartDate || !normativasEndDate) {
      alert("Por favor selecciona una fecha de inicio y una fecha de fin.");
      return;
    }
    setScraping('normativas-manual');
    try {
      const res = await fetch('/api/scrape/normativas/manual', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ start_date: normativasStartDate, end_date: normativasEndDate })
      });
      const data = await res.json();
      if (res.ok) {
        alert(data.message);
      } else {
        alert('Error: ' + data.detail);
      }
    } catch (err) {
      console.error(err);
      alert('Error de conexión');
    }
    setScraping(null);
  };

  const handleDeleteLatest = async (category: string, label: string) => {
    if (!window.confirm(`¿Seguro que deseas borrar el registro más reciente de ${label}?`)) return;
    try {
      const res = await fetch(`/api/admin/debug/delete-latest/${category}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await res.json();
      if (res.ok) {
        const msg = `[${new Date().toLocaleTimeString()}] Borrado registro en ${data.table}. Registros afectados: ${data.deleted}`;
        setDebugLogs(prev => [msg, ...prev]);
      } else {
        alert('Error: ' + data.detail);
      }
    } catch (err) {
      console.error(err);
    }
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
        <p className="report-description">Gestión de usuarios, configuración del sistema y herramientas de depuración.</p>
      </div>

      <div className="report-tabs" style={{ marginTop: '20px' }}>
        <div className={`tab ${activeTab === 'general' ? 'active' : 'inactive'}`} onClick={() => setActiveTab('general')}>
          <ShieldAlert size={18} /> General
        </div>
        <div className={`tab ${activeTab === 'debug' ? 'active' : 'inactive'}`} onClick={() => setActiveTab('debug')}>
          <Bug size={18} /> Depuración
        </div>
      </div>

      {activeTab === 'general' ? (
        <>
          <div style={{ marginTop: '30px', display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '20px' }}>
            <div style={{ background: 'white', padding: '25px', borderRadius: '12px', border: '1px solid var(--border)', display: 'flex', flexDirection: 'column', gap: '15px' }}>
              <h2 style={{ fontSize: '18px', fontWeight: 700, margin: 0, color: 'var(--text-dark)' }}>Reportes de Bugs</h2>
              <p style={{ fontSize: '14px', color: 'var(--text-light)', margin: 0 }}>Gestiona los problemas técnicos informados por los usuarios.</p>
              <button 
                onClick={() => navigate('/admin/reportes')} 
                className="btn-primary" 
                style={{ marginTop: 'auto', alignSelf: 'flex-start', padding: '10px 20px' }}
              >
                Gestionar Reportes
              </button>
            </div>
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
                  <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>SEA (Cada X horas)</label>
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
                <div>
                  <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>Consultas Horario 1</label>
                  <input type="time" value={schedulerConfig.consultas_time_1} onChange={(e) => setSchedulerConfig({...schedulerConfig, consultas_time_1: e.target.value})} className="filter-select" />
                </div>
                <div>
                  <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>Consultas Horario 2</label>
                  <input type="time" value={schedulerConfig.consultas_time_2} onChange={(e) => setSchedulerConfig({...schedulerConfig, consultas_time_2: e.target.value})} className="filter-select" />
                </div>
                <div style={{ flex: '1 1 200px' }}>
                  <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>Hora de Testeo</label>
                  <input 
                    type="time" 
                    value={schedulerConfig.test_time || ''} 
                    onChange={(e) => setSchedulerConfig({...schedulerConfig, test_time: e.target.value})} 
                    className="filter-select"
                  />
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
              <button onClick={() => handleManualScrape('consultas')} disabled={!!scraping} className="btn-secondary" style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
                <Play size={16} /> {scraping === 'consultas' ? '...' : 'Consultas'}
              </button>
              <button onClick={() => fetchLogs()} className="btn-primary" style={{ padding: '6px 15px' }}>
                <RefreshCw size={16} /> Refrescar Logs
              </button>
            </div>
          </div>
          
          <div style={{ marginTop: '20px', background: '#f8fafc', padding: '15px', borderRadius: '12px', border: '1px solid #e2e8f0', display: 'flex', alignItems: 'flex-end', gap: '15px', flexWrap: 'wrap' }}>
            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>SEA: Fecha Inicio</label>
              <input type="date" value={seaStartDate} onChange={(e) => setSeaStartDate(e.target.value)} className="filter-select" />
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>SEA: Fecha Fin</label>
              <input type="date" value={seaEndDate} onChange={(e) => setSeaEndDate(e.target.value)} className="filter-select" />
            </div>
            <button onClick={handleSeaManualScrape} disabled={!!scraping} className="btn-primary" style={{ display: 'flex', alignItems: 'center', gap: '6px', height: '42px' }}>
              <Play size={16} /> {scraping === 'sea-manual' ? 'Iniciando...' : 'Scrapeo SEA por Rango'}
            </button>
          </div>
          
          <div style={{ marginTop: '20px', background: '#f8fafc', padding: '15px', borderRadius: '12px', border: '1px solid #e2e8f0', display: 'flex', alignItems: 'flex-end', gap: '15px', flexWrap: 'wrap' }}>
            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>Normativas: Fecha Inicio</label>
              <input type="date" value={normativasStartDate} onChange={(e) => setNormativasStartDate(e.target.value)} className="filter-select" />
            </div>
            <div>
              <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, marginBottom: '5px' }}>Normativas: Fecha Fin</label>
              <input type="date" value={normativasEndDate} onChange={(e) => setNormativasEndDate(e.target.value)} className="filter-select" />
            </div>
            <button onClick={handleNormativasManualScrape} disabled={!!scraping} className="btn-primary" style={{ display: 'flex', alignItems: 'center', gap: '6px', height: '42px' }}>
              <Play size={16} /> {scraping === 'normativas-manual' ? 'Iniciando...' : 'Scrapeo Normativas por Rango'}
            </button>
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
        </>
      ) : (
        <div style={{ marginTop: '30px' }}>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 350px', gap: '20px' }}>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '25px' }}>
              
              {/* Consultas Públicas */}
              <DebugSection title="Consultas Públicas" icon={<RefreshCw size={18} />}>
                <DebugButton label="MMA Abiertas" onClick={() => handleDeleteLatest('mma_abiertas', 'MMA Abiertas')} />
                <DebugButton label="MMA Cerradas" onClick={() => handleDeleteLatest('mma_cerradas', 'MMA Cerradas')} />
                <DebugButton label="MINSAL Vigentes" onClick={() => handleDeleteLatest('minsal_vigentes', 'MINSAL Vigentes')} />
              </DebugSection>

              {/* SEA */}
              <DebugSection title="SEA" icon={<RefreshCw size={18} />}>
                <DebugButton label="Proyectos Evaluados" onClick={() => handleDeleteLatest('sea_evaluados', 'SEA Evaluados')} />
                <DebugButton label="Pertinencias" onClick={() => handleDeleteLatest('pertinencias', 'Pertinencias')} />
              </DebugSection>

              {/* SMA */}
              <DebugSection title="SMA (Basado en Ficha)" icon={<RefreshCw size={18} />}>
                <DebugButton label="Fiscalizaciones" onClick={() => handleDeleteLatest('fiscalizaciones', 'Fiscalizaciones')} />
                <DebugButton label="Sancionatorios" onClick={() => handleDeleteLatest('sancionatorios', 'Sancionatorios')} />
                <DebugButton label="Sanciones" onClick={() => handleDeleteLatest('sanciones', 'Sanciones')} />
                <DebugButton label="Programas" onClick={() => handleDeleteLatest('programas', 'Programas')} />
                <DebugButton label="Medidas" onClick={() => handleDeleteLatest('medidas', 'Medidas')} />
                <DebugButton label="Requerimientos" onClick={() => handleDeleteLatest('requerimientos', 'Requerimientos')} />
              </DebugSection>

              {/* Tribunales */}
              <DebugSection title="Tribunales Ambientales" icon={<RefreshCw size={18} />}>
                <DebugButton label="1° Tribunal" onClick={() => handleDeleteLatest('tribunal_1', '1° Tribunal')} />
                <DebugButton label="2° Tribunal" onClick={() => handleDeleteLatest('tribunal_2', '2° Tribunal')} />
                <DebugButton label="3° Tribunal" onClick={() => handleDeleteLatest('tribunal_3', '3° Tribunal')} />
              </DebugSection>

            </div>

            {/* Console / Logs */}
            <div style={{ background: '#0f172a', borderRadius: '12px', padding: '20px', color: '#38bdf8', fontFamily: 'monospace', fontSize: '13px', display: 'flex', flexDirection: 'column', height: 'fit-content', position: 'sticky', top: '20px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '15px', borderBottom: '1px solid #1e293b', paddingBottom: '10px', color: '#94a3b8' }}>
                <Terminal size={16} />
                <span style={{ fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.05em' }}>Logs de Depuración</span>
              </div>
              <div style={{ maxHeight: '500px', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                {debugLogs.length === 0 ? (
                  <div style={{ color: '#475569', fontStyle: 'italic' }}>Esperando acciones...</div>
                ) : (
                  debugLogs.map((log, i) => (
                    <div key={i} style={{ borderLeft: '2px solid #0ea5e9', paddingLeft: '10px' }}>{log}</div>
                  ))
                )}
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

const DebugSection = ({ title, icon, children }: { title: string, icon: any, children: any }) => (
  <div style={{ background: 'white', padding: '20px', borderRadius: '12px', border: '1px solid var(--border)' }}>
    <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '15px', color: 'var(--text-dark)' }}>
      {icon}
      <h3 style={{ fontSize: '16px', fontWeight: 700, margin: 0 }}>{title}</h3>
    </div>
    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '10px' }}>
      {children}
    </div>
  </div>
);

const DebugButton = ({ label, onClick }: { label: string, onClick: () => void }) => (
  <button 
    onClick={onClick}
    style={{ 
      padding: '8px 15px', borderRadius: '8px', border: '1px solid #e2e8f0', 
      backgroundColor: '#f8fafc', color: '#475569', fontSize: '13px', fontWeight: 600,
      cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '6px',
      transition: 'all 0.2s'
    }}
    onMouseOver={e => { e.currentTarget.style.backgroundColor = '#fee2e2'; e.currentTarget.style.color = '#ef4444'; e.currentTarget.style.borderColor = '#fecaca'; }}
    onMouseOut={e => { e.currentTarget.style.backgroundColor = '#f8fafc'; e.currentTarget.style.color = '#475569'; e.currentTarget.style.borderColor = '#e2e8f0'; }}
  >
    <Trash size={14} /> {label}
  </button>
);

export default AdminPanel;
