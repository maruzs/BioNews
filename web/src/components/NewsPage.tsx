import { useState, useEffect, useMemo } from 'react';
import { Search, X, Filter, ChevronDown, ChevronUp } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';

interface NewsItem {
  link: string;
  titulo: string;
  fecha: string;
  imagen: string;
  fuente: string;
  fecha_scraping: string;
  is_new: boolean;
}

const NewsPage = () => {
  const { token } = useAuth();
  const { markItemViewed, refreshCategory, markAllRead, setCategoryActive } = useNotifications();
  const [news, setNews] = useState<NewsItem[]>([]);
  const [loading, setLoading] = useState(true);

  // Filter States
  const [searchWord, setSearchWord] = useState('');
  const [filterDate, setFilterDate] = useState('');
  const [selectedSources, setSelectedSources] = useState<Set<string>>(new Set());
  const [showFilters, setShowFilters] = useState(false);

  // Applied Filter States
  const [appliedSearch, setAppliedSearch] = useState('');
  const [appliedDate, setAppliedDate] = useState('');
  const [appliedSources, setAppliedSources] = useState<Set<string>>(new Set());

  const handleApplyFilters = () => {
    setAppliedSearch(searchWord);
    setAppliedDate(filterDate);
    setAppliedSources(new Set(selectedSources));
  };

  const resetFilters = () => {
    setSearchWord('');
    setFilterDate('');
    setSelectedSources(new Set());
    setAppliedSearch('');
    setAppliedDate('');
    setAppliedSources(new Set());
  };

  useEffect(() => {
    setCategoryActive('noticias', true);
    return () => {
      setCategoryActive('noticias', false);
    };
  }, [setCategoryActive]);

  useEffect(() => {
    if (!token) return;
    fetch('/api/news', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(res => res.json())
      .then(data => {
        setNews(data);
        setLoading(false);
        // Actualizar punto rojo al entrar a noticias (sin F5)
        refreshCategory('noticias');
      })
      .catch(err => {
        console.error("API error, using fallback data", err);
        setNews([]);
        setLoading(false);
      });
  }, [token]);

  const uniqueSources = useMemo(() => {
    const sources = Array.from(new Set(news.map(item => {
      // Normalización para el filtro visual si existen registros viejos
      if (item.fuente === 'Tribunal Ambiental') return 'Segundo Tribunal';
      return item.fuente;
    }).filter(Boolean)));
    return sources.sort();
  }, [news]);


  const filteredNews = news.filter(item => {
    const fuenteNormalizada = item.fuente === 'Tribunal Ambiental' ? 'Segundo Tribunal' : item.fuente;

    const matchesSearch = item.titulo?.toLowerCase().includes(appliedSearch.toLowerCase()) ||
      fuenteNormalizada?.toLowerCase().includes(appliedSearch.toLowerCase());

    const matchesDate = appliedDate ? item.fecha.startsWith(appliedDate) : true;

    const matchesSource = appliedSources.size > 0 ? appliedSources.has(fuenteNormalizada) : true;

    return matchesSearch && matchesDate && matchesSource;
  });

  return (
    <div style={{ padding: '20px', maxWidth: '1400px', margin: '0 auto', width: '100%' }}>
      <div style={{ marginBottom: '30px', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
        <div>
          <h1 style={{ fontSize: '28px', fontWeight: 'bold', color: 'var(--text-dark)' }}>Noticias Recientes</h1>
          <p style={{ color: 'var(--text-light)', marginTop: '5px' }}>Mantente al día con las últimas novedades del sector.</p>
        </div>
        <button
          onClick={async () => {
            await markAllRead('noticias');
            setNews(prev => prev.map(item => ({ ...item, is_new: false })));
          }}
          style={{
            fontSize: '13px',
            padding: '8px 16px',
            borderRadius: '8px',
            border: '1px solid var(--primary)',
            color: 'var(--primary)',
            background: 'white',
            cursor: 'pointer',
            fontWeight: 600,
            transition: 'all 0.2s ease'
          }}
          onMouseOver={(e) => {
            e.currentTarget.style.background = 'var(--primary-light)';
          }}
          onMouseOut={(e) => {
            e.currentTarget.style.background = 'white';
          }}
        >
          Marcar todo como leído
        </button>
      </div>

      {/* Control Bar */}
      <div style={{ 
        backgroundColor: 'white', padding: '15px', borderRadius: '12px', 
        border: '1px solid var(--border)', boxShadow: '0 2px 10px rgba(0,0,0,0.03)',
        marginBottom: '15px', display: 'flex', flexWrap: 'wrap', gap: '15px', alignItems: 'center'
      }}>
        <div style={{ position: 'relative', width: '400px', display: 'flex', gap: '10px' }}>
          <div style={{ position: 'relative', flexGrow: 1 }}>
            <Search size={18} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-light)' }} />
            <input 
              type="text" 
              placeholder="Buscar por palabras clave..." 
              value={searchWord}
              onChange={(e) => {
                setSearchWord(e.target.value);
                if (e.target.value === '') setAppliedSearch('');
              }}
              onKeyDown={(e) => {
                if (e.key === 'Enter') {
                  handleApplyFilters();
                }
              }}
              style={{ 
                width: '100%', padding: '10px 40px', borderRadius: '8px', 
                border: '1px solid var(--border)', outline: 'none', fontSize: '14px' 
              }}
            />
            {searchWord && (
              <button 
                onClick={() => { setSearchWord(''); setAppliedSearch(''); }}
                style={{ position: 'absolute', right: '12px', top: '50%', transform: 'translateY(-50%)', background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-light)' }}
              >
                <X size={16} />
              </button>
            )}
          </div>
          <button 
            onClick={handleApplyFilters}
            style={{
              padding: '10px 20px', borderRadius: '8px', border: 'none',
              background: 'var(--primary)', color: 'white', fontWeight: 600, cursor: 'pointer',
              fontSize: '14px'
            }}
          >
            Buscar
          </button>
        </div>
        
        <button 
          onClick={() => setShowFilters(!showFilters)}
          style={{ 
            display: 'flex', alignItems: 'center', gap: '8px', padding: '10px 15px',
            backgroundColor: showFilters ? 'var(--primary-light)' : 'white',
            color: showFilters ? 'var(--primary)' : 'var(--text-dark)',
            border: '1px solid ' + (showFilters ? 'var(--primary)' : 'var(--border)'),
            borderRadius: '8px', cursor: 'pointer', fontWeight: 500, fontSize: '14px',
            transition: 'all 0.2s'
          }}
        >
          <Filter size={18} />
          Filtros Avanzados
          {showFilters ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
        </button>

        <div style={{ color: 'var(--text-light)', fontSize: '14px', marginLeft: 'auto' }}>
          {filteredNews.length} resultados encontrados
        </div>
      </div>

      {/* Real-time Source Filters */}
      <div style={{ 
        display: 'flex', flexWrap: 'wrap', gap: '10px', marginBottom: '25px', 
        padding: '0 5px'
      }}>
        {uniqueSources.map(source => (
          <label key={source} style={{ 
            display: 'flex', alignItems: 'center', gap: '8px', cursor: 'pointer', 
            background: appliedSources.has(source) ? 'var(--primary-light)' : 'white', 
            padding: '6px 14px', borderRadius: '20px', 
            border: '1px solid ' + (appliedSources.has(source) ? 'var(--primary)' : 'var(--border)'),
            fontSize: '13px', transition: 'all 0.2s', 
            color: appliedSources.has(source) ? 'var(--primary)' : 'var(--text-dark)',
            fontWeight: appliedSources.has(source) ? 600 : 400,
            boxShadow: appliedSources.has(source) ? '0 2px 4px rgba(0,0,0,0.05)' : 'none'
          }}>
            <input
              type="checkbox"
              checked={appliedSources.has(source)}
              onChange={() => {
                const next = new Set(appliedSources);
                if (next.has(source)) next.delete(source);
                else next.add(source);
                setAppliedSources(next);
                setSelectedSources(next); // Sync selectedSources for the clear button
              }}
              style={{ display: 'none' }}
            />
            {source}
          </label>
        ))}
      </div>

      {/* Advanced Filters */}
      {showFilters && (
        <div style={{ 
          backgroundColor: '#f8fafc', padding: '20px', borderRadius: '12px', 
          border: '1px solid var(--border)', marginBottom: '25px',
          display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: '15px'
        }}>
          <div>
            <label style={{ display: 'block', fontSize: '12px', fontWeight: 600, color: 'var(--text-dark)', marginBottom: '5px' }}>Fecha</label>
            <input 
              type="date" 
              value={filterDate} 
              onChange={(e) => setFilterDate(e.target.value)} 
              style={{ width: '100%', padding: '8px', borderRadius: '6px', border: '1px solid var(--border)' }} 
            />
          </div>
          
          <div style={{ gridColumn: '1 / -1', display: 'flex', gap: '10px', justifyContent: 'flex-end', borderTop: '1px solid var(--border)', paddingTop: '20px', marginTop: '10px' }}>
            <button 
              onClick={resetFilters}
              style={{ 
                padding: '10px 20px', borderRadius: '8px', border: '1px solid var(--border)', 
                background: 'white', color: 'var(--text-dark)', fontWeight: 600, cursor: 'pointer' 
              }}
            >
              LIMPIAR FILTROS
            </button>
            <button 
              onClick={handleApplyFilters}
              style={{ 
                padding: '10px 20px', borderRadius: '8px', border: 'none', 
                background: 'var(--primary)', color: 'white', fontWeight: 600, cursor: 'pointer' 
              }}
            >
              APLICAR FILTROS
            </button>
          </div>
        </div>
      )}

      <div style={{ marginTop: '20px' }}>
        {loading ? (
          <p className="empty-state">Cargando noticias...</p>
        ) : (
          <div className="news-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '25px', width: '100%' }}>
            {filteredNews.length === 0 ? (
              <p className="empty-state" style={{ gridColumn: '1 / -1', textAlign: 'center' }}>No se encontraron noticias con estos filtros.</p>
            ) : (
              filteredNews.map((item, idx) => {
                const itemIsNew = item.is_new;
                const fuenteNormalizada = item.fuente === 'Tribunal Ambiental' ? 'Segundo Tribunal' : item.fuente;

                return (
                  <div key={idx} className={`card ${itemIsNew ? 'new-highlight' : ''}`} style={itemIsNew ? {
                    border: '2px solid var(--primary)',
                    boxShadow: '0 0 15px rgba(34, 197, 94, 0.2)',
                    position: 'relative'
                  } : {}}>
                    {itemIsNew && (
                      <div style={{
                        position: 'absolute',
                        top: '10px',
                        right: '10px',
                        background: 'var(--primary)',
                        color: 'white',
                        padding: '2px 10px',
                        borderRadius: '10px',
                        fontSize: '0.7rem',
                        fontWeight: 'bold',
                        zIndex: 10
                      }}>
                        NUEVA
                      </div>
                    )}
                    <img
                      src={item.imagen && item.imagen.startsWith('http') ? item.imagen : (item.imagen ? `/assets/${item.imagen}` : '/assets/placeholder.jpg')}
                      alt={fuenteNormalizada}
                      className="card-img"
                      onError={(e) => {
                        (e.target as HTMLImageElement).src = 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=400&h=200&fit=crop';
                      }}
                    />
                    <div className="card-content">
                      <div className="card-source">{fuenteNormalizada}</div>
                      <div className="card-title">{item.titulo}</div>
                      <div className="card-meta">
                        <span>{item.fecha}</span>
                      </div>
                      <a
                        href={item.link}
                        target="_blank"
                        rel="noreferrer"
                        className="card-action"
                        onClick={() => {
                          markItemViewed('noticias', item.link);
                          setNews(prev => prev.map(n => n.link === item.link ? { ...n, is_new: false } : n));
                        }}
                      >
                        Leer más
                      </a>
                    </div>
                  </div>
                );
              })
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default NewsPage;
