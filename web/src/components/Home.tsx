import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Search, X, ExternalLink, Leaf, ShieldAlert, Gavel, 
  FileText, ArrowRight, Activity, Database, BellRing, 
  MapPin, Landmark, Droplets
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';

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
  sea_proyectos_evaluados: 'Proyectos SEA',
};

const MODULES = [
  {
    id: 'sea',
    title: 'Evaluación Ambiental',
    description: 'Explora resoluciones, pertinencias y proyectos en evaluación a nivel nacional.',
    icon: <Leaf size={24} />,
    color: '#10b981',
    bg: 'rgba(16, 185, 129, 0.1)',
    path: '/sea-evaluados'
  },
  {
    id: 'sma',
    title: 'Fiscalización y Sanción',
    description: 'Monitorea procesos sancionatorios, fiscalizaciones y medidas provisionales.',
    icon: <ShieldAlert size={24} />,
    color: '#f59e0b',
    bg: 'rgba(245, 158, 11, 0.1)',
    path: '/sancionatorios'
  },
  {
    id: 'tribunales',
    title: 'Tribunales Ambientales',
    description: 'Seguimiento detallado de causas procesales en los tribunales del país.',
    icon: <Gavel size={24} />,
    color: '#6366f1',
    bg: 'rgba(99, 102, 241, 0.1)',
    path: '/tribunales'
  },
  {
    id: 'dga',
    title: 'Dirección de Aguas',
    description: 'Resoluciones, derechos de aprovechamiento y consultas DGA.',
    icon: <Droplets size={24} />,
    color: '#3b82f6',
    bg: 'rgba(59, 130, 246, 0.1)',
    path: '/consultas/dga'
  }
];

