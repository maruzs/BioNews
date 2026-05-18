import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../../../context/AuthContext';
import styles from './Auth.module.css';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const res = await fetch('/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Error al iniciar sesión');
      login(data.access_token, data.user);
      navigate('/');
    } catch (err: any) {
      setError(err.message);
    }
  };

  return (
    <div className={styles.authPage}>
      <div className={styles.authCard}>
        <div className={styles.authCardHeader}>
          <h2 className={styles.authTitle}>Iniciar Sesión</h2>
          <p className={styles.authSubtitle}>Ingresa a tu cuenta de BioNews</p>
        </div>
        {error && <div className={styles.errorBanner}>{error}</div>}
        <form onSubmit={handleSubmit} className={styles.authForm}>
          <div className={styles.formField}>
            <label>Correo Electrónico</label>
            <input type="email" required value={email} onChange={e => setEmail(e.target.value)} />
          </div>
          <div className={styles.formField}>
            <label>Contraseña</label>
            <input type="password" required value={password} onChange={e => setPassword(e.target.value)} />
          </div>
          <button type="submit" className={styles.submitBtn}>
            Ingresar
          </button>
        </form>
        <p className={styles.authFooter}>
          ¿No tienes una cuenta? <Link to="/register" className={styles.authLink}>Regístrate aquí</Link>
        </p>
      </div>
    </div>
  );
};

export default Login;
