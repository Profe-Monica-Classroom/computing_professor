-- Script para crear la tabla de usuarios en MySQL
-- Ejecutar en la base de datos: computacion1

CREATE TABLE IF NOT EXISTS usuario (
  idusuario INT NOT NULL AUTO_INCREMENT,
  usuario VARCHAR(50) NOT NULL,
  password VARCHAR(50) NOT NULL,
  PRIMARY KEY (idusuario)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Insertar usuario administrador por defecto
-- Usuario: admin
-- Clave: 1234
INSERT INTO usuario (usuario, password) VALUES ('admin', '1234');
