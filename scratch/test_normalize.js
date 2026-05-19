// Replicating normalizeLabel from normalizeLabels.ts
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
  };

  if (stateMappings[lower]) return stateMappings[lower];

  // 3. Extracción de año si es una fecha (basado en el formato del valor o en el nombre de la llave)
  const isDateValue = /^\d{2}[/-]\d{2}[/-]\d{4}/.test(cleaned) || /^\d{4}[/-]\d{2}[/-]\d{2}/.test(cleaned) || cleaned.includes('T00:00:00');
  const isDateKey = !!(key && (key.toLowerCase().includes('fecha') || key.toLowerCase().includes('date') || key.toLowerCase().includes('presentacion')));
  
  if (isDateValue || isDateKey) {
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

  if (cleaned.includes('/')) {
    cleaned = cleaned.split('/')[0].trim();
  }

  return cleaned;
};

// Test with various date formats and key=undefined
const testDates = [
  "23/12/2025",
  "2025-12-23",
  "2025-12-23T00:00:00.000Z",
  "23-12-2025 15:30:00",
  "23/12/2025 15:30:00"
];

console.log("=== Running isolated normalizeLabel tests ===");
testDates.forEach(d => {
  console.log(`Input: "${d}" (key=undefined) => Output: "${normalizeLabel(d, undefined)}"`);
});
