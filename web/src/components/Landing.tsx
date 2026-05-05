import { Link } from 'react-router-dom';

const Landing = () => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh', backgroundColor: '#f8fafc' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '20px 40px', backgroundColor: 'white', borderBottom: '1px solid var(--border)' }}>
        <div className="sidebar-logo-text" style={{ margin: 0 }}>
          <span className="logo-bio">Bio</span><span className="logo-news">News</span>
        </div>
        <div style={{ display: 'flex', gap: '15px' }}>
          <Link to="/login" style={{ textDecoration: 'none', color: 'var(--text-dark)', fontWeight: 500, padding: '8px 16px' }}>Iniciar Sesión</Link>
          <Link to="/register" style={{ textDecoration: 'none', backgroundColor: 'var(--primary)', color: 'white', fontWeight: 500, padding: '8px 16px', borderRadius: '6px' }}>Registrarse</Link>
        </div>
      </header>
      <main style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '40px', textAlign: 'center' }}>
        <h1 style={{ fontSize: '48px', color: 'var(--text-dark)', marginBottom: '20px' }}>Bienvenido a BioNews</h1>
        <p style={{ fontSize: '18px', color: 'var(--text-light)', maxWidth: '600px', lineHeight: '1.6' }}>
          La plataforma definitiva para la gestión, seguimiento y análisis de normativas ambientales, proyectos del SEA, procesos de la SMA y causas en Tribunales Ambientales.
        </p>
        <div style={{ marginTop: '40px', display: 'flex', gap: '20px', flexWrap: 'wrap', justifyContent: 'center' }}>
          <div style={{ background: 'white', padding: '20px', borderRadius: '12px', border: '1px solid var(--border)', width: '250px' }}>
            <h3 style={{ color: 'var(--primary)' }}>Alertas Tempranas</h3>
            <p style={{ fontSize: '14px', color: 'var(--text-light)', marginTop: '10px' }}>Monitorea cambios en normativas y procesos sancionatorios al instante.</p>
          </div>
          <div style={{ background: 'white', padding: '20px', borderRadius: '12px', border: '1px solid var(--border)', width: '250px' }}>
            <h3 style={{ color: 'var(--primary)' }}>Inteligencia de Datos</h3>
            <p style={{ fontSize: '14px', color: 'var(--text-light)', marginTop: '10px' }}>Visualiza estadísticas y gráficos de tendencias ambientales.</p>
          </div>
          <div style={{ background: 'white', padding: '20px', borderRadius: '12px', border: '1px solid var(--border)', width: '250px' }}>
            <h3 style={{ color: 'var(--primary)' }}>Gestión Integral</h3>
            <p style={{ fontSize: '14px', color: 'var(--text-light)', marginTop: '10px' }}>Centraliza toda la información pública ambiental en un solo lugar.</p>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Landing;
