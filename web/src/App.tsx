import { BrowserRouter, Routes, Route, Navigate, useNavigate } from 'react-router-dom';
import { useState, useEffect, useRef } from 'react';
import Sidebar from './components/Sidebar';
import NewsPage from './components/NewsPage';
import ReportLayout from './components/ReportLayout';
import Home from './components/Home';
import Landing from './components/Landing';
import Login from './components/Login';
import Register from './components/Register';
import AdminPanel from './components/AdminPanel';
import Profile from './components/Profile';
import { AuthProvider, useAuth } from './context/AuthContext';
import { NotificationsProvider } from './context/NotificationsContext';

function ProtectedLayout() {
  const { user, logout } = useAuth();
  const [dropdownOpen, setDropdownOpen] = useState(false);
  const navigate = useNavigate();
  const dropdownRef = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setDropdownOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  if (!user) return <Navigate to="/" />;

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <div className="app-container">
      <Sidebar />
      <main className="main-content">
        <div className="top-header">
          <div className="top-header-spacer"></div>
          <div className="top-header-actions" style={{ position: 'relative' }} ref={dropdownRef}>
            <div 
              style={{ display: 'flex', alignItems: 'center', gap: '10px', cursor: 'pointer', background: 'white', padding: '5px 15px', borderRadius: '30px', border: '1px solid var(--border)' }}
              onClick={() => setDropdownOpen(!dropdownOpen)}
            >
              <div style={{ width: '30px', height: '30px', borderRadius: '50%', backgroundColor: 'var(--primary)', color: 'white', display: 'flex', alignItems: 'center', justifyContent: 'center', fontWeight: 'bold' }}>
                {user.name.charAt(0).toUpperCase()}
              </div>
              <span style={{ fontWeight: 500, color: 'var(--text-dark)' }}>{user.name}</span>
            </div>
            {dropdownOpen && (
              <div style={{ position: 'absolute', top: '100%', right: 0, marginTop: '10px', background: 'white', border: '1px solid var(--border)', borderRadius: '8px', boxShadow: '0 4px 12px rgba(0,0,0,0.1)', width: '200px', zIndex: 100 }}>
                {user.role === 'admin' && (
                  <div style={{ padding: '10px 15px', cursor: 'pointer', borderBottom: '1px solid var(--border)', color: 'var(--text-dark)' }} onClick={() => { setDropdownOpen(false); navigate('/admin'); }}>Panel de Admin</div>
                )}
                <div style={{ padding: '10px 15px', cursor: 'pointer', borderBottom: '1px solid var(--border)', color: 'var(--text-dark)' }} onClick={() => { setDropdownOpen(false); navigate('/perfil'); }}>Perfil y Preferencias</div>
                <div style={{ padding: '10px 15px', cursor: 'pointer', color: '#ef4444' }} onClick={handleLogout}>Cerrar Sesión</div>
              </div>
            )}
          </div>
        </div>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/noticias" element={<NewsPage />} />
          <Route path="/favoritos" element={<ReportLayout key="favoritos" title="Favoritos" description="Tus normativas y proyectos guardados." listTitle="Favoritos" isFavoritesPage={true} />} />
          
          {/* Diario Oficial */}
          <Route path="/normativas" element={<ReportLayout key="normativas" title="Normativas" description="Visualización de normativas publicadas en el Diario Oficial." listTitle="Normativas" tableName="normativas" category="normativas" />} />
          
          {/* SEA */}
          <Route path="/pertinencias" element={<ReportLayout key="pertinencias" title="Pertinencias" description="Reporte de pertinencias ingresadas al SEA." listTitle="Pertinencias" tableName="pertinencias" category="pertinencias" />} />

          {/* SMA */}
          <Route path="/fiscalizaciones" element={<ReportLayout key="fiscalizaciones" title="Fiscalizaciones" description="Reporte de fiscalizaciones realizadas por la SMA." listTitle="Fiscalizaciones" tableName="fiscalizaciones" category="fiscalizaciones" />} />
          <Route path="/sancionatorios" element={<ReportLayout key="sancionatorios" title="Sancionatorios" description="Reporte de procesos sancionatorios de la SMA." listTitle="Sancionatorios" tableName="sancionatorios" category="sancionatorios" />} />
          <Route path="/sanciones" element={<ReportLayout key="sanciones" title="Sanciones" description="Registro público de sanciones emitidas." listTitle="Sanciones" tableName="registroSanciones" category="registroSanciones" />} />
          <Route path="/programas" element={<ReportLayout key="programas" title="Programas de Cumplimiento" description="Reporte de programas de cumplimiento (PdC)." listTitle="Programas" tableName="programasDeCumplimiento" category="programasDeCumplimiento" />} />
          <Route path="/medidas" element={<ReportLayout key="medidas" title="Medidas Provisionales" description="Reporte de medidas provisionales dictadas." listTitle="Medidas" tableName="medidas_provisionales" category="medidas_provisionales" />} />
          <Route path="/requerimientos" element={<ReportLayout key="requerimientos" title="Requerimientos de Ingreso" description="Reporte de requerimientos de ingreso." listTitle="Requerimientos" tableName="requerimientos" category="requerimientos" />} />

          {/* Tribunales */}
          <Route path="/tribunales" element={<ReportLayout key="tribunales" title="Tribunales Ambientales" description="Reporte de causas en los Tribunales Ambientales." listTitle="Causas" tableName="Tribunales" category="Tribunales" />} />
          
          {/* Admin Panel */}
          <Route path="/admin" element={<AdminPanel />} />
          
          {/* Profile */}
          <Route path="/perfil" element={<Profile />} />
        </Routes>
      </main>
    </div>
  );
}

function AppRoutes() {
  const { user, loading } = useAuth();
  
  if (loading) return <div style={{display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh'}}>Cargando...</div>;

  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
      <Route path="/*" element={user ? <ProtectedLayout /> : <Landing />} />
    </Routes>
  );
}

function App() {
  return (
    <AuthProvider>
      <NotificationsProvider>
        <BrowserRouter>
          <AppRoutes />
        </BrowserRouter>
      </NotificationsProvider>
    </AuthProvider>
  );
}

export default App;
