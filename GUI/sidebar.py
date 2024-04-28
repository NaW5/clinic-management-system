from flet import Container, Column, Row, padding, colors, icons, ListTile, Icon, Divider, CircleAvatar, IconButton, alignment, border_radius, Text

class SideBar(Container):
    
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.width = 220
        self.padding = padding.only(top=20)
        self.user_info=self.UserInfo()
        self.main_sidebar=self.MainSideBar()
        self.content = Container(
            bgcolor=colors.GREEN_100,
            border_radius=border_radius.only(top_right=20),
            content=Column(
                scroll=True,
                controls=[
                    self.user_info,
                    Divider(height=5, color=colors.TRANSPARENT),
                    self.main_sidebar
                ]
            )
        )
     
    def sidebar_size_toggle(self,e):
        if self.width == 220:
            self.width = 60
        else:
            self.width = 220
        
        self.user_info.content.controls[1].visible=False if self.width == 60 else True
        for control in self.main_sidebar.content.controls:
            if isinstance(control, Container):
                control.content.title.visible=False if self.width == 60 else True
        self.update()

    def UserInfo(self):
        return Container(
            padding=10,
            content=Row(
                wrap=True,
                expand=True,
                expand_loose=True,
                spacing=20,
                controls=[
                    CircleAvatar(Icon(name=icons.MAN_2_ROUNDED, size=32.0)),
                    Column(
                        spacing=1,
                        alignment=alignment.center,
                        controls=[
                            Text('Anh Nam', size=16.0, weight='bold'),
                            Text('Admin', size=12.0, weight='bold')
                        ]
                    ),
                    IconButton(
                        icon=icons.MENU_ROUNDED,
                        on_click=self.sidebar_size_toggle
                    )
                ]
            )
        )
        
    def panelItemClick(self, e):
        match e.control.data:
            case 'Dashboard':
                self.page.controls[0].content.controls[1] = self.page.router.route['/dashboard']
            case 'BenhNhan':
                self.page.controls[0].content.controls[1] = self.page.router.route['/page_list/BenhNhan']
            case 'BacSi':
                self.page.controls[0].content.controls[1] = self.page.router.route['/page_list/BacSi']
            case 'LichKham':
                self.page.controls[0].content.controls[1] = self.page.router.route['/page_list/LichKham']
            case 'DichVu':
                self.page.controls[0].content.controls[1] = self.page.router.route['/page_list/DichVu']
            case 'Thuoc':
                self.page.controls[0].content.controls[1] = self.page.router.route['/page_list/Thuoc']
            case 'PhongKhoa':
                self.page.controls[0].content.controls[1] = self.page.router.route['/page_list/PhongKhoa']
            case 'NhanVien':
                self.page.controls[0].content.controls[1] = self.page.router.route['/page_list/NhanVien']
            case 'HoaDon':
                self.page.controls[0].content.controls[1] = self.page.router.route['/page_list/HoaDon']
            case 'ThietBi':
                self.page.controls[0].content.controls[1] = self.page.router.route['/page_list/ThietBi']
            case 'DangXuat':
                self.page.clean()
                self.page.appbar = None
                self.page.add(self.page.router.route['/login'])
                self.page.window_width = 450
                self.page.window_height = 500
                self.page.window_title_bar_hidden=True
                self.page.window_title_bar_buttons_hidden=True
                self.page.window_center()
                self.page.update()
        self.page.update()
    
    def MainSideBar(self):        
        
        panelItem = lambda ic, name, data: Container(
            data=data,
            content=ListTile(title=Text(name, size=14.0, weight='bold'), leading=Icon(name=ic, size=24.0)),
            on_click=self.panelItemClick,
            ink=True,
            ink_color=colors.GREEN_300,
            border_radius=10
        )
        
        return Container(
            content=Column(
                    controls=[
                    panelItem(icons.DASHBOARD_ROUNDED, 'Tổng quan', 'Dashboard'),
                    panelItem(icons.PERSON_ROUNDED, 'Bệnh nhân', 'BenhNhan'),
                    panelItem(icons.SCHEDULE_ROUNDED, 'Lịch khám', 'LichKham'),
                    panelItem(icons.PERSON_4_ROUNDED, 'Bác sĩ', 'BacSi'),
                    panelItem(icons.PERSON_2_ROUNDED, 'Nhân viên', 'NhanVien'),
                    panelItem(icons.ROOM_SERVICE_ROUNDED, 'Phòng khoa', 'PhongKhoa'),
                    panelItem(icons.LIST_ROUNDED, 'Dịch vụ', 'DichVu'),
                    panelItem(icons.MEDICAL_INFORMATION_ROUNDED, 'Thuốc', 'Thuoc'),
                    panelItem(icons.PLACE_ROUNDED, 'Thiết bị', 'ThietBi'),
                    panelItem(icons.BOOK_ROUNDED, 'Hóa đơn', 'HoaDon'),
                    Divider(height=5, color='#a0a0a0'),
                    panelItem(icons.LOGOUT_ROUNDED, 'Đăng xuất', 'DangXuat'),
                ]
            )
        )

    def build(self):        
        return self
