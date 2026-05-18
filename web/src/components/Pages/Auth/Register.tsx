import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../../../context/AuthContext';
import styles from './Auth.module.css';

const Register = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const res = await fetch('/api/auth/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password })
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || 'Error al registrarse');
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
          <h2 className={styles.authTitle}>Registrarse</h2>
          <p className={styles.authSubtitle}>Crea tu cuenta en BioNews</p>
        </div>
        {error && <div className={styles.errorBanner}>{error}</div>}
        <form onSubmit={handleSubmit} className={styles.authForm}>
          <div className={styles.formField}>
            <label htmlFor="name">Nombre Completo</label>
            <input id="name" name="name" type="text" required value={name} onChange={e => setName(e.target.value)} />
          </div>
          <div className={styles.formField}>
            <label htmlFor="email">Correo Electrónico</label>
            <input id="email" name="email" type="email" required value={email} onChange={e => setEmail(e.target.value)} />
          </div>
          <div className={styles.formField}>
            <label htmlFor="password">Contraseña</label>
            <input id="password" name="password" type="password" required value={password} onChange={e => setPassword(e.target.value)} />
          </div>
          <button type="submit" className={styles.submitBtn}>
            Registrarse
          </button>
        </form>
        <p className={styles.authFooter}>
          ¿Ya tienes cuenta? <Link to="/login" className={styles.authLink}>Inicia sesión</Link>
        </p>
      </div>
    </div>
  );
};

export default Register;
