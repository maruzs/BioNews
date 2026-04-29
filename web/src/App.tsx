import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import NewsPage from './components/NewsPage';
import { Bell } from 'lucide-react';
import ReportLayout from './components/ReportLayout';

// Placeholder for Home
const HomePlaceholder = () => (
  <div style={{padding: 40, textAlign: 'center', color: '#6b7280'}}>
    <h2>Home</h2>
    <p>Página de inicio (en construcción)</p>
  </div>
);

function App() {
  return (
    <BrowserRouter>
      <div className="app-container">
        <Sidebar />
        <main className="main-content">
          <div className="top-header">
            <div className="top-header-spacer"></div>
            <div className="top-header-actions">
              <div className="notification-bell">
                <Bell size={20} />
                <span className="notification-badge">115</span>
              </div>
              <div className="profile-circle">SC</div>
            </div>
          </div>
          <Routes>
            <Route path="/" element={<HomePlaceholder />} />
            <Route path="/noticias" element={<NewsPage />} />
            <Route path="/favoritos" element={<ReportLayout title="Favoritos" description="Tus normativas y proyectos guardados." listTitle="Favoritos" isFavoritesPage={true} />} />
            
            {/* Diario Oficial */}
            <Route path="/normativas" element={<ReportLayout title="Normativas" description="Visualización de normativas publicadas en el Diario Oficial." listTitle="Normativas" filterFn={(item) => item.fuente === 'Diario Oficial'} />} />
            
            {/* SEA */}
            <Route path="/proyectos-evaluados" element={<ReportLayout title="Proyectos Evaluados" description="Reporte de proyectos evaluados en el SEA." listTitle="Proyectos Evaluados" filterFn={(item) => item.fuente === 'SEA'} />} />
            <Route path="/pertinencias" element={<ReportLayout title="Pertinencias" description="Reporte de pertinencias ingresadas al SEA." listTitle="Pertinencias" filterFn={(item) => item.fuente === 'SEA Pertinencias'} />} />
            <Route path="/participacion" element={<ReportLayout title="Participación Ciudadana" description="Reporte de procesos de participación ciudadana." listTitle="Participaciones" filterFn={(item) => !!(item.tipo && item.tipo.includes('Participacion'))} />} />

            {/* SMA */}
            <Route path="/fiscalizaciones" element={<ReportLayout title="Fiscalizaciones" description="Reporte de fiscalizaciones realizadas por la SMA." listTitle="Fiscalizaciones" filterFn={(item) => !!(item.tipo && item.tipo.includes('Fiscalizacion'))} />} />
            <Route path="/sancionatorios" element={<ReportLayout title="Sancionatorios" description="Reporte de procesos sancionatorios de la SMA." listTitle="Sancionatorios" filterFn={(item) => !!(item.tipo && item.tipo.includes('Sancionatorio'))} />} />
            <Route path="/sanciones" element={<ReportLayout title="Sanciones" description="Reporte de sanciones emitidas." listTitle="Sanciones" filterFn={(item) => !!(item.tipo && item.tipo.includes('Sancion'))} />} />
            <Route path="/seguimiento" element={<ReportLayout title="Seguimiento Ambiental" description="Reporte de seguimiento ambiental." listTitle="Seguimientos" filterFn={(item) => !!(item.tipo && item.tipo.includes('Seguimiento'))} />} />
            <Route path="/programas" element={<ReportLayout title="Programas de Cumplimiento" description="Reporte de programas de cumplimiento (PdC)." listTitle="Programas" filterFn={(item) => !!(item.tipo && item.tipo.includes('Programa'))} />} />
            <Route path="/medidas" element={<ReportLayout title="Medidas Provisionales" description="Reporte de medidas provisionales dictadas." listTitle="Medidas" filterFn={(item) => !!(item.tipo && item.tipo.includes('Medida'))} />} />
            <Route path="/requerimientos" element={<ReportLayout title="Requerimientos de Ingreso" description="Reporte de requerimientos de ingreso." listTitle="Requerimientos" filterFn={(item) => !!(item.tipo && item.tipo.includes('Ingreso SEIA'))} />} />

            {/* Tribunales */}
            <Route path="/tribunales" element={
              <ReportLayout title="Tribunales Ambientales" description="Reporte de causas en los Tribunales Ambientales." listTitle="Causas" filterFn={(item) => item.fuente.includes('TA') || item.fuente.includes('Tribunal') || item.fuente.includes('Corte')}>
                <div className="extra-filters">
                  <span className="filter-label">Tribunal:</span>
                  <label className="filter-checkbox"><input type="checkbox" /> Primer Tribunal</label>
                  <label className="filter-checkbox"><input type="checkbox" /> Segundo Tribunal</label>
                  <label className="filter-checkbox"><input type="checkbox" /> Tercer Tribunal</label>
                </div>
              </ReportLayout>
            } />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  );
}

export default App;
