USE [master]
GO

/****** Object:  Database [kutuphaneRezervasyon0]    Script Date: 16.12.2022 11:30:22 ******/
CREATE DATABASE [kutuphaneRezervasyon0]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'kutuphaneRezervasyon0', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\kutuphaneRezervasyon0.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'kutuphaneRezervasyon0_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\kutuphaneRezervasyon0_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [kutuphaneRezervasyon0].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET ARITHABORT OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET  DISABLE_BROKER 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET RECOVERY FULL 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET  MULTI_USER 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET DB_CHAINING OFF 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET QUERY_STORE = OFF
GO

ALTER DATABASE [kutuphaneRezervasyon0] SET  READ_WRITE 
GO

USE [kutuphaneRezervasyon0]
GO

/****** Object:  Table [dbo].[ogrenciUye]    Script Date: 16.12.2022 09:12:41 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[ogrenciUye](
	[UyeID] [int] IDENTITY(1,1) NOT NULL,
	[Ad] [varchar](50) NOT NULL,
	[Soyad] [varchar](50) NOT NULL,
	[Email] [varchar](50) NOT NULL,
	[Sifre] [char](8) NOT NULL,
	[TelNo] [char](11) NOT NULL,
	[Puan] [int] NOT NULL,
	[OgrNo] [varchar](20) NOT NULL,
	[Fakulte] [varchar](50) NULL,
	[Bolum] [varchar](50) NULL,
	[MezunTarihi] [date] NOT NULL,
 CONSTRAINT [PK_ogrenciUye] PRIMARY KEY CLUSTERED 
(
	[UyeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[ogrenciUye] ADD  CONSTRAINT [DF_ogrenciUye_Puan]  DEFAULT ((0)) FOR [Puan]
GO

USE [kutuphaneRezervasyon0]
GO

/****** Object:  Table [dbo].[misafirUye]    Script Date: 16.12.2022 09:12:14 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[misafirUye](
	[UyeID] [int] IDENTITY(10000,1) NOT NULL,
	[Ad] [nvarchar](50) NOT NULL,
	[Soyad] [nvarchar](50) NOT NULL,
	[Email] [nvarchar](50) NOT NULL,
	[Sifre] [char](8) NOT NULL,
	[telNo] [char](11) NOT NULL,
	[meslek] [nvarchar](50) NULL,
 CONSTRAINT [PK_misafirUye] PRIMARY KEY CLUSTERED 
(
	[UyeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

USE [kutuphaneRezervasyon0]
GO

/****** Object:  Table [dbo].[urun]    Script Date: 16.12.2022 09:15:41 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[urun](
	[urunID] [int] IDENTITY(1,1) NOT NULL,
	[urunIsmi] [nvarchar](50) NOT NULL,
	[urunPuan] [int] NOT NULL,
	[stok] [int] NOT NULL,
	[urunFotograf] [image] NULL,
 CONSTRAINT [PK_urun] PRIMARY KEY CLUSTERED 
(
	[urunID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

USE [kutuphaneRezervasyon0]
GO

/****** Object:  Table [dbo].[siparis]    Script Date: 16.12.2022 09:14:21 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[siparis](
	[siparisID] [int] IDENTITY(1,1) NOT NULL,
	[uyeID] [int] NOT NULL,
	[siparisTarih] [datetime] NOT NULL,
	[teslimTarih] [datetime] NULL,
 CONSTRAINT [PK_siparis] PRIMARY KEY CLUSTERED 
(
	[siparisID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[siparis]  WITH CHECK ADD  CONSTRAINT [FK_siparis_misafirUye] FOREIGN KEY([uyeID])
REFERENCES [dbo].[misafirUye] ([UyeID])
GO

ALTER TABLE [dbo].[siparis] CHECK CONSTRAINT [FK_siparis_misafirUye]
GO

ALTER TABLE [dbo].[siparis]  WITH CHECK ADD  CONSTRAINT [FK_siparis_ogrenciUye] FOREIGN KEY([uyeID])
REFERENCES [dbo].[ogrenciUye] ([UyeID])
GO

ALTER TABLE [dbo].[siparis] CHECK CONSTRAINT [FK_siparis_ogrenciUye]
GO

USE [kutuphaneRezervasyon0]
GO

/****** Object:  Table [dbo].[siparisUrun]    Script Date: 16.12.2022 09:15:16 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[siparisUrun](
	[siparisID] [int] NOT NULL,
	[urunID] [int] NOT NULL,
 CONSTRAINT [PK_siparisUrun] PRIMARY KEY CLUSTERED 
(
	[siparisID] ASC,
	[urunID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[siparisUrun]  WITH CHECK ADD  CONSTRAINT [FK_siparisUrun_siparis] FOREIGN KEY([siparisID])
REFERENCES [dbo].[siparis] ([siparisID])
GO

ALTER TABLE [dbo].[siparisUrun] CHECK CONSTRAINT [FK_siparisUrun_siparis]
GO

ALTER TABLE [dbo].[siparisUrun]  WITH CHECK ADD  CONSTRAINT [FK_siparisUrun_urun] FOREIGN KEY([urunID])
REFERENCES [dbo].[urun] ([urunID])
GO

ALTER TABLE [dbo].[siparisUrun] CHECK CONSTRAINT [FK_siparisUrun_urun]
GO

USE [kutuphaneRezervasyon0]
GO

/****** Object:  Table [dbo].[kutuphane]    Script Date: 16.12.2022 09:10:33 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[kutuphane](
	[konumID] [int] IDENTITY(1,1) NOT NULL,
	[OdaNo] [int] NOT NULL,
	[MasaNo] [char](1) NOT NULL,
	[SandaleNo] [char](2) NOT NULL,
 CONSTRAINT [PK_kutuphane] PRIMARY KEY CLUSTERED 
(
	[konumID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

USE [kutuphaneRezervasyon0]
GO

/****** Object:  Table [dbo].[oneri]    Script Date: 16.12.2022 09:13:06 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[oneri](
	[oneriID] [int] IDENTITY(1,1) NOT NULL,
	[UyeID] [int] NOT NULL,
	[oneri] [ntext] NOT NULL,
 CONSTRAINT [PK_oneri] PRIMARY KEY CLUSTERED 
(
	[oneriID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO

ALTER TABLE [dbo].[oneri]  WITH CHECK ADD  CONSTRAINT [FK_oneri_misafirUye] FOREIGN KEY([UyeID])
REFERENCES [dbo].[misafirUye] ([UyeID])
GO

ALTER TABLE [dbo].[oneri] CHECK CONSTRAINT [FK_oneri_misafirUye]
GO

ALTER TABLE [dbo].[oneri]  WITH CHECK ADD  CONSTRAINT [FK_oneri_ogrenciUye] FOREIGN KEY([UyeID])
REFERENCES [dbo].[ogrenciUye] ([UyeID])
GO

ALTER TABLE [dbo].[oneri] CHECK CONSTRAINT [FK_oneri_ogrenciUye]
GO

USE [kutuphaneRezervasyon0]
GO

/****** Object:  Table [dbo].[rezervasyon]    Script Date: 16.12.2022 09:13:47 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[rezervasyon](
	[rezervasyonID] [int] IDENTITY(1,1) NOT NULL,
	[UyeID] [int] NOT NULL,
	[konumID] [int] NOT NULL,
	[tarih] [date] NOT NULL,
	[saatBaslangýc] [time](7) NOT NULL,
	[saatBitis] [time](7) NOT NULL,
	[molaHakký] [time](7) NULL,
 CONSTRAINT [PK_rezervasyon] PRIMARY KEY CLUSTERED 
(
	[rezervasyonID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[rezervasyon]  WITH CHECK ADD  CONSTRAINT [FK_rezervasyon_kutuphane] FOREIGN KEY([konumID])
REFERENCES [dbo].[kutuphane] ([konumID])
GO

ALTER TABLE [dbo].[rezervasyon] CHECK CONSTRAINT [FK_rezervasyon_kutuphane]
GO

ALTER TABLE [dbo].[rezervasyon]  WITH CHECK ADD  CONSTRAINT [FK_rezervasyon_misafirUye] FOREIGN KEY([UyeID])
REFERENCES [dbo].[misafirUye] ([UyeID])
GO

ALTER TABLE [dbo].[rezervasyon] CHECK CONSTRAINT [FK_rezervasyon_misafirUye]
GO

ALTER TABLE [dbo].[rezervasyon]  WITH CHECK ADD  CONSTRAINT [FK_rezervasyon_ogrenciUye] FOREIGN KEY([UyeID])
REFERENCES [dbo].[ogrenciUye] ([UyeID])
GO

ALTER TABLE [dbo].[rezervasyon] CHECK CONSTRAINT [FK_rezervasyon_ogrenciUye]
GO
