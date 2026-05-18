import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Sidebar from './components/Layout/Sidebar/Sidebar';
import TopHeader from './components/Layout/TopHeader/TopHeader';
import layoutStyles from './components/Layout/TopHeader/TopHeader.module.css';
import NewsPage from './components/Pages/News/NewsPage';
import ReportLayout from './components/Shared/ReportLayout/ReportLayout';
import Home from './components/Pages/Home/Home';
import Landing from './components/Pages/Auth/Landing';
import Login from './components/Pages/Auth/Login';
import Register from './components/Pages/Auth/Register';
import AdminPanel from './components/Pages/Admin/AdminPanel';
import Profile from './components/Pages/Profile/Profile';
import MINSALConsultasPage from './components/ConsultasPage/MINSALConsultasPage';
import MMAConsultasPage from './components/ConsultasPage/MMAConsultasPage';
import DGAConsultasPage from './components/ConsultasPage/DGAConsultasPage';
import SEAEvaluadosPage from './components/SEAEvaluadosPage/SEAEvaluadosPage';
import BugReportPage from './components/BugReportPage/BugReportPage';
import AdminBugsPage from './components/Pages/Admin/AdminBugsPage';
import { AuthProvider, useAuth } from './context/AuthContext';
import { NotificationsProvider } from './context/NotificationsContext';

function ProtectedLayout() {
  const { user, loading } = useAuth();

  if (loading) return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      Cargando...
    </div>
  );

  if (!user) return <Navigate to="/" />;

  return (
    <div className="app-container">
      <Sidebar />
      <main className={layoutStyles.mainContent}>
        <TopHeader />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/noticias" element={<NewsPage />} />
          <Route path="/favoritos" element={<ReportLayout key="favoritos" title="Favoritos" description="Tus normativas y proyectos guardados." listTitle="Favoritos" isFavoritesPage={true} />} />

          {/* Diario Oficial */}
          <Route path="/normativas" element={<ReportLayout key="normativas" title="Normativas" description="Visualización de normativas publicadas en el Diario Oficial." listTitle="Normativas" tableName="normativas" category="normativas" />} />

          {/* SEA */}
          <Route path="/pertinencias" element={<ReportLayout key="pertinencias" title="Pertinencias" description="Reporte de pertinencias ingresadas al SEA." listTitle="Pertinencias" tableName="pertinencias" category="pertinencias" />} />
          <Route path="/sea-evaluados" element={<SEAEvaluadosPage />} />

          {/* SMA */}
          <Route path="/fiscalizaciones" element={<ReportLayout key="fiscalizaciones" title="Fiscalizaciones" description="Reporte de fiscalizaciones realizadas por la SMA." listTitle="Fiscalizaciones" tableName="fiscalizaciones" category="fiscalizaciones" />} />
          <Route path="/sancionatorios" element={<ReportLayout key="sancionatorios" title="Sancionatorios" description="Reporte de procesos sancionatorios de la SMA." listTitle="Sancionatorios" tableName="sancionatorios" category="sancionatorios" />} />
          <Route path="/sanciones" element={<ReportLayout key="sanciones" title="Sanciones" description="Registro público de sanciones emitidas." listTitle="Sanciones" tableName="registroSanciones" category="registroSanciones" />} />
          <Route path="/programas" element={<ReportLayout key="programas" title="Programas de Cumplimiento" description="Reporte de programas de cumplimiento (PdC)." listTitle="Programas" tableName="programasDeCumplimiento" category="programasDeCumplimiento" />} />
          <Route path="/medidas" element={<ReportLayout key="medidas" title="Medidas Provisionales" description="Reporte de medidas provisionales dictadas." listTitle="Medidas" tableName="medidas_provisionales" category="medidas_provisionales" />} />
          <Route path="/requerimientos" element={<ReportLayout key="requerimientos" title="Requerimientos de Ingreso" description="Reporte de requerimientos de ingreso." listTitle="Requerimientos" tableName="requerimientos" category="requerimientos" />} />

          {/* Tribunales */}
          <Route path="/tribunales" element={<ReportLayout key="tribunales" title="Tribunales Ambientales" description="Reporte de causas en los Tribunales Ambientales." listTitle="Causas" tableName="Tribunales" category="Tribunales" />} />

          {/* Consultas Públicas */}
          <Route path="/consultas/minsal" element={<MINSALConsultasPage />} />
          <Route path="/consultas/dga" element={<DGAConsultasPage />} />
          <Route path="/consultas/mma" element={<MMAConsultasPage />} />

          {/* Admin */}
          <Route path="/admin" element={<AdminPanel />} />
          <Route path="/admin/reportes" element={<AdminBugsPage />} />

          {/* Profile */}
          <Route path="/perfil" element={<Profile />} />

          {/* Bug Reports */}
          <Route path="/bugs" element={<BugReportPage />} />
        </Routes>
      </main>
    </div>
  );
}

function AppRoutes() {
  const { user, loading } = useAuth();

  if (loading) return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
      Cargando...
    </div>
  );

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
