import { useState, useEffect, useMemo } from 'react';
import { Search } from 'lucide-react';
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
  const { token, user } = useAuth();
  const { markExit, markItemViewed } = useNotifications();
  const [news, setNews] = useState<NewsItem[]>([]);
  const [loading, setLoading] = useState(true);

  // Filter States
  const [searchWord, setSearchWord] = useState('');
  const [filterDate, setFilterDate] = useState('');
  const [selectedSources, setSelectedSources] = useState<Set<string>>(new Set());

  useEffect(() => {
    // Al desmontar la página de noticias, registrar la salida en la DB
    return () => {
      markExit('noticias');
    };
  }, [markExit]);

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

  const handleSourceChange = (source: string) => {
    setSelectedSources(prev => {
      const next = new Set(prev);
      if (next.has(source)) next.delete(source);
      else next.add(source);
      return next;
    });
  };

  const filteredNews = news.filter(item => {
    const fuenteNormalizada = item.fuente === 'Tribunal Ambiental' ? 'Segundo Tribunal' : item.fuente;
    
    const matchesSearch = item.titulo?.toLowerCase().includes(searchWord.toLowerCase()) || 
                          fuenteNormalizada?.toLowerCase().includes(searchWord.toLowerCase());
    
    const matchesDate = filterDate ? item.fecha.startsWith(filterDate) : true;
    
    const matchesSource = selectedSources.size > 0 ? selectedSources.has(fuenteNormalizada) : true;
    
    return matchesSearch && matchesDate && matchesSource;
  });

  return (
    <div>
      <div className="header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1 className="page-title">Noticias Recientes</h1>
        <button 
          onClick={async () => {
            await markExit('noticias');
            setNews(prev => prev.map(item => ({ ...item, is_new: false })));
          }}
          className="btn-mark-read"
          style={{
            fontSize: '13px',
            padding: '6px 12px',
            borderRadius: '20px',
            border: '1px solid var(--primary)',
            color: 'var(--primary)',
            background: 'white',
            cursor: 'pointer',
            fontWeight: 600,
            transition: 'all 0.2s ease'
          }}
        >
          Marcar todo como leído
        </button>
      </div>

      <div className="news-filters" style={{display: 'flex', flexDirection: 'column', gap: '15px'}}>
        
        <div style={{display: 'flex', alignItems: 'center', gap: '15px', flexWrap: 'wrap'}}>
          <div className="search-bar" style={{flex: 1, minWidth: '250px', background: 'white', border: '1px solid var(--border)', borderRadius: '30px', padding: '10px 20px', display: 'flex', alignItems: 'center'}}>
            <Search size={18} color="var(--primary)" style={{marginRight: '10px'}} />
            <input 
              type="text" 
              placeholder="Buscar por palabras clave..." 
              value={searchWord}
              onChange={(e) => setSearchWord(e.target.value)}
              style={{border: 'none', outline: 'none', width: '100%'}}
            />
          </div>

          <div style={{display: 'flex', alignItems: 'center', gap: '10px', background: 'white', border: '1px solid var(--border)', borderRadius: '30px', padding: '10px 20px', flex: 1, minWidth: '200px'}}>
            <span style={{fontSize: '0.85rem', color: 'var(--text-light)', fontWeight: 500}}>Fecha:</span>
            <input 
              type="date" 
              value={filterDate}
              onChange={(e) => setFilterDate(e.target.value)}
              style={{border: 'none', outline: 'none', color: 'var(--text-dark)', width: '100%', backgroundColor: 'transparent'}}
            />
          </div>
        </div>

        <div style={{display: 'flex', alignItems: 'center', gap: '15px', flexWrap: 'wrap'}}>
          <span className="filter-label" style={{fontWeight: 600, color: 'var(--text-dark)'}}>Filtrar por Organismo:</span>
          {uniqueSources.map(source => (
            <label key={source} className="filter-checkbox" style={{display: 'flex', alignItems: 'center', gap: '5px', cursor: 'pointer', background: 'white', padding: '5px 12px', borderRadius: '20px', border: '1px solid var(--border)'}}>
              <input 
                type="checkbox" 
                checked={selectedSources.has(source)}
                onChange={() => handleSourceChange(source)}
              /> 
              {source}
            </label>
          ))}
        </div>
      </div>
      
      <div className="content-wrapper">
        {loading ? (
          <p className="empty-state">Cargando noticias...</p>
        ) : (
          <div className="news-grid">
            {filteredNews.length === 0 ? (
              <p className="empty-state" style={{gridColumn: '1 / -1', textAlign: 'center'}}>No se encontraron noticias con estos filtros.</p>
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
