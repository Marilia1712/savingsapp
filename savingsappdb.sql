CREATE DATABASE  IF NOT EXISTS `savingsapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `savingsapp`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: savingsapp
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `budget`
--

DROP TABLE IF EXISTS `budget`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `budget` (
  `RangeTemporale` enum('settimana','mese','anno') NOT NULL,
  `NomeCatSpese` varchar(45) NOT NULL,
  `Importo` double NOT NULL,
  PRIMARY KEY (`RangeTemporale`,`NomeCatSpese`),
  KEY `fk_budget_idx` (`NomeCatSpese`),
  CONSTRAINT `fk_budget` FOREIGN KEY (`NomeCatSpese`) REFERENCES `categorie_spese` (`NomeCatSpese`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='MUST ADD FOREIGN KEY \n(ref: NomeCatSpese)';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `budget`
--

LOCK TABLES `budget` WRITE;
/*!40000 ALTER TABLE `budget` DISABLE KEYS */;
INSERT INTO `budget` VALUES ('mese','Alimentari',140),('mese','Shopping',250);
/*!40000 ALTER TABLE `budget` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorie_conti`
--

DROP TABLE IF EXISTS `categorie_conti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorie_conti` (
  `NomeCatConti` varchar(45) NOT NULL,
  `IconaCatConti` blob DEFAULT NULL,
  PRIMARY KEY (`NomeCatConti`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorie_conti`
--

LOCK TABLES `categorie_conti` WRITE;
/*!40000 ALTER TABLE `categorie_conti` DISABLE KEYS */;
INSERT INTO `categorie_conti` VALUES ('Bancomat',NULL),('Contanti',NULL),('Cripto',NULL),('Postepay',NULL);
/*!40000 ALTER TABLE `categorie_conti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorie_guadagni`
--

DROP TABLE IF EXISTS `categorie_guadagni`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorie_guadagni` (
  `NomeCatGuad` varchar(45) NOT NULL,
  `IconaCatGuad` blob DEFAULT NULL,
  `GuadagnoTotale` double DEFAULT 0,
  PRIMARY KEY (`NomeCatGuad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorie_guadagni`
--

LOCK TABLES `categorie_guadagni` WRITE;
/*!40000 ALTER TABLE `categorie_guadagni` DISABLE KEYS */;
INSERT INTO `categorie_guadagni` VALUES ('-',NULL,0),('Altro',NULL,200),('Investimenti',NULL,0),('Regalo',NULL,50),('Stipendio',NULL,1500),('Vendita',NULL,0);
/*!40000 ALTER TABLE `categorie_guadagni` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categorie_spese`
--

DROP TABLE IF EXISTS `categorie_spese`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorie_spese` (
  `NomeCatSpese` varchar(45) NOT NULL,
  `IconaCatSpese` blob DEFAULT NULL,
  `SpesaTotale` double DEFAULT 0,
  PRIMARY KEY (`NomeCatSpese`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorie_spese`
--

LOCK TABLES `categorie_spese` WRITE;
/*!40000 ALTER TABLE `categorie_spese` DISABLE KEYS */;
INSERT INTO `categorie_spese` VALUES ('-',NULL,0),('Affitto',NULL,0),('Alimentari',NULL,27.8),('Altro',NULL,0),('Asporto',NULL,0),('Bollette',NULL,0),('Hobby',NULL,0),('Shopping',NULL,254.99),('Socialità',NULL,418.2),('Trasporti',NULL,8.9),('Viaggi',NULL,0);
/*!40000 ALTER TABLE `categorie_spese` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conti`
--

DROP TABLE IF EXISTS `conti`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conti` (
  `NomeConto` varchar(45) NOT NULL,
  `IconaConto` blob DEFAULT NULL,
  `BilancioConto` double NOT NULL DEFAULT 0,
  `Nota` varchar(100) DEFAULT '...',
  `NomeCatConti` varchar(45) NOT NULL,
  `GuadagnoTotale` double DEFAULT 0,
  `SpesaTotale` double DEFAULT 0,
  PRIMARY KEY (`NomeConto`),
  KEY `fk_conti_idx` (`NomeCatConti`),
  CONSTRAINT `fk_conti` FOREIGN KEY (`NomeCatConti`) REFERENCES `categorie_conti` (`NomeCatConti`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conti`
--

LOCK TABLES `conti` WRITE;
/*!40000 ALTER TABLE `conti` DISABLE KEYS */;
INSERT INTO `conti` VALUES ('American Express Gold',NULL,930,'per lo svago','Bancomat',20,340),('PrepagataPP',NULL,171.1,'da usare solo per le emergenze','Postepay',180,8.9),('SanPaoloBancomat',NULL,1060.020000000004,'','Bancomat',1550,489.98);
/*!40000 ALTER TABLE `conti` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `depositi_risparmi`
--

DROP TABLE IF EXISTS `depositi_risparmi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `depositi_risparmi` (
  `NomeDeposito` varchar(45) NOT NULL,
  `NomeSorgente` varchar(45) NOT NULL,
  `NomeDestinazione` varchar(45) NOT NULL,
  `Nota` varchar(100) DEFAULT '...',
  `IconaDeposito` blob DEFAULT NULL,
  `Ciclicita` enum('giorno','settimana','mese') NOT NULL,
  `DataInizio` date NOT NULL,
  `NumeroCicli` int(11) DEFAULT NULL,
  `ImportoSingoloDeposito` double DEFAULT NULL,
  `NomeDesiderio` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`NomeDeposito`,`NomeSorgente`),
  UNIQUE KEY `NomeDesiderio_UNIQUE` (`NomeDesiderio`),
  KEY `fk_contosorgente_idx` (`NomeDesiderio`),
  KEY `fk_depositi_risparmi_idx` (`NomeSorgente`),
  KEY `fk_depositi_risparmi_idx1` (`NomeDestinazione`),
  CONSTRAINT `fk_depositi_risparmi` FOREIGN KEY (`NomeSorgente`) REFERENCES `conti` (`NomeConto`) ON DELETE CASCADE,
  CONSTRAINT `fk_depositi_risparmi1` FOREIGN KEY (`NomeDestinazione`) REFERENCES `conti` (`NomeConto`) ON DELETE CASCADE,
  CONSTRAINT `fk_desiderio` FOREIGN KEY (`NomeDesiderio`) REFERENCES `desideri` (`NomeDesiderio`) ON DELETE CASCADE ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `depositi_risparmi`
--

LOCK TABLES `depositi_risparmi` WRITE;
/*!40000 ALTER TABLE `depositi_risparmi` DISABLE KEYS */;
INSERT INTO `depositi_risparmi` VALUES ('Deposito Panda','SanPaoloBancomat','American Express Gold','',NULL,'giorno','2024-04-03',NULL,15,'Macchina'),('Deposito Regalo Mamma','SanPaoloBancomat','American Express Gold','',NULL,'giorno','2024-06-24',NULL,15,'Chitarra'),('Deposito Vacanze','SanPaoloBancomat','American Express Gold','non vedo l\'ora! :)',NULL,'giorno','2024-06-24',NULL,100,'Caraibi');
/*!40000 ALTER TABLE `depositi_risparmi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `desideri`
--

DROP TABLE IF EXISTS `desideri`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `desideri` (
  `NomeDesiderio` varchar(45) NOT NULL,
  `ImportoTotale` double NOT NULL,
  PRIMARY KEY (`NomeDesiderio`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `desideri`
--

LOCK TABLES `desideri` WRITE;
/*!40000 ALTER TABLE `desideri` DISABLE KEYS */;
INSERT INTO `desideri` VALUES ('Caraibi',2300),('Chitarra',420),('Macchina',9500),('Piscina',15000);
/*!40000 ALTER TABLE `desideri` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `elementi`
--

DROP TABLE IF EXISTS `elementi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `elementi` (
  `Importo` double NOT NULL,
  `Tipo` enum('guadagno','spesa') NOT NULL,
  `Nota` varchar(100) DEFAULT '...',
  `Data` date NOT NULL,
  `Ora` time NOT NULL,
  `NomeMembro` varchar(45) NOT NULL,
  `NomeConto` varchar(45) NOT NULL,
  `NomeLocalita` varchar(45) DEFAULT NULL,
  `NomeCatGuad` varchar(45) DEFAULT '-',
  `NomeCatSpese` varchar(45) DEFAULT '-',
  PRIMARY KEY (`Data`,`Ora`,`NomeMembro`),
  KEY `fk_elementi_idx1` (`NomeConto`),
  KEY `fk_elementi_idx2` (`NomeLocalita`),
  KEY `fk_elementi_idx3` (`NomeCatGuad`),
  KEY `fk_elementi_idx4` (`NomeCatSpese`),
  KEY `fk_elementi_idx5` (`NomeMembro`),
  CONSTRAINT `fk_elementi1` FOREIGN KEY (`NomeConto`) REFERENCES `conti` (`NomeConto`) ON DELETE CASCADE,
  CONSTRAINT `fk_elementi2` FOREIGN KEY (`NomeLocalita`) REFERENCES `località` (`NomeLocalita`) ON DELETE CASCADE,
  CONSTRAINT `fk_elementi3` FOREIGN KEY (`NomeCatGuad`) REFERENCES `categorie_guadagni` (`NomeCatGuad`) ON DELETE CASCADE,
  CONSTRAINT `fk_elementi4` FOREIGN KEY (`NomeCatSpese`) REFERENCES `categorie_spese` (`NomeCatSpese`) ON DELETE CASCADE,
  CONSTRAINT `fk_elementi5` FOREIGN KEY (`NomeMembro`) REFERENCES `membri` (`NomeMembro`) ON DELETE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `elementi`
--

LOCK TABLES `elementi` WRITE;
/*!40000 ALTER TABLE `elementi` DISABLE KEYS */;
INSERT INTO `elementi` VALUES (1500,'guadagno','','2024-06-25','13:54:33','Me','SanPaoloBancomat','Lavoro','Stipendio','-'),(180,'guadagno','Pippi - primo posto nel concorso di bellezza per gatti','2024-06-25','13:57:29','Gatto','PrepagataPP','Centro commerciale','Altro','-'),(50,'guadagno','regalo di compleanno da parte di nonna','2024-06-25','13:58:18','Me','SanPaoloBancomat','Casa','Regalo','-'),(78.2,'spesa','','2024-06-25','13:58:57','Famiglia','SanPaoloBancomat','Sushi','-','Socialità'),(4.99,'spesa','spazzolino nuovo','2024-06-25','13:59:42','Me','SanPaoloBancomat','Conad','-','Shopping'),(8.9,'spesa','','2024-06-25','14:01:16','Me','PrepagataPP','-','-','Trasporti'),(250,'spesa','tende nuove','2024-06-25','14:02:07','Casa','SanPaoloBancomat','Centro commerciale','-','Shopping'),(27.8,'spesa','carote salite a 3.80/kg','2024-06-25','14:04:37','Famiglia','SanPaoloBancomat','Conad','-','Alimentari'),(340,'spesa','weekend fuori porta','2024-06-26','09:01:38','Famiglia','American Express Gold','-','-','Socialità'),(20,'guadagno','','2024-06-26','09:03:43','Me','American Express Gold','Casa','Altro','-');
/*!40000 ALTER TABLE `elementi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `località`
--

DROP TABLE IF EXISTS `località`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `località` (
  `NomeLocalita` varchar(45) NOT NULL,
  `Immagine` blob DEFAULT NULL,
  `Citta` varchar(45) DEFAULT NULL,
  `CAP` int(11) DEFAULT NULL,
  `Via` varchar(45) DEFAULT NULL,
  `NumCivico` int(11) DEFAULT NULL,
  `Latitudine` double DEFAULT NULL,
  `Longitudine` double DEFAULT NULL,
  `GuadagnoTotale` double DEFAULT 0,
  `SpesaTotale` double DEFAULT 0,
  PRIMARY KEY (`NomeLocalita`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `località`
--

LOCK TABLES `località` WRITE;
/*!40000 ALTER TABLE `località` DISABLE KEYS */;
INSERT INTO `località` VALUES ('-',NULL,'',0,'',0,0,0,0,360.9),('Casa',NULL,'Cesena',47522,'Via Roma',1,0,0,70,0),('Centro commerciale',NULL,'Forlì',47122,'Piazzale della Cooperazione',2,0,0,180,366.99),('Conad',NULL,'Cesena',47521,'Via Leopoldo Lucchi',525,0,0,0,32.79),('Lavoro',NULL,'',0,'',0,44.2257134,12.0293177,1500,0),('Sushi',NULL,'',0,'',0,44.247859,12.090786,0,78.2);
/*!40000 ALTER TABLE `località` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `membri`
--

DROP TABLE IF EXISTS `membri`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `membri` (
  `NomeMembro` varchar(45) NOT NULL,
  `IconaMembro` blob DEFAULT NULL,
  `GuadagnoTotale` double DEFAULT 0,
  `SpesaTotale` double DEFAULT 0,
  PRIMARY KEY (`NomeMembro`),
  UNIQUE KEY `NomeMembro_UNIQUE` (`NomeMembro`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `membri`
--

LOCK TABLES `membri` WRITE;
/*!40000 ALTER TABLE `membri` DISABLE KEYS */;
INSERT INTO `membri` VALUES ('Casa',NULL,0,250),('Famiglia',NULL,0,446),('Gatto',NULL,180,0),('Me',NULL,1570,142.88);
/*!40000 ALTER TABLE `membri` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-26 11:01:48
