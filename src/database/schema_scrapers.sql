-- ============================================================
-- schema_scrapers.sql  –  BioNews DB Scrapers
-- PostgreSQL 16
-- ============================================================

-- ── NOTICIAS ─────────────────────────────────────────────────────────────────
CREATE SCHEMA IF NOT EXISTS scrapers;
SET search_path TO scrapers;
CREATE TABLE IF NOT EXISTS noticias (
    link           TEXT PRIMARY KEY,
    titulo         TEXT,
    fecha          TEXT,
    imagen         TEXT,
    fuente         TEXT,
    fecha_scraping TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_noticias_fecha ON noticias (fecha DESC);
CREATE INDEX IF NOT EXISTS idx_noticias_scraping ON noticias (fecha_scraping DESC);

-- ── PERTINENCIAS (SEA) ────────────────────────────────────────────────────────
-- Nota: mantiene las mayúsculas de SQLite original usando comillas en las queries
CREATE TABLE IF NOT EXISTS pertinencias (
    "Expediente"        TEXT PRIMARY KEY,
    "Nombre_de_Proyecto" TEXT,
    "Proponente"        TEXT,
    "Fecha"             TEXT,
    "Estado"            TEXT,
    "Accion"            TEXT,
    fecha_scraping      TIMESTAMP,
    tipo_proyecto       TEXT,
    categoria_economica TEXT
);

CREATE INDEX IF NOT EXISTS idx_pertinencias_fecha ON pertinencias ("Fecha" DESC);
CREATE INDEX IF NOT EXISTS idx_pertinencias_scraping ON pertinencias (fecha_scraping DESC);

-- ── SEA PROYECTOS EVALUADOS ───────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS sea_proyectos_evaluados (
    id                  TEXT PRIMARY KEY,
    nombre              TEXT,
    titular             TEXT,
    via_ingreso         TEXT,
    estado_proyecto     TEXT,
    razon_ingreso       TEXT,
    fecha_presentacion  TEXT,
    subestado_proyecto  TEXT,
    tipo_proyecto       TEXT,
    categoria_economica TEXT,
    region              TEXT,
    url                 TEXT,
    fecha_scraping      TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_sea_fecha ON sea_proyectos_evaluados (fecha_presentacion DESC);

-- ── NORMATIVAS (Diario Oficial) ───────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS normativas (
    fecha          TEXT,
    normativa      TEXT,
    tipo_normativa TEXT,
    organismo      TEXT,
    suborganismo   TEXT,
    accion         TEXT PRIMARY KEY,
    fecha_scraping TEXT,
    ficha_id       INTEGER
);

CREATE INDEX IF NOT EXISTS idx_normativas_fecha ON normativas (fecha DESC);
CREATE INDEX IF NOT EXISTS idx_normativas_organismo ON normativas (organismo);

-- ── FISCALIZACIONES (SNIFA) ───────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS fiscalizaciones (
    expediente          TEXT PRIMARY KEY,
    nombre_razon_social TEXT,
    unidad_fiscalizable TEXT,
    categoria           TEXT,
    region              TEXT,
    estado              TEXT,
    detalle_link        TEXT,
    fecha_scraping      TIMESTAMP,
    ficha_id            INTEGER
);

CREATE INDEX IF NOT EXISTS idx_fisc_ficha ON fiscalizaciones (ficha_id DESC);
CREATE INDEX IF NOT EXISTS idx_fisc_scraping ON fiscalizaciones (fecha_scraping DESC);

-- ── MEDIDAS PROVISIONALES (SNIFA) ─────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS medidas_provisionales (
    expediente          TEXT PRIMARY KEY,
    nombre_razon_social TEXT,
    unidad_fiscalizable TEXT,
    categoria           TEXT,
    region              TEXT,
    estado              TEXT,
    detalle_link        TEXT,
    fecha_scraping      TIMESTAMP,
    ficha_id            INTEGER
);

CREATE INDEX IF NOT EXISTS idx_medidas_ficha ON medidas_provisionales (ficha_id DESC);

-- ── PROGRAMAS DE CUMPLIMIENTO (SNIFA) ────────────────────────────────────────
CREATE TABLE IF NOT EXISTS "programasDeCumplimiento" (
    expediente          TEXT PRIMARY KEY,
    nombre_razon_social TEXT,
    unidad_fiscalizable TEXT,
    categoria           TEXT,
    region              TEXT,
    estado              TEXT,
    detalle_link        TEXT,
    fecha_scraping      TIMESTAMP,
    ficha_id            INTEGER
);

CREATE INDEX IF NOT EXISTS idx_pdc_ficha ON "programasDeCumplimiento" (ficha_id DESC);

-- ── REGISTRO DE SANCIONES (SNIFA) ────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS "registroSanciones" (
    expediente          TEXT PRIMARY KEY,
    nombre_razon_social TEXT,
    unidad_fiscalizable TEXT,
    categoria           TEXT,
    region              TEXT,
    multa_uta           TEXT,
    pago_multa          TEXT,
    estado              TEXT,
    detalle_link        TEXT,
    fecha_scraping      TIMESTAMP,
    ficha_id            INTEGER
);

CREATE INDEX IF NOT EXISTS idx_rs_ficha ON "registroSanciones" (ficha_id DESC);

-- ── REQUERIMIENTOS (SNIFA) ────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS requerimientos (
    expediente          TEXT PRIMARY KEY,
    nombre_razon_social TEXT,
    unidad_fiscalizable TEXT,
    categoria           TEXT,
    region              TEXT,
    estado              TEXT,
    detalle_link        TEXT,
    fecha_scraping      TIMESTAMP,
    ficha_id            INTEGER
);

CREATE INDEX IF NOT EXISTS idx_req_ficha ON requerimientos (ficha_id DESC);

-- ── SANCIONATORIOS (SNIFA) ────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS sancionatorios (
    expediente          TEXT PRIMARY KEY,
    nombre_razon_social TEXT,
    unidad_fiscalizable TEXT,
    categoria           TEXT,
    region              TEXT,
    estado              TEXT,
    detalle_link        TEXT,
    fecha_scraping      TIMESTAMP,
    ficha_id            INTEGER
);

CREATE INDEX IF NOT EXISTS idx_sanc_ficha ON sancionatorios (ficha_id DESC);

-- ── TRIBUNALES ────────────────────────────────────────────────────────────────
-- Nota: Las columnas usan mayúsculas por compatibilidad con el código existente
CREATE TABLE IF NOT EXISTS "Tribunales" (
    "Rol"                   TEXT PRIMARY KEY,
    "Fecha"                 TEXT,
    "Caratula"              TEXT,
    "Tribunal"              TEXT,
    "Tipo_de_Procedimiento" TEXT,
    "Estado_Procesal"       TEXT,
    "Accion"                TEXT,
    fecha_scraping          TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_trib_tribunal ON "Tribunales" ("Tribunal");
CREATE INDEX IF NOT EXISTS idx_trib_fecha ON "Tribunales" ("Fecha" DESC);

-- ── DGA CONSULTAS ─────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS dga_consultas (
    id             TEXT PRIMARY KEY,
    nombre         TEXT,
    imagen         TEXT,
    url            TEXT,
    fecha_scraping TIMESTAMP
);

-- ── DOCUMENTOS (MINSAL / DGA) ─────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS documentos (
    id             SERIAL PRIMARY KEY,
    consulta_id    TEXT,
    tipo_consulta  TEXT,
    nombre_documento TEXT,
    link           TEXT
);

CREATE INDEX IF NOT EXISTS idx_docs_consulta ON documentos (consulta_id, tipo_consulta);

-- ── MINSAL RESULTADOS ─────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS minsal_resultados (
    id             TEXT PRIMARY KEY,
    titulo         TEXT,
    fecha_scraping TIMESTAMP
);

-- ── MINSAL VIGENTES ───────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS minsal_vigentes (
    id              TEXT PRIMARY KEY,
    titulo          TEXT,
    fecha_inicio    TEXT,
    periodo_consulta TEXT,
    indicaciones    TEXT,
    fecha_scraping  TIMESTAMP
);

-- ── MMA ABIERTAS ─────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS mma_abiertas (
    id                 TEXT PRIMARY KEY,
    nombre_instrumento TEXT,
    fecha_inicio       TEXT,
    fecha_termino      TEXT,
    tipo_instrumento   TEXT,
    tipo_proceso       TEXT,
    ambito_territorial TEXT,
    link_detalle       TEXT,
    fecha_scraping     TIMESTAMP
);

-- ── MMA CERRADAS ─────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS mma_cerradas (
    id                 TEXT PRIMARY KEY,
    nombre_instrumento TEXT,
    fecha_inicio       TEXT,
    fecha_termino      TEXT,
    tipo_instrumento   TEXT,
    ambito_territorial TEXT,
    link_detalle       TEXT,
    fecha_scraping     TIMESTAMP
);

-- ── SCRAPER LOGS ─────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS scraper_logs (
    fuente          TEXT PRIMARY KEY,
    ultimo_intento  TIMESTAMP,
    ultimo_exito    TIMESTAMP,
    estado          TEXT,
    error           TEXT,
    nuevos_registros INTEGER
);

-- ── OPTIMIZACIONES E ÍNDICES CRÍTICOS ─────────────────────────────────────────

-- 1. Habilitar extensión trigram para búsquedas rápidas con LIKE
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- 2. Índices de fecha_scraping para agilizar lectura de notificaciones (badges)
CREATE INDEX IF NOT EXISTS idx_sea_scraping ON sea_proyectos_evaluados (fecha_scraping DESC);
CREATE INDEX IF NOT EXISTS idx_normativas_scraping ON normativas (fecha_scraping DESC);
CREATE INDEX IF NOT EXISTS idx_tribunales_scraping ON "Tribunales" (fecha_scraping DESC);
CREATE INDEX IF NOT EXISTS idx_medidas_scraping ON medidas_provisionales (fecha_scraping DESC);

-- 3. Índices funcionales trigram GIN para búsquedas globales LIKE (LOWER(campo) LIKE '%...%')
CREATE INDEX IF NOT EXISTS idx_fisc_trgm_uf ON fiscalizaciones USING GIN (unidad_fiscalizable gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_fisc_trgm_rs ON fiscalizaciones USING GIN (nombre_razon_social gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_sea_trgm_nom ON sea_proyectos_evaluados USING GIN (nombre gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_sea_trgm_tit ON sea_proyectos_evaluados USING GIN (titular gin_trgm_ops);

-- 4. Índice funcional para optimizar el ordenamiento por fecha de presentación en Proyectos Evaluados
CREATE INDEX IF NOT EXISTS idx_sea_fecha_presentacion_date ON sea_proyectos_evaluados (to_date(nullif(fecha_presentacion, ''), 'DD/MM/YYYY') DESC);

