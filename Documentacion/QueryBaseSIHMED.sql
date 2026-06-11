
CREATE TABLE Usuarios
(
id_usuario INT AUTO_INCREMENT PRIMARY KEY,
usuario_name VARCHAR(50) NOT NULL,
usuario_paterno VARCHAR(50) NOT NULL,
usuario_materno VARCHAR(50) NOT NULL,
usuario_password VARCHAR(100) NOT NULL,
usuario_cedula_profesional VARCHAR(13) UNIQUE,
usuario_cedula_especialidad VARCHAR(13) UNIQUE,
id_tipo_usuario INT NOT NULL,
id_consultorio INT NOT NULL,
id_escuela INT NOT NULL
);

CREATE TABLE Tipos_usuarios
(
id_tipo_usuario INT AUTO_INCREMENT PRIMARY KEY,
tipo_usuario VARCHAR(13) NOT NULL UNIQUE
);

CREATE TABLE Escuelas
(
id_escuela INT AUTO_INCREMENT PRIMARY KEY,
escuela VARCHAR(100) NOT NULL UNIQUE,
);

CREATE TABLE Pacientes
(
id_paciente INT AUTO_INCREMENT PRIMARY KEY,
paciente_name VARCHAR(50) NOT NULL,
paciente_paterno VARCHAR(50) NOT NULL,
paciente_materno VARCHAR(50) NOT NULL,
paciente_telefono VARCHAR(13) NOT NULL UNIQUE,
paciente_numero_emergencia1 VARCHAR(13) NOT NULL,
paciente_numero_emergencia2 VARCHAR(13),
paciente_nss VARCHAR(8),
id_tipo_sangre INT NOT NULL,
id_consultorio INT NOT NULL,
id_usuario INT NOT NULL,
);

CREATE TABLE Tipos_sangres
(
id_tipo_sangre INT PRIMARY AUTO_INCREMENT,
tipo_sangre VARCHAR(3) NOT NULL UNIQUE,
);

CREATE TABLE Documentos_pacientes
(
id_documento_paciente INT AUTO_INCREMENT PRIMARY KEY,
id_documento INT NOT NULL,
id_paciente INT NOT NULL
-- Posibles datos de documentos (consentimeientos informados, avisos, etc)
);

CREATE TABLE Documentos
(
id_documento INT AUTO_INCREMENT PRIMARY KEY,
documento_name VARCHAR(50) INT NOT NULL,
id_tipo_documento INT NOT NULL DEFAULT(1)
);

CREATE TABLE Tipos_documentos
(
id_tipo_documento INT AUTO_INCREMENT PRIMARY KEY,
tipo_doucmento VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Citas
(
id_cita INT AUTO_INCREMENT PRIMARY KEY,
cita_date DATETIME NOT NULL DEFAULT(TIMESTAMP)
cita_duracion TIME NOT NULL DEFAULT('01:00:00')
cita_nota VARCHAR(200),
id_paciente INT NOT NULL,
id_consultorio INT NOT NULL,
id_estado_cita INT NOT NULL,
id_tratamiento INT NOT NULL
);

CREATE TABLE Tratamientos
(
id_tratamiento INT AUTO_INCREMENT PRIMARY KEY,
tratamiento_name VARCHAR(25) NOT NULL UNIQUE
);

CREATE TABLE Estado_cita
(
id_estado_cita INT AUTO_INCREMENT PRIMARY KEY,
estado_cita VARCHAR(50) NOT NULL UNIQUE,
);
