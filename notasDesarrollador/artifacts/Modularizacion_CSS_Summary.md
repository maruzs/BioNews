# Modularización CSS — Resumen de cambios

## Estado final del build

✅ `tsc --noEmit` → 0 errores  
✅ `npm run build` → Exitoso (4129 módulos)

---

## Nueva estructura de carpetas creada

```
web/src/
├── index.css                          ← LIMPIADO: solo reset, variables, .app-container, scroll global
├── App.tsx                            ← ACTUALIZADO: imports desde nuevas rutas
│
├── components/
│   ├── Layout/
│   │   ├── Sidebar/
│   │   │   ├── Sidebar.tsx            ← NUEVO (refactorizado con CSS modules)
│   │   │   └── Sidebar.module.css     ← NUEVO (extraído de index.css + inline styles)
│   │   └── TopHeader/
│   │       ├── TopHeader.tsx          ← NUEVO (extraído de App.tsx como componente)
│   │       └── TopHeader.module.css   ← NUEVO (dropdown usuario, área mainContent)
│   │
│   ├── Pages/
│   │   ├── Auth/
│   │   │   ├── Login.tsx              ← NUEVO (refactorizado)
│   │   │   ├── Register.tsx           ← NUEVO (refactorizado)
│   │   │   ├── Landing.tsx            ← NUEVO (refactorizado)
│   │   │   └── Auth.module.css        ← NUEVO (compartido Login+Register+Landing)
│   │   ├── Home/
│   │   │   ├── Home.tsx               ← NUEVO (refactorizado)
│   │   │   └── Home.module.css        ← NUEVO
│   │   ├── News/
│   │   │   ├── NewsPage.tsx           ← NUEVO (refactorizado)
│   │   │   └── NewsPage.module.css    ← NUEVO
│   │   ├── Profile/
│   │   │   ├── Profile.tsx            ← NUEVO (refactorizado)
│   │   │   └── Profile.module.css     ← NUEVO
│   │   └── Admin/
│   │       ├── AdminPanel.tsx         ← NUEVO (refactorizado)
│   │       ├── AdminBugsPage.tsx      ← NUEVO (refactorizado)
│   │       └── Admin.module.css       ← NUEVO (compartido Panel+Bugs)
│   │
│   ├── Shared/
│   │   └── ReportLayout/
│   │       ├── ReportLayout.tsx       ← barrel re-export (apunta al original)
│   │       └── ReportLayout.module.css ← NUEVO (listo para migrar el .tsx)
│   │
│   ├── ConsultasPage/                 ← barrel re-exports (MINSALConsultasPage, MMAConsultasPage, DGAConsultasPage)
│   ├── SEAEvaluadosPage/              ← barrel re-export
│   └── BugReportPage/                 ← barrel re-export
│
│   [Archivos originales conservados para compatibilidad]
│   ├── ReportLayout.tsx               ← original (apuntado por barrel de Shared)
│   ├── MINSALConsultasPage.tsx        ← original (aún no migrado)
│   ├── MMAConsultasPage.tsx           ← original (aún no migrado)
│   ├── DGAConsultasPage.tsx           ← original (aún no migrado)
│   ├── SEAEvaluadosPage.tsx           ← original (aún no migrado)
│   ├── BugReportPage.tsx              ← original (aún no migrado)
│   └── DashboardView.tsx              ← original (sin cambios)
```

---

## Qué se hizo en cada fase

### Fase 1 — index.css limpiado

- Removidas: todas las clases de componentes específicos (sidebar, top-header, report, cards, tabla, noticias, perfil)
- Conservadas: `:root` variables, reset global, `.app-container`, scrollbar global, `.mobile-only` / `.desktop-only`

### Fase 2 — Layout (Sidebar + TopHeader)

- **Sidebar.module.css**: todos los estilos del sidebar extraídos de `index.css` + inline styles convertidos a clases descriptivas (`.sessionAvatar`, `.mobileMenuDropdown`, `.notifDot`, etc.)
- **TopHeader**: extraído de `App.tsx` como componente independiente con su propio módulo CSS (dropdown de usuario, `.userPill`, `.userAvatar`, `.mainContent`)

### Fase 3 — Páginas específicas

- **Auth.module.css**: compartido entre Login, Register y Landing
- **Home.module.css**: búsqueda global, stats cards, tabla de logs de scrapers
- **NewsPage.module.css**: cards de noticias, filtros, chips de fuente (eliminados `onMouseEnter/Leave` con `:hover` CSS)
- **Profile.module.css**: grid de datos personales, checkboxes de preferencias
- **Admin.module.css**: tabs, cards del panel, scheduler, debug console, modal de bugs

### Fase 4 — Shared (ReportLayout)

- **ReportLayout.module.css**: creado con todos los estilos de la barra de control, filtros avanzados, botones de acción
- El `.tsx` de ReportLayout es muy grande (1004 líneas) — se dejó el barrel re-export para una sesión de migración incremental posterior

---

## Componentes pendientes de migración completa (archivos originales no tocados)

Estos archivos tienen sus barrel re-exports creados y sus CSS modules están listos o son el siguiente paso:

| Componente                | Estado                                          |
| ------------------------- | ----------------------------------------------- |
| `ReportLayout.tsx`        | CSS module creado, .tsx pendiente (1004 líneas) |
| `MINSALConsultasPage.tsx` | Barrel re-export, pendiente                     |
| `MMAConsultasPage.tsx`    | Barrel re-export, pendiente                     |
| `DGAConsultasPage.tsx`    | Barrel re-export, pendiente                     |
| `SEAEvaluadosPage.tsx`    | Barrel re-export, pendiente                     |
| `BugReportPage.tsx`       | Barrel re-export, pendiente                     |

> **Nota**: Los componentes de `dashboard/` (KPIStatCard, RelativeBarPanel, AnnualChart, etc.) usan MUI `sx` prop que es el sistema de estilos propio de Material UI — no requieren CSS modules porque el scope ya está garantizado por MUI.
