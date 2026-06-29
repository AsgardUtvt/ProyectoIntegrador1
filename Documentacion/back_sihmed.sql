/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-11.8.6-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: sihmed
-- ------------------------------------------------------
-- Server version	11.8.6-MariaDB-0+deb13u1 from Debian

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `Cita`
--

DROP TABLE IF EXISTS `Cita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cita` (
  `id_cita` int(11) NOT NULL AUTO_INCREMENT,
  `cita_date` datetime NOT NULL DEFAULT current_timestamp(),
  `cita_duracion` time NOT NULL DEFAULT '01:00:00',
  `cita_nota` varchar(200) DEFAULT NULL,
  `id_paciente` int(11) NOT NULL,
  `id_consultorio` int(11) NOT NULL,
  `id_estado_cita` int(11) NOT NULL,
  `id_tratamiento` int(11) NOT NULL,
  PRIMARY KEY (`id_cita`),
  KEY `FK_PACIENTE_CITA` (`id_paciente`),
  KEY `FK_CONSULTORIO_CITA` (`id_consultorio`),
  KEY `FK_ESTADOCITA_CITA` (`id_estado_cita`),
  KEY `FK_TRATAMIENTO_CITA` (`id_tratamiento`),
  CONSTRAINT `FK_CONSULTORIO_CITA` FOREIGN KEY (`id_consultorio`) REFERENCES `Consultorio` (`id_consultorio`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_ESTADOCITA_CITA` FOREIGN KEY (`id_estado_cita`) REFERENCES `Estado_Cita` (`id_estado_cita`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_PACIENTE_CITA` FOREIGN KEY (`id_paciente`) REFERENCES `Paciente` (`id_paciente`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_TRATAMIENTO_CITA` FOREIGN KEY (`id_tratamiento`) REFERENCES `Tratamiento` (`id_tratamiento`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cita`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Cita` WRITE;
/*!40000 ALTER TABLE `Cita` DISABLE KEYS */;
/*!40000 ALTER TABLE `Cita` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Consultorio`
--

DROP TABLE IF EXISTS `Consultorio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Consultorio` (
  `id_consultorio` int(11) NOT NULL AUTO_INCREMENT,
  `conultorio_name` varchar(50) NOT NULL,
  `consultorio_calle` varchar(100) DEFAULT NULL,
  `consultorio_colonia` varchar(100) DEFAULT NULL,
  `consultorio_num_exterior` varchar(3) DEFAULT NULL,
  `consultorio_num_interior` varchar(3) DEFAULT NULL,
  `consultorio_localidad` varchar(100) DEFAULT NULL,
  `id_estado` int(11) NOT NULL,
  `consultorio_telefono` varchar(13) DEFAULT NULL,
  `consultorio_telefono_dos` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`id_consultorio`),
  UNIQUE KEY `conultorio_name` (`conultorio_name`),
  KEY `FK_ESTADO_CONSULTORIO` (`id_estado`),
  CONSTRAINT `FK_CONSULTORIO_ESTADO` FOREIGN KEY (`id_estado`) REFERENCES `Estado` (`id_estado`),
  CONSTRAINT `FK_ESTADO_CONSULTORIO` FOREIGN KEY (`id_estado`) REFERENCES `Estado` (`id_estado`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Consultorio`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Consultorio` WRITE;
/*!40000 ALTER TABLE `Consultorio` DISABLE KEYS */;
/*!40000 ALTER TABLE `Consultorio` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Corte_Caja`
--

DROP TABLE IF EXISTS `Corte_Caja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Corte_Caja` (
  `id_corte_caja` int(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` int(11) NOT NULL,
  `cant_total` decimal(20,2) NOT NULL,
  `corte_caja_date` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id_corte_caja`),
  KEY `FK_USUARIO_CORTECAJA` (`id_usuario`),
  CONSTRAINT `FK_USUARIO_CORTECAJA` FOREIGN KEY (`id_usuario`) REFERENCES `Usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Corte_Caja`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Corte_Caja` WRITE;
/*!40000 ALTER TABLE `Corte_Caja` DISABLE KEYS */;
/*!40000 ALTER TABLE `Corte_Caja` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Denominacion_General`
--

DROP TABLE IF EXISTS `Denominacion_General`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Denominacion_General` (
  `id_denominacion_general` int(11) NOT NULL AUTO_INCREMENT,
  `denominacion_general` varchar(100) NOT NULL,
  PRIMARY KEY (`id_denominacion_general`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Denominacion_General`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Denominacion_General` WRITE;
/*!40000 ALTER TABLE `Denominacion_General` DISABLE KEYS */;
/*!40000 ALTER TABLE `Denominacion_General` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Denominacion_Quimica`
--

DROP TABLE IF EXISTS `Denominacion_Quimica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Denominacion_Quimica` (
  `id_denominacion_quimica` int(11) NOT NULL AUTO_INCREMENT,
  `denominacion_quimica` varchar(100) NOT NULL,
  PRIMARY KEY (`id_denominacion_quimica`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Denominacion_Quimica`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Denominacion_Quimica` WRITE;
/*!40000 ALTER TABLE `Denominacion_Quimica` DISABLE KEYS */;
/*!40000 ALTER TABLE `Denominacion_Quimica` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Documento`
--

DROP TABLE IF EXISTS `Documento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Documento` (
  `id_documento` int(11) NOT NULL AUTO_INCREMENT,
  `documento_name` varchar(50) NOT NULL,
  `id_tipo_documento` int(11) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id_documento`),
  KEY `FK_TIPODOCUMENTO_DOCUMENTO` (`id_tipo_documento`),
  CONSTRAINT `FK_TIPODOCUMENTO_DOCUMENTO` FOREIGN KEY (`id_tipo_documento`) REFERENCES `Tipo_Documento` (`id_tipo_documento`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Documento`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Documento` WRITE;
/*!40000 ALTER TABLE `Documento` DISABLE KEYS */;
/*!40000 ALTER TABLE `Documento` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Documento_Paciente`
--

DROP TABLE IF EXISTS `Documento_Paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Documento_Paciente` (
  `id_documento_paciente` int(11) NOT NULL AUTO_INCREMENT,
  `id_documento` int(11) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  PRIMARY KEY (`id_documento_paciente`),
  KEY `FK_DOCUMENTO_DOCUMENTOPACIENTE` (`id_documento`),
  KEY `FK_PACIENTE_DOCUMENTOPACIENTE` (`id_paciente`),
  CONSTRAINT `FK_DOCUMENTO_DOCUMENTOPACIENTE` FOREIGN KEY (`id_documento`) REFERENCES `Documento` (`id_documento`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_PACIENTE_DOCUMENTOPACIENTE` FOREIGN KEY (`id_paciente`) REFERENCES `Paciente` (`id_paciente`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Documento_Paciente`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Documento_Paciente` WRITE;
/*!40000 ALTER TABLE `Documento_Paciente` DISABLE KEYS */;
/*!40000 ALTER TABLE `Documento_Paciente` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Escuela`
--

DROP TABLE IF EXISTS `Escuela`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Escuela` (
  `id_escuela` int(11) NOT NULL AUTO_INCREMENT,
  `escuela` varchar(100) NOT NULL,
  PRIMARY KEY (`id_escuela`),
  UNIQUE KEY `escuela` (`escuela`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Escuela`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Escuela` WRITE;
/*!40000 ALTER TABLE `Escuela` DISABLE KEYS */;
/*!40000 ALTER TABLE `Escuela` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Estado`
--

DROP TABLE IF EXISTS `Estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Estado` (
  `id_estado` int(11) NOT NULL AUTO_INCREMENT,
  `estado` varchar(50) NOT NULL,
  PRIMARY KEY (`id_estado`),
  UNIQUE KEY `estado` (`estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Estado`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Estado` WRITE;
/*!40000 ALTER TABLE `Estado` DISABLE KEYS */;
/*!40000 ALTER TABLE `Estado` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Estado_Cita`
--

DROP TABLE IF EXISTS `Estado_Cita`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Estado_Cita` (
  `id_estado_cita` int(11) NOT NULL AUTO_INCREMENT,
  `estado_cita` varchar(50) NOT NULL,
  PRIMARY KEY (`id_estado_cita`),
  UNIQUE KEY `estado_cita` (`estado_cita`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Estado_Cita`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Estado_Cita` WRITE;
/*!40000 ALTER TABLE `Estado_Cita` DISABLE KEYS */;
/*!40000 ALTER TABLE `Estado_Cita` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Medicamento`
--

DROP TABLE IF EXISTS `Medicamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Medicamento` (
  `id_medicamento` int(11) NOT NULL AUTO_INCREMENT,
  `medicamento_name` varchar(50) NOT NULL,
  `medicamento_cantidad` int(10) unsigned NOT NULL,
  `medicamento_min` tinyint(3) unsigned NOT NULL,
  `medicamento_caducidad` date NOT NULL,
  `medicamento_dosis` varchar(255) NOT NULL,
  `medicamento_costo` decimal(5,2) NOT NULL,
  `id_denominacion_general` int(11) DEFAULT NULL,
  `id_denominacion_quimica` int(11) DEFAULT NULL,
  `id_consultorio` int(11) NOT NULL,
  `id_via_administrar_medicamento` int(11) NOT NULL DEFAULT 1,
  PRIMARY KEY (`id_medicamento`),
  KEY `FK_DENGENERAL_MEDICAMENTO` (`id_denominacion_general`),
  KEY `FK_DENQUIMICA_MEDICAMENTO` (`id_denominacion_quimica`),
  KEY `FK_CONSULTORIO_MEDICAMENTO` (`id_consultorio`),
  KEY `FK_MEDICAMENTO_VIAADMINISTRARMEDICAMENTO` (`id_via_administrar_medicamento`),
  CONSTRAINT `FK_CONSULTORIO_MEDICAMENTO` FOREIGN KEY (`id_consultorio`) REFERENCES `Consultorio` (`id_consultorio`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_DENGENERAL_MEDICAMENTO` FOREIGN KEY (`id_denominacion_general`) REFERENCES `Denominacion_General` (`id_denominacion_general`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_DENQUIMICA_MEDICAMENTO` FOREIGN KEY (`id_denominacion_quimica`) REFERENCES `Denominacion_Quimica` (`id_denominacion_quimica`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_MEDICAMENTO_CONSULTORIO` FOREIGN KEY (`id_consultorio`) REFERENCES `Consultorio` (`id_consultorio`),
  CONSTRAINT `FK_MEDICAMENTO_DENOMINACION_GENERAL` FOREIGN KEY (`id_denominacion_general`) REFERENCES `Denominacion_General` (`id_denominacion_general`),
  CONSTRAINT `FK_MEDICAMENTO_DENOMINACION_QUIMICA` FOREIGN KEY (`id_denominacion_quimica`) REFERENCES `Denominacion_Quimica` (`id_denominacion_quimica`),
  CONSTRAINT `FK_MEDICAMENTO_VIAADMINISTRARMEDICAMENTO` FOREIGN KEY (`id_via_administrar_medicamento`) REFERENCES `Via_Administrar_Medicamento` (`id_via_administrar_medicamento`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medicamento`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Medicamento` WRITE;
/*!40000 ALTER TABLE `Medicamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `Medicamento` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Nota_Evolucion`
--

DROP TABLE IF EXISTS `Nota_Evolucion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Nota_Evolucion` (
  `id_nota_evolucion` int(11) NOT NULL AUTO_INCREMENT,
  `nota_evolucion` varchar(300) NOT NULL DEFAULT 'FALTAN DATOS - GENERADA ACCIDENTALMENTE',
  `id_paciente` int(11) NOT NULL,
  PRIMARY KEY (`id_nota_evolucion`),
  KEY `FK_PACIENTE_NOTAEVOLUCION` (`id_paciente`),
  CONSTRAINT `FK_PACIENTE_NOTAEVOLUCION` FOREIGN KEY (`id_paciente`) REFERENCES `Paciente` (`id_paciente`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Nota_Evolucion`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Nota_Evolucion` WRITE;
/*!40000 ALTER TABLE `Nota_Evolucion` DISABLE KEYS */;
/*!40000 ALTER TABLE `Nota_Evolucion` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Paciente`
--

DROP TABLE IF EXISTS `Paciente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Paciente` (
  `id_paciente` int(11) NOT NULL AUTO_INCREMENT,
  `paciente_name` varchar(50) NOT NULL,
  `paciente_paterno` varchar(50) NOT NULL,
  `paciente_materno` varchar(50) NOT NULL,
  `paciente_telefono` varchar(13) NOT NULL,
  `paciente_numero_emergencia1` varchar(13) NOT NULL,
  `paciente_numero_emergencia2` varchar(13) DEFAULT NULL,
  `paciente_nss` varchar(8) DEFAULT NULL,
  `id_tipo_sangre` int(11) NOT NULL,
  `id_consultorio` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  PRIMARY KEY (`id_paciente`),
  UNIQUE KEY `paciente_telefono` (`paciente_telefono`),
  KEY `FK_TIPOSANGRE_PACIENTE` (`id_tipo_sangre`),
  KEY `FK_CONSULTORIO_PACIENTE` (`id_consultorio`),
  KEY `FK_USUARIO_PACIENTE` (`id_usuario`),
  CONSTRAINT `FK_CONSULTORIO_PACIENTE` FOREIGN KEY (`id_consultorio`) REFERENCES `Consultorio` (`id_consultorio`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_TIPOSANGRE_PACIENTE` FOREIGN KEY (`id_tipo_sangre`) REFERENCES `Tipo_Sangre` (`id_tipo_sangre`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_USUARIO_PACIENTE` FOREIGN KEY (`id_usuario`) REFERENCES `Usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Paciente`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Paciente` WRITE;
/*!40000 ALTER TABLE `Paciente` DISABLE KEYS */;
/*!40000 ALTER TABLE `Paciente` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Receta`
--

DROP TABLE IF EXISTS `Receta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Receta` (
  `id_receta` int(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` int(11) NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `receta_alergias` varchar(300) DEFAULT NULL,
  `receta_imc` double(5,3) DEFAULT NULL,
  `receta_precion_arterial` varchar(12) DEFAULT NULL,
  `receta_edad` varchar(3) DEFAULT NULL,
  `receta_diganostico` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id_receta`),
  KEY `FK_RECETA_USUARIO` (`id_usuario`),
  KEY `FK_RECETA_PACIENTE` (`id_paciente`),
  CONSTRAINT `FK_RECETA_PACIENTE` FOREIGN KEY (`id_paciente`) REFERENCES `Paciente` (`id_paciente`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_RECETA_USUARIO` FOREIGN KEY (`id_usuario`) REFERENCES `Usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Receta`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Receta` WRITE;
/*!40000 ALTER TABLE `Receta` DISABLE KEYS */;
/*!40000 ALTER TABLE `Receta` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Receta_Medicamento`
--

DROP TABLE IF EXISTS `Receta_Medicamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Receta_Medicamento` (
  `id_receta_medicamento` int(11) NOT NULL AUTO_INCREMENT,
  `id_receta` int(11) NOT NULL,
  `id_medicamento` int(11) NOT NULL,
  `receta_medicamento_dosis` varchar(300) DEFAULT NULL,
  `receta_medicamento_frecuencia` varchar(300) DEFAULT NULL,
  `receta_medicamento_duracion` varchar(300) DEFAULT NULL,
  `receta_medicamento_indicaciones` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id_receta_medicamento`),
  KEY `FK_RECETAMEDICAMENTO_RECETA` (`id_receta`),
  KEY `FK_RECETAMEDICAMENTO_MEDICAMENTO` (`id_medicamento`),
  CONSTRAINT `FK_RECETAMEDICAMENTO_MEDICAMENTO` FOREIGN KEY (`id_medicamento`) REFERENCES `Medicamento` (`id_medicamento`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_RECETAMEDICAMENTO_RECETA` FOREIGN KEY (`id_receta`) REFERENCES `Receta` (`id_receta`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Receta_Medicamento`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Receta_Medicamento` WRITE;
/*!40000 ALTER TABLE `Receta_Medicamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `Receta_Medicamento` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Ticket`
--

DROP TABLE IF EXISTS `Ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ticket` (
  `id_ticket` int(11) NOT NULL AUTO_INCREMENT,
  `ticket_date` datetime NOT NULL DEFAULT current_timestamp(),
  `id_tipo_pago` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  PRIMARY KEY (`id_ticket`),
  KEY `FK_TIPOPAGO_TICKET` (`id_tipo_pago`),
  KEY `FK_USUARIO_TICKET` (`id_usuario`),
  CONSTRAINT `FK_TIPOPAGO_TICKET` FOREIGN KEY (`id_tipo_pago`) REFERENCES `Tipo_Pago` (`id_tipo_pago`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_USUARIO_TICKET` FOREIGN KEY (`id_usuario`) REFERENCES `Usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ticket`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Ticket` WRITE;
/*!40000 ALTER TABLE `Ticket` DISABLE KEYS */;
/*!40000 ALTER TABLE `Ticket` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Ticket_Caja`
--

DROP TABLE IF EXISTS `Ticket_Caja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ticket_Caja` (
  `id_ticket_caja` int(11) NOT NULL AUTO_INCREMENT,
  `id_ticket` int(11) NOT NULL,
  `id_corte_caja` int(11) NOT NULL,
  PRIMARY KEY (`id_ticket_caja`),
  KEY `FK_TICKET_TICKETCAJA` (`id_ticket`),
  KEY `FK_CORTECAJA_TICKETCAJA` (`id_corte_caja`),
  CONSTRAINT `FK_CORTECAJA_TICKETCAJA` FOREIGN KEY (`id_corte_caja`) REFERENCES `Corte_Caja` (`id_corte_caja`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_TICKET_TICKETCAJA` FOREIGN KEY (`id_ticket`) REFERENCES `Ticket` (`id_ticket`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ticket_Caja`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Ticket_Caja` WRITE;
/*!40000 ALTER TABLE `Ticket_Caja` DISABLE KEYS */;
/*!40000 ALTER TABLE `Ticket_Caja` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Ticket_Medicamento`
--

DROP TABLE IF EXISTS `Ticket_Medicamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ticket_Medicamento` (
  `id_ticket_medicamento` int(11) NOT NULL AUTO_INCREMENT,
  `id_ticket` int(11) NOT NULL,
  `id_medicamento` int(11) NOT NULL,
  `cant_medicamento` int(11) NOT NULL,
  `medicina_costo_unidad` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id_ticket_medicamento`),
  KEY `FK_TICKET_TICKETMEDICAMENTO` (`id_ticket`),
  KEY `FK_MEDICAMENTO_TICKETMEDICAMENTO` (`id_medicamento`),
  CONSTRAINT `FK_MEDICAMENTO_TICKETMEDICAMENTO` FOREIGN KEY (`id_medicamento`) REFERENCES `Medicamento` (`id_medicamento`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_TICKET_TICKETMEDICAMENTO` FOREIGN KEY (`id_ticket`) REFERENCES `Ticket` (`id_ticket`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ticket_Medicamento`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Ticket_Medicamento` WRITE;
/*!40000 ALTER TABLE `Ticket_Medicamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `Ticket_Medicamento` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Tipo_Documento`
--

DROP TABLE IF EXISTS `Tipo_Documento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tipo_Documento` (
  `id_tipo_documento` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_doucmento` varchar(50) NOT NULL,
  PRIMARY KEY (`id_tipo_documento`),
  UNIQUE KEY `tipo_doucmento` (`tipo_doucmento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Documento`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Tipo_Documento` WRITE;
/*!40000 ALTER TABLE `Tipo_Documento` DISABLE KEYS */;
/*!40000 ALTER TABLE `Tipo_Documento` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Tipo_Pago`
--

DROP TABLE IF EXISTS `Tipo_Pago`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tipo_Pago` (
  `id_tipo_pago` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_pago` varchar(50) NOT NULL,
  PRIMARY KEY (`id_tipo_pago`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Pago`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Tipo_Pago` WRITE;
/*!40000 ALTER TABLE `Tipo_Pago` DISABLE KEYS */;
/*!40000 ALTER TABLE `Tipo_Pago` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Tipo_Sangre`
--

DROP TABLE IF EXISTS `Tipo_Sangre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tipo_Sangre` (
  `id_tipo_sangre` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_sangre` varchar(3) NOT NULL,
  PRIMARY KEY (`id_tipo_sangre`),
  UNIQUE KEY `tipo_sangre` (`tipo_sangre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Sangre`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Tipo_Sangre` WRITE;
/*!40000 ALTER TABLE `Tipo_Sangre` DISABLE KEYS */;
/*!40000 ALTER TABLE `Tipo_Sangre` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Tipo_Usuario`
--

DROP TABLE IF EXISTS `Tipo_Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tipo_Usuario` (
  `id_tipo_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_usuario` varchar(13) NOT NULL,
  PRIMARY KEY (`id_tipo_usuario`),
  UNIQUE KEY `tipo_usuario` (`tipo_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Usuario`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Tipo_Usuario` WRITE;
/*!40000 ALTER TABLE `Tipo_Usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `Tipo_Usuario` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Tratamiento`
--

DROP TABLE IF EXISTS `Tratamiento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tratamiento` (
  `id_tratamiento` int(11) NOT NULL AUTO_INCREMENT,
  `tratamiento_name` varchar(25) NOT NULL,
  PRIMARY KEY (`id_tratamiento`),
  UNIQUE KEY `tratamiento_name` (`tratamiento_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tratamiento`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Tratamiento` WRITE;
/*!40000 ALTER TABLE `Tratamiento` DISABLE KEYS */;
/*!40000 ALTER TABLE `Tratamiento` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Usuario`
--

DROP TABLE IF EXISTS `Usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_name` varchar(50) NOT NULL,
  `usuario_paterno` varchar(50) NOT NULL,
  `usuario_materno` varchar(50) NOT NULL,
  `usuario_password` varchar(100) NOT NULL,
  `usuario_cedula_profesional` varchar(13) DEFAULT NULL,
  `usuario_cedula_especialidad` varchar(13) DEFAULT NULL,
  `id_tipo_usuario` int(11) NOT NULL,
  `id_consultorio` int(11) NOT NULL,
  `id_escuela` int(11) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `usuario_cedula_profesional` (`usuario_cedula_profesional`),
  UNIQUE KEY `usuario_cedula_especialidad` (`usuario_cedula_especialidad`),
  KEY `FK_TIPOUSUARIO_USUARIO` (`id_tipo_usuario`),
  KEY `FK_CONSULTORIO_USUARIO` (`id_consultorio`),
  KEY `FK_ESCUELA_USUARIO` (`id_escuela`),
  CONSTRAINT `FK_CONSULTORIO_USUARIO` FOREIGN KEY (`id_consultorio`) REFERENCES `Consultorio` (`id_consultorio`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_ESCUELA_USUARIO` FOREIGN KEY (`id_escuela`) REFERENCES `Escuela` (`id_escuela`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_TIPOUSUARIO_USUARIO` FOREIGN KEY (`id_tipo_usuario`) REFERENCES `Tipo_Usuario` (`id_tipo_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `Usuario` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Via_Administrar_Medicamento`
--

DROP TABLE IF EXISTS `Via_Administrar_Medicamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Via_Administrar_Medicamento` (
  `id_via_administrar_medicamento` int(11) NOT NULL AUTO_INCREMENT,
  `via_administrar_medicamento` varchar(20) NOT NULL,
  PRIMARY KEY (`id_via_administrar_medicamento`),
  UNIQUE KEY `via_administrar_medicamento` (`via_administrar_medicamento`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Via_Administrar_Medicamento`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Via_Administrar_Medicamento` WRITE;
/*!40000 ALTER TABLE `Via_Administrar_Medicamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `Via_Administrar_Medicamento` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2026-06-27 19:17:00
