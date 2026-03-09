-- Database: Autos_Colombia

CREATE DATABASE "Autos_Colombia"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'es_CO.UTF-8'
    LC_CTYPE = 'es_CO.UTF-8'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- NOTE: The instructions imply that the tables should be created inside the Autos_Colombia database.
\c "Autos_Colombia"

CREATE TABLE IF NOT EXISTS vehiculo (
    placa   VARCHAR(6)  PRIMARY KEY,
    marca   VARCHAR(12) NOT NULL,
    modelo  VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS registro (
    id_registro    INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    placa_vehiculo VARCHAR(6)  NOT NULL,
    fecha_entrada  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    fecha_salida   TIMESTAMPTZ,
    CONSTRAINT fk_placa_vehiculo FOREIGN KEY (placa_vehiculo)
        REFERENCES vehiculo (placa)
);

CREATE TABLE IF NOT EXISTS novedad (
    id_novedad  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_registro INTEGER      NOT NULL,
    fecha       TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    descripcion VARCHAR(512) NOT NULL,
    CONSTRAINT fk_id_registro FOREIGN KEY (id_registro)
        REFERENCES registro (id_registro)
        ON DELETE CASCADE
);
