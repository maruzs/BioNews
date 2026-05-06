import { useState, useEffect, useRef } from 'react';
import { NavLink, useLocation, Link, useNavigate } from 'react-router-dom';
import { 
  Home, Heart, Newspaper,
  CalendarCheck, UserSquare2,
  UserSearch, MoreHorizontal, Gavel, 
  FileCheck, Edit3, LogIn, Scale, 
  ChevronDown, ChevronUp, Menu,
  BookOpen, Leaf, Search,
  User, LogOut, Settings
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';

const Sidebar = () => {
  const [collapsed, setCollapsed] = useState(false);
  const [userMenuOpen, setUserMenuOpen] = useState(false);
  const location = useLocation();
  const navigate = useNavigate();
  const { token, user, logout } = useAuth();
  const { categoryStatus } = useNotifications();
  const sidebarRef = useRef<HTMLDivElement>(null);
  
  // Click outside to close
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (window.innerWidth <= 768 && sidebarRef.current && !sidebarRef.current.contains(event.target as Node)) {
        setCollapsed(true);
        setUserMenuOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

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
    <aside ref={sidebarRef} className={`sidebar ${collapsed ? 'collapsed' : ''}`}>
      <div className="sidebar-header">
        <button className="burger-menu-btn" onClick={() => setCollapsed(!collapsed)}>
          <Menu size={24} color="var(--primary)" />
        </button>
        
        <Link to="/" className="sidebar-logo-text" style={{ textDecoration: 'none', display: (collapsed && window.innerWidth > 768) ? 'none' : 'flex' }}>
          <span className="logo-bio">Bio</span>
          {(window.innerWidth <= 768 || !collapsed) && <span className="logo-news">News</span>}
        </Link>

        {/* Mobile Session Icon */}
        <div className="mobile-only" style={{ position: 'relative' }}>
          <div 
            onClick={() => setUserMenuOpen(!userMenuOpen)}
            style={{ 
              width: '32px', height: '32px', borderRadius: '50%', 
              backgroundColor: 'var(--primary)', color: 'white', 
              display: 'flex', alignItems: 'center', justifyContent: 'center', 
              fontWeight: 'bold', cursor: 'pointer' 
            }}
          >
            {user?.name?.charAt(0).toUpperCase()}
          </div>
          {userMenuOpen && (
            <div style={{ 
              position: 'absolute', top: '100%', right: 0, marginTop: '10px', 
              background: 'white', border: '1px solid var(--border)', 
              borderRadius: '8px', boxShadow: '0 4px 12px rgba(0,0,0,0.1)', 
              width: '180px', zIndex: 100 
            }}>
              <div style={{ padding: '10px 15px', fontSize: '14px', borderBottom: '1px solid var(--border)', fontWeight: 600 }}>{user?.name}</div>
              {user?.role === 'admin' && (
                <div 
                  style={{ padding: '10px 15px', cursor: 'pointer', fontSize: '14px', display: 'flex', alignItems: 'center', gap: '8px', borderBottom: '1px solid var(--border)' }} 
                  onClick={() => { setUserMenuOpen(false); setCollapsed(true); navigate('/admin'); }}
                >
                  <Settings size={14} /> Panel de Admin
                </div>
              )}
              <div 
                style={{ padding: '10px 15px', cursor: 'pointer', fontSize: '14px', display: 'flex', alignItems: 'center', gap: '8px' }} 
                onClick={() => { setUserMenuOpen(false); setCollapsed(true); navigate('/perfil'); }}
              >
                <User size={14} /> Perfil
              </div>
              <div 
                style={{ padding: '10px 15px', cursor: 'pointer', fontSize: '14px', color: '#ef4444', display: 'flex', alignItems: 'center', gap: '8px' }} 
                onClick={() => { logout(); navigate('/'); }}
              >
                <LogOut size={14} /> Cerrar Sesión
              </div>
            </div>
          )}
        </div>
      </div>
      <div className="sidebar-menu">
        <NavLink onClick={handleMobileClose} to="/" className={({isActive}) => `menu-item ${isActive ? 'active' : ''}`} title="Home">
          <Home size={20} className="icon" />
          {!collapsed && <span>Home</span>}
        </NavLink>
        
        <NavLink onClick={handleMobileClose} to="/noticias" className={({isActive}) => `menu-item ${isActive ? 'active' : ''}`} title="Noticias">
          <Newspaper size={20} className="icon" />
          {!collapsed && <span>Noticias</span>}
          {!collapsed && <Dot show={categoryStatus.noticias} />}
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
              {!collapsed && <Dot show={categoryStatus.normativas} />}
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
              {!collapsed && <Dot show={categoryStatus.pertinencias} />}
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
              {!collapsed && <Dot show={categoryStatus.fiscalizaciones} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/sancionatorios" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Sancionatorios">
              <MoreHorizontal size={18} /> {!collapsed && "Sancionatorios"}
              {!collapsed && <Dot show={categoryStatus.sancionatorios} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/sanciones" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Sanciones">
              <Gavel size={18} /> {!collapsed && "Sanciones"}
              {!collapsed && <Dot show={categoryStatus.registroSanciones} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/programas" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Programas de cumplimiento">
              <FileCheck size={18} /> {!collapsed && "Programas"}
              {!collapsed && <Dot show={categoryStatus.programasDeCumplimiento} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/medidas" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Medidas provisionales">
              <Edit3 size={18} /> {!collapsed && "Medidas"}
              {!collapsed && <Dot show={categoryStatus.medidas_provisionales} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/requerimientos" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`} title="Requerimientos de ingreso">
              <LogIn size={18} /> {!collapsed && "Requerimientos"}
              {!collapsed && <Dot show={categoryStatus.requerimientos} />}
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
              {!collapsed && <Dot show={categoryStatus.Tribunales} />}
            </NavLink>
          </ul>
        )}
      </div>
    </aside>
  );
};

export default Sidebar;
