# Use the official PostgreSQL 16.4 image
FROM postgres:latest

# Initialize script to create the test database
COPY ./init-test-db.sh /docker-entrypoint-initdb.d/

# Expose PostgreSQL port
EXPOSE 5432

