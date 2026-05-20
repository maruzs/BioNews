import { useState, useEffect, useMemo } from 'react';
import { Search, ExternalLink, X, HelpCircle, Pencil, ClipboardList, Heart, Table, LayoutGrid } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useNotifications } from '../context/NotificationsContext';
import { DataGrid } from '@mui/x-data-grid';
import { esES } from '@mui/x-data-grid/locales';

interface DGAConsulta {
  id: string;
  nombre: string;
  imagen: string;
  url: string;
  fecha_scraping: string;
  is_new: boolean;
}

const DGAConsultasPage = () => {
  const { token } = useAuth();
  const { refreshCategory, setCategoryActive } = useNotifications();
  const [data, setData] = useState<DGAConsulta[]>([]);
  const [loading, setLoading] = useState(true);
  const [totalRecords, setTotalRecords] = useState<number | null>(null);
  const [search, setSearch] = useState('');
  const [selectedItem, setSelectedItem] = useState<DGAConsulta | null>(null);
  const [favorites, setFavorites] = useState<Set<string>>(new Set());

  const [appliedSearch, setAppliedSearch] = useState('');
  const [viewMode, setViewMode] = useState<'table' | 'cards'>(
    typeof window !== 'undefined' && window.innerWidth < 768 ? 'cards' : 'table'
  );

  // Paginación server-side
  const [paginationModel, setPaginationModel] = useState({ page: 0, pageSize: 25 });
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 12;

  const handleApplyFilters = () => {
    setAppliedSearch(search);
    setPaginationModel(prev => ({ ...prev, page: 0 }));
    setCurrentPage(1);
  };

  const category = 'dga';

  useEffect(() => {
    setCategoryActive(category, true);
    return () => {
      setCategoryActive(category, false);
    };
  }, [setCategoryActive]);

  // Sincronizar currentPage con paginationModel
  useEffect(() => {
    if (viewMode === 'cards') {
      setPaginationModel(prev => ({ ...prev, page: currentPage - 1 }));
    }
  }, [currentPage, viewMode]);

  useEffect(() => {
    setCurrentPage(paginationModel.page + 1);
  }, [paginationModel.page]);

  const fetchData = async () => {
    if (!token) return;
    setLoading(true);
    try {
      // 1. Obtener count con filtros
      const countParams = new URLSearchParams();
      if (appliedSearch) countParams.append('search', appliedSearch);

      try {
        const countRes = await fetch(`/api/data/dga_consultas/count?${countParams.toString()}`, {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        const countJson = await countRes.json();
        setTotalRecords(countJson.count || 0);
      } catch (e) {
        console.error("Error fetching count:", e);
      }

      // 2. Obtener datos de la página
      const dataParams = new URLSearchParams(countParams);
      dataParams.append('limit', String(paginationModel.pageSize));
      dataParams.append('offset', String(paginationModel.page * paginationModel.pageSize));

      const response = await fetch(`/api/data/dga_consultas?${dataParams.toString()}`, {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      if (!response.ok) throw new Error('Error al obtener los datos');
      const result = await response.json();
      setData(Array.isArray(result) ? result : []);

      // Cargar favoritos
      const favRes = await fetch('/api/favorites', {
        headers: { 'Authorization': `Bearer ${token}` }
      });
      const favJson = await favRes.json();
      setFavorites(new Set(favJson.map((f: any) => f.id_o_link)));
      refreshCategory(category);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, [token, paginationModel.page, paginationModel.pageSize, appliedSearch]);

  const handleOpenModal = (item: DGAConsulta) => {
    setSelectedItem(item);
  };

  const filteredData = data;

  const totalPages = Math.ceil((totalRecords || 0) / itemsPerPage);

  const columns = useMemo(() => [
    { field: 'rowNumber', headerName: 'N°', width: 60, sortable: false },
    { field: 'nombre', headerName: 'Nombre de la Consulta', flex: 1, minWidth: 300 },
    {
      field: 'tipo',
      headerName: 'Tipo',
      width: 250,
      valueGetter: (_: any, row: any) => {
        const name = row.nombre.toLowerCase();
        if (name.includes('condiciones técnicas') && name.includes('obras hidráulicas')) {
          return 'Condiciones Técnicas';
        }
        if (name.includes('declaración jurada')) {
          return 'Declaración Jurada';
        }
        return 'Consulta General';
      }
    },
    {
      field: 'accion',
      headerName: 'Acciones',
      width: 100,
      sortable: false,
      renderCell: (params: any) => (
        <div style={{ display: 'flex', gap: '8px', alignItems: 'center', height: '100%' }}>
          <button
            onClick={(e) => { e.stopPropagation(); handleOpenModal(params.row); }}
            style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--primary)', display: 'flex', alignItems: 'center' }}
            title="Ver detalles"
          >
            <ExternalLink size={18} />
          </button>
          <button
            onClick={(e) => toggleFavorite(e, params.row)}
            style={{ background: 'none', border: 'none', cursor: 'pointer', color: favorites.has(params.row.id) ? 'var(--orange)' : 'var(--text-light)', display: 'flex', alignItems: 'center' }}
          >
            <Heart size={18} fill={favorites.has(params.row.id) ? 'var(--orange)' : 'none'} />
          </button>
        </div>
      )
    }
  ], [favorites]);

  const rows = useMemo(() => {
    const offsetNumber = paginationModel.page * paginationModel.pageSize;
    return filteredData.map((item, index) => ({
      ...item,
      rowNumber: offsetNumber + index + 1
    }));
  }, [filteredData, paginationModel.page, paginationModel.pageSize]);

  const toggleFavorite = async (e: React.MouseEvent, item: DGAConsulta) => {
    e.stopPropagation();
    const isFav = favorites.has(item.id);
    try {
      if (isFav) {
        await fetch(`/api/favorites/${encodeURIComponent(item.id)}`, {
          method: 'DELETE',
          headers: { 'Authorization': `Bearer ${token}` }
        });
        setFavorites(prev => {
          const next = new Set(prev);
          next.delete(item.id);
          return next;
        });
      } else {
        await fetch('/api/favorites', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
          body: JSON.stringify({
            id_o_link: item.id,
            fuente: 'DGA',
            nombre: item.nombre,
            accion: item.url
          })
        });
        setFavorites(prev => {
          const next = new Set(prev);
          next.add(item.id);
          return next;
        });
      }
    } catch (err) {
      console.error("Error toggling favorite:", err);
    }
  };

  // Determinar si es un formulario de Google o no
  const isGoogleForm = (url: string) => url.includes('forms.gle') || url.includes('docs.google.com/forms');

  return (
    <div style={{ padding: '20px', maxWidth: '1400px', margin: '0 auto', width: '100%' }}>
      <div style={{ marginBottom: '30px' }}>
        <h1 style={{ fontSize: '28px', fontWeight: 'bold', color: 'var(--text-dark)' }}>DGA - Consultas Públicas</h1>
        <p style={{ color: 'var(--text-light)', marginTop: '5px' }}>Consultas y participación ciudadana de la Dirección General de Aguas.</p>
      </div>

      {/* Control Bar */}
      <div style={{
        backgroundColor: 'white', padding: '15px', borderRadius: '12px',
        border: '1px solid var(--border)', boxShadow: '0 2px 10px rgba(0,0,0,0.03)',
        marginBottom: '25px', display: 'flex', flexWrap: 'wrap', gap: '15px', alignItems: 'center'
      }}>
        <div style={{ position: 'relative', width: '400px' }}>
          <Search size={18} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-light)' }} />
          <input
            type="text"
            placeholder="Buscar por nombre..."
            value={search}
            onChange={(e) => {
              setSearch(e.target.value);
              if (e.target.value === '') setAppliedSearch('');
            }}
            onKeyDown={(e) => { if (e.key === 'Enter') handleApplyFilters(); }}
            style={{
              width: '100%', padding: '10px 40px', borderRadius: '8px',
              border: '1px solid var(--border)', outline: 'none', fontSize: '14px'
            }}
          />
          {search && (
            <button
              onClick={() => { setSearch(''); setAppliedSearch(''); }}
              style={{ position: 'absolute', right: '12px', top: '50%', transform: 'translateY(-50%)', background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-light)' }}
            >
              <X size={16} />
            </button>
          )}
        </div>

        <div style={{ display: 'flex', border: '1px solid var(--border)', borderRadius: '8px', overflow: 'hidden' }}>
          <button
            onClick={() => setViewMode('table')}
            style={{
              padding: '10px 15px',
              backgroundColor: viewMode === 'table' ? 'var(--primary-light)' : 'white',
              color: viewMode === 'table' ? 'var(--primary)' : 'var(--text-dark)',
              border: 'none',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              fontWeight: 500,
              fontSize: '14px',
              transition: 'all 0.2s'
            }}
            title="Ver como tabla"
          >
            <Table size={18} />
            <span className="desktop-only">Tabla</span>
          </button>
          <button
            onClick={() => setViewMode('cards')}
            style={{
              padding: '10px 15px',
              backgroundColor: viewMode === 'cards' ? 'var(--primary-light)' : 'white',
              color: viewMode === 'cards' ? 'var(--primary)' : 'var(--text-dark)',
              border: 'none',
              borderLeft: '1px solid var(--border)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '8px',
              fontWeight: 500,
              fontSize: '14px',
              transition: 'all 0.2s'
            }}
            title="Ver como tarjetas"
          >
            <LayoutGrid size={18} />
            <span className="desktop-only">Tarjetas</span>
          </button>
        </div>

        <div style={{ color: 'var(--text-light)', fontSize: '14px', marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: '8px' }}>
          {totalRecords !== null ? `${totalRecords} resultados` : `${filteredData.length} resultados`}
        </div>
      </div>

      <div className="content-wrapper" style={{ padding: '0' }}>
        {loading ? (
          <div style={{ textAlign: 'center', padding: '100px 0' }}>
            <div className="loader" style={{ margin: '0 auto 20px auto' }}></div>
            <p style={{ color: 'var(--text-light)' }}>Cargando consultas...</p>
          </div>
        ) : viewMode === 'table' ? (
          <div className="table-container" style={{ height: 600, width: '100%', backgroundColor: 'white', borderRadius: '12px', padding: '10px' }}>
            <DataGrid
              rows={rows}
              columns={columns}
              loading={loading}
              paginationMode="server"
              paginationModel={paginationModel}
              onPaginationModelChange={setPaginationModel}
              rowCount={totalRecords || 0}
              pageSizeOptions={[10, 25, 50, 100]}
              disableRowSelectionOnClick
              localeText={esES.components.MuiDataGrid.defaultProps.localeText}
              getRowClassName={(params) => {
                return params.row.is_new ? 'new-record-highlight' : '';
              }}
              sx={{
                border: 'none',
                '& .MuiDataGrid-cell:focus': { outline: 'none' },
                '& .new-record-highlight': {
                  backgroundColor: 'rgba(34, 197, 94, 0.12)',
                  fontWeight: '500',
                  borderLeft: '5px solid var(--primary)',
                },
                '& .MuiDataGrid-row.new-record-highlight:hover': {
                  backgroundColor: 'rgba(34, 197, 94, 0.18)',
                },
                '& .MuiDataGrid-cell': {
                  borderBottom: '1px solid #f0f0f0',
                },
                '& .MuiDataGrid-columnHeaders': {
                  backgroundColor: '#f8f9fa',
                  borderBottom: '2px solid #e0e0e0',
                  fontWeight: 'bold',
                },
              }}
            />
          </div>
        ) : (
          <>
            <div className="news-grid" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(320px, 1fr))', gap: '25px', marginBottom: '40px' }}>
              {filteredData.length === 0 ? (
                <p style={{ gridColumn: '1 / -1', textAlign: 'center' }}>No hay consultas para mostrar.</p>
              ) : (
                filteredData.map((item) => (
                  <div key={item.id} className={`card ${item.is_new ? 'new-highlight' : ''}`} style={{ cursor: 'pointer', position: 'relative', height: '100%', display: 'flex', flexDirection: 'column' }} onClick={() => handleOpenModal(item)}>
                    {item.is_new && (
                      <div style={{ position: 'absolute', top: '10px', right: '10px', background: 'var(--primary)', color: 'white', padding: '2px 10px', borderRadius: '10px', fontSize: '0.7rem', fontWeight: 'bold', zIndex: 5 }}>
                        NUEVO
                      </div>
                    )}
                    <div className="card-content" style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                      <div style={{
                        width: '100%',
                        height: '160px',
                        background: '#f8fafc',
                        borderRadius: '12px',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        marginBottom: '15px',
                        fontSize: '4rem',
                        color: 'var(--primary)',
                        fontFamily: 'etmodules'
                      }}>
                        {(() => {
                          const nombre = item.nombre.toLowerCase();
                          if (nombre.includes('condiciones técnicas') && nombre.includes('obras hidráulicas')) {
                            return <Pencil size={64} />;
                          }
                          if (nombre.includes('declaración jurada') && (nombre.includes('bocatomas') || nombre.includes('cauces naturales'))) {
                            return <ClipboardList size={64} />;
                          }
                          return item.imagen && item.imagen.length === 1 ? item.imagen : <HelpCircle size={64} />;
                        })()}
                      </div>
                      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: '10px', marginBottom: '15px', flex: 1 }}>
                        <div className="card-title" style={{ fontSize: '1rem', fontWeight: 600, margin: 0 }}>{item.nombre}</div>
                        <Heart
                          size={20}
                          onClick={(e) => toggleFavorite(e, item)}
                          style={{
                            cursor: 'pointer',
                            flexShrink: 0,
                            fill: favorites.has(item.id) ? 'var(--orange)' : 'none',
                            color: favorites.has(item.id) ? 'var(--orange)' : 'var(--text-light)',
                            transition: 'all 0.2s'
                          }}
                        />
                      </div>
                      <div className="card-action" style={{ marginTop: 'auto', borderTop: '1px solid #f1f5f9', paddingTop: '15px', display: 'flex', alignItems: 'center', gap: '5px', color: 'var(--primary)', fontWeight: 600 }}>
                        <ExternalLink size={16} /> Ver detalles
                      </div>
                    </div>
                  </div>
                ))
              )}
            </div>

            {/* Pagination control for card layout */}
            {totalPages > 1 && (
              <div style={{ display: 'flex', justifyContent: 'center', gap: '15px', alignItems: 'center', marginTop: '20px' }}>
                <button
                  onClick={() => { setCurrentPage(p => Math.max(1, p - 1)); window.scrollTo(0, 0); }}
                  disabled={currentPage === 1}
                  style={{
                    padding: '10px 20px', borderRadius: '8px', border: '1px solid var(--border)',
                    background: currentPage === 1 ? '#f1f5f9' : 'white',
                    cursor: currentPage === 1 ? 'not-allowed' : 'pointer',
                    fontWeight: 600, color: 'var(--text-dark)'
                  }}
                >
                  Anterior
                </button>
                <div style={{ display: 'flex', gap: '5px' }}>
                  <span style={{ fontWeight: 'bold', color: 'var(--primary)' }}>{currentPage}</span>
                  <span style={{ color: 'var(--text-light)' }}>de {totalPages}</span>
                </div>
                <button
                  onClick={() => { setCurrentPage(p => Math.min(totalPages, p + 1)); window.scrollTo(0, 0); }}
                  disabled={currentPage === totalPages}
                  style={{
                    padding: '10px 20px', borderRadius: '8px', border: '1px solid var(--border)',
                    background: currentPage === totalPages ? '#f1f5f9' : 'white',
                    cursor: currentPage === totalPages ? 'not-allowed' : 'pointer',
                    fontWeight: 600, color: 'var(--text-dark)'
                  }}
                >
                  Siguiente
                </button>
              </div>
            )}
          </>
        )}
      </div>


      {selectedItem && (
        <div className="modal-overlay" style={{ position: 'fixed', top: 0, left: 0, right: 0, bottom: 0, backgroundColor: 'rgba(0,0,0,0.5)', display: 'flex', justifyContent: 'center', alignItems: 'center', zIndex: 1000, padding: '20px' }} onClick={() => setSelectedItem(null)}>
          <div className="modal-content" style={{ backgroundColor: 'white', borderRadius: '16px', padding: '40px', maxWidth: '500px', width: '100%', position: 'relative', boxShadow: '0 20px 25px -5px rgba(0, 0, 0, 0.1)', textAlign: 'center' }} onClick={e => e.stopPropagation()}>
            <button onClick={() => setSelectedItem(null)} style={{ position: 'absolute', top: '20px', right: '20px', background: '#f1f5f9', border: 'none', cursor: 'pointer', width: '36px', height: '36px', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#64748b' }}>
              <X size={20} />
            </button>

            <div style={{ marginBottom: '25px', display: 'flex', justifyContent: 'center' }}>
              <div style={{ width: '80px', height: '80px', background: 'rgba(59, 130, 246, 0.1)', borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--primary)' }}>
                <ExternalLink size={40} />
              </div>
            </div>

            <h3 style={{ fontSize: '1.4rem', fontWeight: 700, marginBottom: '15px', color: '#1e293b' }}>
              {isGoogleForm(selectedItem.url) ? 'Formulario de Google' : 'Enlace Externo'}
            </h3>

            <div style={{ position: 'absolute', top: '20px', left: '20px' }}>
              <Heart
                size={24}
                onClick={(e) => toggleFavorite(e, selectedItem)}
                style={{
                  cursor: 'pointer',
                  fill: favorites.has(selectedItem.id) ? 'var(--orange)' : 'none',
                  color: favorites.has(selectedItem.id) ? 'var(--orange)' : 'var(--text-light)',
                  transition: 'all 0.2s'
                }}
              />
            </div>

            <p style={{ color: '#64748b', marginBottom: '30px', lineHeight: '1.6' }}>
              {isGoogleForm(selectedItem.url)
                ? 'Esto te llevará a un formulario de Google para participar en esta consulta.'
                : 'Esto no es un formulario, te llevará al link asociado a esta consulta.'}
            </p>

            <a
              href={selectedItem.url}
              target="_blank"
              rel="noopener noreferrer"
              className="btn-primary"
              style={{
                display: 'inline-flex',
                alignItems: 'center',
                gap: '10px',
                padding: '12px 30px',
                borderRadius: '12px',
                textDecoration: 'none',
                fontWeight: 600,
                width: '100%',
                justifyContent: 'center'
              }}
            >
              Ir al {isGoogleForm(selectedItem.url) ? 'formulario' : 'enlace'}
            </a>
          </div>
        </div>
      )}
    </div>
  );
};

export default DGAConsultasPage;
