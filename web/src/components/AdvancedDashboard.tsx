import React, { useState, useMemo } from 'react';
import { 
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, 
  PieChart, Pie, Cell, LabelList
} from 'recharts';
import { X, LayoutDashboard, RefreshCcw, Maximize2, Download, FileCode } from 'lucide-react';

interface DimensionConfig {
  key: string;
  label: string;
  type: 'bar-horizontal' | 'bar-vertical' | 'pie' | 'relative-bar' | 'grouped-vertical';
  groupField?: string;
}

interface AdvancedDashboardProps {
  data: any[];
  config: {
    title: string;
    kpiField?: string;
    dimensions: DimensionConfig[];
  };
  onClose: () => void;
}

const COLORS = [
  '#0d9488', '#2563eb', '#f59e0b', '#db2777', '#8b5cf6', 
  '#14b8a6', '#3b82f6', '#f97316', '#ec4899', '#a855f7', 
  '#0f766e', '#1d4ed8', '#d97706', '#be185d', '#7c3aed',
  '#115e59', '#1e40af', '#b45309', '#9d174d', '#6d28d9'
];

// Persistent color map to keep colors consistent across charts
const colorCache: Record<string, string> = {};
let colorIndex = 0;

const getColorForValue = (value: string) => {
  if (colorCache[value]) return colorCache[value];
  const color = COLORS[colorIndex % COLORS.length];
  colorCache[value] = color;
  colorIndex++;
  return color;
};

// Utility to clean labels
const cleanLabel = (label: string | null | undefined, key?: string): string => {
  if (label === null || label === undefined || label === '') return 'No especificado';
  let cleaned = String(label).trim();
  
  // Year extraction if the field is a date or if it's explicitly for years
  const dateFields = ['fecha', 'Fecha', 'fecha_inicio', 'fecha_termino', 'fecha_presentacion', 'fecha_agregado'];
  if (key && (dateFields.includes(key) || key.toLowerCase().includes('fecha'))) {
    // Try to find a 4-digit year
    const yearMatch = cleaned.match(/\b(19|20)\d{2}\b/);
    if (yearMatch) return yearMatch[0];
    
    // Check for DD/MM/YYYY
    if (cleaned.includes('/')) {
      const parts = cleaned.split('/');
      const last = parts[parts.length - 1];
      if (last.length === 4) return last;
    }
  }

  // Handle expediente years (SMA)
  if (key && (key === 'expediente' || key === 'Expediente')) {
    const parts = cleaned.split('-');
    const yearPart = parts.find(p => /^(20)\d{2}$/.test(p));
    if (yearPart) return yearPart;
  }

  // Truncate at first / for categories
  if (cleaned.includes('/')) {
    cleaned = cleaned.split('/')[0].trim();
  }

  // Consolidate states
  const lower = cleaned.toLowerCase();
  const stateMappings: Record<string, string> = {
    'archivada': 'Archivada', 'archivadas': 'Archivada',
    'suspendida': 'Suspendida', 'suspendidas': 'Suspendida',
    'finalizada': 'Finalizada', 'finalizadas': 'Finalizada',
    'en trámite': 'En trámite', 'en tramite': 'En trámite',
    'aprobada': 'Aprobada', 'aprobado': 'Aprobada',
    'rechazada': 'Rechazada', 'rechazado': 'Rechazada',
    'desistido': 'Desistido', 'desistida': 'Desistido',
    'caducado': 'Caducado', 'caducada': 'Caducado',
    'vigente': 'Vigente', 'no vigente': 'No vigente'
  };

  if (stateMappings[lower]) return stateMappings[lower];
  
  return cleaned;
};

