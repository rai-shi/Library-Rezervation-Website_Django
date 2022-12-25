CREATE TABLE `kutuphane` (
  `konumID` int NOT NULL AUTO_INCREMENT,
  `odaNo` int NOT NULL,
  `MasaNo` char(1) NOT NULL,
  `sandalyeNo` char(2) NOT NULL,
  PRIMARY KEY (`konumID`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `misafiruye` (
  `UyeID` int NOT NULL AUTO_INCREMENT,
  `Ad` varchar(45) NOT NULL,
  `Soyad` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Sifre` varchar(8) NOT NULL,
  `Meslek` varchar(45) DEFAULT NULL,
  `telno` char(11) NOT NULL,
  PRIMARY KEY (`UyeID`),
  UNIQUE KEY `Email_UNIQUE` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `ogrenciuye` (
  `uyeID` int NOT NULL AUTO_INCREMENT,
  `Ad` varchar(40) NOT NULL,
  `Soyad` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Sifre` varchar(8) NOT NULL,
  `Telno` varchar(45) DEFAULT NULL,
  `Puan` int DEFAULT NULL,
  `OgrNo` int NOT NULL,
  `Fakulte` varchar(45) DEFAULT NULL,
  `Bolum` varchar(45) DEFAULT NULL,
  `MezunTarihi` date DEFAULT NULL,
  PRIMARY KEY (`uyeID`),
  UNIQUE KEY `Email_UNIQUE` (`Email`),
  UNIQUE KEY `OgrNo_UNIQUE` (`OgrNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `oneri` (
  `oneriID` int NOT NULL AUTO_INCREMENT,
  `oneri` tinytext,
  `UyeID` int NOT NULL,
  PRIMARY KEY (`oneriID`),
  KEY `ogr` (`UyeID`),
  CONSTRAINT `misafir` FOREIGN KEY (`UyeID`) REFERENCES `misafiruye` (`UyeID`),
  CONSTRAINT `ogr` FOREIGN KEY (`UyeID`) REFERENCES `ogrenciuye` (`uyeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `rezervasyon` (
  `rezervasyonID` int NOT NULL AUTO_INCREMENT,
  `uyeID` int NOT NULL,
  `tarih` date NOT NULL,
  `saatBaslangic` time NOT NULL,
  `saatBitis` time NOT NULL,
  `molahakki` time DEFAULT NULL,
  `konumID` int NOT NULL,
  PRIMARY KEY (`rezervasyonID`),
  KEY `rezervasyonUyeO` (`uyeID`),
  KEY `konumRezerve` (`konumID`),
  CONSTRAINT `konumRezerve` FOREIGN KEY (`konumID`) REFERENCES `kutuphane` (`konumID`),
  CONSTRAINT `rezervasyonUyeM` FOREIGN KEY (`uyeID`) REFERENCES `misafiruye` (`UyeID`),
  CONSTRAINT `rezervasyonUyeO` FOREIGN KEY (`uyeID`) REFERENCES `ogrenciuye` (`uyeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `siparis` (
  `siparisID` int NOT NULL AUTO_INCREMENT,
  `uyeID` int NOT NULL,
  `siparisTarih` datetime NOT NULL,
  `teslimTarih` datetime NOT NULL,
  PRIMARY KEY (`siparisID`),
  KEY `msfr` (`uyeID`),
  CONSTRAINT `msfr` FOREIGN KEY (`uyeID`) REFERENCES `misafiruye` (`UyeID`),
  CONSTRAINT `ogrenci` FOREIGN KEY (`uyeID`) REFERENCES `ogrenciuye` (`uyeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `siparisurun` (
  `siparisID` int NOT NULL,
  `urunID` int NOT NULL,
  PRIMARY KEY (`siparisID`,`urunID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `urun` (
  `urunID` int NOT NULL AUTO_INCREMENT,
  `urunIsmi` varchar(45) NOT NULL,
  `urunPuan` int DEFAULT NULL,
  `stok` int DEFAULT NULL,
  `urunFotograf` mediumblob,
  PRIMARY KEY (`urunID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
