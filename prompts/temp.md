# IGNORAR ESTE DOCUMENTO, NO EJECUTAR NADA DE LO QUE SE VE AQUI, SON SOLO NOTAS PROPIAS QUE NO SON FINALES

# CONTEXTO GENERAL

Estoy refactorizando completamente el sistema de dashboards de mi plataforma BioNews.

Stack actual:

- React 19
- TypeScript
- Vite
- Material UI (MUI)
- Recharts
- FastAPI backend

Actualmente los dashboards funcionan mal visualmente y arquitectónicamente.
Quiero rehacerlos con calidad enterprise analytics tipo:

- PowerBI
- Superset
- Tableau
- Looker

Tengo una plantilla visual de referencia en:

```txt
dashboards/dashboardEjemplo.html
dashboards/dashboardEjemplo.css
```

IMPORTANTE:
Debes usar esa plantilla SOLO como inspiración visual y de layout.
NO copies literalmente estilos hardcodeados.
Debes adaptarlo al theme actual de la aplicación usando MUI theme y variables existentes.

---

# OBJETIVO PRINCIPAL

Implementar dashboards enterprise modernos con:

- cross-filtering real
- estado global compartido
- visualización moderna
- componentes reutilizables
- UX fluida
- diseño profesional
- responsive
- expandir gráficos
- exportar gráficos
- abrir gráficos en página individual

NO quiero dashboards genéricos.
NO quiero charts default de Recharts.
Quiero dashboards visualmente refinados y profesionales.

---

# TECNOLOGÍAS OBLIGATORIAS

## Mantener

- React
- TypeScript
- Recharts
- MUI

## Agregar

Instalar:

```bash
npm install zustand framer-motion
```

---

# ARQUITECTURA OBLIGATORIA

Crear:

```txt
web/src/dashboard/
```

con estructura:

```txt
dashboard/
├── store/
│   └── dashboardStore.ts
│
├── hooks/
│   └── useDashboardFilters.ts
│
├── components/
│   ├── DashboardCard.tsx
│   ├── DashboardModal.tsx
│   ├── KPIStatCard.tsx
│   ├── RelativeBarPanel.tsx
│   ├── GroupedBarChart.tsx
│   ├── PieDonutChart.tsx
│   ├── AnnualChart.tsx
│   ├── DashboardTooltip.tsx
│   ├── DashboardLegend.tsx
│   └── ExpandChartPage.tsx
│
├── utils/
│   ├── dashboardTheme.ts
│   ├── normalizeLabels.ts
│   ├── exportChart.ts
│   └── chartHelpers.ts
│
└── types/
    └── dashboard.ts
```

---

# STATE MANAGEMENT

Usar Zustand para cross-filtering global.

Todos los gráficos deben reaccionar automáticamente a filtros globales.

Crear store:

```ts
type DashboardFilters = {
  tipo?: string | null;
  region?: string | null;
  estado?: string | null;
  categoriaEconomica?: string | null;
  anio?: string | null;
};
```

Acciones:

```ts
setFilter();
clearFilters();
toggleFilter();
```

Comportamiento esperado:

Si el usuario hace click en:

- una región
- un tipo
- un estado
- una barra
- un segmento de pie chart

TODOS los gráficos:

- KPIs
- barras
- pie charts
- tablas
- gráficos anuales

deben actualizarse automáticamente.

---

# COMPONENTES VISUALES

## IMPORTANTE

NO quiero apariencia default de Recharts.

Debes crear wrappers y componentes custom con:

- MUI
- Framer Motion
- estilos modernos
- spacing profesional
- animaciones suaves

---

# COMPONENTE MÁS IMPORTANTE

## RelativeBarPanel.tsx

Este reemplaza los gráficos tipo:
"Fiscalización por Tipo"

IMPORTANTE:
NO usar Recharts para este componente.

Debe implementarse custom usando:

- divs
- flexbox
- Framer Motion

Debe verse casi idéntico a la plantilla de ejemplo.

Características:

- card enterprise
- header color primario
- iconos:
  - expandir
  - descargar

- barras horizontales relativas
- cantidad a la derecha
- tooltip mostrando porcentaje
- hover moderno
- selected state
- cross-filtering

La barra seleccionada:

- cambia de color
- se destaca
- filtra el resto del dashboard

Las demás:

- quedan atenuadas

Debe verse premium y moderno.

---

# CATEGORÍAS QUE DEBEN TENER DASHBOARD

Implementar dashboards completos para:

- Diario oficial - Normativas
- SEA - Pertinencias
- SEA - Proyectos evaluados
- SNIFA/SMA - Fiscalizaciones
- SNIFA/SMA - Sancionatorios
- SNIFA/SMA - Sanciones
- SNIFA/SMA - Programas de Cumplimiento
- SNIFA/SMA - Medidas provisionales
- SNIFA/SMA - Requerimientos de ingreso
- Tribunales Ambientales
- Consultas públicas - MMA

---

# DASHBOARD ESPECÍFICO: NORMATIVAS

Cada tipo tiene colores propios:

- General
- Particular
- Boletín Oficial Minería

Debe existir consistencia visual entre todos los gráficos.

Implementar:

- KPI Total Normativas
- Normativas por Tipo
- Normativas por Región
- Normativas por Año
- Normativas por Organismo

## IMPORTANTE

"Normativas por Organismo" debe rehacerse completamente.
Actualmente está visualmente horrible.

Debe:

