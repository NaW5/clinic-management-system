from .login import Login, Register
from .dashboard import DashBoard
from .page_form import PageForm
from .page_list import PageList
from .entry import Entry

class Router():
    def __init__(self, page):
        self.page = page
        self.route = {
            '/login': Login(self.page),
            '/register': Register(self.page),
            '/entry': Entry(self.page),
            '/dashboard': DashBoard(self.page),
            '/page_list/BenhNhan': PageList(self.page, 'BenhNhan'),
            '/page_list/BacSi': PageList(self.page, 'BacSi'),
            '/page_list/LichKham': PageList(self.page, 'LichKham'),
            '/page_list/DichVu': PageList(self.page, 'DichVu'),
            '/page_list/Thuoc': PageList(self.page, 'Thuoc'),
            '/page_list/PhongKhoa': PageList(self.page, 'PhongKhoa'),
            '/page_list/NhanVien': PageList(self.page, 'NhanVien'),
            '/page_list/ThietBi': PageList(self.page, 'ThietBi'),
            '/page_list/HoaDon': PageList(self.page, 'HoaDon'),
            '/page_form/BenhNhan': PageForm(self.page, 'BenhNhan'),
            '/page_form/BacSi': PageForm(self.page, 'BacSi'),
            '/page_form/LichKham': PageForm(self.page, 'LichKham'),
            '/page_form/DichVu': PageForm(self.page, 'DichVu'),
            '/page_form/Thuoc': PageForm(self.page, 'Thuoc'),
            '/page_form/PhongKhoa': PageForm(self.page, 'PhongKhoa'),
            '/page_form/NhanVien': PageForm(self.page, 'NhanVien'),
            '/page_form/ThietBi': PageForm(self.page, 'ThietBi'),
            '/page_form/HoaDon': PageForm(self.page, 'HoaDon')
        }