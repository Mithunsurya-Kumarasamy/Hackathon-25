-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: disaster_db
-- ------------------------------------------------------
-- Server version	8.0.41

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `allocations`
--

DROP TABLE IF EXISTS `allocations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `allocations` (
  `alloc_id` int NOT NULL AUTO_INCREMENT,
  `request_id` int DEFAULT NULL,
  `item_name` varchar(255) NOT NULL,
  `allocated_to` varchar(255) NOT NULL,
  PRIMARY KEY (`alloc_id`),
  KEY `request_id` (`request_id`),
  CONSTRAINT `allocations_ibfk_1` FOREIGN KEY (`request_id`) REFERENCES `requests` (`request_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `allocations`
--

LOCK TABLES `allocations` WRITE;
/*!40000 ALTER TABLE `allocations` DISABLE KEYS */;
/*!40000 ALTER TABLE `allocations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bangalore_inventory`
--

DROP TABLE IF EXISTS `bangalore_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bangalore_inventory` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(255) NOT NULL,
  `quantity` int NOT NULL,
  `item_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bangalore_inventory`
--

LOCK TABLES `bangalore_inventory` WRITE;
/*!40000 ALTER TABLE `bangalore_inventory` DISABLE KEYS */;
INSERT INTO `bangalore_inventory` VALUES (1,'Rice',100,'Food'),(2,'Wheat Flour',80,'Food'),(3,'Bottled Water',200,'General'),(4,'First Aid Kit',50,'Medical'),(5,'Canned Food',120,'Food'),(6,'Blankets',75,'General'),(7,'Painkillers',90,'Medical'),(8,'Milk Powder',60,'Food'),(9,'Torch',30,'General'),(10,'Sanitary Pads',110,'Medical');
/*!40000 ALTER TABLE `bangalore_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chennai_inventory`
--

DROP TABLE IF EXISTS `chennai_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chennai_inventory` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(255) NOT NULL,
  `quantity` int NOT NULL,
  `item_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chennai_inventory`
--

LOCK TABLES `chennai_inventory` WRITE;
/*!40000 ALTER TABLE `chennai_inventory` DISABLE KEYS */;
INSERT INTO `chennai_inventory` VALUES (1,'Rice',100,'Food'),(2,'Wheat Flour',80,'Food'),(3,'Bottled Water',200,'General'),(4,'First Aid Kit',50,'Medical'),(5,'Canned Food',120,'Food'),(6,'Blankets',75,'General'),(7,'Painkillers',90,'Medical'),(8,'Milk Powder',60,'Food'),(9,'Torch',30,'General'),(10,'Sanitary Pads',110,'Medical');
/*!40000 ALTER TABLE `chennai_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `information`
--

DROP TABLE IF EXISTS `information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `information` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Disaster` varchar(255) DEFAULT NULL,
  `Address` text,
  `Severity` int DEFAULT NULL,
  `People` int DEFAULT NULL,
  `Urgency` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `information`
--

LOCK TABLES `information` WRITE;
/*!40000 ALTER TABLE `information` DISABLE KEYS */;
INSERT INTO `information` VALUES (1,'Earthquake','',2,1,1),(2,'Flood','kjhgf',1,2,2);
/*!40000 ALTER TABLE `information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(255) NOT NULL,
  `quantity` int NOT NULL,
  `item_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,'Rice',100,'Food'),(2,'Wheat Flour',80,'Food'),(3,'Bottled Water',200,'General'),(4,'First Aid Kit',50,'Medical'),(5,'Canned Food',120,'Food'),(6,'Blankets',75,'General'),(7,'Painkillers',90,'Medical'),(8,'Milk Powder',60,'Food'),(9,'Torch',30,'General'),(10,'Sanitary Pads',110,'Medical');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `location_id` int NOT NULL AUTO_INCREMENT,
  `city_name` varchar(255) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=301 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES (1,'Chennai',13.08,80.27),(2,'Coimbatore',11.01,76.95),(3,'Madurai',9.92,78.11),(4,'Tiruchirappalli',10.79,78.7),(5,'Salem',11.66,78.14),(6,'Tirunelveli',8.71,77.75),(7,'Erode',11.34,77.71),(8,'Vellore',12.91,79.13),(9,'Thoothukudi',8.76,78.13),(10,'Tiruppur',11.1,77.34),(11,'Kanchipuram',12.83,79.7),(12,'Dindigul',10.36,77.97),(13,'Thanjavur',10.78,79.13),(14,'Karur',10.96,78.07),(15,'Nagapattinam',10.76,79.83),(16,'Chennai',13.08,80.27),(17,'Coimbatore',11.01,76.95),(18,'Madurai',9.92,78.11),(19,'Tiruchirappalli',10.79,78.7),(20,'Salem',11.66,78.14),(21,'Tirunelveli',8.71,77.75),(22,'Erode',11.34,77.71),(23,'Vellore',12.91,79.13),(24,'Thoothukudi',8.76,78.13),(25,'Tiruppur',11.1,77.34),(26,'Kanchipuram',12.83,79.7),(27,'Dindigul',10.36,77.97),(28,'Thanjavur',10.78,79.13),(29,'Karur',10.96,78.07),(30,'Nagapattinam',10.76,79.83),(31,'Chennai',13.08,80.27),(32,'Coimbatore',11.01,76.95),(33,'Madurai',9.92,78.11),(34,'Tiruchirappalli',10.79,78.7),(35,'Salem',11.66,78.14),(36,'Tirunelveli',8.71,77.75),(37,'Erode',11.34,77.71),(38,'Vellore',12.91,79.13),(39,'Thoothukudi',8.76,78.13),(40,'Tiruppur',11.1,77.34),(41,'Kanchipuram',12.83,79.7),(42,'Dindigul',10.36,77.97),(43,'Thanjavur',10.78,79.13),(44,'Karur',10.96,78.07),(45,'Nagapattinam',10.76,79.83),(46,'Chennai',13.08,80.27),(47,'Coimbatore',11.01,76.95),(48,'Madurai',9.92,78.11),(49,'Tiruchirappalli',10.79,78.7),(50,'Salem',11.66,78.14),(51,'Tirunelveli',8.71,77.75),(52,'Erode',11.34,77.71),(53,'Vellore',12.91,79.13),(54,'Thoothukudi',8.76,78.13),(55,'Tiruppur',11.1,77.34),(56,'Kanchipuram',12.83,79.7),(57,'Dindigul',10.36,77.97),(58,'Thanjavur',10.78,79.13),(59,'Karur',10.96,78.07),(60,'Nagapattinam',10.76,79.83),(61,'Chennai',13.08,80.27),(62,'Coimbatore',11.01,76.95),(63,'Madurai',9.92,78.11),(64,'Tiruchirappalli',10.79,78.7),(65,'Salem',11.66,78.14),(66,'Tirunelveli',8.71,77.75),(67,'Erode',11.34,77.71),(68,'Vellore',12.91,79.13),(69,'Thoothukudi',8.76,78.13),(70,'Tiruppur',11.1,77.34),(71,'Kanchipuram',12.83,79.7),(72,'Dindigul',10.36,77.97),(73,'Thanjavur',10.78,79.13),(74,'Karur',10.96,78.07),(75,'Nagapattinam',10.76,79.83),(76,'Chennai',13.08,80.27),(77,'Coimbatore',11.01,76.95),(78,'Madurai',9.92,78.11),(79,'Tiruchirappalli',10.79,78.7),(80,'Salem',11.66,78.14),(81,'Tirunelveli',8.71,77.75),(82,'Erode',11.34,77.71),(83,'Vellore',12.91,79.13),(84,'Thoothukudi',8.76,78.13),(85,'Tiruppur',11.1,77.34),(86,'Kanchipuram',12.83,79.7),(87,'Dindigul',10.36,77.97),(88,'Thanjavur',10.78,79.13),(89,'Karur',10.96,78.07),(90,'Nagapattinam',10.76,79.83),(91,'Chennai',13.08,80.27),(92,'Coimbatore',11.01,76.95),(93,'Madurai',9.92,78.11),(94,'Tiruchirappalli',10.79,78.7),(95,'Salem',11.66,78.14),(96,'Tirunelveli',8.71,77.75),(97,'Erode',11.34,77.71),(98,'Vellore',12.91,79.13),(99,'Thoothukudi',8.76,78.13),(100,'Tiruppur',11.1,77.34),(101,'Kanchipuram',12.83,79.7),(102,'Dindigul',10.36,77.97),(103,'Thanjavur',10.78,79.13),(104,'Karur',10.96,78.07),(105,'Nagapattinam',10.76,79.83),(106,'Chennai',13.08,80.27),(107,'Coimbatore',11.01,76.95),(108,'Madurai',9.92,78.11),(109,'Tiruchirappalli',10.79,78.7),(110,'Salem',11.66,78.14),(111,'Tirunelveli',8.71,77.75),(112,'Erode',11.34,77.71),(113,'Vellore',12.91,79.13),(114,'Thoothukudi',8.76,78.13),(115,'Tiruppur',11.1,77.34),(116,'Kanchipuram',12.83,79.7),(117,'Dindigul',10.36,77.97),(118,'Thanjavur',10.78,79.13),(119,'Karur',10.96,78.07),(120,'Nagapattinam',10.76,79.83),(121,'Chennai',13.08,80.27),(122,'Coimbatore',11.01,76.95),(123,'Madurai',9.92,78.11),(124,'Tiruchirappalli',10.79,78.7),(125,'Salem',11.66,78.14),(126,'Tirunelveli',8.71,77.75),(127,'Erode',11.34,77.71),(128,'Vellore',12.91,79.13),(129,'Thoothukudi',8.76,78.13),(130,'Tiruppur',11.1,77.34),(131,'Kanchipuram',12.83,79.7),(132,'Dindigul',10.36,77.97),(133,'Thanjavur',10.78,79.13),(134,'Karur',10.96,78.07),(135,'Nagapattinam',10.76,79.83),(136,'Chennai',13.08,80.27),(137,'Coimbatore',11.01,76.95),(138,'Madurai',9.92,78.11),(139,'Tiruchirappalli',10.79,78.7),(140,'Salem',11.66,78.14),(141,'Tirunelveli',8.71,77.75),(142,'Erode',11.34,77.71),(143,'Vellore',12.91,79.13),(144,'Thoothukudi',8.76,78.13),(145,'Tiruppur',11.1,77.34),(146,'Kanchipuram',12.83,79.7),(147,'Dindigul',10.36,77.97),(148,'Thanjavur',10.78,79.13),(149,'Karur',10.96,78.07),(150,'Nagapattinam',10.76,79.83),(151,'Chennai',13.08,80.27),(152,'Coimbatore',11.01,76.95),(153,'Madurai',9.92,78.11),(154,'Tiruchirappalli',10.79,78.7),(155,'Salem',11.66,78.14),(156,'Tirunelveli',8.71,77.75),(157,'Erode',11.34,77.71),(158,'Vellore',12.91,79.13),(159,'Thoothukudi',8.76,78.13),(160,'Tiruppur',11.1,77.34),(161,'Kanchipuram',12.83,79.7),(162,'Dindigul',10.36,77.97),(163,'Thanjavur',10.78,79.13),(164,'Karur',10.96,78.07),(165,'Nagapattinam',10.76,79.83),(166,'Chennai',13.08,80.27),(167,'Coimbatore',11.01,76.95),(168,'Madurai',9.92,78.11),(169,'Tiruchirappalli',10.79,78.7),(170,'Salem',11.66,78.14),(171,'Tirunelveli',8.71,77.75),(172,'Erode',11.34,77.71),(173,'Vellore',12.91,79.13),(174,'Thoothukudi',8.76,78.13),(175,'Tiruppur',11.1,77.34),(176,'Kanchipuram',12.83,79.7),(177,'Dindigul',10.36,77.97),(178,'Thanjavur',10.78,79.13),(179,'Karur',10.96,78.07),(180,'Nagapattinam',10.76,79.83),(181,'Chennai',13.08,80.27),(182,'Coimbatore',11.01,76.95),(183,'Madurai',9.92,78.11),(184,'Tiruchirappalli',10.79,78.7),(185,'Salem',11.66,78.14),(186,'Tirunelveli',8.71,77.75),(187,'Erode',11.34,77.71),(188,'Vellore',12.91,79.13),(189,'Thoothukudi',8.76,78.13),(190,'Tiruppur',11.1,77.34),(191,'Kanchipuram',12.83,79.7),(192,'Dindigul',10.36,77.97),(193,'Thanjavur',10.78,79.13),(194,'Karur',10.96,78.07),(195,'Nagapattinam',10.76,79.83),(196,'Chennai',13.08,80.27),(197,'Coimbatore',11.01,76.95),(198,'Madurai',9.92,78.11),(199,'Tiruchirappalli',10.79,78.7),(200,'Salem',11.66,78.14),(201,'Tirunelveli',8.71,77.75),(202,'Erode',11.34,77.71),(203,'Vellore',12.91,79.13),(204,'Thoothukudi',8.76,78.13),(205,'Tiruppur',11.1,77.34),(206,'Kanchipuram',12.83,79.7),(207,'Dindigul',10.36,77.97),(208,'Thanjavur',10.78,79.13),(209,'Karur',10.96,78.07),(210,'Nagapattinam',10.76,79.83),(211,'Chennai',13.08,80.27),(212,'Coimbatore',11.01,76.95),(213,'Madurai',9.92,78.11),(214,'Tiruchirappalli',10.79,78.7),(215,'Salem',11.66,78.14),(216,'Tirunelveli',8.71,77.75),(217,'Erode',11.34,77.71),(218,'Vellore',12.91,79.13),(219,'Thoothukudi',8.76,78.13),(220,'Tiruppur',11.1,77.34),(221,'Kanchipuram',12.83,79.7),(222,'Dindigul',10.36,77.97),(223,'Thanjavur',10.78,79.13),(224,'Karur',10.96,78.07),(225,'Nagapattinam',10.76,79.83),(226,'Chennai',13.08,80.27),(227,'Coimbatore',11.01,76.95),(228,'Madurai',9.92,78.11),(229,'Tiruchirappalli',10.79,78.7),(230,'Salem',11.66,78.14),(231,'Tirunelveli',8.71,77.75),(232,'Erode',11.34,77.71),(233,'Vellore',12.91,79.13),(234,'Thoothukudi',8.76,78.13),(235,'Tiruppur',11.1,77.34),(236,'Kanchipuram',12.83,79.7),(237,'Dindigul',10.36,77.97),(238,'Thanjavur',10.78,79.13),(239,'Karur',10.96,78.07),(240,'Nagapattinam',10.76,79.83),(241,'Chennai',13.08,80.27),(242,'Coimbatore',11.01,76.95),(243,'Madurai',9.92,78.11),(244,'Tiruchirappalli',10.79,78.7),(245,'Salem',11.66,78.14),(246,'Tirunelveli',8.71,77.75),(247,'Erode',11.34,77.71),(248,'Vellore',12.91,79.13),(249,'Thoothukudi',8.76,78.13),(250,'Tiruppur',11.1,77.34),(251,'Kanchipuram',12.83,79.7),(252,'Dindigul',10.36,77.97),(253,'Thanjavur',10.78,79.13),(254,'Karur',10.96,78.07),(255,'Nagapattinam',10.76,79.83),(256,'Chennai',13.08,80.27),(257,'Coimbatore',11.01,76.95),(258,'Madurai',9.92,78.11),(259,'Tiruchirappalli',10.79,78.7),(260,'Salem',11.66,78.14),(261,'Tirunelveli',8.71,77.75),(262,'Erode',11.34,77.71),(263,'Vellore',12.91,79.13),(264,'Thoothukudi',8.76,78.13),(265,'Tiruppur',11.1,77.34),(266,'Kanchipuram',12.83,79.7),(267,'Dindigul',10.36,77.97),(268,'Thanjavur',10.78,79.13),(269,'Karur',10.96,78.07),(270,'Nagapattinam',10.76,79.83),(271,'Chennai',13.08,80.27),(272,'Coimbatore',11.01,76.95),(273,'Madurai',9.92,78.11),(274,'Tiruchirappalli',10.79,78.7),(275,'Salem',11.66,78.14),(276,'Tirunelveli',8.71,77.75),(277,'Erode',11.34,77.71),(278,'Vellore',12.91,79.13),(279,'Thoothukudi',8.76,78.13),(280,'Tiruppur',11.1,77.34),(281,'Kanchipuram',12.83,79.7),(282,'Dindigul',10.36,77.97),(283,'Thanjavur',10.78,79.13),(284,'Karur',10.96,78.07),(285,'Nagapattinam',10.76,79.83),(286,'Chennai',13.08,80.27),(287,'Coimbatore',11.01,76.95),(288,'Madurai',9.92,78.11),(289,'Tiruchirappalli',10.79,78.7),(290,'Salem',11.66,78.14),(291,'Tirunelveli',8.71,77.75),(292,'Erode',11.34,77.71),(293,'Vellore',12.91,79.13),(294,'Thoothukudi',8.76,78.13),(295,'Tiruppur',11.1,77.34),(296,'Kanchipuram',12.83,79.7),(297,'Dindigul',10.36,77.97),(298,'Thanjavur',10.78,79.13),(299,'Karur',10.96,78.07),(300,'Nagapattinam',10.76,79.83);
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mumbai_inventory`
--

DROP TABLE IF EXISTS `mumbai_inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mumbai_inventory` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(255) NOT NULL,
  `quantity` int NOT NULL,
  `item_type` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`item_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mumbai_inventory`
--

LOCK TABLES `mumbai_inventory` WRITE;
/*!40000 ALTER TABLE `mumbai_inventory` DISABLE KEYS */;
INSERT INTO `mumbai_inventory` VALUES (1,'Rice',100,'Food'),(2,'Wheat Flour',80,'Food'),(3,'Bottled Water',200,'General'),(4,'First Aid Kit',50,'Medical'),(5,'Canned Food',120,'Food'),(6,'Blankets',75,'General'),(7,'Painkillers',90,'Medical'),(8,'Milk Powder',60,'Food'),(9,'Torch',30,'General'),(10,'Sanitary Pads',110,'Medical');
/*!40000 ALTER TABLE `mumbai_inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requests` (
  `request_id` int NOT NULL AUTO_INCREMENT,
  `item_name` varchar(255) NOT NULL,
  `quantity_needed` int NOT NULL,
  `priority` int NOT NULL,
  `location` varchar(255) NOT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `volunteers`
--

DROP TABLE IF EXISTS `volunteers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `volunteers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `assigned_location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `volunteers`
--

LOCK TABLES `volunteers` WRITE;
/*!40000 ALTER TABLE `volunteers` DISABLE KEYS */;
INSERT INTO `volunteers` VALUES (1,'Mithun',14,'cbe','Relief Camp A');
/*!40000 ALTER TABLE `volunteers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-17  2:59:30
