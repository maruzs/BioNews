import { useState, useEffect } from 'react';
import { Search, ExternalLink, X, HelpCircle, Pencil, ClipboardList, Heart } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';

interface DGAConsulta {
  id: string;
  nombre: string;
  imagen: string;
  url: string;
  fecha_scraping: string;
  is_new: boolean;
}

const DGAConsultasPage = () => {
  const { token } = useAuth();
  const { markItemViewed, refreshCategory, setCategoryActive } = useNotifications();
  const [data, setData] = useState<DGAConsulta[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [selectedItem, setSelectedItem] = useState<DGAConsulta | null>(null);
  const [favorites, setFavorites] = useState<Set<string>>(new Set());

  const [appliedSearch, setAppliedSearch] = useState('');

  const handleApplyFilters = () => {
    setAppliedSearch(search);
  };


  const category = 'dga';

  useEffect(() => {
    setCategoryActive(category, true);
    return () => {
      setCategoryActive(category, false);
    };
  }, [setCategoryActive]);

  const fetchData = async () => {
    setLoading(true);
    try {
      const res = await fetch(`/api/data/dga_consultas?limit=-1`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const json = await res.json();
      setData(Array.isArray(json) ? json : []);
      refreshCategory(category);
      
      // Cargar favoritos
      const favRes = await fetch('/api/favorites', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const favJson = await favRes.json();
      setFavorites(new Set(favJson.map((f: any) => f.id_o_link)));
    } catch (err) {
      console.error(err);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleOpenModal = (item: DGAConsulta) => {
    setSelectedItem(item);
    if (item.is_new) {
      markItemViewed(category, item.id);
      setData(prev => prev.map(n => n.id === item.id ? { ...n, is_new: false } : n));
    }
  };

  const filteredData = data.filter(item => 
    item.nombre.toLowerCase().includes(appliedSearch.toLowerCase())
  );

  const toggleFavorite = async (e: React.MouseEvent, item: DGAConsulta) => {
    e.stopPropagation();
    const isFav = favorites.has(item.id);
    try {
      if (isFav) {
        await fetch(`/api/favorites/${encodeURIComponent(item.id)}`, {
          method: 'DELETE',
          headers: { 'Authorization': `Bearer ${token}` }
        });
        setFavorites(prev => {
          const next = new Set(prev);
          next.delete(item.id);
          return next;
        });
      } else {
        await fetch('/api/favorites', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
          body: JSON.stringify({
            id_o_link: item.id,
            fuente: 'DGA',
            nombre: item.nombre,
            accion: item.url
          })
        });
        setFavorites(prev => {
          const next = new Set(prev);
          next.add(item.id);
          return next;
        });
      }
    } catch (err) {
      console.error("Error toggling favorite:", err);
    }
  };

  // Determinar si es un formulario de Google o no
  const isGoogleForm = (url: string) => url.includes('forms.gle') || url.includes('docs.google.com/forms');

  return (
    <div style={{ padding: '20px', maxWidth: '1400px', margin: '0 auto', width: '100%' }}>
      <div style={{ marginBottom: '30px' }}>
        <h1 style={{ fontSize: '28px', fontWeight: 'bold', color: 'var(--text-dark)' }}>DGA - Consultas Públicas</h1>
        <p style={{ color: 'var(--text-light)', marginTop: '5px' }}>Consultas y participación ciudadana de la Dirección General de Aguas.</p>
      </div>

      {/* Control Bar */}
      <div style={{ 
        backgroundColor: 'white', padding: '15px', borderRadius: '12px', 
        border: '1px solid var(--border)', boxShadow: '0 2px 10px rgba(0,0,0,0.03)',
        marginBottom: '25px', display: 'flex', flexWrap: 'wrap', gap: '15px', alignItems: 'center'
      }}>
        <div style={{ position: 'relative', width: '400px' }}>
          <Search size={18} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-light)' }} />
          <input 
            type="text" 
            placeholder="Buscar por nombre..." 
            value={search}
            onChange={(e) => {
              setSearch(e.target.value);
              if (e.target.value === '') setAppliedSearch('');
            }}
            onKeyDown={(e) => { if (e.key === 'Enter') handleApplyFilters(); }}
            style={{ 
              width: '100%', padding: '10px 40px', borderRadius: '8px', 
              border: '1px solid var(--border)', outline: 'none', fontSize: '14px' 
            }}
          />
          {search && (
            <button 
              onClick={() => { setSearch(''); setAppliedSearch(''); }}
              style={{ position: 'absolute', right: '12px', top: '50%', transform: 'translateY(-50%)', background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-light)' }}
            >
              <X size={16} />
            </button>
          )}
        </div>
        
        <div style={{ color: 'var(--text-light)', fontSize: '14px', marginLeft: 'auto' }}>
          {filteredData.length} resultados encontrados
        </div>
      </div>

      <div className="content-wrapper" style={{ padding: '0' }}>
          {loading ? (
            <p>Cargando consultas...</p>
          ) : (
          <div className="news-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '25px' }}>
            {filteredData.length === 0 ? (
              <p style={{ gridColumn: '1 / -1', textAlign: 'center' }}>No hay consultas para mostrar.</p>
            ) : (
              filteredData.map((item) => (
                <div key={item.id} className={`card ${item.is_new ? 'new-highlight' : ''}`} style={{ cursor: 'pointer', position: 'relative', height: '100%', display: 'flex', flexDirection: 'column' }} onClick={() => handleOpenModal(item)}>
                  {item.is_new && (
                    <div style={{ position: 'absolute', top: '10px', right: '10px', background: 'var(--primary)', color: 'white', padding: '2px 10px', borderRadius: '10px', fontSize: '0.7rem', fontWeight: 'bold', zIndex: 5 }}>
                      NUEVO
                    </div>
                  )}
                  <div className="card-content" style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                    <div style={{ 
                        width: '100%', 
                        height: '160px', 
                        background: '#f8fafc', 
                        borderRadius: '12px', 
                        display: 'flex', 
                        alignItems: 'center', 
                        justifyContent: 'center',
                        marginBottom: '15px',
                        fontSize: '4rem',
                        color: 'var(--primary)',
                        fontFamily: 'etmodules'
                    }}>
                      {(() => {
                        const nombre = item.nombre.toLowerCase();
                        if (nombre.includes('condiciones técnicas') && nombre.includes('obras hidráulicas')) {
                          return <Pencil size={64} />;
                        }
                        if (nombre.includes('declaración jurada') && (nombre.includes('bocatomas') || nombre.includes('cauces naturales'))) {
                          return <ClipboardList size={64} />;
                        }
                        return item.imagen && item.imagen.length === 1 ? item.imagen : <HelpCircle size={64} />;
                      })()}
                    </div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '10px', marginBottom: '15px', flex: 1 }}>
                      <div className="card-title" style={{ fontSize: '1rem', fontWeight: 600, margin: 0 }}>{item.nombre}</div>
                      <Heart 
                        size={20} 
                        onClick={(e) => toggleFavorite(e, item)}
                        style={{ 
                          cursor: 'pointer', 
                          flexShrink: 0,
                          fill: favorites.has(item.id) ? 'var(--orange)' : 'none', 
                          color: favorites.has(item.id) ? 'var(--orange)' : 'var(--text-light)',
                          transition: 'all 0.2s'
                        }} 
                      />
                    </div>
                    <div className="card-action" style={{ marginTop: 'auto', borderTop: '1px solid #f1f5f9', paddingTop: '15px', display: 'flex', alignItems: 'center', gap: '5px', color: 'var(--primary)', fontWeight: 600 }}>
                      <ExternalLink size={16} /> Ver detalles
                    </div>
                  </div>
                </div>
              ))
            )}
          </div>
        )}
      </div>
      

      {selectedItem && (
        <div className="modal-overlay" style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex', justifyContent: 'center', alignItems: 'center', zIndex: 1000, padding: '20px' }} onClick={() => setSelectedItem(null)}>
          <div className="modal-content" style={{ backgroundColor: 'white', borderRadius: '16px', padding: '40px', maxWidth: '500px', width: '100%', position: 'relative', boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.1)', textAlign: 'center' }} onClick={e => e.stopPropagation()}>
            <button onClick={() => setSelectedItem(null)} style={{ position: 'absolute', top: '20px', right: '20px', background: '#f1f5f9', border: 'none', cursor: 'pointer', width: '36px', height: '36px', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#64748b' }}>
              <X size={20} />
            </button>
            
            <div style={{ marginBottom: '25px', display: 'flex', justifyContent: 'center' }}>
              <div style={{ width: '80px', height: '80px', background: 'rgba(59, 130, 246, 0.1)', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--primary)' }}>
                <ExternalLink size={40} />
              </div>
            </div>

            <h3 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: '15px', color: '#1e293b' }}>
                {isGoogleForm(selectedItem.url) ? 'Formulario de Google' : 'Enlace Externo'}
            </h3>
            
            <div style={{ position: 'absolute', top: '20px', left: '20px' }}>
                <Heart 
                    size={24} 
                    onClick={(e) => toggleFavorite(e, selectedItem)}
                    style={{ 
                        cursor: 'pointer', 
                        fill: favorites.has(selectedItem.id) ? 'var(--orange)' : 'none', 
                        color: favorites.has(selectedItem.id) ? 'var(--orange)' : 'var(--text-light)',
                        transition: 'all 0.2s'
                    }} 
                />
            </div>
            
            <p style={{ color: '#64748b', marginBottom: '30px', lineHeight: '1.6' }}>
                {isGoogleForm(selectedItem.url) 
                    ? 'Esto te llevará a un formulario de Google para participar en esta consulta.' 
                    : 'Esto no es un formulario, te llevará al link asociado a esta consulta.'}
            </p>
            
            <a 
                href={selectedItem.url} 
                target="_blank" 
                rel="noopener noreferrer"
                className="btn-primary"
                style={{ 
                    display: 'inline-flex', 
                    alignItems: 'center', 
                    gap: '10px', 
                    padding: '12px 30px', 
                    borderRadius: '12px',
                    textDecoration: 'none',
                    fontWeight: 600,
                    width: '100%',
                    justifyContent: 'center'
                }}
            >
                Ir al {isGoogleForm(selectedItem.url) ? 'formulario' : 'enlace'}
            </a>
          </div>
        </div>
      )}
    </div>
  );
};

export default DGAConsultasPage;
