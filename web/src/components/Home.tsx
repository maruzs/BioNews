import { useState, useEffect, useRef } from 'react';
import { Activity, AlertTriangle, CheckCircle2, Search, ExternalLink, X } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';

interface ScraperLog {
  fuente: string;
  ultimo_intento: string;
  ultimo_exito: string;
  estado: string;
  error: string;
  nuevos_registros: number;
}

interface SearchResult {
  id: string;
  titulo: string;
  accion: string;
  extra: string;
}

const TABLE_LABELS: Record<string, string> = {
  fiscalizaciones: 'Fiscalizaciones',
  sancionatorios: 'Sancionatorios',
  registroSanciones: 'Registro Sanciones',
  programasDeCumplimiento: 'Programas de Cumplimiento',
  medidas_provisionales: 'Medidas Provisionales',
  requerimientos: 'Requerimientos',
  normativas: 'Normativas',
  noticias: 'Noticias',
  Tribunales: 'Tribunales Ambientales',
  pertinencias: 'Pertinencias SEA',
};

const Home = () => {
  const { token } = useAuth();
  const { setCategoryActive } = useNotifications();
  const [logs, setLogs] = useState<ScraperLog[]>([]);

  // Search state
  const [searchQuery, setSearchQuery] = useState('');
  const [debouncedQuery, setDebouncedQuery] = useState('');
  const [searchResults, setSearchResults] = useState<Record<string, SearchResult[]>>({});
  const [searchTotal, setSearchTotal] = useState(0);
  const [searching, setSearching] = useState(false);
  const [searchOpen, setSearchOpen] = useState(false);
  const searchRef = useRef<HTMLDivElement>(null);
  const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    setCategoryActive(null);
  }, [setCategoryActive]);

  const fetchLogs = () => {
    if (!token) return;
    fetch('/api/logs', {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(res => res.json())
      .then(data => setLogs(data))
      .catch(err => console.error("Error fetching logs:", err));
  };

  useEffect(() => {
    fetchLogs();
  }, []);

  // Debounce search
  useEffect(() => {
    if (debounceRef.current) clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(() => {
      setDebouncedQuery(searchQuery);
    }, 400);
    return () => { if (debounceRef.current) clearTimeout(debounceRef.current); };
  }, [searchQuery]);

  // Execute search when debouncedQuery changes
  useEffect(() => {
    if (!debouncedQuery || debouncedQuery.trim().length < 2) {
      setSearchResults({});
      setSearchTotal(0);
      setSearchOpen(false);
      return;
    }
    setSearching(true);
    setSearchOpen(true);
    fetch(`/api/search?q=${encodeURIComponent(debouncedQuery)}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(res => res.json())
      .then(data => {
        setSearchResults(data.results || {});
        setSearchTotal(data.total || 0);
        setSearching(false);
      })
      .catch(() => setSearching(false));
  }, [debouncedQuery, token]);

  // Close dropdown on outside click
  useEffect(() => {
    const handleClick = (e: MouseEvent) => {
      if (searchRef.current && !searchRef.current.contains(e.target as Node)) {
        setSearchOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClick);
    return () => document.removeEventListener('mousedown', handleClick);
  }, []);

  const clearSearch = () => {
    setSearchQuery('');
    setDebouncedQuery('');
    setSearchResults({});
    setSearchTotal(0);
    setSearchOpen(false);
  };

  const tableEntries = Object.entries(searchResults);

  return (
    <div className="report-container">
      <div className="report-header-text">
        <h1 className="report-title">Dashboard del Sistema</h1>
        <p className="report-description">Estado actual de la recolección de datos y actualización de fuentes.</p>
      </div>

      {/* Búsqueda Global */}
      <div ref={searchRef} style={{ position: 'relative', marginBottom: '30px' }}>
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: '12px',
          background: 'white',
          border: '2px solid var(--border)',
          borderRadius: '14px',
          padding: '14px 20px',
          boxShadow: '0 2px 8px rgba(0,0,0,0.06)',
          transition: 'border-color 0.2s',
          ...(searchOpen && searchQuery ? { borderColor: 'var(--primary)' } : {})
        }}>
          <Search size={20} color="var(--primary)" style={{ flexShrink: 0 }} />
          <input
            type="text"
            placeholder="Buscar en todas las fuentes: expediente, empresa, normativa, causa..."
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
            onFocus={() => { if (debouncedQuery.length >= 2) setSearchOpen(true); }}
            style={{
              border: 'none',
              outline: 'none',
              width: '100%',
              fontSize: '15px',
              color: 'var(--text-dark)',
              background: 'transparent'
            }}
          />
          {searchQuery && (
            <button onClick={clearSearch} style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-light)', display: 'flex', padding: '2px' }}>
              <X size={18} />
            </button>
          )}
          {searching && (
            <span style={{ fontSize: '12px', color: 'var(--text-light)', flexShrink: 0 }}>Buscando...</span>
          )}
        </div>

        {/* Resultados dropdown */}
        {searchOpen && debouncedQuery.length >= 2 && !searching && (
          <div style={{
            position: 'absolute',
            top: 'calc(100% + 8px)',
            left: 0,
            right: 0,
            background: 'white',
            border: '1px solid var(--border)',
            borderRadius: '14px',
            boxShadow: '0 8px 30px rgba(0,0,0,0.12)',
            zIndex: 1000,
            maxHeight: '60vh',
            overflowY: 'auto'
          }}>
            {tableEntries.length === 0 ? (
              <div style={{ padding: '20px', textAlign: 'center', color: 'var(--text-light)', fontSize: '14px' }}>
                No se encontraron resultados para "<strong>{debouncedQuery}</strong>"
              </div>
            ) : (
              <>
                <div style={{ padding: '12px 18px', borderBottom: '1px solid var(--border)', fontSize: '13px', color: 'var(--text-light)', fontWeight: 600 }}>
                  {searchTotal} resultado{searchTotal !== 1 ? 's' : ''} en {tableEntries.length} fuente{tableEntries.length !== 1 ? 's' : ''}
                </div>
                {tableEntries.map(([table, items]) => (
                  <div key={table}>
                    <div style={{
                      padding: '8px 18px',
                      fontSize: '11px',
                      fontWeight: 700,
                      textTransform: 'uppercase',
                      letterSpacing: '0.08em',
                      color: 'var(--primary)',
                      background: '#f0fdf4',
                      borderBottom: '1px solid var(--border)'
                    }}>
                      {TABLE_LABELS[table] || table} ({items.length})
                    </div>
                    {items.slice(0, 10).map((item, i) => (
                      <a
                        key={`${table}-${i}`}
                        href={item.accion || '#'}
                        target={item.accion?.startsWith('http') ? '_blank' : '_self'}
                        rel="noreferrer"
                        style={{
                          display: 'flex',
                          alignItems: 'flex-start',
                          gap: '10px',
                          padding: '10px 18px',
                          textDecoration: 'none',
                          borderBottom: '1px solid #f5f5f5',
                          transition: 'background 0.15s'
                        }}
                        onMouseEnter={e => (e.currentTarget.style.background = '#f9fafb')}
                        onMouseLeave={e => (e.currentTarget.style.background = 'transparent')}
                        onClick={() => setSearchOpen(false)}
                      >
                        <div style={{ flex: 1, minWidth: 0 }}>
                          <div style={{ fontSize: '13px', fontWeight: 600, color: 'var(--text-dark)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                            {item.titulo || item.id}
                          </div>
                          {item.extra && (
                            <div style={{ fontSize: '11px', color: 'var(--text-light)', marginTop: '2px' }}>
                              {item.extra}
                            </div>
                          )}
                        </div>
                        {item.accion?.startsWith('http') && (
                          <ExternalLink size={13} color="var(--primary)" style={{ flexShrink: 0, marginTop: '2px' }} />
                        )}
                      </a>
                    ))}
                    {items.length > 10 && (
                      <div style={{ padding: '8px 18px', fontSize: '12px', color: 'var(--text-light)', borderBottom: '1px solid var(--border)' }}>
                        ... y {items.length - 10} resultado{items.length - 10 !== 1 ? 's' : ''} más en esta fuente
                      </div>
                    )}
                  </div>
                ))}
              </>
            )}
          </div>
        )}
      </div>

      {/* Stats cards */}
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

      {/* Logs table */}
      {logs.length > 0 && (
        <div style={{ background: 'white', border: '1px solid var(--border)', borderRadius: '12px', overflow: 'hidden' }}>
          <div style={{ padding: '16px 20px', borderBottom: '1px solid var(--border)', fontWeight: 700, color: 'var(--text-dark)', fontSize: '15px' }}>
            Últimas ejecuciones de scrapers
          </div>
          <div style={{ overflowX: 'auto' }}>
            <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px' }}>
              <thead>
                <tr style={{ background: '#f8f9fa' }}>
                  <th style={{ padding: '10px 16px', textAlign: 'left', color: 'var(--text-light)', fontWeight: 600 }}>Fuente</th>
                  <th style={{ padding: '10px 16px', textAlign: 'left', color: 'var(--text-light)', fontWeight: 600 }}>Último Intento</th>
                  <th style={{ padding: '10px 16px', textAlign: 'left', color: 'var(--text-light)', fontWeight: 600 }}>Estado</th>
                  <th style={{ padding: '10px 16px', textAlign: 'left', color: 'var(--text-light)', fontWeight: 600 }}>Nuevos</th>
                </tr>
              </thead>
              <tbody>
                {logs.map((log, i) => (
                  <tr key={i} style={{ borderTop: '1px solid var(--border)' }}>
                    <td style={{ padding: '10px 16px', color: 'var(--text-dark)', fontWeight: 500 }}>{log.fuente}</td>
                    <td style={{ padding: '10px 16px', color: 'var(--text-light)' }}>{log.ultimo_intento}</td>
                    <td style={{ padding: '10px 16px' }}>
                      <span style={{
                        display: 'inline-flex', alignItems: 'center', gap: '5px',
                        background: log.estado === 'OK' ? '#ecfdf5' : '#fef2f2',
                        color: log.estado === 'OK' ? '#10b981' : '#ef4444',
                        padding: '2px 10px', borderRadius: '20px', fontSize: '12px', fontWeight: 600
                      }}>
                        {log.estado === 'OK' ? <CheckCircle2 size={12} /> : <AlertTriangle size={12} />}
                        {log.estado}
                      </span>
                    </td>
                    <td style={{ padding: '10px 16px', color: log.nuevos_registros > 0 ? 'var(--primary)' : 'var(--text-light)', fontWeight: log.nuevos_registros > 0 ? 700 : 400 }}>
                      {log.nuevos_registros > 0 ? `+${log.nuevos_registros}` : '—'}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  );
};

export default Home;
