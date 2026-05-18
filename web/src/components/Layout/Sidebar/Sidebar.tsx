import { useState, useEffect, useRef } from 'react';
import { NavLink, Link, useNavigate } from 'react-router-dom';
import {
  Home, Heart, Newspaper,
  CalendarCheck, UserSquare2,
  UserSearch, MoreHorizontal, Gavel,
  FileCheck, Edit3, LogIn, Scale,
  ChevronDown, ChevronUp, Menu,
  BookOpen, Leaf, Search,
  User, LogOut, Settings
} from 'lucide-react';
import { useAuth } from '../../../context/AuthContext';
import { useNotifications } from '../../../context/NotificationsContext';
import styles from './Sidebar.module.css';

const Sidebar = () => {
  const [collapsed, setCollapsed] = useState(false);
  const [userMenuOpen, setUserMenuOpen] = useState(false);

  const navigate = useNavigate();
  const { user, logout } = useAuth();
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

  const Dot = ({ show }: { show?: boolean }) =>
    show ? <div className={styles.notifDot} /> : null;

  const [openSections, setOpenSections] = useState({
    diario: true,
    sea: true,
    sma: true,
    tribunales: true,
    consultas: true
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
    <aside ref={sidebarRef} className={`${styles.sidebar} ${collapsed ? styles.collapsed : ''}`}>
      <div className={styles.sidebarHeader}>
        <button className={styles.burgerMenuBtn} onClick={() => setCollapsed(!collapsed)}>
          <Menu size={24} color="var(--primary)" />
        </button>

        <Link
          to="/"
          className={styles.sidebarLogoText}
          style={{ display: (collapsed && window.innerWidth > 768) ? 'none' : 'flex' }}
        >
          <span className={styles.logoBio}>Bio</span>
          {(window.innerWidth <= 768 || !collapsed) && <span className={styles.logoNews}>News</span>}
        </Link>

        {/* Mobile Session Icon */}
        <div className="mobile-only" style={{ position: 'relative' }}>
          <div
            onClick={() => setUserMenuOpen(!userMenuOpen)}
            className={styles.sessionAvatar}
          >
            {user?.name?.charAt(0)?.toUpperCase()}
          </div>
          {userMenuOpen && (
            <div className={styles.mobileMenuDropdown}>
              <div className={styles.mobileMenuDropdownHeader}>{user?.name}</div>
              {user?.role === 'admin' && (
                <button
                  className={styles.mobileMenuDropdownItem}
                  onClick={() => { setUserMenuOpen(false); setCollapsed(true); navigate('/admin'); }}
                >
                  <Settings size={14} /> Panel de Admin
                </button>
              )}
              <button
                className={styles.mobileMenuDropdownItem}
                onClick={() => { setUserMenuOpen(false); setCollapsed(true); navigate('/perfil'); }}
              >
                <User size={14} /> Perfil
              </button>
              <button
                className={styles.mobileMenuDropdownItemDanger}
                onClick={() => { logout(); navigate('/'); }}
              >
                <LogOut size={14} /> Cerrar Sesión
              </button>
            </div>
          )}
        </div>
      </div>

      <div className={styles.sidebarMenu}>
        <NavLink onClick={handleMobileClose} to="/" className={({ isActive }) => `${styles.menuItem} ${isActive ? styles.active : ''}`} title="Home">
          <Home size={20} className="icon" />
          {!collapsed && <span>Home</span>}
        </NavLink>

        <NavLink onClick={handleMobileClose} to="/noticias" className={({ isActive }) => `${styles.menuItem} ${isActive ? styles.active : ''}`} title="Noticias">
          <Newspaper size={20} className="icon" />
          {!collapsed && <span>Noticias</span>}
          {!collapsed && <Dot show={categoryStatus.noticias} />}
        </NavLink>

        <NavLink onClick={handleMobileClose} to="/favoritos" className={({ isActive }) => `${styles.menuItem} ${isActive ? styles.active : ''}`} title="Mis Favoritos">
          <Heart size={20} className="icon" />
          {!collapsed && <span>Mis Favoritos</span>}
        </NavLink>

        {/* Diario Oficial */}
        <div className={styles.menuCategory} onClick={() => toggleSection('diario')} title="Diario Oficial">
          {!collapsed ? <span>Diario Oficial</span> : <BookOpen size={20} className="icon" />}
          {!collapsed && (openSections.diario ? <ChevronUp size={16} /> : <ChevronDown size={16} />)}
        </div>
        {(!collapsed && openSections.diario) && (
          <ul className={styles.submenu}>
            <NavLink onClick={handleMobileClose} to="/normativas" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="Normativas">
              <CalendarCheck size={18} /> {!collapsed && "Normativas"}
              {!collapsed && <Dot show={categoryStatus.normativas} />}
            </NavLink>
          </ul>
        )}

        {/* SEA */}
        <div className={styles.menuCategory} onClick={() => toggleSection('sea')} title="SEA">
          {!collapsed ? <span>SEA</span> : <Leaf size={20} className="icon" />}
          {!collapsed && (openSections.sea ? <ChevronUp size={16} /> : <ChevronDown size={16} />)}
        </div>
        {(!collapsed && openSections.sea) && (
          <ul className={styles.submenu}>
            <NavLink onClick={handleMobileClose} to="/pertinencias" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="Pertinencias">
              <UserSquare2 size={18} /> {!collapsed && "Pertinencias"}
              {!collapsed && <Dot show={categoryStatus.pertinencias} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/sea-evaluados" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="Proyectos Evaluados">
              <FileCheck size={18} /> {!collapsed && "Proyectos Evaluados"}
              {!collapsed && <Dot show={categoryStatus.sea_proyectos_evaluados} />}
            </NavLink>
          </ul>
        )}

        {/* SMA */}
        <div className={styles.menuCategory} onClick={() => toggleSection('sma')} title="SMA">
          {!collapsed ? <span>SMA</span> : <Search size={20} className="icon" />}
          {!collapsed && (openSections.sma ? <ChevronUp size={16} /> : <ChevronDown size={16} />)}
        </div>
        {(!collapsed && openSections.sma) && (
          <ul className={styles.submenu}>
            <NavLink onClick={handleMobileClose} to="/fiscalizaciones" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="Fiscalizaciones">
              <UserSearch size={18} /> {!collapsed && "Fiscalizaciones"}
              {!collapsed && <Dot show={categoryStatus.fiscalizaciones} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/sancionatorios" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="Sancionatorios">
              <MoreHorizontal size={18} /> {!collapsed && "Sancionatorios"}
              {!collapsed && <Dot show={categoryStatus.sancionatorios} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/sanciones" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="Sanciones">
              <Gavel size={18} /> {!collapsed && "Sanciones"}
              {!collapsed && <Dot show={categoryStatus.registroSanciones} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/programas" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="Programas de cumplimiento">
              <FileCheck size={18} /> {!collapsed && "Programas"}
              {!collapsed && <Dot show={categoryStatus.programasDeCumplimiento} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/medidas" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="Medidas provisionales">
              <Edit3 size={18} /> {!collapsed && "Medidas"}
              {!collapsed && <Dot show={categoryStatus.medidas_provisionales} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/requerimientos" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="Requerimientos de ingreso">
              <LogIn size={18} /> {!collapsed && "Requerimientos"}
              {!collapsed && <Dot show={categoryStatus.requerimientos} />}
            </NavLink>
          </ul>
        )}

        {/* Tribunales */}
        <div className={styles.menuCategory} onClick={() => toggleSection('tribunales')} title="Tribunales ambientales">
          {!collapsed ? <span>Tribunales ambientales</span> : <Scale size={20} className="icon" />}
          {!collapsed && (openSections.tribunales ? <ChevronUp size={16} /> : <ChevronDown size={16} />)}
        </div>
        {(!collapsed && openSections.tribunales) && (
          <ul className={styles.submenu}>
            <NavLink onClick={handleMobileClose} to="/tribunales" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="Tribunales Ambientales">
              <Scale size={18} /> {!collapsed && "Tribunales"}
              {!collapsed && <Dot show={categoryStatus.Tribunales} />}
            </NavLink>
          </ul>
        )}

        {/* Consultas Públicas */}
        <div className={styles.menuCategory} onClick={() => toggleSection('consultas')} title="Consultas Públicas">
          {!collapsed ? <span>Consultas Públicas</span> : <UserSearch size={20} className="icon" />}
          {!collapsed && (openSections.consultas ? <ChevronUp size={16} /> : <ChevronDown size={16} />)}
        </div>
        {(!collapsed && openSections.consultas) && (
          <ul className={styles.submenu}>
            <NavLink onClick={handleMobileClose} to="/consultas/minsal" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="MINSAL">
              <CalendarCheck size={18} /> {!collapsed && "MINSAL"}
              {!collapsed && <Dot show={categoryStatus.minsal_vigentes || categoryStatus.minsal_resultados} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/consultas/dga" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="DGA">
              <Leaf size={18} /> {!collapsed && "DGA"}
              {!collapsed && <Dot show={categoryStatus.dga} />}
            </NavLink>
            <NavLink onClick={handleMobileClose} to="/consultas/mma" className={({ isActive }) => `${styles.submenuItem} ${isActive ? styles.active : ''}`} title="MMA">
              <Leaf size={18} /> {!collapsed && "MMA"}
              {!collapsed && <Dot show={categoryStatus.mma} />}
            </NavLink>
          </ul>
        )}
      </div>
    </aside>
  );
};

export default Sidebar;
