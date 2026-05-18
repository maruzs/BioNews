import { useState, useEffect } from 'react';
import { useAuth } from '../../../context/AuthContext';
import { useNavigate } from 'react-router-dom';
import styles from './Profile.module.css';

const Profile = () => {
  const navigate = useNavigate();
  const { user, token, updatePreferences } = useAuth();
  const [options, setOptions] = useState<{normativas: string[], sma: string[]}>({ normativas: [], sma: [] });
  const [prefs, setPrefs] = useState<{normativas: string[], sma: string[]}>({ normativas: [], sma: [] });
  const [saving, setSaving] = useState(false);

  useEffect(() => {
    fetch('/api/options', { headers: { 'Authorization': `Bearer ${token}` } })
      .then(res => res.json())
      .then(data => {
        setOptions({
          normativas: data.normativas_organismos || [],
          sma: data.sma_categorias || []
        });
      })
      .catch(err => console.error(err));

    if (user?.preferences) {
      try {
        const parsed = JSON.parse(user.preferences);
        setPrefs({
          normativas: parsed.normativas || [],
          sma: parsed.sma || []
        });
      } catch (e) {
        // ignore
      }
    }
  }, [user, token]);

  const togglePref = (type: 'normativas' | 'sma', val: string) => {
    setPrefs(prev => {
      const current = prev[type];
      const next = current.includes(val) ? current.filter((x: string) => x !== val) : [...current, val];
      return { ...prev, [type]: next };
    });
  };

  const handleSave = async () => {
    setSaving(true);
    try {
      const bodyStr = JSON.stringify(prefs);
      await fetch('/api/auth/preferences', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
        body: bodyStr
      });
      updatePreferences(bodyStr);
      alert('Preferencias guardadas exitosamente.');
    } catch (err) {
      console.error(err);
      alert('Error al guardar preferencias.');
    }
    setSaving(false);
  };

  if (!user) return null;

  return (
    <div className={styles.pageContainer}>
      <div>
        <h1 className={styles.pageTitle}>Perfil y Preferencias</h1>
        <p className={styles.pageDescription}>Configura los datos que deseas visualizar por defecto.</p>
      </div>

      <div className={styles.infoCard}>
        <h2 className={styles.sectionTitle}>Información Personal</h2>
        <div className={styles.profileGrid}>
          <strong className={styles.profileLabel}>Nombre:</strong>
          <span className={styles.profileValue}>{user.name}</span>

          <strong className={styles.profileLabel}>Correo:</strong>
          <span className={styles.profileValue}>{user.email}</span>

          <strong className={styles.profileLabel}>Rol:</strong>
          <span className={styles.profileValue}>{user.role === 'admin' ? 'Administrador' : 'Usuario'}</span>
        </div>

        <div className={styles.bugReportSection}>
          <button
            onClick={() => navigate('/bugs')}
            className={styles.bugReportBtn}
          >
            Reportar un Bug / Problema Técnico
          </button>
        </div>

        <h2 className={styles.sectionTitleBordered}>Preferencias de Filtrado (Opcional)</h2>
        <p className={styles.prefDescription}>
          Selecciona los elementos que te interesan. Si no seleccionas ninguno, se mostrarán todos por defecto en sus respectivas tablas.
        </p>

        <div className={styles.prefsGrid}>
          <div className={styles.prefGroup}>
            <h3 className={styles.prefGroupTitle}>Normativas (Organismos)</h3>
            <div className={styles.checkboxList}>
              {options.normativas.map(org => (
                <label key={org} className={styles.checkboxLabel}>
                  <input type="checkbox" checked={prefs.normativas.includes(org)} onChange={() => togglePref('normativas', org)} />
                  {org}
                </label>
              ))}
            </div>
          </div>

          <div className={styles.prefGroup}>
            <h3 className={styles.prefGroupTitle}>SMA (Categorías)</h3>
            <div className={styles.checkboxList}>
              {options.sma.map(cat => (
                <label key={cat} className={styles.checkboxLabel}>
                  <input type="checkbox" checked={prefs.sma.includes(cat)} onChange={() => togglePref('sma', cat)} />
                  {cat}
                </label>
              ))}
            </div>
          </div>
        </div>

        <div className={styles.saveRow}>
          <button
            onClick={handleSave}
            disabled={saving}
            className={styles.saveBtn}
          >
            {saving ? 'Guardando...' : 'Guardar Preferencias'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default Profile;
