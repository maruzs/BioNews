const normalizeLabel = (label, key) => {
  if (label === null || label === undefined || label === '') return 'No especificado';
  
  let cleaned = String(label).trim();

  const lower = cleaned.toLowerCase();
  
  const stateMappings = {
    'archivada': 'Archivada',
    'archivadas': 'Archivada',
    'finalizada': 'Finalizada',
    'finalizadas': 'Finalizada',
    'suspendida': 'Suspendida',
    'suspendidas': 'Suspendida',
    'en tramite': 'En trámite',
    'en trámite': 'En trámite',
    'aprobado': 'Aprobada',
    'aprobada': 'Aprobada',
    'rechazado': 'Rechazada',
    'rechazada': 'Rechazada',
    'terminada': 'Terminada',
    'terminadas': 'Terminada',
    'en tramitacion': 'En tramitación',
    'en tramitación': 'En tramitación',
    'tramitacion': 'En tramitación',
    'tramitación': 'En tramitación',
    'reclamación': 'Reclamación',
    'reclamacion': 'Reclamación',
    'solicitud': 'Solicitud',
    'solicitud sma': 'Solicitud',
    'demanda ejecutiva ': 'Demanda Ejecutiva',
    'demanda ejecutiva': 'Demanda Ejecutiva',
  };

  if (stateMappings[lower]) return stateMappings[lower];

  if (cleaned.includes('/')) {
    cleaned = cleaned.split('/')[0].trim();
  }

  // 3. Extracción de año si es una fecha
  const dateFields = ['fecha', 'Fecha', 'fecha_inicio', 'fecha_termino', 'fecha_presentacion', 'fecha_agregado'];
  if (key && (dateFields.includes(key) || key.toLowerCase().includes('fecha'))) {
    const yearMatch = cleaned.match(/\b(19|20)\d{2}\b/);
    if (yearMatch) return yearMatch[0];
    
    if (cleaned.includes('/') || cleaned.includes('-')) {
      const separator = cleaned.includes('/') ? '/' : '-';
      const parts = cleaned.split(separator);
      const last = parts[parts.length - 1].split(' ')[0];
      if (last.length === 4) return last;
      if (parts[0].length === 4) return parts[0];
    }
  }

  if (key && (key === 'expediente' || key === 'Expediente')) {
    const parts = cleaned.split('-');
    const yearPart = parts.find(p => /^(20)\d{2}$/.test(p));
    if (yearPart) return yearPart;
  }

  return cleaned;
};

const aggregateData = (data, dim) => {
  if (!data || data.length === 0) return [];

  const counts = {};
  
  if (dim.type === 'grouped-vertical' && dim.groupField) {
    data.forEach(item => {
      const primary = normalizeLabel(item[dim.key], dim.key);
      const secondary = normalizeLabel(item[dim.groupField], dim.groupField);
      if (!counts[primary]) counts[primary] = { name: primary };
      counts[primary][secondary] = (counts[primary][secondary] || 0) + 1;
      counts[primary].total = (counts[primary].total || 0) + 1;
    });
    const result = Object.values(counts);
    if (dim.key.toLowerCase().includes('anio') || dim.key.toLowerCase().includes('año') || dim.key.toLowerCase().includes('fecha') || dim.label.toLowerCase().includes('evolucion') || dim.label.toLowerCase().includes('evolución') || dim.label.toLowerCase().includes('año')) {
      return result.sort((a, b) => String(a.name).localeCompare(String(b.name), undefined, { numeric: true }));
    }
    return result.sort((a, b) => a.name.localeCompare(b.name));
  }

  data.forEach(item => {
    let val = normalizeLabel(item[dim.key], dim.key);
    counts[val] = (counts[val] || 0) + 1;
  });

  const total = Object.values(counts).reduce((sum, count) => sum + count, 0);
  const result = Object.entries(counts).map(([name, count]) => ({
    name,
    count: count,
    percentage: total > 0 ? Number(((count / total) * 100).toFixed(1)) : 0
  }));

  if (dim.key.toLowerCase().includes('anio') || dim.key.toLowerCase().includes('año') || dim.key.toLowerCase().includes('fecha') || dim.label.toLowerCase().includes('evolucion') || dim.label.toLowerCase().includes('evolución') || dim.label.toLowerCase().includes('año')) {
    return result.sort((a, b) => String(a.name).localeCompare(String(b.name), undefined, { numeric: true }));
  }

  return result.sort((a, b) => b.count - a.count);
};

// TEST
const data = [
  { fecha_presentacion: "23/12/2025" },
  { fecha_presentacion: "23/12/2025" },
  { fecha_presentacion: "19/12/2024" }
];

const dim = { key: 'fecha_presentacion', label: 'Presentaciones por Año', type: 'grouped-vertical' };

console.log("Aggregated:", aggregateData(data, dim));
console.log("Normalized:", normalizeLabel("23/12/2025", "fecha_presentacion"));
