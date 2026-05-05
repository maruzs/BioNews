import { useState, useEffect } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { 
  Home, Heart, Newspaper,
  CalendarCheck, UserSquare2,
  UserSearch, MoreHorizontal, Gavel, 
  FileCheck, Edit3, LogIn, Scale, 
  ChevronDown, ChevronUp, Menu,
  BookOpen, Leaf, Search
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';

const Sidebar = () => {
  const [collapsed, setCollapsed] = useState(false);
  const [updates, setUpdates] = useState<Record<string, boolean>>({});
  const location = useLocation();
  const { token } = useAuth();
  
  const checkUpdates = (data: any[]) => {
    const hasUpdates = (fuenteKeys: string[], category: string) => {
      const categoryLogs = data.filter(log => fuenteKeys.includes(log.fuente) && log.nuevos_registros > 0);
      if (categoryLogs.length === 0) return false;
      
      const lastRead = localStorage.getItem(`read_${category}`);
      if (!lastRead) return true;

      // Check if any log's ultimo_exito is newer than lastRead
      return categoryLogs.some(log => new Date(log.ultimo_exito) > new Date(lastRead));
    };

    const newsLogs = data.filter(log => (log.fuente.includes('Noticias') || log.fuente === 'MMA' || log.fuente === 'SMA' || log.fuente === 'Corte Suprema' || log.fuente === 'Sernageomin' || log.fuente === 'SBAP') && log.nuevos_registros > 0);
    const lastReadNews = localStorage.getItem('read_noticias');
    const newsHasUpdate = newsLogs.length > 0 && (!lastReadNews || newsLogs.some(log => new Date(log.ultimo_exito) > new Date(lastReadNews)));

    setUpdates({
      noticias: newsHasUpdate,
      normativas: hasUpdates(['Diario Oficial (Normativas)'], 'normativas'),
      pertinencias: hasUpdates(['Pertinencias SEA'], 'pertinencias'),
      fiscalizaciones: hasUpdates(['SNIFA Fiscalizaciones'], 'fiscalizaciones'),
      sancionatorios: hasUpdates(['SNIFA Sancionatorios'], 'sancionatorios'),
      sanciones: hasUpdates(['SNIFA Registro Sanciones'], 'sanciones'),
      programas: hasUpdates(['SNIFA Programas de Cumplimiento'], 'programas'),
      medidas: hasUpdates(['SNIFA Medidas Provisionales'], 'medidas'),
      requerimientos: hasUpdates(['SNIFA Requerimientos'], 'requerimientos'),
      tribunales: hasUpdates(['Primer Tribunal Ambiental', 'Segundo Tribunal Ambiental', 'Tercer Tribunal Ambiental'], 'tribunales')
    });
  };

  useEffect(() => {
    if (!token) return;
    fetch('/api/logs', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(res => res.json())
      .then(checkUpdates)
      .catch(() => {});
  }, [token]);

  useEffect(() => {
    // Clear red dot if path matches and save to localStorage
    const path = location.pathname;
    const now = new Date().toISOString();
    
    setUpdates(prev => {
      const next = { ...prev };
      const markRead = (key: string) => {
        next[key] = false;
        localStorage.setItem(`read_${key}`, now);
      };

      if (path === '/noticias') markRead('noticias');
      if (path === '/normativas') markRead('normativas');
      if (path === '/pertinencias') markRead('pertinencias');
      if (path === '/fiscalizaciones') markRead('fiscalizaciones');
      if (path === '/sancionatorios') markRead('sancionatorios');
      if (path === '/sanciones') markRead('sanciones');
      if (path === '/programas') markRead('programas');
      if (path === '/medidas') markRead('medidas');
      if (path === '/requerimientos') markRead('requerimientos');
      if (path === '/tribunales') markRead('tribunales');
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
          {!collapsed ? <span>Diario Oficial</span> : <BookOpen size={20} className="icon" />}
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
          {!collapsed ? <span>SEA</span> : <Leaf size={20} className="icon" />}
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
          {!collapsed ? <span>SMA</span> : <Search size={20} className="icon" />}
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
          {!collapsed ? <span>Tribunales ambientales</span> : <Scale size={20} className="icon" />}
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