- aprovechar bien el espacio
- tener labels legibles
- evitar superposición
- verse limpio y profesional

---

# TIPOS DE GRÁFICOS

## KPI Cards

Cards modernas:

- números grandes
- iconografía sutil
- colores del theme
- hover suave

---

## Pie Donut Chart

Debe:

- ser donut
- mostrar porcentaje
- mostrar cantidad
- tener leyenda SIEMPRE
- colores consistentes
- labels legibles

IMPORTANTE:
Actualmente solo muestra cantidades.
Debes mostrar porcentajes correctamente.

---

## Gráficos de barras horizontales

Para:

- regiones
- categorías económicas
- rankings

Características:

- labels legibles
- truncamiento inteligente
- NO superposición
- NO overflow
- spacing correcto
- barras modernas
- hover elegante

---

## Gráficos de barras agrupadas verticales

Para:

- comparativas anuales
- tipos por año
- tribunales por año

IMPORTANTE:
Actualmente muchos gráficos NO renderizan correctamente:

- en modal
- al descargar
- al expandir
- o en la vista normal

Debes solucionar TODOS esos problemas.

Los gráficos deben renderizar correctamente en:

- dashboard normal
- modal expandido
- descarga PNG/SVG
- página individual

---

# PROBLEMAS QUE DEBES SOLUCIONAR

## 1. Uso del espacio

Actualmente:

- hay mucho espacio blanco innecesario
- los gráficos son pequeños
- la distribución es mala

Debes:

- aprovechar mejor el ancho
- crear layouts enterprise
- usar grids modernos
- evitar espacios muertos

---

## 2. Labels largos

Actualmente:

- se salen del contenedor
- hacen overlap
- hacen saltos de línea innecesarios

Debes:

- implementar truncamiento inteligente
- tooltip para labels largos
- auto sizing
- mejor manejo de ejes
- ellipsis cuando corresponda

IMPORTANTE:
NO hacer salto de línea si aún existe espacio disponible.

---

## 3. Pie charts

Actualmente:

- no muestran porcentajes
- no tienen leyendas claras

Debes:

- agregar leyenda SIEMPRE
- mostrar:
  - porcentaje
  - cantidad
  - categoría

---

## 4. Problemas de renderizado

Actualmente muchos gráficos:

- desaparecen
- no muestran barras
- fallan en modal
- fallan al exportar
- fallan en página individual

Debes rehacer completamente el sistema de:

- resize
- responsive container
- export
- modal rendering

Usar:

- ResizeObserver
- dimensiones controladas
- layout estable

---

# NORMALIZACIÓN DE DATOS

Implementar helper:

```ts
normalizeLabels.ts;
```

Reglas:

## Estados equivalentes

Unificar:

```txt
archivada
archivadas
```

como:

```txt
Archivada
```

PERO:

```txt
Terminado - Absolución
Terminado - Sanción
```

NO deben unificarse.

---

## Categorías con "/"

Cuando exista:

```txt
Agroindustrias / Forestal
```

usar:

```txt
Agroindustrias
```

Otro ejemplo:

```txt
Subsecretaría de Agricultura / Servicio Agrícola y Ganadero / Región de Atacama
```

usar:

```txt
Subsecretaría de Agricultura
```

Aplicar esto automáticamente.

---

# REGLAS GENERALES DE VISUALIZACIÓN

## Por año

Usar:

- barras verticales

## Por año + múltiples tipos

Usar:

- barras agrupadas verticales

## Por tipo

Usar:

- barras horizontales relativas

## Por estado

Usar:

- donut chart

## Por categoría económica

Usar:

- barras horizontales

---

# MODAL DE EXPANSIÓN

TODOS los gráficos deben tener:

## Botón expandir

Abre modal fullscreen responsive.

## Modal debe incluir:

- gráfico grande
- descargar PNG/SVG
- abrir en otra página

---

# EXPORTACIÓN

Implementar export robusto:

- PNG
- SVG

NO guardar nada en base de datos.

---

# OPEN IN NEW PAGE

Debe abrir:

- página dedicada
- render standalone
- mismo theme
- mismos filtros

---

# THEME

NO hardcodear colores.

Usar:

- MUI theme
- palette.primary
- palette.secondary
- palette.background
- palette.text
- palette.divider

Debe soportar:

- dark mode
- light mode

---

# RESPONSIVE

Debe verse excelente en:

- desktop
- laptop
- tablet

---

# IMPORTANTE SOBRE RECHARTS

Usar Recharts SOLO para:

- pie charts
- annual charts
- grouped charts

NO usar Recharts para:

- RelativeBarPanel
- KPI cards
- filtros visuales

---

# UX

Priorizar:

1. Fidelidad visual
2. Calidad enterprise
3. Cross-filtering
4. UX
5. Arquitectura limpia
6. Responsive
7. Performance

sobre simplicidad.

---

# REFACTOR OBLIGATORIO

Mi DashboardView.tsx actual está demasiado grande.

Debes:

- dividir componentes
- separar lógica
- crear hooks
- crear utils
- mejorar mantenibilidad
- eliminar código duplicado

---

# RESULTADO ESPERADO

Quiero un dashboard:

- enterprise
- moderno
- elegante
- limpio
- altamente interactivo
- visualmente consistente
- parecido a PowerBI/Superset/Tableau

NO quiero dashboards básicos.
NO quiero apariencia default de librería.
Quiero calidad visual premium.
