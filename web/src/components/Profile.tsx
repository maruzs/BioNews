import { useState, useEffect } from 'react';
import { useAuth } from '../context/AuthContext';

const Profile = () => {
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
    <div className="report-container">
      <div className="report-header-text">
        <h1 className="report-title">Perfil y Preferencias</h1>
        <p className="report-description">Configura los datos que deseas visualizar por defecto.</p>
      </div>

      <div style={{ marginTop: '30px', background: 'white', padding: '30px', borderRadius: '12px', border: '1px solid var(--border)' }}>
        <h2 style={{ fontSize: '20px', color: 'var(--text-dark)', marginBottom: '15px' }}>Información Personal</h2>
        <div className="profile-grid" style={{ display: 'grid', gridTemplateColumns: '150px 1fr', gap: '15px', marginBottom: '30px' }}>
          <strong style={{ color: 'var(--text-light)' }}>Nombre:</strong>
          <span className="profile-value" style={{ color: 'var(--text-dark)', fontWeight: 500 }}>{user.name}</span>
          
          <strong style={{ color: 'var(--text-light)' }}>Correo:</strong>
          <span className="profile-value" style={{ color: 'var(--text-dark)', fontWeight: 500 }}>{user.email}</span>
          
          <strong style={{ color: 'var(--text-light)' }}>Rol:</strong>
          <span className="profile-value" style={{ color: 'var(--text-dark)', fontWeight: 500 }}>{user.role === 'admin' ? 'Administrador' : 'Usuario'}</span>
        </div>

        <h2 style={{ fontSize: '20px', color: 'var(--text-dark)', marginBottom: '15px', paddingTop: '20px', borderTop: '1px solid var(--border)' }}>Preferencias de Filtrado (Opcional)</h2>
        <p style={{ color: 'var(--text-light)', marginBottom: '20px', fontSize: '14px' }}>Selecciona los elementos que te interesan. Si no seleccionas ninguno, se mostrarán todos por defecto en sus respectivas tablas.</p>

        <div style={{ display: 'flex', gap: '30px', flexWrap: 'wrap' }}>
          <div style={{ flex: '1 1 300px' }}>
            <h3 style={{ fontSize: '16px', color: 'var(--primary)', marginBottom: '10px' }}>Normativas (Organismos)</h3>
            <div style={{ maxHeight: '250px', overflowY: 'auto', background: '#f8fafc', padding: '15px', borderRadius: '8px', border: '1px solid var(--border)' }}>
              {options.normativas.map(org => (
                <label key={org} style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px', cursor: 'pointer', fontSize: '14px' }}>
                  <input type="checkbox" checked={prefs.normativas.includes(org)} onChange={() => togglePref('normativas', org)} />
                  {org}
                </label>
              ))}
            </div>
          </div>

          <div style={{ flex: '1 1 300px' }}>
            <h3 style={{ fontSize: '16px', color: 'var(--primary)', marginBottom: '10px' }}>SMA (Categorías)</h3>
            <div style={{ maxHeight: '250px', overflowY: 'auto', background: '#f8fafc', padding: '15px', borderRadius: '8px', border: '1px solid var(--border)' }}>
              {options.sma.map(cat => (
                <label key={cat} style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '8px', cursor: 'pointer', fontSize: '14px' }}>
                  <input type="checkbox" checked={prefs.sma.includes(cat)} onChange={() => togglePref('sma', cat)} />
                  {cat}
                </label>
              ))}
            </div>
          </div>
        </div>

        <div style={{ marginTop: '30px', display: 'flex', justifyContent: 'flex-end' }}>
          <button 
            onClick={handleSave} 
            disabled={saving}
            className="btn-primary" 
            style={{ padding: '10px 20px', borderRadius: '8px', fontWeight: 600 }}
          >
            {saving ? 'Guardando...' : 'Guardar Preferencias'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default Profile;
