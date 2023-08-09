FROM postgres:latest
LABEL description="Postgres Image for reddit r/Health daily top post data"
COPY dump.sql /docker-entrypoint-initdb.d/
