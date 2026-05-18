import { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../../context/AuthContext';
import styles from './TopHeader.module.css';

const TopHeader = () => {
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

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  if (!user) return null;

  return (
    <div className={styles.topHeader}>
      <div className={styles.topHeaderSpacer} />
      <div className={styles.topHeaderActions} ref={dropdownRef}>
        <div
          className={styles.userPill}
          onClick={() => setDropdownOpen(!dropdownOpen)}
        >
          <div className={styles.userAvatar}>
            {user.name.charAt(0)?.toUpperCase()}
          </div>
          <span className={styles.userName}>{user.name}</span>
        </div>

        {dropdownOpen && (
          <div className={styles.userDropdown}>
            {user.role === 'admin' && (
              <button
                className={styles.dropdownItem}
                onClick={() => { setDropdownOpen(false); navigate('/admin'); }}
              >
                Panel de Admin
              </button>
            )}
            <button
              className={styles.dropdownItem}
              onClick={() => { setDropdownOpen(false); navigate('/perfil'); }}
            >
              Perfil y Preferencias
            </button>
            <button
              className={styles.dropdownItemDanger}
              onClick={handleLogout}
            >
              Cerrar Sesión
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export { styles as topHeaderStyles };
export default TopHeader;
