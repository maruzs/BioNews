import { Link } from 'react-router-dom';
import styles from './Auth.module.css';

const Landing = () => {
  return (
    <div className={styles.landingPage}>
      <header className={styles.landingHeader}>
        <div className={styles.logoText}>
          <span className={styles.logoBio}>Bio</span><span className={styles.logoNews}>News</span>
        </div>
        <nav className={styles.landingHeaderNav}>
          <Link to="/login" className={styles.navLink}>Iniciar Sesión</Link>
          <Link to="/register" className={styles.navLinkPrimary}>Registrarse</Link>
        </nav>
      </header>
      <main className={styles.landingMain}>
        <h1 className={styles.landingTitle}>Bienvenido a BioNews</h1>
        <p className={styles.landingSubtitle}>
          La plataforma definitiva para la gestión, seguimiento y análisis de normativas ambientales, proyectos del SEA, procesos de la SMA y causas en Tribunales Ambientales.
        </p>
        <div className={styles.landingFeatures}>
          <div className={styles.featureCard}>
            <h3>Alertas Tempranas</h3>
            <p>Monitorea cambios en normativas y procesos sancionatorios al instante.</p>
          </div>
          <div className={styles.featureCard}>
            <h3>Inteligencia de Datos</h3>
            <p>Visualiza estadísticas y gráficos de tendencias ambientales.</p>
          </div>
          <div className={styles.featureCard}>
            <h3>Gestión Integral</h3>
            <p>Centraliza toda la información pública ambiental en un solo lugar.</p>
          </div>
        </div>
      </main>
    </div>
  );
};

export default Landing;
