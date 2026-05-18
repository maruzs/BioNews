import { useState, useEffect, useMemo } from 'react';
import { Search, X, Filter, ChevronDown, ChevronUp } from 'lucide-react';
import { useAuth } from '../../../context/AuthContext';
import { useNotifications } from '../../../context/NotificationsContext';
import styles from './NewsPage.module.css';

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

  const [searchWord, setSearchWord] = useState('');
  const [filterDate, setFilterDate] = useState('');
  const [selectedSources, setSelectedSources] = useState<Set<string>>(new Set());
  const [showFilters, setShowFilters] = useState(false);

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
    return () => { setCategoryActive('noticias', false); };
  }, [setCategoryActive]);

  useEffect(() => {
    if (!token) return;
    fetch('/api/news', { headers: { 'Authorization': `Bearer ${token}` } })
      .then(res => res.json())
      .then(data => {
        setNews(data);
        setLoading(false);
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
    <div className={styles.pageContainer}>
      <div className={styles.pageHeader}>
        <div>
          <h1 className={styles.pageTitle}>Noticias Recientes</h1>
          <p className={styles.pageSubtitle}>Mantente al día con las últimas novedades del sector.</p>
        </div>
        <button
          onClick={async () => {
            await markAllRead('noticias');
            setNews(prev => prev.map(item => ({ ...item, is_new: false })));
          }}
          className={styles.markAllReadBtn}
        >
          Marcar todo como leído
        </button>
      </div>

      {/* Control Bar */}
      <div className={styles.controlBar}>
        <div className={styles.searchGroup}>
          <div className={styles.searchInputWrapper}>
            <Search size={18} className={styles.searchIcon} />
            <input
              type="text"
              placeholder="Buscar por palabras clave..."
              value={searchWord}
              onChange={(e) => {
                setSearchWord(e.target.value);
                if (e.target.value === '') setAppliedSearch('');
              }}
              onKeyDown={(e) => { if (e.key === 'Enter') handleApplyFilters(); }}
              className={styles.searchInput}
            />
            {searchWord && (
              <button
                onClick={() => { setSearchWord(''); setAppliedSearch(''); }}
                className={styles.clearBtn}
              >
                <X size={16} />
              </button>
            )}
          </div>
          <button onClick={handleApplyFilters} className={styles.searchSubmitBtn}>
            Buscar
          </button>
        </div>

        <button
          onClick={() => setShowFilters(!showFilters)}
          className={`${styles.filtersToggleBtn} ${showFilters ? styles.filtersToggleBtnOpen : styles.filtersToggleBtnClosed}`}
        >
          <Filter size={18} />
          Filtros Avanzados
          {showFilters ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
        </button>

        <div className={styles.resultsCount}>
          {filteredNews.length} resultados encontrados
        </div>
      </div>

      {/* Source Chips */}
      <div className={styles.sourceChips}>
        {uniqueSources.map(source => (
          <label
            key={source}
            className={`${styles.sourceChip} ${appliedSources.has(source) ? styles.sourceChipActive : styles.sourceChipInactive}`}
          >
            <input
              type="checkbox"
              checked={appliedSources.has(source)}
              onChange={() => {
                const next = new Set(appliedSources);
                if (next.has(source)) next.delete(source);
                else next.add(source);
                setAppliedSources(next);
                setSelectedSources(next);
              }}
              className={styles.hiddenCheckbox}
            />
            {source}
          </label>
        ))}
      </div>

      {/* Advanced Filters */}
      {showFilters && (
        <div className={styles.advancedFilters}>
          <div>
            <label className={styles.filterFieldLabel}>Fecha</label>
            <input
              type="date"
              value={filterDate}
              onChange={(e) => setFilterDate(e.target.value)}
              className={styles.filterDateInput}
            />
          </div>
          <div className={styles.filterActions}>
            <button onClick={resetFilters} className={styles.btnClearFilters}>LIMPIAR FILTROS</button>
            <button onClick={handleApplyFilters} className={styles.btnApplyFilters}>APLICAR FILTROS</button>
          </div>
        </div>
      )}

      {/* News Grid */}
      <div className={styles.newsSection}>
        {loading ? (
          <p className={styles.emptyState}>Cargando noticias...</p>
        ) : (
          <div className={styles.newsGrid}>
            {filteredNews.length === 0 ? (
              <p className={styles.emptyState}>No se encontraron noticias con estos filtros.</p>
            ) : (
              filteredNews.map((item, idx) => {
                const itemIsNew = item.is_new;
                const fuenteNormalizada = item.fuente === 'Tribunal Ambiental' ? 'Segundo Tribunal' : item.fuente;

                return (
                  <div key={idx} className={`${styles.card} ${itemIsNew ? styles.cardNew : ''}`}>
                    {itemIsNew && (
                      <div className={styles.newBadge}>NUEVA</div>
                    )}
                    <img
                      src={item.imagen && item.imagen.startsWith('http') ? item.imagen : (item.imagen ? `/assets/${item.imagen}` : '/assets/placeholder.jpg')}
                      alt={fuenteNormalizada}
                      className={styles.cardImg}
                      onError={(e) => {
                        (e.target as HTMLImageElement).src = 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?q=80&w=400&h=200&fit=crop';
                      }}
                    />
                    <div className={styles.cardContent}>
                      <div className={styles.cardSource}>{fuenteNormalizada}</div>
                      <div className={styles.cardTitle}>{item.titulo}</div>
                      <div className={styles.cardMeta}>
                        <span>{item.fecha}</span>
                      </div>
                      <a
                        href={item.link}
                        target="_blank"
                        rel="noreferrer"
                        className={styles.cardAction}
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
