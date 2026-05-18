const cleaned = "06/05/2026";
const yearMatch = cleaned.match(/\b(19|20)\d{2}\b/);
console.log("yearMatch:", yearMatch);

const key = "fecha_presentacion";
const dateFields = ['fecha', 'Fecha', 'fecha_inicio', 'fecha_termino', 'fecha_presentacion', 'fecha_agregado'];
const isDate = key && (dateFields.includes(key) || key.toLowerCase().includes('fecha'));
console.log("isDate:", isDate);
