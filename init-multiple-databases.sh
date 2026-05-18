#!/bin/bash
# =============================================================
# BioNews - PostgreSQL Multi-Database Initializer
# =============================================================
# Este script se monta en /docker-entrypoint-initdb.d/ y se
# ejecuta automáticamente la primera vez que el contenedor
# de PostgreSQL arranca con un volumen de datos vacío.
#
# Lee la variable de entorno POSTGRES_MULTIPLE_DATABASES
# (lista separada por comas) y crea cada base de datos
# lógica, otorgando todos los privilegios al usuario admin.
# =============================================================

set -e
set -u

# Función principal que crea cada base de datos
create_user_and_database() {
    local database=$1
    echo "  [init-db] Creando base de datos: '$database'"
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
        CREATE DATABASE "$database";
        GRANT ALL PRIVILEGES ON DATABASE "$database" TO "$POSTGRES_USER";
EOSQL
    echo "  [init-db] Base de datos '$database' creada correctamente."
}

# Solo actúa si la variable de entorno está definida
if [ -n "${POSTGRES_MULTIPLE_DATABASES:-}" ]; then
    echo "============================================================"
    echo " BioNews: Inicializando múltiples bases de datos..."
    echo "============================================================"

    # Dividir por comas e iterar
    for db in $(echo "$POSTGRES_MULTIPLE_DATABASES" | tr ',' ' '); do
        create_user_and_database "$db"
    done

    echo "============================================================"
    echo " BioNews: Todas las bases de datos han sido creadas."
    echo "============================================================"
fi
