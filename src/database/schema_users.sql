-- ============================================================
-- schema_users.sql  –  BioNews DB Usuarios
-- PostgreSQL 16
-- ============================================================
-- Este archivo se monta en /docker-entrypoint-initdb.d/
-- y se ejecuta automáticamente cuando el contenedor se crea
-- por primera vez con un volumen vacío.
-- ============================================================

-- Extensiones útiles
CREATE EXTENSION IF NOT EXISTS pgcrypto;  -- para gen_random_uuid() si se necesita en el futuro

-- ── USERS ────────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS users (
    id           SERIAL PRIMARY KEY,
    name         TEXT,
    email        TEXT UNIQUE NOT NULL,
    password_hash TEXT,
    role         TEXT DEFAULT 'user',
    blocked      INTEGER DEFAULT 0,
    preferences  TEXT DEFAULT '{}',
    last_login   TIMESTAMP
);

-- ── FAVORITOS ────────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS favoritos (
    user_id      INTEGER NOT NULL,
    id_o_link    TEXT    NOT NULL,
    fuente       TEXT,
    nombre       TEXT,
    fecha_agregado TIMESTAMP,
    accion       TEXT,
    PRIMARY KEY (user_id, id_o_link)
    -- No FK cross-DB. La integridad se valida en la app.
);

CREATE INDEX IF NOT EXISTS idx_favoritos_user ON favoritos (user_id);
CREATE INDEX IF NOT EXISTS idx_favoritos_fuente ON favoritos (fuente);

-- ── USER CATEGORY VIEWS ───────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS user_category_views (
    id             SERIAL PRIMARY KEY,
    user_id        INTEGER NOT NULL,
    category_slug  TEXT    NOT NULL,
    last_exit_at   TIMESTAMP,
    UNIQUE (user_id, category_slug)
);

CREATE INDEX IF NOT EXISTS idx_ucv_user ON user_category_views (user_id);

-- ── USER ITEM VIEWS ───────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS user_item_views (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER NOT NULL,
    item_id_or_link TEXT    NOT NULL,
    category_slug   TEXT    NOT NULL,
    viewed_at       TIMESTAMP,
    UNIQUE (user_id, item_id_or_link, category_slug)
);

CREATE INDEX IF NOT EXISTS idx_uiv_user_cat ON user_item_views (user_id, category_slug);

-- ── BUG REPORTS ──────────────────────────────────────────────────────────────
CREATE TABLE IF NOT EXISTS bug_reports (
    id              SERIAL PRIMARY KEY,
    user_id         INTEGER,
    titulo          TEXT,
    descripcion     TEXT,
    screenshot_path TEXT,
    fecha_reporte   TIMESTAMP,
    status          TEXT DEFAULT 'pendiente'
);

CREATE INDEX IF NOT EXISTS idx_bug_user ON bug_reports (user_id);
CREATE INDEX IF NOT EXISTS idx_bug_status ON bug_reports (status);
