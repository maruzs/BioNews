import { useState, useEffect } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { 
  Home, Heart, Newspaper,
  CalendarCheck, UserSquare2,
  UserSearch, MoreHorizontal, Gavel, 
  FileCheck, Edit3, LogIn, Scale, 
  ChevronDown, ChevronUp, Menu
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';

const Sidebar = () => {
  const [collapsed, setCollapsed] = useState(false);
  const [updates, setUpdates] = useState<Record<string, boolean>>({});
  const location = useLocation();
  const { token } = useAuth();
  
  useEffect(() => {
    if (!token) return;
    fetch('/api/logs', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(res => res.json())
      .then((data: any[]) => {
        const hasUpdates = (fuenteKeys: string[]) => {
          return data.some(log => fuenteKeys.includes(log.fuente) && log.nuevos_registros > 0);
        };
        
        // Simplified mapping based on scraper names in backend
        setUpdates({
          noticias: data.some(log => (log.fuente.includes('Noticias') || log.fuente === 'MMA' || log.fuente === 'SMA' || log.fuente === 'Corte Suprema' || log.fuente === 'Sernageomin' || log.fuente === 'SBAP') && log.nuevos_registros > 0),
          normativas: hasUpdates(['Diario Oficial (Normativas)']),
          pertinencias: hasUpdates(['Pertinencias SEA']),
          fiscalizaciones: hasUpdates(['SNIFA Fiscalizaciones']),
          sancionatorios: hasUpdates(['SNIFA Sancionatorios']),
          sanciones: hasUpdates(['SNIFA Registro Sanciones']),
          programas: hasUpdates(['SNIFA Programas de Cumplimiento']),
          medidas: hasUpdates(['SNIFA Medidas Provisionales']),
          requerimientos: hasUpdates(['SNIFA Requerimientos']),
          tribunales: hasUpdates(['Primer Tribunal Ambiental', 'Segundo Tribunal Ambiental', 'Tercer Tribunal Ambiental'])
        });
      })
      .catch(() => {});
  }, []);

  useEffect(() => {
    // Clear red dot if path matches
    const path = location.pathname;
    setUpdates(prev => {
      const next = { ...prev };
      if (path === '/noticias') next.noticias = false;
      if (path === '/normativas') next.normativas = false;
      if (path === '/pertinencias') next.pertinencias = false;
      if (path === '/fiscalizaciones') next.fiscalizaciones = false;
      if (path === '/sancionatorios') next.sancionatorios = false;
      if (path === '/sanciones') next.sanciones = false;
      if (path === '/programas') next.programas = false;
      if (path === '/medidas') next.medidas = false;
      if (path === '/requerimientos') next.requerimientos = false;
      if (path === '/tribunales') next.tribunales = false;
      return next;
    });
  }, [location.pathname]);

  const handleMobileClose = () => {
    if (window.innerWidth <= 768) {
      setCollapsed(true);
    }
  };

  const Dot = ({ show }: { show?: boolean }) => show ? <div style={{width: 6, height: 6, borderRadius: '50%', backgroundColor: '#ef4444', marginLeft: 'auto'}} /> : null;
  const [openSections, setOpenSections] = useState({
    diario: true,
    sea: true,
    sma: true,
    tribunales: true
  });

  const toggleSection = (section: keyof typeof openSections) => {
    if (collapsed) {
      setCollapsed(false);
      setOpenSections(prev => ({ ...prev, [section]: true }));
    } else {
      setOpenSections(prev => ({ ...prev, [section]: !prev[section] }));
    }
  };

  return (
    <aside className={`sidebar ${collapsed ? 'collapsed' : ''}`}>
      <div className="sidebar-header">
        {!collapsed && (
          <div className="sidebar-logo-text">
            <span className="logo-bio">Bio</span><span className="logo-news">News</span>
          </div>
        )}
        <button className="burger-menu-btn" onClick={() => setCollapsed(!collapsed)}>
          <Menu size={24} color="var(--primary)" />
        </button>
      </div>
      <div className="sidebar-menu">
        <NavLink onClick={handleMobileClose} to="/" className={({isActive}) => `menu-item ${isActive ? 'active' : ''}`} title="Home">
          <Home size={20} className="icon" />
          {!collapsed && <span>Home</span>}
        </NavLink>
        
        <NavLink onClick={handleMobileClose} to="/noticias" className={({isActive}) => `menu-item ${isActive ? 'active' : ''}`} title="Noticias">
          <Newspaper size={20} className="icon" />
          {!collapsed && <span>Noticias</span>}
          {!collapsed && <Dot show={updates.noticias} />}
        </NavLink>
        
        <NavLink onClick={handleMobileClose} to="/favoritos" className={({isActive}) => `menu-item ${isActive ? 'active' : ''}`} title="Mis Favoritos">
          <Heart size={20} className="icon" />
          {!collapsed && <span>Mis Favoritos</span>}
        </NavLink>

        {/* Diario Oficial */}
        <div className="menu-category" onClick={() => toggleSection('diario')} title="Diario Oficial">
          {!collapsed ? <span>Diario Oficial</span> : <span className="cat-icon">🏛️</span>}
          {!collapsed && (openSections.diario ? <ChevronUp size={16} /> : <ChevronDown size={16} />)}
        </div>
        {(!collapsed && openSections.diario) && (
          <ul className="submenu">
            <NavLink onClick={handleMobileClose} to="/normativas" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Normativas">
              <CalendarCheck size={18} /> {!collapsed && "Normativas"}
              {!collapsed && <Dot show={updates.normativas} />}
            </NavLink>
          </ul>
        )}

        {/* SEA */}
        <div className="menu-category" onClick={() => toggleSection('sea')} title="SEA">
          {!collapsed ? <span>SEA</span> : <span className="cat-icon">🌱</span>}
          {!collapsed && (openSections.sea ? <ChevronUp size={16} /> : <ChevronDown size={16} />)}
        </div>
        {(!collapsed && openSections.sea) && (
          <ul className="submenu">
            <NavLink onClick={handleMobileClose} to="/pertinencias" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Pertinencias">
              <UserSquare2 size={18} /> {!collapsed && "Pertinencias"}
              {!collapsed && <Dot show={updates.pertinencias} />}
            </NavLink>
          </ul>
        )}

        {/* SMA */}
        <div className="menu-category" onClick={() => toggleSection('sma')} title="SMA">
          {!collapsed ? <span>SMA</span> : <span className="cat-icon">🔍</span>}
          {!collapsed && (openSections.sma ? <ChevronUp size={16} /> : <ChevronDown size={16} />)}
        </div>
        {(!collapsed && openSections.sma) && (
          <ul className="submenu">
            <NavLink onClick={handleMobileClose} to="/fiscalizaciones" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Fiscalizaciones">
              <UserSearch size={18} /> {!collapsed && "Fiscalizaciones"}
              {!collapsed && <Dot show={updates.fiscalizaciones} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/sancionatorios" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Sancionatorios">
              <MoreHorizontal size={18} /> {!collapsed && "Sancionatorios"}
              {!collapsed && <Dot show={updates.sancionatorios} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/sanciones" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Sanciones">
              <Gavel size={18} /> {!collapsed && "Sanciones"}
              {!collapsed && <Dot show={updates.sanciones} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/programas" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Programas de cumplimiento">
              <FileCheck size={18} /> {!collapsed && "Programas"}
              {!collapsed && <Dot show={updates.programas} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/medidas" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Medidas provisionales">
              <Edit3 size={18} /> {!collapsed && "Medidas"}
              {!collapsed && <Dot show={updates.medidas} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/requerimientos" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Requerimientos de ingreso">
              <LogIn size={18} /> {!collapsed && "Requerimientos"}
              {!collapsed && <Dot show={updates.requerimientos} />}
            </NavLink>
          </ul>
        )}

        {/* Tribunales */}
        <div className="menu-category" onClick={() => toggleSection('tribunales')} title="Tribunales ambientales">
          {!collapsed ? <span>Tribunales ambientales</span> : <span className="cat-icon">⚖️</span>}
          {!collapsed && (openSections.tribunales ? <ChevronUp size={16} /> : <ChevronDown size={16} />)}
        </div>
        {(!collapsed && openSections.tribunales) && (
          <ul className="submenu">
            <NavLink onClick={handleMobileClose} to="/tribunales" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Tribunales Ambientales">
              <Scale size={18} /> {!collapsed && "Tribunales"}
              {!collapsed && <Dot show={updates.tribunales} />}
            </NavLink>
          </ul>
        )}
      </div>
    </aside>
  );
};

export default Sidebar;