const AdvancedDashboard: React.FC<AdvancedDashboardProps> = ({ data, config, onClose }) => {
  const [activeFilters, setActiveFilters] = useState<Record<string, string>>({});
  const [expandedChart, setExpandedChart] = useState<{dim: DimensionConfig, data: any[]} | null>(null);

  // 1. Filtering logic
  const filteredData = useMemo(() => {
    return data.filter(item => {
      for (const [key, value] of Object.entries(activeFilters)) {
        if (cleanLabel(item[key], key) !== value) return false;
      }
      return true;
    });
  }, [data, activeFilters]);

  const toggleFilter = (key: string, value: string) => {
    setActiveFilters(prev => {
      const next = { ...prev };
      if (next[key] === value) {
        delete next[key];
      } else {
        next[key] = value;
      }
      return next;
    });
  };

  const clearFilters = () => setActiveFilters({});
  const isFiltered = Object.keys(activeFilters).length > 0;

  // 2. Data aggregation for each dimension
  const getChartData = (dim: DimensionConfig) => {
    const counts: Record<string, any> = {};
    
    if (dim.type === 'grouped-vertical' && dim.groupField) {
      // Group by year (usually) and then by groupField
      filteredData.forEach(item => {
        const primary = cleanLabel(item[dim.key], dim.key);
        const secondary = cleanLabel(item[dim.groupField!], dim.groupField!);
        if (!counts[primary]) counts[primary] = { name: primary };
        counts[primary][secondary] = (counts[primary][secondary] || 0) + 1;
        counts[primary].total = (counts[primary].total || 0) + 1;
      });
      return Object.values(counts).sort((a, b) => a.name.localeCompare(b.name));
    }

    filteredData.forEach(item => {
      const val = cleanLabel(item[dim.key], dim.key);
      counts[val] = (counts[val] || 0) + 1;
    });

    const result = Object.entries(counts).map(([name, count]) => ({
      name,
      count,
      percentage: ((count / filteredData.length) * 100).toFixed(1)
    }));

    // Sorting
    if (dim.type === 'bar-horizontal') {
      return result.sort((a, b) => b.count - a.count);
    }
    return result.sort((a, b) => a.name.localeCompare(b.name));
  };

  const renderKPIs = () => {
    const total = filteredData.length;
    const isFiltered = Object.keys(activeFilters).length > 0;

    return (
      <div className="dashboard-kpis">
        <div className="kpi-card">
          <div className="kpi-icon total"><LayoutDashboard size={20} /></div>
          <div className="kpi-content">
            <span className="kpi-label">Total de Registros</span>
            <span className="kpi-value">{total.toLocaleString()}</span>
            {isFiltered && <span className="kpi-sublabel">Filtrados de {data.length.toLocaleString()}</span>}
          </div>
        </div>
        {/* Additional KPIs could go here based on config */}
      </div>
    );
  };

  return (
    <div className="advanced-dashboard">
      <div className="dashboard-header">
        <div className="header-info">
          <h1>Dashboard: {config.title}</h1>
          <p>Análisis interactivo y filtros cruzados</p>
        </div>
        <div className="header-actions">
          {isFiltered && (
            <button className="clear-filters-btn" onClick={clearFilters}>
              <RefreshCcw size={16} className="refresh-animation" /> Limpiar Filtros ({Object.keys(activeFilters).length})
            </button>
          )}
          <button className="close-dashboard-btn" onClick={onClose}>
            <X size={20} />
          </button>
        </div>
      </div>

      <div className="dashboard-content">
        {renderKPIs()}

        <div className="dashboard-grid">
          {config.dimensions.map((dim, idx) => {
            const chartData = getChartData(dim);
            return (
            <div key={`${dim.key}-${idx}`} className={`chart-container ${dim.type === 'grouped-vertical' || (idx === 0 && config.dimensions.length % 2 !== 0) ? 'span-2' : ''}`}>
              <div className="chart-header">
                <h3>{dim.label}</h3>
                <button 
                  className="expand-btn" 
                  onClick={() => setExpandedChart({ dim, data: chartData })}
                  title="Expandir gráfico"
                >
                  <Maximize2 size={14} />
                </button>
              </div>
              <div className="chart-body">
                <ResponsiveContainer width="100%" height={380}>
                  {dim.type === 'pie' ? (
                    <PieChart>
                      <Pie
                        data={chartData}
                        dataKey="count"
                        nameKey="name"
                        innerRadius={60}
                        outerRadius={100}
                        paddingAngle={5}
                        label={({ name, percent }) => `${name.length > 15 ? name.substring(0, 15) + '...' : name} ${(percent * 100).toFixed(0)}%`}
                        labelLine={true}
                        onClick={(data) => toggleFilter(dim.key, String(data.name || ''))}
                        style={{ cursor: 'pointer' }}
                      >
                        {chartData.map((entry: any, index: number) => (
                          <Cell 
                            key={`cell-${index}`} 
                            fill={getColorForValue(entry.name)} 
                            opacity={activeFilters[dim.key] && activeFilters[dim.key] !== entry.name ? 0.3 : 1}
                          />
                        ))}
                      </Pie>
                      <Tooltip formatter={(value: any, _name: any, props: any) => [`${value} (${props.payload?.percentage || 0}%)`, 'Cantidad']} />
                      <Legend layout="horizontal" verticalAlign="bottom" align="center" wrapperStyle={{ fontSize: '11px', paddingTop: '10px' }} />
                    </PieChart>
                  ) : dim.type === 'bar-horizontal' || dim.type === 'relative-bar' ? (
                    <BarChart 
                      data={chartData} 
                      layout="vertical" 
                      margin={{ left: 100, right: 30 }}
                      onClick={(data) => data && data.activeLabel && toggleFilter(dim.key, data.activeLabel as string)}
                    >
                      <CartesianGrid strokeDasharray="3 3" horizontal={false} stroke="#f1f5f9" />
                      <XAxis type="number" hide={dim.type === 'relative-bar'} />
                      <YAxis 
                        dataKey="name" 
                        type="category" 
                        width={200} 
                        style={{ fontSize: '11px', fontWeight: 500 }} 
                        tick={{ width: 200 }}
                      />
                      <Tooltip 
                        formatter={(value: any, _name: any, props: any) => [
                          `${value} (${props.payload?.percentage || 0}%)`, 
                          'Cantidad'
                        ]}
                      />
                      <Bar dataKey="count" radius={[0, 4, 4, 0]}>
                        {chartData.map((entry: any, index: number) => (
                          <Cell 
                            key={`cell-${index}`} 
                            fill={getColorForValue(entry.name)}
                            opacity={activeFilters[dim.key] && activeFilters[dim.key] !== entry.name ? 0.3 : 1}
                            style={{ cursor: 'pointer' }}
                          />
                        ))}
                        <LabelList dataKey="count" position="right" style={{ fontSize: '11px', fill: '#64748b' }} />
                      </Bar>
                    </BarChart>
                  ) : dim.type === 'grouped-vertical' ? (
                    <BarChart 
                      data={chartData}
                      margin={{ top: 20, right: 30, left: 20, bottom: 5 }}
                    >
                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
                      <XAxis dataKey="name" />
                      <YAxis />
                      <Tooltip />
                      <Legend />
                      {/* We need to dynamically find all unique keys for grouping */}
                      {dim.groupField ? (
                        Array.from(new Set(filteredData.map(item => cleanLabel(item[dim.groupField!], dim.groupField!)))).slice(0, 10).map((key, kIdx) => (
                          <Bar 
                            key={kIdx} 
                            dataKey={key} 
                            stackId="a" 
                            fill={getColorForValue(key as string)} 
                            radius={[4, 4, 0, 0]} 
                            onClick={(data: any) => {
                              if (data && data.activeLabel) {
                                toggleFilter(dim.key, data.activeLabel as string);
                              }
                            }}
                          />
                        ))
                      ) : (
                        <Bar 
                          dataKey="count" 
                          fill="var(--primary)" 
                          radius={[4, 4, 0, 0]} 
                          onClick={(data: any) => {
                            if (data && data.activeLabel) {
                              toggleFilter(dim.key, data.activeLabel as string);
                            }
                          }}
                        />
                      )}
                    </BarChart>
                  ) : (
                    <BarChart data={chartData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                      <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
                      <XAxis dataKey="name" />
                      <YAxis />
                      <Tooltip />
                      <Bar dataKey="count" radius={[4, 4, 0, 0]}>
                        {chartData.map((entry: any, index: number) => (
                          <Cell 
                            key={`cell-${index}`} 
                            fill={getColorForValue(entry.name)}
                            opacity={activeFilters[dim.key] && activeFilters[dim.key] !== entry.name ? 0.3 : 1}
                            style={{ cursor: 'pointer' }}
                          />
                        ))}
                        <LabelList dataKey="count" position="top" style={{ fontSize: '11px', fill: '#64748b' }} />
                      </Bar>
                    </BarChart>
                  )}
                </ResponsiveContainer>
              </div>
            </div>
          )
        })}
        </div>
      </div>

      <style>{`
        .advanced-dashboard {
          width: 100%;
          min-height: 600px;
          background: #f8fafc;
          display: flex;
          flex-direction: column;
          color: #1e293b;
          border-radius: 16px;
          border: 1px solid #e2e8f0;
          overflow: hidden;
          margin-top: 20px;
        }
        .dashboard-header {
          background: white;
          padding: 20px 30px;
          border-bottom: 1px solid #e2e8f0;
          display: flex;
          justify-content: space-between;
          align-items: center;
          box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        }
        .header-info h1 {
          font-size: 24px;
          font-weight: 800;
          color: #0f172a;
          margin-bottom: 4px;
        }
        .header-info p {
          color: #64748b;
          font-size: 14px;
        }
        .header-actions {
          display: flex;
          gap: 12px;
          align-items: center;
        }
        .clear-filters-btn {
          display: flex;
          align-items: center;
          gap: 8px;
          padding: 8px 16px;
          background: #f1f5f9;
          border: 1px solid #e2e8f0;
          border-radius: 8px;
          color: #475569;
          font-size: 13px;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
        }
        .clear-filters-btn:hover {
          background: #e2e8f0;
        }
        .close-dashboard-btn {
          width: 40px;
          height: 40px;
          display: flex;
          align-items: center;
          justify-content: center;
          border-radius: 50%;
          background: #f1f5f9;
          border: none;
          color: #64748b;
          cursor: pointer;
          transition: all 0.2s;
        }
        .close-dashboard-btn:hover {
          background: #fee2e2;
          color: #ef4444;
        }
        .dashboard-content {
          padding: 30px 40px;
          max-width: 1400px;
          margin: 0 auto;
          width: 100%;
        }
        .dashboard-kpis {
          display: grid;
          grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
          gap: 20px;
          margin-bottom: 30px;
        }
        .kpi-card {
          background: white;
          padding: 20px;
          border-radius: 16px;
          display: flex;
          gap: 16px;
          align-items: center;
          box-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1);
          border: 1px solid #e2e8f0;
        }
        .kpi-icon {
          width: 48px;
          height: 48px;
          border-radius: 12px;
          display: flex;
          align-items: center;
          justify-content: center;
        }
        .kpi-icon.total { background: #eff6ff; color: #3b82f6; }
        .kpi-content {
          display: flex;
          flex-direction: column;
        }
        .kpi-label {
          font-size: 12px;
          color: #64748b;
          font-weight: 600;
          text-transform: uppercase;
          letter-spacing: 0.025em;
        }
        .kpi-value {
          font-size: 28px;
          font-weight: 800;
          color: #0f172a;
          line-height: 1;
          margin: 4px 0;
        }
        .kpi-sublabel {
          font-size: 11px;
          color: #3b82f6;
          font-weight: 600;
        }
        .dashboard-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 25px;
        }
        .chart-container {
          background: white;
          padding: 24px;
          border-radius: 20px;
          box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);
          border: 1px solid #e2e8f0;
        }
        .chart-container.span-2 {
          grid-column: span 2;
        }
        .chart-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 20px;
        }
        .chart-header h3 {
          font-size: 16px;
          font-weight: 700;
          color: #1e293b;
        }
        .expand-btn {
          background: none;
          border: none;
          color: #94a3b8;
          cursor: pointer;
          padding: 4px;
          border-radius: 4px;
          transition: all 0.2s;
        }
        .expand-btn:hover {
          background: #f1f5f9;
          color: var(--primary);
        }
        .modal-overlay {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: rgba(15, 23, 42, 0.7);
          backdrop-filter: blur(4px);
          z-index: 2000;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 40px;
        }
        .modal-content {
          background: white;
          width: 100%;
          max-width: 1000px;
          border-radius: 24px;
          overflow: hidden;
          box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
          animation: modalFadeIn 0.3s ease-out;
        }
        @keyframes modalFadeIn {
          from { opacity: 0; transform: scale(0.95) translateY(20px); }
          to { opacity: 1; transform: scale(1) translateY(0); }
        }
        .modal-header {
          padding: 24px 32px;
          border-bottom: 1px solid #f1f5f9;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }
        .modal-header h2 {
          font-size: 20px;
          font-weight: 800;
          color: #0f172a;
        }
        .modal-actions {
          display: flex;
          gap: 12px;
        }
        .modal-action-btn {
          display: flex;
          align-items: center;
          gap: 8px;
          padding: 8px 16px;
          background: #f8fafc;
          border: 1px solid #e2e8f0;
          border-radius: 8px;
          color: #475569;
          font-size: 13px;
          font-weight: 600;
          cursor: pointer;
          transition: all 0.2s;
        }
        .modal-action-btn:hover {
          background: white;
          border-color: var(--primary);
          color: var(--primary);
        }
        .close-modal-btn {
          background: #f1f5f9;
          border: none;
          width: 32px;
          height: 32px;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          cursor: pointer;
          color: #64748b;
        }
        .modal-body {
          padding: 40px;
        }
        .chart-body {
          min-height: 380px;
        }
        .refresh-animation { animation: spin 1s linear infinite reverse; animation-play-state: paused; }
        .clear-filters-btn:hover .refresh-animation { animation-play-state: running; }
        @keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

        @media (max-width: 1200px) {
          .dashboard-grid { grid-template-columns: repeat(2, 1fr); }
          .chart-container.span-2 { grid-column: span 2; }
        }
        @media (max-width: 768px) {
          .dashboard-grid { grid-template-columns: 1fr; }
          .chart-container.span-2 { grid-column: span 1; }
        }
      `}</style>

      {/* Expand Modal */}
      {expandedChart && (
        <div className="modal-overlay" onClick={() => setExpandedChart(null)}>
          <div className="modal-content" onClick={e => e.stopPropagation()}>
            <div className="modal-header">
              <h2>{expandedChart.dim.label}</h2>
              <div className="modal-actions">
                <button className="modal-action-btn" title="Ver SVG en otra pestaña" onClick={() => {
                  const svg = document.querySelector('.modal-body svg');
                  if (svg) {
                    const svgData = new XMLSerializer().serializeToString(svg);
                    const svgBlob = new Blob([svgData], {type: 'image/svg+xml;charset=utf-8'});
                    const url = URL.createObjectURL(svgBlob);
                    window.open(url, '_blank');
                  }
                }}>
                  <FileCode size={18} /> SVG
                </button>
                <button className="modal-action-btn" title="Descargar como Imagen" onClick={() => {
                   const svg = document.querySelector('.modal-body svg');
                   if (svg) {
                     const canvas = document.createElement('canvas');
                     const svgData = new XMLSerializer().serializeToString(svg);
                     const img = new Image();
                     img.onload = () => {
                       canvas.width = img.width * 2;
                       canvas.height = img.height * 2;
                       const ctx = canvas.getContext('2d');
                       if (ctx) {
                         ctx.fillStyle = 'white';
                         ctx.fillRect(0, 0, canvas.width, canvas.height);
                         ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
                         const pngUrl = canvas.toDataURL('image/png');
                         const downloadLink = document.createElement('a');
                         downloadLink.href = pngUrl;
                         downloadLink.download = `${expandedChart.dim.label}.png`;
                         downloadLink.click();
                       }
                     };
                     img.src = 'data:image/svg+xml;base64,' + btoa(unescape(encodeURIComponent(svgData)));
                   }
                }}>
                  <Download size={18} /> PNG
                </button>
                <button className="close-modal-btn" onClick={() => setExpandedChart(null)}><X size={20} /></button>
              </div>
            </div>
            <div className="modal-body">
               <ResponsiveContainer width="100%" height={500}>
                  {expandedChart.dim.type === 'pie' ? (
                    <PieChart>
                      <Pie
                        data={expandedChart.data}
                        dataKey="count"
                        nameKey="name"
                        innerRadius={100}
                        outerRadius={180}
                        paddingAngle={5}
                        label={({ name, percent }) => `${name} ${(percent * 100).toFixed(1)}%`}
                        labelLine={true}
                      >
                        {expandedChart.data.map((entry: any, index: number) => (
                          <Cell key={`cell-${index}`} fill={getColorForValue(entry.name)} />
                        ))}
                      </Pie>
                      <Tooltip formatter={(value: any, _name: any, props: any) => [`${value} (${props.payload?.percentage || 0}%)`, 'Cantidad']} />
                      <Legend />
                    </PieChart>
                  ) : expandedChart.dim.type === 'bar-horizontal' || expandedChart.dim.type === 'relative-bar' ? (
                    <BarChart data={expandedChart.data} layout="vertical" margin={{ left: 250, right: 50 }}>
                      <CartesianGrid strokeDasharray="3 3" horizontal={false} />
                      <XAxis type="number" />
                      <YAxis dataKey="name" type="category" width={240} style={{ fontSize: '13px' }} tick={{ width: 240 }} />
                      <Tooltip formatter={(value: any, _name: any, props: any) => [`${value} (${props.payload?.percentage || 0}%)`, 'Cantidad']} />
                      <Bar dataKey="count">
                        {expandedChart.data.map((entry: any, index: number) => (
                          <Cell key={`cell-${index}`} fill={getColorForValue(entry.name)} />
                        ))}
                        <LabelList dataKey="count" position="right" />
                      </Bar>
                    </BarChart>
                  ) : (
                    <BarChart data={expandedChart.data} margin={{ top: 20, right: 30, left: 20, bottom: 80 }}>
                      <CartesianGrid strokeDasharray="3 3" vertical={false} />
                      <XAxis dataKey="name" angle={-45} textAnchor="end" height={100} style={{ fontSize: '13px' }} />
                      <YAxis />
                      <Tooltip />
                      {expandedChart.dim.type === 'grouped-vertical' && expandedChart.dim.groupField ? (
                        <>
                          <Legend verticalAlign="top" wrapperStyle={{ paddingBottom: '20px' }} />
                          {Array.from(new Set(filteredData.map(item => cleanLabel(item[expandedChart.dim.groupField!], expandedChart.dim.groupField!)))).slice(0, 10).map((key, kIdx) => (
                            <Bar 
                              key={kIdx} 
                              dataKey={key as string} 
                              stackId="a" 
                              fill={getColorForValue(key as string)} 
                            />
                          ))}
                        </>
                      ) : (
                        <Bar dataKey="count">
                          {expandedChart.data.map((entry: any, index: number) => (
                            <Cell key={`cell-${index}`} fill={getColorForValue(entry.name)} />
                          ))}
                          <LabelList dataKey="count" position="top" />
                        </Bar>
                      )}
                    </BarChart>
                  )}
               </ResponsiveContainer>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default AdvancedDashboard;