const Home = () => {
  const { token } = useAuth();
  const navigate = useNavigate();

  // Search state
  const [searchQuery, setSearchQuery] = useState('');
  const [debouncedQuery, setDebouncedQuery] = useState('');
  const [searchResults, setSearchResults] = useState<Record<string, SearchResult[]>>({});
  const [searchTotal, setSearchTotal] = useState(0);
  const [searching, setSearching] = useState(false);
  const [searchOpen, setSearchOpen] = useState(false);
  
  const searchRef = useRef<HTMLDivElement>(null);
  const debounceRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  // Debounce search
  useEffect(() => {
    if (debounceRef.current) clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(() => {
      setDebouncedQuery(searchQuery);
    }, 400);
    return () => { if (debounceRef.current) clearTimeout(debounceRef.current); };
  }, [searchQuery]);

  // Execute search
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

  // Animation variants
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: { 
      opacity: 1,
      transition: { staggerChildren: 0.1 }
    }
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: { 
      opacity: 1, 
      y: 0,
      transition: { type: 'spring', stiffness: 300, damping: 24 }
    }
  };

  return (
    <div style={{ 
      maxWidth: '1200px', 
      margin: '0 auto', 
      padding: '40px 20px',
      minHeight: '100vh'
    }}>
      
      {/* Hero Section */}
      <motion.div 
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: 'easeOut' }}
        style={{ textAlign: 'center', marginBottom: '60px', marginTop: '20px' }}
      >
        <h1 style={{ 
          fontSize: 'clamp(32px, 5vw, 48px)', 
          fontWeight: 800, 
          color: 'var(--text-dark)',
          marginBottom: '16px',
          letterSpacing: '-0.02em',
          background: 'linear-gradient(135deg, var(--text-dark) 0%, var(--primary) 100%)',
          WebkitBackgroundClip: 'text',
          WebkitTextFillColor: 'transparent'
        }}>
          Inteligencia Ambiental Centralizada
        </h1>
        <p style={{ 
          fontSize: '18px', 
          color: 'var(--text-light)', 
          maxWidth: '600px', 
          margin: '0 auto',
          lineHeight: 1.6 
        }}>
          Accede, analiza y monitorea el estado normativo y ambiental de todo Chile en tiempo real desde un único lugar.
        </p>
      </motion.div>

      {/* Global Search Centerpiece */}
      <motion.div 
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5, delay: 0.2 }}
        ref={searchRef} 
        style={{ 
          position: 'relative', 
          maxWidth: '800px', 
          margin: '0 auto 60px auto',
          zIndex: 50
        }}
      >
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: '16px',
          background: 'rgba(255, 255, 255, 0.8)',
          backdropFilter: 'blur(12px)',
          WebkitBackdropFilter: 'blur(12px)',
          border: '1px solid rgba(0,0,0,0.08)',
          borderRadius: '24px',
          padding: '16px 28px',
          boxShadow: searchOpen && searchQuery 
            ? '0 12px 40px rgba(var(--primary-rgb), 0.15)' 
            : '0 8px 30px rgba(0,0,0,0.04)',
          transition: 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)',
        }}>
          <Search size={24} color="var(--primary)" style={{ flexShrink: 0 }} />
          <input
            type="text"
            placeholder="Buscar proyectos, resoluciones, empresas, normativas..."
            value={searchQuery}
            onChange={e => setSearchQuery(e.target.value)}
            onFocus={() => { if (debouncedQuery.length >= 2) setSearchOpen(true); }}
            style={{
              border: 'none',
              outline: 'none',
              width: '100%',
              fontSize: '18px',
              color: 'var(--text-dark)',
              background: 'transparent',
              fontWeight: 500
            }}
          />
          {searchQuery && (
            <button 
              onClick={clearSearch} 
              style={{ 
                background: 'var(--bg-light)', 
                border: 'none', 
                cursor: 'pointer', 
                color: 'var(--text-light)', 
                display: 'flex', 
                padding: '6px',
                borderRadius: '50%',
                transition: 'background 0.2s'
              }}
              onMouseEnter={e => e.currentTarget.style.background = '#e2e8f0'}
              onMouseLeave={e => e.currentTarget.style.background = 'var(--bg-light)'}
            >
              <X size={18} />
            </button>
          )}
        </div>

        {/* Search Results Dropdown */}
        <AnimatePresence>
          {searchOpen && debouncedQuery.length >= 2 && !searching && (
            <motion.div 
              initial={{ opacity: 0, y: 10, scale: 0.98 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: -10, scale: 0.98 }}
              transition={{ duration: 0.2 }}
              style={{
                position: 'absolute',
                top: 'calc(100% + 12px)',
                left: 0,
                right: 0,
                background: 'rgba(255, 255, 255, 0.95)',
                backdropFilter: 'blur(20px)',
                border: '1px solid rgba(0,0,0,0.08)',
                borderRadius: '20px',
                boxShadow: '0 20px 50px rgba(0,0,0,0.1)',
                maxHeight: '60vh',
                overflowY: 'auto',
                overflowX: 'hidden'
              }}
            >
              {tableEntries.length === 0 ? (
                <div style={{ padding: '30px', textAlign: 'center', color: 'var(--text-light)' }}>
                  <Search size={40} style={{ opacity: 0.2, margin: '0 auto 15px' }} />
                  <div style={{ fontSize: '16px' }}>No se encontraron resultados para "<strong>{debouncedQuery}</strong>"</div>
                  <div style={{ fontSize: '14px', marginTop: '8px', opacity: 0.7 }}>Intenta con términos más generales o el rol exacto.</div>
                </div>
              ) : (
                <>
                  <div style={{ 
                    padding: '16px 24px', 
                    borderBottom: '1px solid rgba(0,0,0,0.06)', 
                    fontSize: '14px', 
                    color: 'var(--text-light)', 
                    fontWeight: 600,
                    position: 'sticky',
                    top: 0,
                    background: 'rgba(255,255,255,0.95)',
                    zIndex: 2
                  }}>
                    {searchTotal} resultado{searchTotal !== 1 ? 's' : ''} en {tableEntries.length} fuente{tableEntries.length !== 1 ? 's' : ''}
                  </div>
                  {tableEntries.map(([table, items]) => (
                    <div key={table}>
                      <div style={{
                        padding: '10px 24px',
                        fontSize: '12px',
                        fontWeight: 700,
                        textTransform: 'uppercase',
                        letterSpacing: '0.1em',
                        color: 'var(--primary)',
                        background: 'rgba(var(--primary-rgb), 0.04)',
                        borderBottom: '1px solid rgba(0,0,0,0.04)'
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
                            alignItems: 'center',
                            gap: '14px',
                            padding: '14px 24px',
                            textDecoration: 'none',
                            borderBottom: '1px solid rgba(0,0,0,0.03)',
                            transition: 'all 0.2s ease'
                          }}
                          onMouseEnter={e => {
                            e.currentTarget.style.background = 'rgba(0,0,0,0.02)';
                            e.currentTarget.style.paddingLeft = '28px';
                          }}
                          onMouseLeave={e => {
                            e.currentTarget.style.background = 'transparent';
                            e.currentTarget.style.paddingLeft = '24px';
                          }}
                          onClick={() => setSearchOpen(false)}
                        >
                          <div style={{ flex: 1, minWidth: 0 }}>
                            <div style={{ 
                              fontSize: '14px', 
                              fontWeight: 600, 
                              color: 'var(--text-dark)', 
                              whiteSpace: 'nowrap', 
                              overflow: 'hidden', 
                              textOverflow: 'ellipsis' 
                            }}>
                              {item.titulo || item.id}
                            </div>
                            {item.extra && (
                              <div style={{ fontSize: '12px', color: 'var(--text-light)', marginTop: '4px' }}>
                                {item.extra}
                              </div>
                            )}
                          </div>
                          {item.accion?.startsWith('http') ? (
                            <ExternalLink size={16} color="var(--primary)" style={{ flexShrink: 0, opacity: 0.5 }} />
                          ) : (
                            <ArrowRight size={16} color="var(--text-light)" style={{ flexShrink: 0, opacity: 0.5 }} />
                          )}
                        </a>
                      ))}
                    </div>
                  ))}
                </>
              )}
            </motion.div>
          )}
        </AnimatePresence>
      </motion.div>

      {/* Modules Grid */}
      <motion.div 
        variants={containerVariants}
        initial="hidden"
        animate="visible"
        style={{ 
          display: 'grid', 
          gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', 
          gap: '24px',
          marginBottom: '60px'
        }}
      >
        {MODULES.map((mod) => (
          <motion.div 
            key={mod.id}
            variants={itemVariants}
            whileHover={{ y: -5, scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            onClick={() => navigate(mod.path)}
            style={{
              background: 'rgba(255, 255, 255, 0.7)',
              backdropFilter: 'blur(10px)',
              border: '1px solid rgba(255, 255, 255, 0.5)',
              borderRadius: '24px',
              padding: '30px',
              cursor: 'pointer',
              boxShadow: '0 10px 40px rgba(0,0,0,0.03)',
              display: 'flex',
              flexDirection: 'column',
              transition: 'all 0.3s ease'
            }}
          >
            <div style={{ 
              width: '56px', 
              height: '56px', 
              borderRadius: '16px', 
              background: mod.bg,
              color: mod.color,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              marginBottom: '20px'
            }}>
              {mod.icon}
            </div>
            <h3 style={{ fontSize: '18px', fontWeight: 700, color: 'var(--text-dark)', marginBottom: '10px' }}>
              {mod.title}
            </h3>
            <p style={{ fontSize: '14px', color: 'var(--text-light)', lineHeight: 1.5, flex: 1 }}>
              {mod.description}
            </p>
            <div style={{ 
              display: 'flex', 
              alignItems: 'center', 
              gap: '8px', 
              color: mod.color,
              fontSize: '13px',
              fontWeight: 600,
              marginTop: '20px'
            }}>
              Acceder al módulo <ArrowRight size={14} />
            </div>
          </motion.div>
        ))}
      </motion.div>

      {/* Global Stats Footer */}
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.8, duration: 1 }}
        style={{
          display: 'flex',
          flexWrap: 'wrap',
          justifyContent: 'center',
          gap: '40px',
          padding: '40px',
          borderTop: '1px solid rgba(0,0,0,0.05)',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{ padding: '10px', background: 'rgba(var(--primary-rgb), 0.1)', borderRadius: '12px', color: 'var(--primary)' }}>
            <Database size={20} />
          </div>
          <div>
            <div style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text-dark)' }}>+30.000</div>
            <div style={{ fontSize: '12px', color: 'var(--text-light)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Registros Históricos</div>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{ padding: '10px', background: 'rgba(16, 185, 129, 0.1)', borderRadius: '12px', color: '#10b981' }}>
            <Activity size={20} />
          </div>
          <div>
            <div style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text-dark)' }}>24/7</div>
            <div style={{ fontSize: '12px', color: 'var(--text-light)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Actualización Continua</div>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
          <div style={{ padding: '10px', background: 'rgba(245, 158, 11, 0.1)', borderRadius: '12px', color: '#f59e0b' }}>
            <BellRing size={20} />
          </div>
          <div>
            <div style={{ fontSize: '20px', fontWeight: 800, color: 'var(--text-dark)' }}>Tiempo Real</div>
            <div style={{ fontSize: '12px', color: 'var(--text-light)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Alertas y Notificaciones</div>
          </div>
        </div>
      </motion.div>

    </div>
  );
};

export default Home;
