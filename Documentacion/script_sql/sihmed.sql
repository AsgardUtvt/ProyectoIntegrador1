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
  `id_tratamiento` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_cita`),
  KEY `FK_PACIENTE_CITA` (`id_paciente`),
  KEY `FK_CONSULTORIO_CITA` (`id_consultorio`),
  KEY `FK_ESTADOCITA_CITA` (`id_estado_cita`),
  KEY `FK_TRATAMIENTO_CITA` (`id_tratamiento`),
  CONSTRAINT `FK_CONSULTORIO_CITA` FOREIGN KEY (`id_consultorio`) REFERENCES `Consultorio` (`id_consultorio`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_ESTADOCITA_CITA` FOREIGN KEY (`id_estado_cita`) REFERENCES `Estado_Cita` (`id_estado_cita`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_PACIENTE_CITA` FOREIGN KEY (`id_paciente`) REFERENCES `Paciente` (`id_paciente`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_TRATAMIENTO_CITA` FOREIGN KEY (`id_tratamiento`) REFERENCES `Tratamiento` (`id_tratamiento`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=131 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cita`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Cita` WRITE;
/*!40000 ALTER TABLE `Cita` DISABLE KEYS */;
INSERT INTO `Cita` VALUES
(1,'2026-06-07 09:00:00','01:00:00','Consulta general',1,1,1,NULL),
(2,'2026-06-09 11:30:00','00:30:00','Control de signos vitales',1,1,1,NULL),
(3,'2026-06-11 12:00:00','00:45:00','Consulta por dolor abdominal',1,1,1,NULL),
(4,'2026-06-14 09:30:00','01:00:00','Valoración inicial',1,1,1,NULL),
(5,'2026-06-16 10:00:00','00:30:00','Consulta por cuadro gripal',1,1,1,NULL),
(6,'2026-06-18 13:30:00','00:45:00','Control de glucosa',1,1,1,NULL),
(7,'2026-06-21 10:00:00','01:00:00','Consulta general',1,1,1,NULL),
(8,'2026-06-23 16:00:00','00:30:00','Curación y revisión',1,1,1,NULL),
(9,'2026-06-25 09:15:00','00:45:00','Seguimiento de tratamiento',1,1,1,NULL),
(10,'2026-06-28 11:45:00','01:00:00','Consulta por alergias',1,1,1,NULL),
(11,'2026-06-30 15:00:00','00:30:00','Control de presión arterial',1,1,1,NULL),
(12,'2026-07-07 09:00:00','01:00:00','Consulta y emisión de receta',1,1,1,NULL),
(13,'2026-07-09 10:30:00','00:45:00','Consulta y emisión de receta',1,1,1,NULL),
(14,'2026-07-11 12:00:00','01:00:00','Consulta y emisión de receta',1,1,1,NULL),
(15,'2026-07-14 09:30:00','00:30:00','Consulta y emisión de receta',1,1,1,NULL),
(16,'2026-07-16 11:00:00','00:45:00','Consulta y emisión de receta',1,1,1,NULL),
(17,'2026-07-18 13:30:00','01:00:00','Consulta y emisión de receta',1,1,1,NULL),
(18,'2026-07-21 10:00:00','00:30:00','Consulta y emisión de receta',1,1,1,NULL),
(19,'2026-07-23 16:00:00','00:45:00','Consulta y emisión de receta',1,1,1,NULL),
(20,'2026-07-25 09:15:00','01:00:00','Consulta y emisión de receta',1,1,1,NULL),
(21,'2026-07-28 11:45:00','00:30:00','Consulta y emisión de receta',1,1,1,NULL),
(22,'2026-07-30 15:00:00','00:45:00','Consulta y emisión de receta',1,1,1,NULL),
(23,'2026-08-01 10:20:00','01:00:00','Consulta y emisión de receta',1,1,1,NULL),
(24,'2026-08-03 12:40:00','00:30:00','Consulta y emisión de receta',1,1,1,NULL),
(25,'2026-08-05 17:10:00','00:45:00','Consulta y emisión de receta',1,1,1,NULL),
(26,'2026-08-07 09:50:00','01:00:00','Consulta y emisión de receta',1,1,1,NULL),
(27,'2026-06-08 10:00:00','00:45:00','Consulta y emisión de receta',31,1,1,NULL),
(28,'2026-06-12 12:30:00','01:00:00','Consulta y emisión de receta',32,1,1,NULL),
(29,'2026-06-15 09:00:00','00:30:00','Consulta y emisión de receta',33,1,1,NULL),
(30,'2026-06-19 17:00:00','00:45:00','Consulta y emisión de receta',34,1,1,NULL),
(31,'2026-06-24 11:15:00','01:00:00','Consulta y emisión de receta',35,1,1,NULL),
(32,'2026-06-27 13:00:00','00:30:00','Consulta y emisión de receta',1,1,1,NULL),
(33,'2026-07-08 10:45:00','00:45:00','Consulta y emisión de receta',3,1,1,NULL),
(34,'2026-07-15 16:30:00','01:00:00','Consulta y emisión de receta',5,1,1,NULL),
(35,'2026-07-22 09:30:00','00:45:00','Consulta y emisión de receta',7,1,1,NULL),
(36,'2026-08-04 12:00:00','01:00:00','Consulta y emisión de receta',9,1,1,NULL),
(37,'2026-06-09 09:00:00','00:45:00','Consulta y emisión de receta',2,1,1,NULL),
(38,'2026-06-09 13:00:00','00:30:00','Control de presión arterial',4,1,1,NULL),
(39,'2026-06-09 17:00:00','00:45:00','Consulta general',6,1,1,NULL),
(40,'2026-06-16 08:30:00','00:30:00','Consulta por cuadro gripal',8,1,1,NULL),
(41,'2026-06-16 12:30:00','01:00:00','Consulta y emisión de receta',10,1,1,NULL),
(42,'2026-06-16 18:00:00','00:45:00','Seguimiento de tratamiento',12,1,1,NULL),
(43,'2026-06-23 09:00:00','01:00:00','Consulta y emisión de receta',14,1,1,NULL),
(44,'2026-06-23 12:00:00','00:30:00','Control de glucosa',31,1,1,NULL),
(45,'2026-07-10 10:00:00','00:45:00','Consulta y emisión de receta',32,1,1,NULL),
(46,'2026-07-10 12:30:00','00:30:00','Curación y revisión',33,1,1,NULL),
(47,'2026-07-10 17:00:00','00:45:00','Consulta y emisión de receta',34,1,1,NULL),
(48,'2026-07-24 09:30:00','01:00:00','Consulta y emisión de receta',35,1,1,NULL),
(49,'2026-07-24 14:00:00','00:45:00','Consulta y emisión de receta',1,1,1,NULL),
(50,'2026-07-24 16:30:00','00:30:00','Consulta general',3,1,1,NULL),
(51,'2026-08-10 08:00:00','00:30:00','Consulta general',5,1,1,NULL),
(52,'2026-08-10 11:00:00','00:45:00','Consulta y emisión de receta',7,1,1,NULL),
(53,'2026-08-10 15:30:00','01:00:00','Valoración inicial',9,1,1,NULL),
(54,'2026-08-11 09:00:00','00:45:00','Consulta y emisión de receta',11,1,1,NULL),
(55,'2026-08-11 13:30:00','00:30:00','Control de signos vitales',13,1,1,NULL),
(56,'2026-07-07 11:30:00','00:45:00','Consulta y emisión de receta',2,1,1,NULL),
(57,'2026-07-07 16:00:00','00:30:00','Control de presión arterial',4,1,1,NULL),
(58,'2026-07-10 09:00:00','00:30:00','Consulta general',6,1,1,NULL),
(59,'2026-07-10 18:00:00','00:45:00','Seguimiento de tratamiento',8,1,1,NULL),
(60,'2026-07-14 12:00:00','01:00:00','Consulta y emisión de receta',10,1,1,NULL),
(61,'2026-07-14 17:30:00','00:30:00','Control de glucosa',12,1,1,NULL),
(62,'2026-07-16 09:00:00','00:30:00','Consulta por cuadro gripal',13,1,1,NULL),
(63,'2026-07-16 14:30:00','00:45:00','Consulta y emisión de receta',15,1,1,NULL),
(64,'2026-07-21 13:00:00','01:00:00','Consulta y emisión de receta',31,1,1,NULL),
(65,'2026-07-21 17:00:00','00:30:00','Curación y revisión',33,1,1,NULL),
(66,'2026-07-24 11:00:00','00:45:00','Consulta y emisión de receta',2,1,1,NULL),
(67,'2026-07-24 18:30:00','00:30:00','Consulta general',4,1,1,NULL),
(68,'2026-07-28 09:30:00','00:30:00','Consulta por alergias',6,1,1,NULL),
(69,'2026-07-28 16:30:00','00:45:00','Consulta y emisión de receta',8,1,1,NULL),
(70,'2026-08-03 10:00:00','00:30:00','Control de signos vitales',10,1,1,NULL),
(71,'2026-08-03 17:00:00','01:00:00','Valoración inicial',12,1,1,NULL),
(72,'2026-08-07 12:30:00','00:45:00','Consulta y emisión de receta',14,1,1,NULL),
(73,'2026-08-07 15:00:00','00:30:00','Control de presión arterial',31,1,1,NULL),
(74,'2026-08-10 10:00:00','00:30:00','Consulta general',33,1,1,NULL),
(75,'2026-08-10 13:00:00','00:45:00','Consulta y emisión de receta',35,1,1,NULL),
(76,'2026-08-10 17:30:00','01:00:00','Seguimiento de tratamiento',1,1,1,NULL),
(77,'2026-08-11 11:30:00','00:30:00','Curación y revisión',3,1,1,NULL),
(78,'2026-08-11 16:00:00','00:45:00','Consulta general',5,1,1,NULL),
(79,'2026-06-07 11:30:00','00:30:00','Control de presión arterial',1,1,1,NULL),
(80,'2026-06-07 16:30:00','00:45:00','Consulta general',2,1,1,NULL),
(81,'2026-06-08 09:00:00','01:00:00','Consulta y emisión de receta',3,1,1,NULL),
(82,'2026-06-08 13:00:00','00:30:00','Control de glucosa',4,1,1,NULL),
(83,'2026-06-11 09:30:00','00:45:00','Consulta por cuadro gripal',5,1,1,NULL),
(84,'2026-06-11 17:00:00','01:00:00','Seguimiento de tratamiento',6,1,1,NULL),
(85,'2026-06-12 10:00:00','00:30:00','Curación y revisión',7,1,1,NULL),
(86,'2026-06-12 16:00:00','00:45:00','Consulta general',8,1,1,NULL),
(87,'2026-06-14 12:30:00','01:00:00','Consulta y emisión de receta',9,1,1,NULL),
(88,'2026-06-14 17:30:00','00:30:00','Valoración inicial',10,1,1,NULL),
(89,'2026-06-15 11:00:00','00:45:00','Consulta por alergias',11,1,1,NULL),
(90,'2026-06-15 15:30:00','01:00:00','Control de signos vitales',12,1,1,NULL),
(91,'2026-06-18 09:00:00','00:30:00','Consulta general',13,1,1,NULL),
(92,'2026-06-18 16:30:00','00:45:00','Control de presión arterial',14,1,1,NULL),
(93,'2026-06-19 10:30:00','01:00:00','Consulta por cuadro gripal',15,1,1,NULL),
(94,'2026-06-19 13:30:00','00:30:00','Curación y revisión',31,1,1,NULL),
(95,'2026-06-21 12:30:00','00:45:00','Consulta y emisión de receta',32,1,1,NULL),
(96,'2026-06-21 17:00:00','01:00:00','Consulta general',33,1,1,NULL),
(97,'2026-06-24 09:00:00','00:30:00','Control de glucosa',34,1,1,NULL),
(98,'2026-06-24 15:00:00','00:45:00','Seguimiento de tratamiento',35,1,1,NULL),
(99,'2026-06-25 11:30:00','01:00:00','Consulta general',1,1,1,NULL),
(100,'2026-06-25 16:00:00','00:30:00','Control de signos vitales',2,1,1,NULL),
(101,'2026-06-27 09:30:00','00:45:00','Valoración inicial',3,1,1,NULL),
(102,'2026-06-27 17:30:00','01:00:00','Consulta por alergias',4,1,1,NULL),
(103,'2026-06-28 09:00:00','00:30:00','Consulta y emisión de receta',5,1,1,NULL),
(104,'2026-06-28 13:30:00','00:45:00','Control de presión arterial',6,1,1,NULL),
(105,'2026-06-30 10:30:00','01:00:00','Consulta general',7,1,1,NULL),
(106,'2026-06-30 17:00:00','00:30:00','Curación y revisión',8,1,1,NULL),
(107,'2026-07-08 09:00:00','00:45:00','Consulta y emisión de receta',9,1,1,NULL),
(108,'2026-07-08 14:00:00','01:00:00','Control de glucosa',10,1,1,NULL),
(109,'2026-07-09 12:30:00','00:30:00','Consulta general',11,1,1,NULL),
(110,'2026-07-09 17:00:00','00:45:00','Seguimiento de tratamiento',12,1,1,NULL),
(111,'2026-07-11 09:30:00','01:00:00','Consulta por cuadro gripal',13,1,1,NULL),
(112,'2026-07-11 16:30:00','00:30:00','Valoración inicial',14,1,1,NULL),
(113,'2026-07-15 10:00:00','00:45:00','Consulta y emisión de receta',15,1,1,NULL),
(114,'2026-07-15 13:00:00','01:00:00','Control de signos vitales',31,1,1,NULL),
(115,'2026-07-18 09:30:00','00:30:00','Consulta general',32,1,1,NULL),
(116,'2026-07-18 17:00:00','00:45:00','Control de presión arterial',33,1,1,NULL),
(117,'2026-07-22 12:00:00','01:00:00','Curación y revisión',34,1,1,NULL),
(118,'2026-07-22 16:30:00','00:30:00','Consulta por alergias',35,1,1,NULL),
(119,'2026-07-23 10:30:00','00:45:00','Consulta y emisión de receta',1,1,1,NULL),
(120,'2026-07-23 13:30:00','01:00:00','Consulta general',2,1,1,NULL),
(121,'2026-07-25 11:00:00','00:30:00','Control de glucosa',3,1,1,NULL),
(122,'2026-07-25 15:30:00','00:45:00','Seguimiento de tratamiento',4,1,1,NULL),
(123,'2026-07-30 09:30:00','01:00:00','Consulta general',5,1,1,NULL),
(124,'2026-07-30 12:30:00','00:30:00','Valoración inicial',6,1,1,NULL),
(125,'2026-08-01 12:00:00','00:45:00','Consulta y emisión de receta',7,1,1,NULL),
(126,'2026-08-01 16:00:00','01:00:00','Control de presión arterial',8,1,1,NULL),
(127,'2026-08-04 09:30:00','00:30:00','Consulta general',9,1,1,NULL),
(128,'2026-08-04 15:30:00','00:45:00','Curación y revisión',10,1,1,NULL),
(129,'2026-08-05 10:00:00','01:00:00','Consulta y emisión de receta',11,1,1,NULL),
(130,'2026-08-05 13:30:00','00:30:00','Control de signos vitales',12,1,1,NULL);
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
  `consultorio_name` varchar(50) NOT NULL,
  `consultorio_calle` varchar(100) DEFAULT NULL,
  `consultorio_colonia` varchar(100) DEFAULT NULL,
  `consultorio_num_exterior` varchar(5) DEFAULT NULL,
  `consultorio_num_interior` varchar(5) DEFAULT NULL,
  `consultorio_localidad` varchar(100) DEFAULT NULL,
  `id_estado` int(11) NOT NULL,
  `consultorio_telefono` varchar(13) DEFAULT NULL,
  `consultorio_telefono_dos` varchar(13) DEFAULT NULL,
  `consultorio_municipio` varchar(100) DEFAULT NULL,
  `consultorio_cp` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_consultorio`),
  KEY `FK_ESTADO_CONSULTORIO` (`id_estado`),
  KEY `INDEX_CONSULTORIO_NAME` (`consultorio_name`),
  CONSTRAINT `FK_CONSULTORIO_ESTADO` FOREIGN KEY (`id_estado`) REFERENCES `Estado` (`id_estado`),
  CONSTRAINT `FK_ESTADO_CONSULTORIO` FOREIGN KEY (`id_estado`) REFERENCES `Estado` (`id_estado`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Consultorio`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Consultorio` WRITE;
/*!40000 ALTER TABLE `Consultorio` DISABLE KEYS */;
INSERT INTO `Consultorio` VALUES
(1,'JAU Tecnologic','Celaya','San Gaspar Tlahuelilpan','7','Sn','México',12,'5591109383','5291109382','Metepec','52147'),
(2,'Prueba consultorio 1','Celaya','Ciudad Juarez','1','2','San Gaspar',13,'3123513251234','1234123412351','Metepec','52147'),
(3,'JAU Tecnologics','Celaya ','juarearsa','Sn','Sn','Localidad',1,'1324123412341','2341234214124','cholula','13241'),
(4,'Kawasaki','Celaya','arst13241234','0','9','srtarstasrta',14,'1234123412341','3214123412341','arstrstfw214134','13242'),
(5,'1234123412341234','asratasrtarsta','123412341234132412343124arstarst','112','123','arstarstasr',14,'1343124123412','3214123412341','arstarstar','31241'),
(6,'acoinesoiteant','startarstarstarst','arstarstarst','sss','sss','arstarstsarts',14,'1331412341234','5123512341234','12341234123413','13241'),
(7,'arstarstarstars','arstartsarst','srtrtarstar','ss','sss','srarstarsta',14,'1412341234234','1234123412341','asrtartsarstars','12343'),
(8,'Prueba1','Prueba','Prueba','1','1','Prueba',1,'1234123412341','2341234123412','Prueba','13245'),
(9,'Prueba2','calle','colonia','Sn','123','Localidad',25,'1234512345123','1234134515145','municipio','12345');
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Denominacion_General`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Denominacion_General` WRITE;
/*!40000 ALTER TABLE `Denominacion_General` DISABLE KEYS */;
INSERT INTO `Denominacion_General` VALUES
(1,'Sin Definir'),
(2,'Paracetamol'),
(3,'Ibuprofeno'),
(4,'Amoxicilina'),
(5,'Metformina'),
(6,'Losartán'),
(7,'Omeprazol'),
(8,'Salbutamol'),
(9,'Diclofenaco'),
(10,'Azitromicina'),
(11,'Cetirizina'),
(12,'Loratadina'),
(13,'Naproxeno'),
(14,'Butilhioscina'),
(15,'Ambroxol'),
(16,'Ciprofloxacino');
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Denominacion_Quimica`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Denominacion_Quimica` WRITE;
/*!40000 ALTER TABLE `Denominacion_Quimica` DISABLE KEYS */;
INSERT INTO `Denominacion_Quimica` VALUES
(1,'Sin Definir'),
(2,'N-(4-hidroxifenil)acetamida'),
(3,'Ácido 2-(4-isobutilfenil)propiónico'),
(4,'Amoxicilina trihidrato'),
(5,'Clorhidrato de metformina'),
(6,'Losartán potásico'),
(7,'Omeprazol'),
(8,'Sulfato de salbutamol'),
(9,'Diclofenaco sódico'),
(10,'Azitromicina dihidrato'),
(11,'Diclorhidrato de cetirizina'),
(12,'Loratadina'),
(13,'Naproxeno sódico'),
(14,'Bromuro de butilhioscina'),
(15,'Clorhidrato de ambroxol'),
(16,'Clorhidrato de ciprofloxacino');
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
  `escuela_name` varchar(200) DEFAULT NULL,
  `escuela_acronimo` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_escuela`),
  UNIQUE KEY `escuela` (`escuela_name`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Escuela`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Escuela` WRITE;
/*!40000 ALTER TABLE `Escuela` DISABLE KEYS */;
INSERT INTO `Escuela` VALUES
(1,'Sin Definir','SD'),
(2,'Universidad Nacional Autónoma de México','UNAM'),
(3,'Instituto Politécnico Nacional','IPN'),
(4,'Universidad Autónoma Metropolitana','UAM'),
(5,'Centro Médico Nacional Siglo XXI del Instituto Mexicano del Seguro Social','IMSS'),
(6,'Secretaría de Salud de la Ciudad de México','SEDESA'),
(7,'Escuela Nacional de Enfermería e Investigación del Instituto de Seguridad y Servicios Sociales de los Trabajadores del Estado','ENEI-ISSSTE'),
(8,'Universidad Panamericana','UP'),
(9,'Instituto Tecnológico y de Estudios Superiores de Monterrey','ITESM'),
(10,'Escuela de Enfermeras de Guadalupe, Asociación Civil','EEGAC'),
(11,'Universidad de la Salud','UNISA');
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
  `estado` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_estado`),
  UNIQUE KEY `estado` (`estado`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Estado`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Estado` WRITE;
/*!40000 ALTER TABLE `Estado` DISABLE KEYS */;
INSERT INTO `Estado` VALUES
(2,'Aguascalientes'),
(3,'Baja California'),
(4,'Baja California Sur'),
(5,'Campeche'),
(6,'Chiapas'),
(7,'Chihuahua'),
(8,'Ciudad de México'),
(9,'Coahuila'),
(10,'Colima'),
(11,'Durango'),
(12,'Estado de México'),
(13,'Guanajuato'),
(14,'Guerrero'),
(15,'Hidalgo'),
(16,'Jalisco'),
(17,'Michoacán'),
(18,'Morelos'),
(19,'Nayarit'),
(1,'No Asignado'),
(20,'Nuevo León'),
(21,'Oaxaca'),
(22,'Puebla'),
(23,'Querétaro'),
(24,'Quintana Roo'),
(25,'San Luis Potosí'),
(26,'Sinaloa'),
(27,'Sonora'),
(28,'Tabasco'),
(29,'Tamaulipas'),
(30,'Tlaxcala'),
(31,'Veracruz'),
(32,'Yucatán'),
(33,'Zacatecas');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Estado_Cita`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Estado_Cita` WRITE;
/*!40000 ALTER TABLE `Estado_Cita` DISABLE KEYS */;
INSERT INTO `Estado_Cita` VALUES
(1,'Sin Definir');
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medicamento`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Medicamento` WRITE;
/*!40000 ALTER TABLE `Medicamento` DISABLE KEYS */;
INSERT INTO `Medicamento` VALUES
(1,'Paracetamol 500 mg tableta',100,20,'2027-06-30','500 mg cada 8 horas por 5 días',35.50,2,2,1,2),
(2,'Ibuprofeno 400 mg tableta',80,15,'2027-05-31','400 mg cada 8 horas por 5 días',48.00,3,3,1,2),
(3,'Amoxicilina 500 mg cápsula',120,20,'2026-12-31','500 mg cada 8 horas por 7 días',65.00,4,4,1,2),
(4,'Metformina 850 mg tableta',90,15,'2027-09-30','850 mg cada 12 horas',52.50,5,5,1,2),
(5,'Losartán 50 mg tableta',85,15,'2027-08-31','50 mg cada 24 horas',60.00,6,6,1,2),
(6,'Omeprazol 20 mg cápsula',100,20,'2027-03-31','20 mg cada 24 horas antes del desayuno',45.00,7,7,1,2),
(7,'Salbutamol inhalador 100 mcg',25,5,'2026-11-30','2 inhalaciones cada 6 horas por indicación',120.00,8,8,1,3),
(8,'Diclofenaco 50 mg tableta',70,10,'2027-02-28','50 mg cada 8 horas por 5 días',38.00,9,9,1,2),
(9,'Azitromicina 500 mg tableta',60,10,'2026-10-31','500 mg cada 24 horas por 3 días',95.00,10,10,1,2),
(10,'Cetirizina 10 mg tableta',90,15,'2027-07-31','10 mg cada 24 horas',30.00,11,11,1,2),
(11,'Loratadina 10 mg tableta',95,15,'2027-04-30','10 mg cada 24 horas',28.50,12,12,1,2),
(12,'Naproxeno 250 mg tableta',75,15,'2027-01-31','250 mg cada 12 horas',42.00,13,13,1,2),
(13,'Butilhioscina 10 mg tableta',50,10,'2026-12-31','10 mg cada 8 horas',55.00,14,14,1,2),
(14,'Ambroxol jarabe 100 ml',40,8,'2026-09-30','10 ml cada 12 horas por 7 días',49.90,15,15,1,2),
(15,'Ciprofloxacino 500 mg tableta',65,10,'2026-11-30','500 mg cada 12 horas por 7 días',78.00,16,16,1,2),
(16,'PruebaMed1',10,2,'2027-12-31','1 cada 8 horas',100.00,NULL,NULL,1,1);
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
  `Ubicacion_Documento` varchar(500) DEFAULT NULL,
  `paciente_alergia` varchar(500) DEFAULT NULL,
  `paciente_fecha_nacimiento` datetime DEFAULT NULL,
  `paciente_sexo` varchar(15) DEFAULT NULL,
  `paciente_correo_electronico` varchar(300) DEFAULT NULL,
  `paciente_direccion` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_paciente`),
  UNIQUE KEY `paciente_telefono` (`paciente_telefono`),
  UNIQUE KEY `uq_ubicacion_documento` (`Ubicacion_Documento`),
  KEY `FK_TIPOSANGRE_PACIENTE` (`id_tipo_sangre`),
  KEY `FK_CONSULTORIO_PACIENTE` (`id_consultorio`),
  KEY `FK_USUARIO_PACIENTE` (`id_usuario`),
  CONSTRAINT `FK_CONSULTORIO_PACIENTE` FOREIGN KEY (`id_consultorio`) REFERENCES `Consultorio` (`id_consultorio`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_TIPOSANGRE_PACIENTE` FOREIGN KEY (`id_tipo_sangre`) REFERENCES `Tipo_Sangre` (`id_tipo_sangre`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_USUARIO_PACIENTE` FOREIGN KEY (`id_usuario`) REFERENCES `Usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Paciente`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Paciente` WRITE;
/*!40000 ALTER TABLE `Paciente` DISABLE KEYS */;
INSERT INTO `Paciente` VALUES
(1,'Juan','Pérez','López','5510000001','5520000001',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(2,'María','García','Martínez','5510000002','5520000002',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(3,'Luis','Hernández','Sánchez','5510000003','5520000003',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(4,'Laura','López','Ramírez','5510000004','5520000004',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(5,'Carlos','Sánchez','Torres','5510000005','5520000005',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(6,'Ana','Ramírez','Cruz','5510000006','5520000006',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(7,'Pedro','Flores','Morales','5510000007','5520000007',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(8,'Sofía','Morales','Reyes','5510000008','5520000008',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(9,'Miguel','Torres','Gutiérrez','5510000009','5520000009',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(10,'Lucía','Gutiérrez','Díaz','5510000010','5520000010',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(11,'Jorge','Díaz','Vargas','5510000011','5520000011',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(12,'Carmen','Vargas','Mendoza','5510000012','5520000012',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(13,'Ricardo','Mendoza','Ruiz','5510000013','5520000013',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(14,'Elena','Ruiz','Castro','5510000014','5520000014',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(15,'Fernando','Castro','Ortiz','5510000015','5520000015',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(31,'Valeria','Ortiz','Silva','5510000016','5520000016',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(32,'Andrés','Silva','Rojas','5510000017','5520000017',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(33,'Gabriela','Rojas','Vega','5510000018','5520000018',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(34,'Raúl','Vega','Campos','5510000019','5520000019',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL),
(35,'Daniela','Campos','Nava','5510000020','5520000020',NULL,NULL,8,1,1,NULL,NULL,NULL,NULL,NULL,NULL);
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
  `receta_date` datetime NOT NULL DEFAULT @`CURRENT_TIMESTAMP`,
  PRIMARY KEY (`id_receta`),
  KEY `FK_RECETA_USUARIO` (`id_usuario`),
  KEY `FK_RECETA_PACIENTE` (`id_paciente`),
  CONSTRAINT `FK_RECETA_PACIENTE` FOREIGN KEY (`id_paciente`) REFERENCES `Paciente` (`id_paciente`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_RECETA_USUARIO` FOREIGN KEY (`id_usuario`) REFERENCES `Usuario` (`id_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Receta`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Receta` WRITE;
/*!40000 ALTER TABLE `Receta` DISABLE KEYS */;
INSERT INTO `Receta` VALUES
(1,1,1,NULL,NULL,NULL,NULL,NULL,'2026-07-07 09:00:00'),
(2,1,2,NULL,NULL,NULL,NULL,NULL,'2026-07-09 10:30:00'),
(3,1,3,NULL,NULL,NULL,NULL,NULL,'2026-07-11 12:00:00'),
(4,1,4,NULL,NULL,NULL,NULL,NULL,'2026-07-14 09:30:00'),
(5,1,5,NULL,NULL,NULL,NULL,NULL,'2026-07-16 11:00:00'),
(6,1,6,NULL,NULL,NULL,NULL,NULL,'2026-07-18 13:30:00'),
(7,1,7,NULL,NULL,NULL,NULL,NULL,'2026-07-21 10:00:00'),
(8,1,8,NULL,NULL,NULL,NULL,NULL,'2026-07-23 16:00:00'),
(9,1,9,NULL,NULL,NULL,NULL,NULL,'2026-07-25 09:15:00'),
(10,1,10,NULL,NULL,NULL,NULL,NULL,'2026-07-28 11:45:00'),
(11,1,11,NULL,NULL,NULL,NULL,NULL,'2026-07-30 15:00:00'),
(12,1,12,NULL,NULL,NULL,NULL,NULL,'2026-08-01 10:20:00'),
(13,1,13,NULL,NULL,NULL,NULL,NULL,'2026-08-03 12:40:00'),
(14,1,14,NULL,NULL,NULL,NULL,NULL,'2026-08-05 17:10:00'),
(15,1,15,NULL,NULL,NULL,NULL,NULL,'2026-08-07 09:50:00'),
(16,1,31,NULL,NULL,NULL,NULL,NULL,'2026-06-08 10:00:00'),
(17,1,32,NULL,NULL,NULL,NULL,NULL,'2026-06-12 12:30:00'),
(18,1,33,NULL,NULL,NULL,NULL,NULL,'2026-06-15 09:00:00'),
(19,1,34,NULL,NULL,NULL,NULL,NULL,'2026-06-19 17:00:00'),
(20,1,35,NULL,NULL,NULL,NULL,NULL,'2026-06-24 11:15:00'),
(21,1,1,NULL,NULL,NULL,NULL,NULL,'2026-06-27 13:00:00'),
(22,1,3,NULL,NULL,NULL,NULL,NULL,'2026-07-08 10:45:00'),
(23,1,5,NULL,NULL,NULL,NULL,NULL,'2026-07-15 16:30:00'),
(24,1,7,NULL,NULL,NULL,NULL,NULL,'2026-07-22 09:30:00'),
(25,1,9,NULL,NULL,NULL,NULL,NULL,'2026-08-04 12:00:00'),
(26,1,2,NULL,NULL,NULL,NULL,NULL,'2026-06-09 09:00:00'),
(27,1,10,NULL,NULL,NULL,NULL,NULL,'2026-06-16 12:30:00'),
(28,1,14,NULL,NULL,NULL,NULL,NULL,'2026-06-23 09:00:00'),
(29,1,32,NULL,NULL,NULL,NULL,NULL,'2026-07-10 10:00:00'),
(30,1,34,NULL,NULL,NULL,NULL,NULL,'2026-07-10 17:00:00'),
(31,1,35,NULL,NULL,NULL,NULL,NULL,'2026-07-24 09:30:00'),
(32,1,1,NULL,NULL,NULL,NULL,NULL,'2026-07-24 14:00:00'),
(33,1,7,NULL,NULL,NULL,NULL,NULL,'2026-08-10 11:00:00'),
(34,1,11,NULL,NULL,NULL,NULL,NULL,'2026-08-11 09:00:00'),
(35,1,2,NULL,NULL,NULL,NULL,NULL,'2026-07-07 11:30:00'),
(36,1,10,NULL,NULL,NULL,NULL,NULL,'2026-07-14 12:00:00'),
(37,1,15,NULL,NULL,NULL,NULL,NULL,'2026-07-16 14:30:00'),
(38,1,31,NULL,NULL,NULL,NULL,NULL,'2026-07-21 13:00:00'),
(39,1,2,NULL,NULL,NULL,NULL,NULL,'2026-07-24 11:00:00'),
(40,1,8,NULL,NULL,NULL,NULL,NULL,'2026-07-28 16:30:00'),
(41,1,14,NULL,NULL,NULL,NULL,NULL,'2026-08-07 12:30:00'),
(42,1,35,NULL,NULL,NULL,NULL,NULL,'2026-08-10 13:00:00'),
(43,1,3,NULL,NULL,NULL,NULL,NULL,'2026-06-08 09:00:00'),
(44,1,9,NULL,NULL,NULL,NULL,NULL,'2026-06-14 12:30:00'),
(45,1,32,NULL,NULL,NULL,NULL,NULL,'2026-06-21 12:30:00'),
(46,1,5,NULL,NULL,NULL,NULL,NULL,'2026-06-28 09:00:00'),
(47,1,9,NULL,NULL,NULL,NULL,NULL,'2026-07-08 09:00:00'),
(48,1,15,NULL,NULL,NULL,NULL,NULL,'2026-07-15 10:00:00'),
(49,1,1,NULL,NULL,NULL,NULL,NULL,'2026-07-23 10:30:00'),
(50,1,7,NULL,NULL,NULL,NULL,NULL,'2026-08-01 12:00:00'),
(51,1,11,NULL,NULL,NULL,NULL,NULL,'2026-08-05 10:00:00');
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
) ENGINE=InnoDB AUTO_INCREMENT=157 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Receta_Medicamento`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Receta_Medicamento` WRITE;
/*!40000 ALTER TABLE `Receta_Medicamento` DISABLE KEYS */;
INSERT INTO `Receta_Medicamento` VALUES
(1,1,1,NULL,NULL,NULL,NULL),
(2,1,6,NULL,NULL,NULL,NULL),
(4,2,2,NULL,NULL,NULL,NULL),
(5,2,7,NULL,NULL,NULL,NULL),
(7,3,3,NULL,NULL,NULL,NULL),
(8,3,8,NULL,NULL,NULL,NULL),
(10,4,4,NULL,NULL,NULL,NULL),
(11,4,9,NULL,NULL,NULL,NULL),
(13,5,5,NULL,NULL,NULL,NULL),
(14,5,10,NULL,NULL,NULL,NULL),
(16,6,6,NULL,NULL,NULL,NULL),
(17,6,11,NULL,NULL,NULL,NULL),
(19,7,7,NULL,NULL,NULL,NULL),
(20,7,12,NULL,NULL,NULL,NULL),
(22,8,8,NULL,NULL,NULL,NULL),
(23,8,13,NULL,NULL,NULL,NULL),
(25,9,9,NULL,NULL,NULL,NULL),
(26,9,14,NULL,NULL,NULL,NULL),
(28,10,10,NULL,NULL,NULL,NULL),
(29,10,15,NULL,NULL,NULL,NULL),
(31,11,1,NULL,NULL,NULL,NULL),
(32,11,11,NULL,NULL,NULL,NULL),
(34,12,2,NULL,NULL,NULL,NULL),
(35,12,12,NULL,NULL,NULL,NULL),
(37,13,3,NULL,NULL,NULL,NULL),
(38,13,13,NULL,NULL,NULL,NULL),
(40,14,4,NULL,NULL,NULL,NULL),
(41,14,14,NULL,NULL,NULL,NULL),
(43,15,5,NULL,NULL,NULL,NULL),
(44,15,15,NULL,NULL,NULL,NULL),
(46,16,1,NULL,NULL,NULL,NULL),
(47,16,14,NULL,NULL,NULL,NULL),
(48,17,2,NULL,NULL,NULL,NULL),
(49,17,13,NULL,NULL,NULL,NULL),
(50,18,3,NULL,NULL,NULL,NULL),
(51,18,1,NULL,NULL,NULL,NULL),
(52,19,4,NULL,NULL,NULL,NULL),
(53,19,5,NULL,NULL,NULL,NULL),
(54,20,6,NULL,NULL,NULL,NULL),
(55,20,12,NULL,NULL,NULL,NULL),
(56,21,10,NULL,NULL,NULL,NULL),
(57,21,11,NULL,NULL,NULL,NULL),
(58,22,7,NULL,NULL,NULL,NULL),
(59,22,10,NULL,NULL,NULL,NULL),
(60,23,9,NULL,NULL,NULL,NULL),
(61,23,1,NULL,NULL,NULL,NULL),
(62,24,8,NULL,NULL,NULL,NULL),
(63,24,12,NULL,NULL,NULL,NULL),
(64,25,15,NULL,NULL,NULL,NULL),
(65,25,14,NULL,NULL,NULL,NULL),
(77,26,1,NULL,NULL,NULL,NULL),
(78,26,14,NULL,NULL,NULL,NULL),
(79,27,10,NULL,NULL,NULL,NULL),
(80,27,11,NULL,NULL,NULL,NULL),
(81,28,4,NULL,NULL,NULL,NULL),
(82,28,5,NULL,NULL,NULL,NULL),
(83,29,2,NULL,NULL,NULL,NULL),
(84,29,12,NULL,NULL,NULL,NULL),
(85,30,3,NULL,NULL,NULL,NULL),
(86,30,1,NULL,NULL,NULL,NULL),
(87,31,15,NULL,NULL,NULL,NULL),
(88,31,14,NULL,NULL,NULL,NULL),
(89,32,6,NULL,NULL,NULL,NULL),
(90,32,13,NULL,NULL,NULL,NULL),
(91,33,7,NULL,NULL,NULL,NULL),
(92,33,10,NULL,NULL,NULL,NULL),
(93,34,9,NULL,NULL,NULL,NULL),
(94,34,1,NULL,NULL,NULL,NULL),
(108,35,1,NULL,NULL,NULL,NULL),
(109,35,2,NULL,NULL,NULL,NULL),
(110,36,10,NULL,NULL,NULL,NULL),
(111,36,11,NULL,NULL,NULL,NULL),
(112,37,3,NULL,NULL,NULL,NULL),
(113,37,1,NULL,NULL,NULL,NULL),
(114,38,4,NULL,NULL,NULL,NULL),
(115,38,5,NULL,NULL,NULL,NULL),
(116,39,6,NULL,NULL,NULL,NULL),
(117,39,12,NULL,NULL,NULL,NULL),
(118,40,7,NULL,NULL,NULL,NULL),
(119,40,10,NULL,NULL,NULL,NULL),
(120,41,9,NULL,NULL,NULL,NULL),
(121,41,14,NULL,NULL,NULL,NULL),
(122,42,15,NULL,NULL,NULL,NULL),
(123,42,13,NULL,NULL,NULL,NULL),
(139,43,1,NULL,NULL,NULL,NULL),
(140,43,14,NULL,NULL,NULL,NULL),
(141,44,2,NULL,NULL,NULL,NULL),
(142,44,12,NULL,NULL,NULL,NULL),
(143,45,10,NULL,NULL,NULL,NULL),
(144,45,11,NULL,NULL,NULL,NULL),
(145,46,3,NULL,NULL,NULL,NULL),
(146,46,1,NULL,NULL,NULL,NULL),
(147,47,4,NULL,NULL,NULL,NULL),
(148,47,5,NULL,NULL,NULL,NULL),
(149,48,6,NULL,NULL,NULL,NULL),
(150,48,13,NULL,NULL,NULL,NULL),
(151,49,7,NULL,NULL,NULL,NULL),
(152,49,10,NULL,NULL,NULL,NULL),
(153,50,9,NULL,NULL,NULL,NULL),
(154,50,14,NULL,NULL,NULL,NULL),
(155,51,15,NULL,NULL,NULL,NULL),
(156,51,1,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Receta_Medicamento` ENABLE KEYS */;
UNLOCK TABLES;
COMMIT;
SET AUTOCOMMIT=@OLD_AUTOCOMMIT;

--
-- Table structure for table `Sub_Consultorio`
--

DROP TABLE IF EXISTS `Sub_Consultorio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `Sub_Consultorio` (
  `id_sub_consultorio` int(11) NOT NULL AUTO_INCREMENT,
  `sub_consultorio_name` varchar(50) NOT NULL,
  `sub_consultorio_calle` varchar(100) DEFAULT NULL,
  `sub_consultorio_colonia` varchar(100) DEFAULT NULL,
  `sub_consultorio_num_exterior` varchar(3) DEFAULT NULL,
  `sub_consultorio_num_interior` varchar(3) DEFAULT NULL,
  `sub_consultorio_localidad` varchar(100) DEFAULT NULL,
  `sub_consultorio_telefono` varchar(13) DEFAULT NULL,
  `sub_consultorio_telefono_dos` varchar(13) DEFAULT NULL,
  `id_estado` int(11) NOT NULL,
  `id_consultorio` int(11) NOT NULL,
  `sub_consultorio_cp` varchar(10) DEFAULT NULL,
  `sub_consultorio_municipio` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_sub_consultorio`),
  UNIQUE KEY `sub_conultorio_name` (`sub_consultorio_name`),
  KEY `FK_SUB_CONSULTORIO_CONSULTORIO` (`id_consultorio`),
  KEY `FK_SUB_CONSULTORIO_ID_ESTADO` (`id_estado`),
  CONSTRAINT `FK_SUB_CONSULTORIO_CONSULTORIO` FOREIGN KEY (`id_consultorio`) REFERENCES `Consultorio` (`id_consultorio`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_SUB_CONSULTORIO_ID_ESTADO` FOREIGN KEY (`id_estado`) REFERENCES `Estado` (`id_estado`)
<<<<<<< HEAD
<<<<<<< HEAD
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
=======
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
>>>>>>> 0bbe361 (Consultorio con delete y generar nuevo)
=======
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
>>>>>>> 15feac0 (Se suben modulo de medicamentos y base de datos)
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Sub_Consultorio`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Sub_Consultorio` WRITE;
/*!40000 ALTER TABLE `Sub_Consultorio` DISABLE KEYS */;
<<<<<<< HEAD
<<<<<<< HEAD
INSERT INTO `Sub_Consultorio` VALUES
(1,'SubClinicaUno','arstarstarst','sraastarst','s','s','No encontrado','1235123532152','1235123512351',1,1,'12345','holamundo'),
(2,'SubConsultoiroDos','arstarstrst','arstarstars','ss','ss','arstqw341234','1235123124351','1235123412341',1,1,'12312','arstarstarst');
=======
>>>>>>> 0bbe361 (Consultorio con delete y generar nuevo)
=======
INSERT INTO `Sub_Consultorio` VALUES
(1,'SubClinicaUno','arstarstarst','sraastarst','s','s','No encontrado','1235123532152','1235123512351',1,1,'12345','holamundo'),
(2,'SubConsultoiroDos','arstarstrst','arstarstars','ss','ss','arstqw341234','1235123124351','1235123412341',1,1,'12312','arstarstarst');
>>>>>>> 15feac0 (Se suben modulo de medicamentos y base de datos)
/*!40000 ALTER TABLE `Sub_Consultorio` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Documento`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Tipo_Documento` WRITE;
/*!40000 ALTER TABLE `Tipo_Documento` DISABLE KEYS */;
INSERT INTO `Tipo_Documento` VALUES
(1,'Sin Definir');
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
  PRIMARY KEY (`id_tipo_pago`),
  UNIQUE KEY `tipo_pago` (`tipo_pago`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Pago`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Tipo_Pago` WRITE;
/*!40000 ALTER TABLE `Tipo_Pago` DISABLE KEYS */;
INSERT INTO `Tipo_Pago` VALUES
(1,'Efectivo'),
(2,'Tarjeta');
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Sangre`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Tipo_Sangre` WRITE;
/*!40000 ALTER TABLE `Tipo_Sangre` DISABLE KEYS */;
INSERT INTO `Tipo_Sangre` VALUES
(3,'A-'),
(2,'A+'),
(7,'AB-'),
(6,'AB+'),
(5,'B-'),
(4,'B+'),
(9,'O-'),
(8,'O+'),
(1,'SN');
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
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tipo_Usuario`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Tipo_Usuario` WRITE;
/*!40000 ALTER TABLE `Tipo_Usuario` DISABLE KEYS */;
INSERT INTO `Tipo_Usuario` VALUES
(2,'Administrador'),
(5,'Caja'),
(1,'Enfermero'),
(4,'Farmacéutico'),
(6,'Médico'),
(3,'Propietario');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tratamiento`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Tratamiento` WRITE;
/*!40000 ALTER TABLE `Tratamiento` DISABLE KEYS */;
INSERT INTO `Tratamiento` VALUES
(1,'Sin Definir');
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
  KEY `FK_TIPOUSUARIO_USUARIO` (`id_tipo_usuario`),
  KEY `FK_CONSULTORIO_USUARIO` (`id_consultorio`),
  KEY `FK_ESCUELA_USUARIO` (`id_escuela`),
  KEY `INDEX_USUARIO_CONTRASEÑA` (`usuario_password`,`usuario_name`),
  CONSTRAINT `FK_CONSULTORIO_USUARIO` FOREIGN KEY (`id_consultorio`) REFERENCES `Consultorio` (`id_consultorio`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_ESCUELA_USUARIO` FOREIGN KEY (`id_escuela`) REFERENCES `Escuela` (`id_escuela`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `FK_TIPOUSUARIO_USUARIO` FOREIGN KEY (`id_tipo_usuario`) REFERENCES `Tipo_Usuario` (`id_tipo_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Usuario`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Usuario` WRITE;
/*!40000 ALTER TABLE `Usuario` DISABLE KEYS */;
INSERT INTO `Usuario` VALUES
(1,'Asgard','Juarez','Campos','$argon2id$v=19$m=65536,t=3,p=4$MSBBnmcG/Iyp77iBOnn5gg$+vw8pZ9VUvCrU1CnDCyqS1XgcSPhZKxXNnyiqha7AU0','0000','0000',3,1,5),
(2,'arstarstarst','arsarstarst','arstartsart','$argon2id$v=19$m=65536,t=3,p=4$kfPyA8kxxaV8pgd5saHqFw$TaSA1w1f+tGncQRSoAViDRIFuktKhG3K8pEdZ/eAEhs','1212512431351','1234132412341',3,7,2),
(3,'Jessica','Alvarez','Centeno','$argon2id$v=19$m=65536,t=3,p=4$uvAuAfHHsDwD+hvBaS6XHA$eurVKNSzKzsWwxreMDm29kxKlr4IeDvYCcrjWbu8tkM','1324124234213','1324123412341',1,1,4),
(4,'Tonatiuh Uriel','Miranda','Gonzales','$argon2id$v=19$m=65536,t=3,p=4$CiALXjri/6tKmV0AhVwCcg$KbBgnRQMaamE+GjuKHI9HCfiDQ1nRepFa6xPPWWGRCw','1234123412341','3214123412341',6,1,4),
(6,'Pruebados','PaternoDos','MaternoDos','$argon2id$v=19$m=65536,t=3,p=4$4U1/CfzeupYSrUDGKHL3Yw$kQDxCc50Lr49wxD6dv3VIFnQBZ11vMh+g5g/rZk55sM','1234123412341','1234123412341',3,9,11);
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Via_Administrar_Medicamento`
--

SET @OLD_AUTOCOMMIT=@@AUTOCOMMIT, @@AUTOCOMMIT=0;
LOCK TABLES `Via_Administrar_Medicamento` WRITE;
/*!40000 ALTER TABLE `Via_Administrar_Medicamento` DISABLE KEYS */;
INSERT INTO `Via_Administrar_Medicamento` VALUES
(3,'Inhalada'),
(2,'Oral'),
(1,'Sin Definir');
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

<<<<<<< HEAD
<<<<<<< HEAD
-- Dump completed on 2026-08-14  4:55:56
=======
-- Dump completed on 2026-08-13 22:40:13
>>>>>>> 0bbe361 (Consultorio con delete y generar nuevo)
=======
-- Dump completed on 2026-08-14  4:55:56
>>>>>>> 15feac0 (Se suben modulo de medicamentos y base de datos)
