
CREATE TABLE Usuario
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

CREATE TABLE Tipo_usuario
(
id_tipo_usuario INT AUTO_INCREMENT PRIMARY KEY,
tipo_usuario VARCHAR(13) NOT NULL UNIQUE
);

CREATE TABLE Escuela
(
id_escuela INT AUTO_INCREMENT PRIMARY KEY,
escuela VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE Paciente
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
id_usuario INT NOT NULL
);

CREATE TABLE Tipo_Sangre
(
id_tipo_sangre INT  AUTO_INCREMENT PRIMARY KEY,
tipo_sangre VARCHAR(3) NOT NULL UNIQUE
);

CREATE TABLE Documento_Paciente
(
id_documento_paciente INT AUTO_INCREMENT PRIMARY KEY,
id_documento INT NOT NULL,
id_paciente INT NOT NULL
-- Posibles datos de documentos (consentimeientos informados, avisos, etc)
);

CREATE TABLE Documento
(
id_documento INT AUTO_INCREMENT PRIMARY KEY,
documento_name VARCHAR(50) NOT NULL,
id_tipo_documento INT NOT NULL DEFAULT(1)
);

CREATE TABLE Tipo_Documento
(
id_tipo_documento INT AUTO_INCREMENT PRIMARY KEY,
tipo_doucmento VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Cita
(
id_cita INT AUTO_INCREMENT PRIMARY KEY,
cita_date DATETIME NOT NULL DEFAULT(CURRENT_TIMESTAMP),
cita_duracion TIME NOT NULL DEFAULT('01:00:00'),
cita_nota VARCHAR(200),
id_paciente INT NOT NULL,
id_consultorio INT NOT NULL,
id_estado_cita INT NOT NULL,
id_tratamiento INT NOT NULL
);

CREATE TABLE Tratamiento
(
id_tratamiento INT AUTO_INCREMENT PRIMARY KEY,
tratamiento_name VARCHAR(25) NOT NULL UNIQUE
);

CREATE TABLE Estado_Cita
(
id_estado_cita INT AUTO_INCREMENT PRIMARY KEY,
estado_cita VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Nota_Evolucion
(
id_nota_evolucion INT AUTO_INCREMENT PRIMARY KEY,
nota_evolucion VARCHAR(300) NOT NULL DEFAULT('FALTAN DATOS - GENERADA ACCIDENTALMENTE'),
id_paciente INT NOT NULL
);

CREATE TABLE Consultorio
(
id_consultorio INT AUTO_INCREMENT PRIMARY KEY,
conultorio_name VARCHAR(50) NOT NULL UNIQUE,
consultorio_calle VARCHAR(100),
consultorio_colonia VARCHAR(100),
consultorio_num_exterior VARCHAR(3),
consultorio_num_interior VARCHAR(3),
consultorio_localidad VARCHAR(100),
consultorio_telefono VARCHAR(13),
consultorio_telefono_dos VARCHAR(13)
id_estado INT NOT NULL
);

CREATE TABLE Estado
(
id_estado INT AUTO_INCREMENT PRIMARY KEY,
estado VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Medicamento
(
id_medicamento INT AUTO_INCREMENT PRIMARY KEY,
medicamento_name VARCHAR(50) NOT NULL,
medicamento_cantidad INT UNSIGNED NOT NULL,
medicamento_min TINYINT UNSIGNED NOT NULL,
medicamento_caducidad DATE NOT NULL,
medicamento_dosis VARCHAR(255) NOT NULL,
medicamento_costo DECIMAL(5,2) NOT NULL,
id_denominacion_general INT,
id_denominacion_quimica INT,
id_consultorio INT NOT NULL,
id_via_administrar_medicamento INT NOT NULL DEFAULT(1)
);

CREATE TABLE Via_Administrar_Medicamento
(
id_via_administrar_medicamento INT AUTO_INCREMENT PRIMARY KEY,
via_administrar_medicmamento VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE Denominacion_General
(
id_denominacion_general INT AUTO_INCREMENT PRIMARY KEY,
denominacion_general VARCHAR(100) NOT NULL
);

CREATE TABLE Denominacion_Quimica
(
id_denominacion_quimica INT AUTO_INCREMENT PRIMARY KEY,
denominacion_quimica VARCHAR(100) NOT NULL
);

CREATE TABLE Ticket_Medicamento
(
id_ticket_medicamento INT AUTO_INCREMENT PRIMARY KEY,
id_ticket INT NOT NULL,
id_medicamento INT NOT NULL,
cant_medicamento INT NOT NULL,
medicina_costo_unidad DECIMAL(10,2) NOT NULL
);

CREATE TABLE Ticket
(
id_ticket INT AUTO_INCREMENT PRIMARY KEY,
ticket_date DATETIME NOT NULL DEFAULT(CURRENT_TIMESTAMP),
id_tipo_pago INT NOT NULL
);

CREATE TABLE Tipo_Pago
(
id_tipo_pago INT AUTO_INCREMENT PRIMARY KEY,
tipo_pago VARCHAR(50) NOT NULL
);

CREATE TABLE Ticket_Caja
(
id_ticket_caja INT AUTO_INCREMENT PRIMARY KEY,
id_ticket INT NOT NULL,
id_corte_caja INT NOT NULL
);

CREATE TABLE Corte_Caja
(
id_corte_caja INT AUTO_INCREMENT PRIMARY KEY,
id_usuario INT NOT NULL,
cant_total DECIMAL(20,2) NOT NULL,
DESC Medicamento;
corte_caja_date DATETIME NOT NULL DEFAULT(CURRENT_TIMESTAMP)
);

CREATE TABLE Via_Administrar_Medicamento
(
id_via_administrar_medicamento INT AUTO_INCREMENT PRIMARY KEY,
via_administrar_medicamento VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE Receta_Medicamento
(
id_receta_medicamento INT AUTO_INCREMENT PRIMARY KEY,
id_receta INT NOT NULL,
id_medicamento INT NOT NULL,
receta_medicamento_dosis VARCHAR(300),
receta_medicamento_frecuencia VARCHAR(300),
receta_medicamento_duracion VARCHAR(300),
receta_medicamento_indicaciones VARCHAR(300)
);
CREATE TABLE Receta
(
id_receta INT AUTO_INCREMENT PRIMARY KEY,
id_usuario INT NOT NULL,
id_paciente INT NOT NULL,
receta_alergias VARCHAR(300),
receta_imc DOUBLE(5,3),
receta_precion_arterial VARCHAR(12),
receta_edad VARCHAR(3),
receta_diganostico VARCHAR(500)
);
