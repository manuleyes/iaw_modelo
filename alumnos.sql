DROP DATABASE IF EXISTS mleyes;
CREATE DATABASE mleyes;

USE mleyes;

DROP TABLE IF EXISTS alumnos;
CREATE TABLE alumnos
(
    id     INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nota1  INT          NOT NULL,
    nota2  INT          NOT NULL,
    nota3  INT          NOT NULL
);

INSERT INTO alumnos (nombre, nota1, nota2, nota3) VALUES ('JUANA', 1, 6, 4);
INSERT INTO alumnos (nombre, nota1, nota2, nota3) VALUES ('PEDRO', 4, 8, 9);
INSERT INTO alumnos (nombre, nota1, nota2, nota3) VALUES ('LUIS', 6, 1, 1);
INSERT INTO alumnos (nombre, nota1, nota2, nota3) VALUES ('MARIA', 4, 4, 6);
INSERT INTO alumnos (nombre, nota1, nota2, nota3) VALUES ('ONGOMBO', 6, 3, 1);
INSERT INTO alumnos (nombre, nota1, nota2, nota3) VALUES ('MARIA LUCIA', 4, 1, 2);
INSERT INTO alumnos (nombre, nota1, nota2, nota3) VALUES ('FERNANDO', 6, 4, 6);
