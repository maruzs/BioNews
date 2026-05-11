/**
 * Normaliza los labels de los datos para visualización consistente.
 */
export const normalizeLabel = (label: any, key?: string): string => {
  if (label === null || label === undefined || label === '') return 'No especificado';
  
  let cleaned = String(label).trim();

  // 1. Unificación de estados (archivada, archivadas -> Archivada)
  const lower = cleaned.toLowerCase();
  
  // Casos especiales que NO deben unificarse
  if (lower.startsWith('terminado -')) {
    return cleaned;
  }

  const stateMappings: Record<string, string> = {
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

  // 2. Categorías con "/" (Agroindustrias / Forestal -> Agroindustrias)
  if (cleaned.includes('/')) {
    cleaned = cleaned.split('/')[0].trim();
  }

  // 3. Extracción de año si es una fecha
  const dateFields = ['fecha', 'Fecha', 'fecha_inicio', 'fecha_termino', 'fecha_presentacion', 'fecha_agregado'];
  if (key && (dateFields.includes(key) || key.toLowerCase().includes('fecha'))) {
    // Buscar primero YYYY en cualquier parte
    const yearMatch = cleaned.match(/\b(19|20)\d{2}\b/);
    if (yearMatch) return yearMatch[0];
    
    // Si no lo encuentra, buscar split por - o /
    if (cleaned.includes('/') || cleaned.includes('-')) {
      const separator = cleaned.includes('/') ? '/' : '-';
      const parts = cleaned.split(separator);
      const last = parts[parts.length - 1].split(' ')[0]; // quitar la hora si existe
      if (last.length === 4) return last;
      if (parts[0].length === 4) return parts[0];
    }
  }

  // Handle SMA expediente years
  if (key && (key === 'expediente' || key === 'Expediente')) {
    const parts = cleaned.split('-');
    const yearPart = parts.find(p => /^(20)\d{2}$/.test(p));
    if (yearPart) return yearPart;
  }

  return cleaned;
};
