import { useState, useEffect, useMemo } from 'react';
import { Search } from 'lucide-react';

interface NewsItem {
  link: string;
  titulo: string;
  fecha: string;
  imagen: string;
  fuente: string;
}

const NewsPage = () => {
  const [news, setNews] = useState<NewsItem[]>([]);
  const [loading, setLoading] = useState(true);

  // Filter States
  const [searchWord, setSearchWord] = useState('');
  const [filterDate, setFilterDate] = useState('');
  const [selectedSources, setSelectedSources] = useState<Set<string>>(new Set());

  // Here we would normally fetch from our FastAPI backend, e.g. http://localhost:8000/api/news
  // For the initial design iteration, we'll use dummy data if the API is not up yet
  useEffect(() => {
    fetch('http://localhost:8000/api/news')
      .then(res => res.json())
      .then(data => {
        setNews(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("API error, using fallback data", err);
        // Fallback data for design viewing without python backend running
        setNews([
          {
            link: "#",
            titulo: "Min. Medioambiente - Aprueban nuevo reglamento de evaluación ambiental estratégica",
            fecha: "2026-04-29",
            imagen: "logo_diario.jpg",
            fuente: "Diario Oficial"
          },
          {
            link: "#",
            titulo: "Corte Suprema ratifica fallo sobre humedales urbanos",
            fecha: "2026-04-28",
            imagen: "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=400&h=200&fit=crop",
            fuente: "Corte Suprema"
          },
          {
            link: "#",
            titulo: "Nuevo programa de cumplimiento para empresa minera en la región de Antofagasta",
            fecha: "2026-04-27",
            imagen: "logo_sernageomin.png",
            fuente: "Sernageomin"
          }
        ]);
        setLoading(false);
      });
  }, []);

  const uniqueSources = useMemo(() => Array.from(new Set(news.map(item => item.fuente).filter(Boolean))), [news]);

  const handleSourceChange = (source: string) => {
    setSelectedSources(prev => {
      const next = new Set(prev);
      if (next.has(source)) next.delete(source);
      else next.add(source);
      return next;
    });
  };

  const filteredNews = news.filter(item => {
    const matchesSearch = item.titulo?.toLowerCase().includes(searchWord.toLowerCase()) || 
                          item.fuente?.toLowerCase().includes(searchWord.toLowerCase());
    const matchesDate = filterDate ? item.fecha.startsWith(filterDate) : true;
    const matchesSource = selectedSources.size > 0 ? selectedSources.has(item.fuente) : true;
    
    return matchesSearch && matchesDate && matchesSource;
  });

  return (
    <div>
      <div className="header">
        <h1 className="page-title">Noticias Recientes</h1>
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

          <div style={{display: 'flex', alignItems: 'center', gap: '10px', background: 'white', border: '1px solid var(--border)', borderRadius: '30px', padding: '10px 20px'}}>
            <input 
              type="date" 
              value={filterDate}
              onChange={(e) => setFilterDate(e.target.value)}
              style={{border: 'none', outline: 'none', color: 'var(--text-dark)'}}
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
              filteredNews.map((item, idx) => (
                <div key={idx} className="card">
                  <img 
                    src={item.imagen.startsWith('http') ? item.imagen : `/assets/${item.imagen}`} 
                    alt={item.fuente} 
                    className="card-img"
                    onError={(e) => {
                      (e.target as HTMLImageElement).src = 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=400&h=200&fit=crop';
                    }}
                  />
                  <div className="card-content">
                    <div className="card-source">{item.fuente}</div>
                    <div className="card-title">{item.titulo}</div>
                    <div className="card-meta">
                      <span>{item.fecha}</span>
                    </div>
                    <a href={item.link} target="_blank" rel="noreferrer" className="card-action">
                      Leer más
                    </a>
                  </div>
                </div>
              ))
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default NewsPage;
