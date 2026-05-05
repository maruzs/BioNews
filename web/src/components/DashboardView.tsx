import React, { useState, useEffect } from 'react';
import { 
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, 
  PieChart, Pie, Cell, LineChart, Line, AreaChart, Area
} from 'recharts';
import { useAuth } from '../context/AuthContext';

interface DashboardViewProps {
  tableName: string;
  title: string;
}

const COLORS = ['#2563eb', '#7c3aed', '#db2777', '#ea580c', '#16a34a', '#0891b2', '#4f46e5', '#9333ea', '#c026d3', '#e11d48'];

const DashboardView: React.FC<DashboardViewProps> = ({ tableName, title }) => {
  const [stats, setStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const { token } = useAuth();

  useEffect(() => {
    const fetchStats = async () => {
      setLoading(true);
      try {
        const res = await fetch(`/api/stats/${tableName}`, {
          headers: { 'Authorization': `Bearer ${token}` }
        });
        const data = await res.json();
        setStats(data);
      } catch (err) {
        console.error("Error fetching stats:", err);
      } finally {
        setLoading(false);
      }
    };
    fetchStats();
  }, [tableName, token]);

  if (loading) return <div style={{ padding: '40px', textAlign: 'center' }}>Cargando estadísticas...</div>;
  if (!stats || stats.error) return <div style={{ padding: '40px', textAlign: 'center' }}>No hay estadísticas disponibles para {title}</div>;

  const renderNormativasDashboard = () => (
    <div className="dashboard-grid">
      <div className="stat-card total-card">
        <h3>Total de Normativas</h3>
        <div className="big-number">{stats.total.toLocaleString()}</div>
        <p>Registros a la fecha</p>
      </div>

      <div className="chart-card span-2">
        <h3>Normativas por Organismo (Top 15)</h3>
        <div style={{ width: '100%', height: 350 }}>
          <ResponsiveContainer>
            <BarChart data={stats.by_organismo} layout="vertical" margin={{ left: 100 }}>
              <CartesianGrid strokeDasharray="3 3" horizontal={false} />
              <XAxis type="number" />
              <YAxis dataKey="name" type="category" width={180} style={{ fontSize: '11px' }} />
              <Tooltip />
              <Bar dataKey="count" fill="var(--primary)" radius={[0, 4, 4, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="chart-card span-3">
        <h3>Normativas por Año y Tipo</h3>
        <div style={{ width: '100%', height: 400 }}>
          <ResponsiveContainer>
            <BarChart data={processYearTypeData(stats.by_year_type)}>
              <CartesianGrid strokeDasharray="3 3" vertical={false} />
              <XAxis dataKey="anio" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="General" stackId="a" fill="#2563eb" />
              <Bar dataKey="Particular" stackId="a" fill="#7c3aed" />
              <Bar dataKey="Boletin Oficial Mineria" stackId="a" fill="#db2777" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );

  const renderFiscalizacionesDashboard = () => (
    <div className="dashboard-grid">
      <div className="stat-card total-card">
        <h3>Total de Fiscalizaciones</h3>
        <div className="big-number">{stats.total.toLocaleString()}</div>
        <p>Procesos registrados</p>
      </div>

      <div className="chart-card span-2">
        <h3>Distribución por Tipo (Porcentaje)</h3>
        <div style={{ width: '100%', height: 300 }}>
          <ResponsiveContainer>
            <BarChart data={stats.by_tipo} layout="vertical" margin={{ left: 20 }}>
                <XAxis type="number" domain={[0, stats.total]} hide />
                <YAxis dataKey="name" type="category" width={80} />
                <Tooltip />
                <Bar dataKey="count" fill="var(--orange)" radius={[0, 4, 4, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="chart-card">
        <h3>Fiscalizaciones por Región</h3>
        <div style={{ width: '100%', height: 350 }}>
          <ResponsiveContainer>
            <PieChart>
              <Pie
                data={stats.by_region}
                innerRadius={60}
                outerRadius={100}
                paddingAngle={5}
                dataKey="count"
              >
                {stats.by_region.map((_: any, index: number) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
              <Legend layout="vertical" align="right" verticalAlign="middle" />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="chart-card span-2">
        <h3>Evolución Anual</h3>
        <div style={{ width: '100%', height: 350 }}>
          <ResponsiveContainer>
            <AreaChart data={stats.by_year.sort((a: any, b: any) => a.anio.localeCompare(b.anio))}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="anio" />
              <YAxis />
              <Tooltip />
              <Area type="monotone" dataKey="count" stroke="var(--primary)" fill="var(--primary-light)" fillOpacity={0.3} />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );

  const renderTribunalesDashboard = () => (
    <div className="dashboard-grid">
      <div className="stat-card total-card">
        <h3>Total de Causas</h3>
        <div className="big-number">{stats.total.toLocaleString()}</div>
        <p>En tribunales ambientales</p>
      </div>

      <div className="chart-card">
        <h3>Procedimientos por Tribunal</h3>
        <div style={{ width: '100%', height: 300 }}>
          <ResponsiveContainer>
            <PieChart>
              <Pie
                data={stats.by_tribunal}
                outerRadius={80}
                fill="#8884d8"
                dataKey="count"
                label
              >
                {stats.by_tribunal.map((_: any, index: number) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="chart-card">
        <h3>Por Tipo de Procedimiento</h3>
        <div style={{ width: '100%', height: 300 }}>
          <ResponsiveContainer>
            <BarChart data={stats.by_procedimiento}>
              <XAxis dataKey="name" hide />
              <YAxis />
              <Tooltip />
              <Bar dataKey="count" fill="var(--secondary)" radius={[4, 4, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="chart-card span-3">
        <h3>Ingreso de Causas por Año</h3>
        <div style={{ width: '100%', height: 350 }}>
          <ResponsiveContainer>
            <BarChart data={stats.by_year.sort((a: any, b: any) => a.anio.localeCompare(b.anio))}>
              <CartesianGrid strokeDasharray="3 3" vertical={false} />
              <XAxis dataKey="anio" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="count" fill="var(--primary)" radius={[4, 4, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );

  const renderMedidasDashboard = () => (
    <div className="dashboard-grid">
      <div className="stat-card total-card">
        <h3>Total de Medidas</h3>
        <div className="big-number">{stats.total.toLocaleString()}</div>
        <p>Expedientes registrados</p>
      </div>

      <div className="chart-card">
        <h3>Por Estado</h3>
        <div style={{ width: '100%', height: 300 }}>
          <ResponsiveContainer>
            <PieChart>
              <Pie data={stats.by_estado} dataKey="count" nameKey="name" cx="50%" cy="50%" outerRadius={80} label>
                {stats.by_estado.map((_: any, index: number) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="chart-card span-2">
        <h3>Medidas por Región</h3>
        <div style={{ width: '100%', height: 300 }}>
          <ResponsiveContainer>
            <BarChart data={stats.by_region}>
              <XAxis dataKey="name" hide />
              <YAxis />
              <Tooltip />
              <Bar dataKey="count" fill="var(--primary)" radius={[4, 4, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="chart-card span-3">
        <h3>Evolución Anual</h3>
        <div style={{ width: '100%', height: 350 }}>
          <ResponsiveContainer>
            <LineChart data={stats.by_year.sort((a: any, b: any) => a.anio.localeCompare(b.anio))}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="anio" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="count" stroke="var(--primary)" strokeWidth={3} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );

  // Helper for Year/Type grouping
  function processYearTypeData(data: any[]) {
    const years: any = {};
    data.forEach(item => {
      if (!years[item.anio]) years[item.anio] = { anio: item.anio };
      years[item.anio][item.tipo] = item.count;
    });
    return Object.values(years).sort((a: any, b: any) => a.anio.localeCompare(b.anio));
  }

  return (
    <div className="dashboard-container">
      {tableName === 'normativas' && renderNormativasDashboard()}
      {tableName === 'fiscalizaciones' && renderFiscalizacionesDashboard()}
      {tableName === 'Tribunales' && renderTribunalesDashboard()}
      {tableName === 'medidas_provisionales' && renderMedidasDashboard()}
      
      {!['normativas', 'fiscalizaciones', 'Tribunales', 'medidas_provisionales'].includes(tableName) && (
        <div style={{ padding: '40px', textAlign: 'center' }}>
          Dashboard genérico en construcción para {title}
        </div>
      )}

      <style>{`
        .dashboard-container {
          padding: 20px 0;
        }
        .dashboard-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 20px;
        }
        .span-2 { grid-column: span 2; }
        .span-3 { grid-column: span 3; }
        .stat-card {
          background: white;
          padding: 24px;
          border-radius: 16px;
          border: 1px solid var(--border);
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          text-align: center;
          box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);
        }
        .total-card {
          background: linear-gradient(135deg, var(--primary), #1d4ed8);
          color: white;
          border: none;
        }
        .total-card h3 { color: rgba(255,255,255,0.9); font-size: 14px; margin-bottom: 10px; }
        .big-number {
          font-size: 48px;
          font-weight: 800;
          margin: 10px 0;
        }
        .total-card p { opacity: 0.8; font-size: 13px; }
        .chart-card {
          background: white;
          padding: 20px;
          border-radius: 16px;
          border: 1px solid var(--border);
          box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);
        }
        .chart-card h3 {
          font-size: 15px;
          font-weight: 600;
          color: var(--text-dark);
          margin-bottom: 20px;
        }
        @media (max-width: 1024px) {
          .dashboard-grid { grid-template-columns: 1fr; }
          .span-2, .span-3 { grid-column: span 1; }
        }
      `}</style>
    </div>
  );
};

export default DashboardView;
