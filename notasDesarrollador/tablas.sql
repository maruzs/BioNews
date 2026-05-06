Table: fiscalizaciones
expediente (TEXT) PK
nombre_razon_social (TEXT)
unidad_fiscalizable (TEXT)
categoria (TEXT)
region (TEXT)
estado (TEXT)
detalle_link (TEXT)
fecha_scraping (TIMESTAMP)

Table: programasDeCumplimiento
expediente (TEXT) PK
unidad_fiscalizable (TEXT)
nombre_razon_social (TEXT)
categoria (TEXT)
region (TEXT)
detalle_link (TEXT)
fecha_scraping (TIMESTAMP)

Table: registroSanciones
expediente (TEXT) PK
unidad_fiscalizable (TEXT)
nombre_razon_social (TEXT)
categoria (TEXT)
region (TEXT)
multa_uta (TEXT)
pago_multa (TEXT)
detalle_link (TEXT)
fecha_scraping (TIMESTAMP)

Table: requerimientos
expediente (TEXT) PK
unidad_fiscalizable (TEXT)
nombre_razon_social (TEXT)
categoria (TEXT)
region (TEXT)
detalle_link (TEXT)
fecha_scraping (TIMESTAMP)

Table: sancionatorios
expediente (TEXT) PK
unidad_fiscalizable (TEXT)
nombre_razon_social (TEXT)
categoria (TEXT)
region (TEXT)
estado (TEXT)
detalle_link (TEXT)
fecha_scraping (TIMESTAMP)

Table: medidas_provisionales
expediente (TEXT) PK
unidad_fiscalizable (TEXT)
nombre_razon_social (TEXT)
categoria (TEXT)
region (TEXT)
estado (TEXT)
detalle_link (TEXT)
fecha_scraping (TIMESTAMP)

Table: sqlite_sequence
name ()
seq ()

Table: Tribunales
Rol (TEXT) PK
Fecha (TEXT)
Caratula (TEXT)
Tribunal (TEXT)
Tipo_de_Procedimiento (TEXT)
Estado_Procesal (TEXT)
Accion (TEXT)
fecha_scraping (TIMESTAMP)

Table: pertinencias
Expediente (TEXT) PK
Nombre_de_Proyecto (TEXT)
Proponente (TEXT)
Fecha (TEXT)
Estado (TEXT)
Accion (TEXT)
fecha_scraping (TIMESTAMP)

Table: normativas
fecha (TEXT)
normativa (TEXT)
tipo_normativa (TEXT)
organismo (TEXT)
suborganismo (TEXT)
accion (TEXT)
fecha_scraping (TIMESTAMP)

Table: noticias
link (TEXT) PK
titulo (TEXT)
fecha (TEXT)
imagen (TEXT)
fuente (TEXT)
fecha_scraping (TIMESTAMP)

Table: scraper_logs
fuente (TEXT) PK
ultimo_intento (TIMESTAMP)
ultimo_exito (TIMESTAMP)
estado (TEXT)
error (TEXT)
nuevos_registros (INTEGER)

Table: favoritos
user_id (INTEGER) PK
id_o_link (TEXT) PK
fuente (TEXT)
nombre (TEXT)
fecha_agregado (TIMESTAMP)
accion (TEXT)

Table: users
id (INTEGER) PK
name (TEXT)
email (TEXT)
password_hash (TEXT)
role (TEXT)
blocked (INTEGER)
preferences (TEXT)
last_login (TIMESTAMP)
