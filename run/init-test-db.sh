#!/bin/bash
set -e

# Check if the test database exists, and create it if it doesn't
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" -tc "SELECT 1 FROM pg_database WHERE datname = 'gap_python_ai_workshop_test'" | grep -q 1 || psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE "gap_python_ai_workshop_test";
EOSQL

