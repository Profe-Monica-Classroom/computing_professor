/*
   DEMOSTRACIÓN DE BASE DE DATOS - CLASE INTRODUCTORIA
   ---------------------------------------------------
   Instrucciones para la Profe:
   1. Copie todo este contenido.
   2. Vaya a https://www.db-fiddle.com/
   3. Pegue este código en la columna izquierda (Schema SQL).
   4. Presione el botón "Run".
   5. Use la columna derecha para hacer las consultas (al final de este archivo).
*/

-- ---------------------------------------------------------
-- 1. ESTRUCTURA (DDL)
-- ---------------------------------------------------------

-- TABLA 1: PERSONA
-- Guardamos los datos comunes. Así no repetimos nombre y apellido 
-- si alguien es profesor y estudiante a la vez.
CREATE TABLE Persona (
    id_persona INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(20) UNIQUE,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100),
    tipo ENUM('Estudiante', 'Profesor') NOT NULL
);

-- TABLA 2: ASIGNATURA
-- Lista de materias disponibles.
CREATE TABLE Asignatura (
    codigo_asignatura VARCHAR(10) PRIMARY KEY,
    nombre_materia VARCHAR(100) NOT NULL,
    creditos INT DEFAULT 3
);

-- TABLA 3: ESTUDIANTE_INSCRITO (Relación N:M)
-- Conecta: ¿Qué persona (estudiante) ve qué materia?
CREATE TABLE Estudiante_Inscrito (
    id_inscripcion INT AUTO_INCREMENT PRIMARY KEY,
    id_persona INT,                 -- Quién
    codigo_asignatura VARCHAR(10),  -- Qué materia
    fecha_inscripcion DATE,
    FOREIGN KEY (id_persona) REFERENCES Persona(id_persona),
    FOREIGN KEY (codigo_asignatura) REFERENCES Asignatura(codigo_asignatura)
);

-- TABLA 4: PROFESOR_DICTA (Relación N:M)
-- Conecta: ¿Qué persona (profesor) da qué materia?
CREATE TABLE Profesor_Dicta (
    id_carga INT AUTO_INCREMENT PRIMARY KEY,
    id_persona INT,                 -- Quién
    codigo_asignatura VARCHAR(10),  -- Qué materia
    turno VARCHAR(20),              -- Mañana, Tarde, Noche
    FOREIGN KEY (id_persona) REFERENCES Persona(id_persona),
    FOREIGN KEY (codigo_asignatura) REFERENCES Asignatura(codigo_asignatura)
);

-- ---------------------------------------------------------
-- 2. DATOS DE PRUEBA (DML)
-- ---------------------------------------------------------

-- Personas
INSERT INTO Persona (dni, nombre, apellido, email, tipo) VALUES 
('V-123456', 'Mónica', 'Pérez', 'monica@unexpo.edu', 'Profesor'),
('V-987654', 'Roberto', 'Gómez', 'roberto@unexpo.edu', 'Profesor'),
('V-111111', 'Juan', 'Rodríguez', 'juan@mail.com', 'Estudiante'),
('V-222222', 'Ana', 'Silva', 'ana@mail.com', 'Estudiante');

-- Asignaturas
INSERT INTO Asignatura (codigo_asignatura, nombre_materia, creditos) VALUES 
('BD-1', 'Base de Datos I', 4),
('PROG-2', 'Programación II', 3);

-- Relaciones (Inscripciones y Cargas)
INSERT INTO Profesor_Dicta (id_persona, codigo_asignatura, turno) VALUES 
(1, 'BD-1', 'Mañana'),   -- Mónica da BD
(2, 'PROG-2', 'Tarde');  -- Roberto da Progra

INSERT INTO Estudiante_Inscrito (id_persona, codigo_asignatura, fecha_inscripcion) VALUES 
(3, 'BD-1', '2024-01-20'),    -- Juan ve BD
(3, 'PROG-2', '2024-01-21'),  -- Juan ve Progra
(4, 'PROG-2', '2024-01-22');  -- Ana ve Progra

/*
   ---------------------------------------------------------
   3. CONSULTAS PARA LA CLASE (Copiar y pegar a la derecha)
   ---------------------------------------------------------
   
   -- CONSULTA A: Ver lista de estudiantes en Base de Datos I
   SELECT p.nombre, p.apellido 
   FROM Estudiante_Inscrito e
   JOIN Persona p ON e.id_persona = p.id_persona
   WHERE e.codigo_asignatura = 'BD-1';

   -- CONSULTA B: Ver qué materias da la Profe Mónica
   SELECT a.nombre_materia, pr.turno
   FROM Profesor_Dicta pr
   JOIN Persona p ON pr.id_persona = p.id_persona
   JOIN Asignatura a ON pr.codigo_asignatura = a.codigo_asignatura
   WHERE p.nombre = 'Mónica';
*/
