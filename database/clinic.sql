USE [master]
GO

CREATE DATABASE [clinic]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'clinic_backup', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\clinic_backup.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'clinic_backup_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\clinic_backup_log.ldf' , SIZE = 73728KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [clinic] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [clinic].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [clinic] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [clinic] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [clinic] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [clinic] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [clinic] SET ARITHABORT OFF 
GO
ALTER DATABASE [clinic] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [clinic] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [clinic] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [clinic] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [clinic] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [clinic] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [clinic] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [clinic] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [clinic] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [clinic] SET  DISABLE_BROKER 
GO
ALTER DATABASE [clinic] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [clinic] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [clinic] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [clinic] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [clinic] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [clinic] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [clinic] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [clinic] SET RECOVERY FULL 
GO
ALTER DATABASE [clinic] SET  MULTI_USER 
GO
ALTER DATABASE [clinic] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [clinic] SET DB_CHAINING OFF 
GO
ALTER DATABASE [clinic] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [clinic] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [clinic] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [clinic] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'clinic', N'ON'
GO
ALTER DATABASE [clinic] SET QUERY_STORE = ON
GO
ALTER DATABASE [clinic] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [clinic]
GO
/****** Object:  Table [dbo].[BacSi]    Script Date: 4/29/2024 1:29:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BacSi](
	[ID] [char](10) NOT NULL,
	[HoTen] [nvarchar](50) NOT NULL,
	[GioiTinh] [nvarchar](10) NOT NULL,
	[Khoa] [char](10) NOT NULL,
	[BangCap] [nvarchar](50) NOT NULL,
	[Email] [varchar](100) NOT NULL,
	[SDT] [char](10) NOT NULL,
	[HinhAnh] [varchar](max) NOT NULL,
 CONSTRAINT [PK_BacSi] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[BenhNhan]    Script Date: 4/29/2024 1:29:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BenhNhan](
	[ID] [char](10) NOT NULL,
	[HoTen] [nvarchar](50) NOT NULL,
	[GioiTinh] [nvarchar](10) NOT NULL,
	[NgaySinh] [date] NOT NULL,
	[DiaChi] [nvarchar](max) NOT NULL,
	[SDT] [char](10) NOT NULL,
	[TienSuBenhAn] [nvarchar](max) NULL,
 CONSTRAINT [PK_BenhNhan] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[DichVu]    Script Date: 4/29/2024 1:29:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[DichVu](
	[ID] [char](10) NOT NULL,
	[TenDichVu] [nvarchar](100) NOT NULL,
	[Khoa] [char](10) NOT NULL,
	[MoTa] [nvarchar](max) NOT NULL,
	[Phi] [money] NOT NULL,
 CONSTRAINT [PK_DichVu] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[HoaDon]    Script Date: 4/29/2024 1:29:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[HoaDon](
	[ID] [char](10) NOT NULL,
	[BenhNhan] [char](10) NOT NULL,
	[BacSi] [char](10) NOT NULL,
	[NgayTao] [date] NOT NULL,
	[GiamGia] [varchar](5) NULL,
	[TongTien] [money] NOT NULL,
	[TongThu] [money] NOT NULL,
 CONSTRAINT [PK_HoaDon] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[KetQua]    Script Date: 4/29/2024 1:29:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[KetQua](
	[LichKham] [char](10) NOT NULL,
	[ChanDoan] [nvarchar](max) NOT NULL,
	[DieuTri] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_KetQua] PRIMARY KEY CLUSTERED 
(
	[LichKham] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[LichKham]    Script Date: 4/29/2024 1:29:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[LichKham](
	[ID] [char](10) NOT NULL,
	[BenhNhan] [char](10) NOT NULL,
	[BacSi] [char](10) NULL,
	[DichVu] [char](10) NOT NULL,
	[Ngay] [date] NOT NULL,
	[Gio] [time](7) NOT NULL,
	[TrieuChung] [nvarchar](100) NULL,
	[TrangThai] [nvarchar](50) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[NCC]    Script Date: 4/29/2024 1:29:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[NCC](
	[ID] [char](10) NOT NULL,
	[TenNCC] [nvarchar](100) NOT NULL,
	[Email] [varchar](100) NOT NULL,
	[SDT] [char](10) NOT NULL,
 CONSTRAINT [PK_NCC] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[NhanVien]    Script Date: 4/29/2024 1:29:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[NhanVien](
	[ID] [char](10) NOT NULL,
	[HoTen] [nvarchar](50) NOT NULL,
	[GioiTinh] [nvarchar](10) NOT NULL,
	[DiaChi] [nvarchar](max) NOT NULL,
	[Email] [varchar](100) NOT NULL,
	[SDT] [char](10) NOT NULL,
	[HinhAnh] [varchar](max) NOT NULL,
 CONSTRAINT [PK_NhanVien] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PhongKhoa]    Script Date: 4/29/2024 1:29:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PhongKhoa](
	[ID] [char](10) NOT NULL,
	[TenPhong] [nvarchar](100) NOT NULL,
	[MoTa] [nvarchar](max) NOT NULL,
	[TrangThai] [bit] NOT NULL,
 CONSTRAINT [PK_PhongKhoa] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[TaiKhoan]    Script Date: 4/29/2024 1:29:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[TaiKhoan](
	[ID] [char](10) NOT NULL,
	[TenDangNhap] [varchar](100) NOT NULL,
	[MatKhau] [varchar](50) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[ThietBi]    Script Date: 4/29/2024 1:29:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[ThietBi](
	[ID] [char](10) NOT NULL,
	[TenThietBi] [nvarchar](100) NOT NULL,
	[Loai] [nvarchar](20) NOT NULL,
	[NCC] [char](10) NOT NULL,
	[NgayMua] [date] NOT NULL,
	[Gia] [money] NOT NULL,
	[SoLuong] [varchar](10) NOT NULL,
 CONSTRAINT [PK_ThietBi] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Thuoc]    Script Date: 4/29/2024 1:29:51 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Thuoc](
	[ID] [char](10) NOT NULL,
	[TenThuoc] [nvarchar](50) NOT NULL,
	[Loai] [nvarchar](50) NOT NULL,
	[NCC] [char](10) NOT NULL,
	[DonGia] [money] NOT NULL,
	[SoLuong] [smallint] NOT NULL,
	[NgayMua] [date] NOT NULL,
	[NgayHetHan] [date] NOT NULL,
 CONSTRAINT [PK_Thuoc] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[BacSi]  WITH CHECK ADD  CONSTRAINT [FK_BacSi_PhongKhoa] FOREIGN KEY([Khoa])
REFERENCES [dbo].[PhongKhoa] ([ID])
GO
ALTER TABLE [dbo].[BacSi] CHECK CONSTRAINT [FK_BacSi_PhongKhoa]
GO
ALTER TABLE [dbo].[DichVu]  WITH CHECK ADD  CONSTRAINT [FK_DichVu_PhongKhoa] FOREIGN KEY([Khoa])
REFERENCES [dbo].[PhongKhoa] ([ID])
GO
ALTER TABLE [dbo].[DichVu] CHECK CONSTRAINT [FK_DichVu_PhongKhoa]
GO
ALTER TABLE [dbo].[HoaDon]  WITH CHECK ADD  CONSTRAINT [FK_HoaDon_BacSi] FOREIGN KEY([BacSi])
REFERENCES [dbo].[BacSi] ([ID])
GO
ALTER TABLE [dbo].[HoaDon] CHECK CONSTRAINT [FK_HoaDon_BacSi]
GO
ALTER TABLE [dbo].[HoaDon]  WITH CHECK ADD  CONSTRAINT [FK_HoaDon_BenhNhan] FOREIGN KEY([BenhNhan])
REFERENCES [dbo].[BenhNhan] ([ID])
GO
ALTER TABLE [dbo].[HoaDon] CHECK CONSTRAINT [FK_HoaDon_BenhNhan]
GO
ALTER TABLE [dbo].[LichKham]  WITH CHECK ADD  CONSTRAINT [FK_LichKham_BacSi] FOREIGN KEY([BacSi])
REFERENCES [dbo].[BacSi] ([ID])
GO
ALTER TABLE [dbo].[LichKham] CHECK CONSTRAINT [FK_LichKham_BacSi]
GO
ALTER TABLE [dbo].[LichKham]  WITH CHECK ADD  CONSTRAINT [FK_LichKham_BenhNhan] FOREIGN KEY([BenhNhan])
REFERENCES [dbo].[BenhNhan] ([ID])
GO
ALTER TABLE [dbo].[LichKham] CHECK CONSTRAINT [FK_LichKham_BenhNhan]
GO
ALTER TABLE [dbo].[LichKham]  WITH CHECK ADD  CONSTRAINT [FK_LichKham_DichVu] FOREIGN KEY([DichVu])
REFERENCES [dbo].[DichVu] ([ID])
GO
ALTER TABLE [dbo].[LichKham] CHECK CONSTRAINT [FK_LichKham_DichVu]
GO
ALTER TABLE [dbo].[ThietBi]  WITH CHECK ADD  CONSTRAINT [FK_ThietBi_NCC] FOREIGN KEY([NCC])
REFERENCES [dbo].[NCC] ([ID])
GO
ALTER TABLE [dbo].[ThietBi] CHECK CONSTRAINT [FK_ThietBi_NCC]
GO
ALTER TABLE [dbo].[Thuoc]  WITH CHECK ADD  CONSTRAINT [FK_Thuoc_NCC] FOREIGN KEY([NCC])
REFERENCES [dbo].[NCC] ([ID])
GO
ALTER TABLE [dbo].[Thuoc] CHECK CONSTRAINT [FK_Thuoc_NCC]
GO
USE [master]
GO
ALTER DATABASE [clinic] SET  READ_WRITE 
GO
