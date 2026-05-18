import { useState, useEffect, useRef } from 'react';
import { Activity, AlertTriangle, CheckCircle2, Search, ExternalLink, X } from 'lucide-react';
import { useAuth } from '../../../context/AuthContext';
import styles from './Home.module.css';

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
  const [logs, setLogs] = useState<ScraperLog[]>([]);

  const [searchQuery, setSearchQuery] = useState('');
  const [debouncedQuery, setDebouncedQuery] = useState('');
  const [searchResults, setSearchResults] = useState<Record<string, SearchResult[]>>({});
  const [searchTotal, setSearchTotal] = useState(0);
  const [searching, setSearching] = useState(false);
  const [searchOpen, setSearchOpen] = useState(false);
  const searchRef = useRef<HTMLDivElement>(null);
  const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null);

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

  useEffect(() => {
    if (debounceRef.current) clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(() => {
      setDebouncedQuery(searchQuery);
    }, 400);
    return () => { if (debounceRef.current) clearTimeout(debounceRef.current); };
  }, [searchQuery]);

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
    <div className={styles.pageContainer}>
      <div>
        <h1 className={styles.pageTitle}>Dashboard del Sistema</h1>
        <p className={styles.pageDescription}>Estado actual de la recolección de datos y actualización de fuentes.</p>
      </div>

      {/* Búsqueda Global */}
      <div ref={searchRef} className={styles.searchWrapper}>
        <div className={`${styles.searchBox} ${searchOpen && searchQuery ? styles.focused : ''}`}>
          <Search size={20} color="var(--primary)" style={{ flexShrink: 0 }} />
          <input
            type="text"
            placeholder="Buscar en todas las fuentes: expediente, empresa, normativa, causa..."
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
            onFocus={() => { if (debouncedQuery.length >= 2) setSearchOpen(true); }}
            className={styles.searchInput}
          />
          {searchQuery && (
            <button onClick={clearSearch} className={styles.clearButton}>
              <X size={18} />
            </button>
          )}
          {searching && (
            <span className={styles.searchingLabel}>Buscando...</span>
          )}
        </div>

        {/* Resultados dropdown */}
        {searchOpen && debouncedQuery.length >= 2 && !searching && (
          <div className={styles.searchDropdown}>
            {tableEntries.length === 0 ? (
              <div className={styles.noResults}>
                No se encontraron resultados para "<strong>{debouncedQuery}</strong>"
              </div>
            ) : (
              <>
                <div className={styles.searchResultsHeader}>
                  {searchTotal} resultado{searchTotal !== 1 ? 's' : ''} en {tableEntries.length} fuente{tableEntries.length !== 1 ? 's' : ''}
                </div>
                {tableEntries.map(([table, items]) => (
                  <div key={table}>
                    <div className={styles.sourceGroupHeader}>
                      {TABLE_LABELS[table] || table} ({items.length})
                    </div>
                    {items.slice(0, 10).map((item, i) => (
                      <a
                        key={`${table}-${i}`}
                        href={item.accion || '#'}
                        target={item.accion?.startsWith('http') ? '_blank' : '_self'}
                        rel="noreferrer"
                        className={styles.resultItem}
                        onClick={() => setSearchOpen(false)}
                      >
                        <div className={styles.resultItemContent}>
                          <div className={styles.resultTitle}>
                            {item.titulo || item.id}
                          </div>
                          {item.extra && (
                            <div className={styles.resultExtra}>
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
                      <div className={styles.moreResults}>
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
      <div className={styles.statsGrid}>
        <div className={styles.statCard}>
          <div className={`${styles.statIcon} ${styles.statIconPrimary}`}>
            <Activity size={24} />
          </div>
          <div>
            <div className={styles.statLabel}>Fuentes Activas</div>
            <div className={styles.statValue}>{logs.length}</div>
          </div>
        </div>

        <div className={styles.statCard}>
          <div className={`${styles.statIcon} ${styles.statIconSuccess}`}>
            <CheckCircle2 size={24} />
          </div>
          <div>
            <div className={styles.statLabel}>Scraping Exitoso</div>
            <div className={styles.statValue}>{logs.filter(l => l.estado === 'OK').length}</div>
          </div>
        </div>

        <div className={styles.statCard}>
          <div className={`${styles.statIcon} ${styles.statIconDanger}`}>
            <AlertTriangle size={24} />
          </div>
          <div>
            <div className={styles.statLabel}>Con Errores</div>
            <div className={styles.statValue}>{logs.filter(l => l.estado === 'ERROR').length}</div>
          </div>
        </div>
      </div>

      {/* Logs table */}
      {logs.length > 0 && (
        <div className={styles.logsCard}>
          <div className={styles.logsCardHeader}>
            Últimas ejecuciones de scrapers
          </div>
          <div className={styles.logsTableWrapper}>
            <table className={styles.logsTable}>
              <thead>
                <tr>
                  <th>Fuente</th>
                  <th>Último Intento</th>
                  <th>Estado</th>
                  <th>Nuevos</th>
                </tr>
              </thead>
              <tbody>
                {logs.map((log, i) => (
                  <tr key={i}>
                    <td className={styles.tdFuente}>{log.fuente}</td>
                    <td className={styles.tdDate}>{log.ultimo_intento}</td>
                    <td>
                      <span className={`${styles.statusBadge} ${log.estado === 'OK' ? styles.statusOk : styles.statusError}`}>
                        {log.estado === 'OK' ? <CheckCircle2 size={12} /> : <AlertTriangle size={12} />}
                        {log.estado}
                      </span>
                    </td>
                    <td className={log.nuevos_registros > 0 ? styles.tdNewRecords : styles.tdNewRecordsNone}>
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
