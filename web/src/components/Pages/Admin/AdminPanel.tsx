import { useState, useEffect } from 'react';
import { useAuth } from '../../../context/AuthContext';
import { ShieldAlert, Trash2, ShieldOff, Play, Save, Bug, RefreshCw, Terminal, Trash } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import styles from './Admin.module.css';

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
      const res = await fetch('/api/admin/users', { headers: { 'Authorization': `Bearer ${token}` } });
      if (res.ok) setUsers(await res.json());
    } catch (err) { console.error(err); }
  };

  const fetchLogs = async () => {
    try {
      const res = await fetch('/api/logs', { headers: { 'Authorization': `Bearer ${token}` } });
      if (res.ok) setLogs(await res.json());
    } catch (err) { console.error(err); }
  };

  const fetchSchedulerConfig = async () => {
    try {
      const res = await fetch('/api/admin/scheduler', { headers: { 'Authorization': `Bearer ${token}` } });
      if (res.ok) setSchedulerConfig(await res.json());
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
    } catch (err) { console.error(err); }
  };

  const toggleBlock = async (userId: number, currentBlocked: number) => {
    try {
      await fetch(`/api/admin/users/${userId}/block`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ blocked: currentBlocked ? 0 : 1 })
      });
      fetchUsers();
    } catch (err) { console.error(err); }
  };

  const deleteUser = async (userId: number) => {
    if (!window.confirm("¿Seguro que deseas eliminar este usuario?")) return;
    try {
      await fetch(`/api/admin/users/${userId}`, { method: 'DELETE', headers: { 'Authorization': `Bearer ${token}` } });
      fetchUsers();
    } catch (err) { console.error(err); }
  };

  const handleManualScrape = async (type: string) => {
    setScraping(type);
    const urlMap: Record<string, string> = {
      news: '/api/scrape/news', sea: '/api/scrape/sea', snifa: '/api/scrape/snifa',
      normativas: '/api/scrape/normativas', tribunales: '/api/scrape/tribunales', consultas: '/api/scrape/consultas'
    };
    const url = urlMap[type];
    if (!url) { setScraping(null); return; }
    try {
      await fetch(url, { method: 'POST', headers: { 'Authorization': `Bearer ${token}` } });
      alert('Scraping iniciado en segundo plano. Los logs se actualizarán cuando finalice.');
    } catch (err) { console.error(err); }
    setScraping(null);
  };

  const handleSeaManualScrape = async () => {
    if (!seaStartDate || !seaEndDate) { alert("Por favor selecciona una fecha de inicio y una fecha de fin."); return; }
    setScraping('sea-manual');
    try {
      const res = await fetch('/api/scrape/sea/manual', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ start_date: seaStartDate, end_date: seaEndDate })
      });
      const data = await res.json();
      if (res.ok) alert(data.message); else alert('Error: ' + data.detail);
    } catch (err) { console.error(err); alert('Error de conexión'); }
    setScraping(null);
  };

  const handleNormativasManualScrape = async () => {
    if (!normativasStartDate || !normativasEndDate) { alert("Por favor selecciona una fecha de inicio y una fecha de fin."); return; }
    setScraping('normativas-manual');
    try {
      const res = await fetch('/api/scrape/normativas/manual', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: JSON.stringify({ start_date: normativasStartDate, end_date: normativasEndDate })
      });
      const data = await res.json();
      if (res.ok) alert(data.message); else alert('Error: ' + data.detail);
    } catch (err) { console.error(err); alert('Error de conexión'); }
    setScraping(null);
  };

  const handleDeleteLatest = async (category: string, label: string) => {
    if (!window.confirm(`¿Seguro que deseas borrar el registro más reciente de ${label}?`)) return;
    try {
      const res = await fetch(`/api/admin/debug/delete-latest/${category}`, {
        method: 'DELETE', headers: { 'Authorization': `Bearer ${token}` }
      });
      const data = await res.json();
      if (res.ok) {
        const msg = `[${new Date().toLocaleTimeString()}] Borrado registro en ${data.table}. Registros afectados: ${data.deleted}`;
        setDebugLogs(prev => [msg, ...prev]);
      } else {
        alert('Error: ' + data.detail);
      }
    } catch (err) { console.error(err); }
  };

  if (user?.role !== 'admin') {
    return <div className={styles.noAccess}>No tienes acceso a esta página.</div>;
  }

  const formatDate = (dateString: string) => {
    if (!dateString) return 'Nunca';
    return new Date(dateString).toLocaleString('es-ES', {
      day: '2-digit', month: '2-digit', year: 'numeric',
      hour: '2-digit', minute: '2-digit'
    });
  };

  return (
    <div className={styles.pageContainer}>
      <div>
        <h1 className={styles.pageTitle}>Panel de Administrador</h1>
        <p className={styles.pageDescription}>Gestión de usuarios, configuración del sistema y herramientas de depuración.</p>
      </div>

      <div className={styles.tabsRow}>
        <button className={`${styles.tab} ${activeTab === 'general' ? styles.tabActive : styles.tabInactive}`} onClick={() => setActiveTab('general')}>
          <ShieldAlert size={18} /> General
        </button>
        <button className={`${styles.tab} ${activeTab === 'debug' ? styles.tabActive : styles.tabInactive}`} onClick={() => setActiveTab('debug')}>
          <Bug size={18} /> Depuración
        </button>
      </div>

      {activeTab === 'general' ? (
        <>
          {/* Cards */}
          <div className={styles.cardsGrid}>
            <div className={styles.panelCard}>
              <h2 className={styles.panelCardTitle}>Reportes de Bugs</h2>
              <p className={styles.panelCardDesc}>Gestiona los problemas técnicos informados por los usuarios.</p>
              <button onClick={() => navigate('/admin/reportes')} className={styles.panelCardBtn}>
                Gestionar Reportes
              </button>
            </div>
          </div>

          {/* Usuarios */}
          <div style={{ marginTop: '30px' }}>
            <h2 className={styles.sectionTitle}>Usuarios Registrados</h2>
            <div className="table-container" style={{ width: '100%', backgroundColor: 'white', borderRadius: '12px', padding: '0', overflow: 'auto' }}>
              <table className="data-table">
                <thead>
                  <tr>
                    <th>Nº</th><th>Nombre</th><th>Correo</th><th>Rol</th>
                    <th>Estado</th><th>Último Ingreso</th><th>Acciones</th>
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
                        {u.blocked
                          ? <span className={styles.statusBlocked}>Bloqueado</span>
                          : <span className={styles.statusActive}>Activo</span>}
                      </td>
                      <td>{formatDate(u.last_login)}</td>
                      <td className={styles.tdActions}>
                        {u.role !== 'admin' && (
                          <>
                            <button onClick={() => toggleBlock(u.id, u.blocked)} className={`${styles.iconBtn} ${u.blocked ? styles.iconBtnSuccess : styles.iconBtnWarn}`} title={u.blocked ? 'Desbloquear' : 'Bloquear'}>
                              {u.blocked ? <ShieldOff size={18} /> : <ShieldAlert size={18} />}
                            </button>
                            <button onClick={() => deleteUser(u.id)} className={`${styles.iconBtn} ${styles.iconBtnDanger}`} title="Eliminar">
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

          {/* Scheduler */}
          <div style={{ marginTop: '50px' }}>
            <h2 className={styles.sectionTitle}>Configuración del Scheduler</h2>
            <div className={styles.schedulerCard}>
              <div className={styles.schedulerGrid}>
                {[
                  { label: 'SNIFA Horario 1', key: 'snifa_time_1', type: 'time' },
                  { label: 'SNIFA Horario 2', key: 'snifa_time_2', type: 'time' },
                  { label: 'SEA (Cada X horas)', key: 'pertinencias_interval', type: 'number' },
                  { label: 'Noticias (Cada X horas)', key: 'noticias_interval', type: 'number' },
                  { label: 'Tribunales (Cada X horas)', key: 'tribunales_interval', type: 'number' },
                  { label: 'Hora de Inicio (Diario)', key: 'hora_inicio', type: 'time' },
                  { label: 'Hora de Fin (Diario)', key: 'hora_fin', type: 'time' },
                  { label: 'Consultas Horario 1', key: 'consultas_time_1', type: 'time' },
                  { label: 'Consultas Horario 2', key: 'consultas_time_2', type: 'time' },
                  { label: 'Hora de Testeo', key: 'test_time', type: 'time' },
                ].map(({ label, key, type }) => (
                  <div key={key} className={styles.schedulerField}>
                    <label>{label}</label>
                    <input
                      type={type}
                      value={schedulerConfig[key] || ''}
                      onChange={(e) => setSchedulerConfig({ ...schedulerConfig, [key]: e.target.value })}
                      className="filter-select"
                      {...(type === 'number' ? { min: 1, max: 24 } : {})}
                    />
                  </div>
                ))}
              </div>
              <button onClick={saveSchedulerConfig} className={styles.btnPrimary} style={{ padding: '10px 20px', borderRadius: '8px' }}>
                <Save size={18} /> Guardar Configuración
              </button>
            </div>
          </div>

          {/* Scrapers */}
          <div className={styles.sectionHeader}>
            <h2 className={styles.sectionTitle}>Logs de Scrapers</h2>
            <div className={styles.scraperButtons}>
              {['news', 'sea', 'snifa', 'normativas', 'tribunales', 'consultas'].map(type => (
                <button key={type} onClick={() => handleManualScrape(type)} disabled={!!scraping} className={styles.btnSecondary}>
                  <Play size={16} /> {scraping === type ? '...' : type.charAt(0).toUpperCase() + type.slice(1)}
                </button>
              ))}
              <button onClick={() => fetchLogs()} className={styles.btnPrimary}>
                <RefreshCw size={16} /> Refrescar Logs
              </button>
            </div>
          </div>

          {/* SEA range */}
          <div className={styles.scraperRangeForm}>
            <div className={styles.scraperRangeField}>
              <label>SEA: Fecha Inicio</label>
              <input type="date" value={seaStartDate} onChange={(e) => setSeaStartDate(e.target.value)} className="filter-select" />
            </div>
            <div className={styles.scraperRangeField}>
              <label>SEA: Fecha Fin</label>
              <input type="date" value={seaEndDate} onChange={(e) => setSeaEndDate(e.target.value)} className="filter-select" />
            </div>
            <button onClick={handleSeaManualScrape} disabled={!!scraping} className={styles.scraperRangeBtn}>
              <Play size={16} /> {scraping === 'sea-manual' ? 'Iniciando...' : 'Scrapeo SEA por Rango'}
            </button>
          </div>

          {/* Normativas range */}
          <div className={styles.scraperRangeForm}>
            <div className={styles.scraperRangeField}>
              <label>Normativas: Fecha Inicio</label>
              <input type="date" value={normativasStartDate} onChange={(e) => setNormativasStartDate(e.target.value)} className="filter-select" />
            </div>
            <div className={styles.scraperRangeField}>
              <label>Normativas: Fecha Fin</label>
              <input type="date" value={normativasEndDate} onChange={(e) => setNormativasEndDate(e.target.value)} className="filter-select" />
            </div>
            <button onClick={handleNormativasManualScrape} disabled={!!scraping} className={styles.scraperRangeBtn}>
              <Play size={16} /> {scraping === 'normativas-manual' ? 'Iniciando...' : 'Scrapeo Normativas por Rango'}
            </button>
          </div>

          {/* Logs table */}
          <div className="table-container" style={{ width: '100%', backgroundColor: 'white', borderRadius: '12px', padding: '0', overflow: 'auto', marginTop: '15px' }}>
            <table className="data-table">
              <thead>
                <tr>
                  <th>Fuente</th><th>Último Intento</th><th>Último Éxito</th>
                  <th>Nuevos Reg.</th><th>Estado / Error</th>
                </tr>
              </thead>
              <tbody>
                {logs.map((log, idx) => (
                  <tr key={idx} className={log.estado === 'ERROR' ? styles.trError : ''}>
                    <td className={styles.tdFontBold}>{log.fuente}</td>
                    <td>{formatDate(log.ultimo_intento)}</td>
                    <td>{formatDate(log.ultimo_exito)}</td>
                    <td>
                      {log.nuevos_registros > 0
                        ? <span className={styles.badgeNew}>+{log.nuevos_registros}</span>
                        : <span className={styles.statusBlocked} style={{ color: 'var(--text-light)', fontWeight: 400 }}>0</span>}
                    </td>
                    <td>
                      {log.estado === 'OK'
                        ? <span className={styles.statusOk}>OK</span>
                        : <span className={styles.statusError}>{log.error}</span>}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </>
      ) : (
        <div className={styles.debugLayout}>
          <div className={styles.debugSections}>
            {[
              { title: 'Consultas Públicas', items: [{ label: 'MMA Abiertas', cat: 'mma_abiertas' }, { label: 'MMA Cerradas', cat: 'mma_cerradas' }, { label: 'MINSAL Vigentes', cat: 'minsal_vigentes' }] },
              { title: 'SEA', items: [{ label: 'Proyectos Evaluados', cat: 'sea_evaluados' }, { label: 'Pertinencias', cat: 'pertinencias' }] },
              { title: 'SMA (Basado en Ficha)', items: [{ label: 'Fiscalizaciones', cat: 'fiscalizaciones' }, { label: 'Sancionatorios', cat: 'sancionatorios' }, { label: 'Sanciones', cat: 'sanciones' }, { label: 'Programas', cat: 'programas' }, { label: 'Medidas', cat: 'medidas' }, { label: 'Requerimientos', cat: 'requerimientos' }] },
              { title: 'Tribunales Ambientales', items: [{ label: '1° Tribunal', cat: 'tribunal_1' }, { label: '2° Tribunal', cat: 'tribunal_2' }, { label: '3° Tribunal', cat: 'tribunal_3' }] },
            ].map(section => (
              <div key={section.title} className={styles.debugSection}>
                <div className={styles.debugSectionHeader}>
                  <RefreshCw size={18} />
                  <h3 className={styles.debugSectionTitle}>{section.title}</h3>
                </div>
                <div className={styles.debugButtonsRow}>
                  {section.items.map(item => (
                    <button key={item.cat} onClick={() => handleDeleteLatest(item.cat, item.label)} className={styles.debugButton}>
                      <Trash size={14} /> {item.label}
                    </button>
                  ))}
                </div>
              </div>
            ))}
          </div>

          <div className={styles.debugConsole}>
            <div className={styles.debugConsoleHeader}>
              <Terminal size={16} />
              <span className={styles.debugConsoleTitle}>Logs de Depuración</span>
            </div>
            <div className={styles.debugConsoleLogs}>
              {debugLogs.length === 0
                ? <div className={styles.debugConsoleEmpty}>Esperando acciones...</div>
                : debugLogs.map((log, i) => (
                  <div key={i} className={styles.debugLogEntry}>{log}</div>
                ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default AdminPanel;
