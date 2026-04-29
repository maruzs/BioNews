import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { 
  Home, Heart, Newspaper,
  CalendarCheck, Eye, UserSquare2, Users, 
  UserSearch, MoreHorizontal, Gavel, Sprout, 
  FileCheck, Edit3, LogIn, Scale, 
  ChevronDown, ChevronUp, User
} from 'lucide-react';

const Sidebar = () => {
  const [openSections, setOpenSections] = useState({
    diario: true,
    sea: true,
    sma: true,
    tribunales: true
  });

  const toggleSection = (section: keyof typeof openSections) => {
    setOpenSections(prev => ({ ...prev, [section]: !prev[section] }));
  };

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <div className="sidebar-logo-text">
          <span className="logo-bio">Bio</span><span className="logo-news">News</span>
        </div>
      </div>
      <div className="sidebar-menu">
        <NavLink to="/" className={({isActive}) => `menu-item ${isActive ? 'active' : ''}`}>
          <Home size={20} className="icon" />
          <span>Home</span>
        </NavLink>
        
        <NavLink to="/noticias" className={({isActive}) => `menu-item ${isActive ? 'active' : ''}`}>
          <Newspaper size={20} className="icon" />
          <span>Noticias</span>
        </NavLink>
        
        <NavLink to="/favoritos" className={({isActive}) => `menu-item ${isActive ? 'active' : ''}`}>
          <Heart size={20} className="icon" />
          <span>Mis Favoritos</span>
        </NavLink>

        {/* Diario Oficial */}
        <div className="menu-category" onClick={() => toggleSection('diario')}>
          <span>Diario Oficial</span>
          {openSections.diario ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
        </div>
        {openSections.diario && (
          <ul className="submenu">
            <NavLink to="/normativas" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`}>
              <CalendarCheck size={18} /> Normativas
            </NavLink>
          </ul>
        )}

        {/* SEA */}
        <div className="menu-category" onClick={() => toggleSection('sea')}>
          <span>SEA</span>
          {openSections.sea ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
        </div>
        {openSections.sea && (
          <ul className="submenu">
            <NavLink to="/proyectos-evaluados" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`}>
              <Eye size={18} /> Proyectos Evaluados
            </NavLink>
            <NavLink to="/pertinencias" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`}>
              <UserSquare2 size={18} /> Pertinencias
            </NavLink>
            <NavLink to="/participacion" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`}>
              <Users size={18} /> Participación Ciudadana
            </NavLink>
          </ul>
        )}

        {/* SMA */}
        <div className="menu-category" onClick={() => toggleSection('sma')}>
          <span>SMA</span>
          {openSections.sma ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
        </div>
        {openSections.sma && (
          <ul className="submenu">
            <NavLink to="/fiscalizaciones" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`}>
              <UserSearch size={18} /> Fiscalizaciones
            </NavLink>
            <NavLink to="/sancionatorios" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`}>
              <MoreHorizontal size={18} /> Sancionatorios
            </NavLink>
            <NavLink to="/sanciones" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`}>
              <Gavel size={18} /> Sanciones
            </NavLink>
            <NavLink to="/seguimiento" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`}>
              <Sprout size={18} /> Seguimiento ambiental
            </NavLink>
            <NavLink to="/programas" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`}>
              <FileCheck size={18} /> Programas de cumplimiento
            </NavLink>
            <NavLink to="/medidas" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`}>
              <Edit3 size={18} /> Medidas provisionales
            </NavLink>
            <NavLink to="/requerimientos" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`}>
              <LogIn size={18} /> Requerimientos de ingreso
            </NavLink>
          </ul>
        )}

        {/* Tribunales */}
        <div className="menu-category" onClick={() => toggleSection('tribunales')}>
          <span>Tribunales ambientales</span>
          {openSections.tribunales ? <ChevronUp size={16} /> : <ChevronDown size={16} />}
        </div>
        {openSections.tribunales && (
          <ul className="submenu">
            <NavLink to="/tribunales" className={({isActive}) => `submenu-item ${isActive ? 'active' : ''}`}>
              <Scale size={18} /> Tribunales Ambientales
            </NavLink>
          </ul>
        )}
      </div>

      <div className="sidebar-footer">
        <div className="profile-pic">
          <User size={20} />
        </div>
        <div className="profile-info">
          <span className="profile-name">Iniciar Sesión</span>
          <span className="profile-role">Ingresar a tu cuenta</span>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
