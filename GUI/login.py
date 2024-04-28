from flet import Container, Column, Row, TextField, ElevatedButton, WindowDragArea, IconButton, Icon, SnackBar, Text, CrossAxisAlignment, padding, colors, icons, alignment, Divider, TextButton, ListTile
from BUS import accounts
from DTO import Account

class Login(Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.page.window_width = 450
        self.page.window_height = 500
        self.page.window_title_bar_hidden=True
        self.page.window_title_bar_buttons_hidden=True
        self.expand = True
        self.bgcolor='#e6faf2'
        self.username=self.username()
        self.password=self.password()
        self.btn=self.btnLogin()
        self.account_list = [row for row in accounts.get_accounts()]
        self.page.window_center()
        
        self.content=Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                WindowDragArea(
                    Container(
                        alignment=alignment.center_right,
                        padding=padding.symmetric(horizontal=8, vertical=5),
                        content=Row(
                            tight=True,
                            controls=[
                                IconButton(icon=icons.REMOVE_ROUNDED, on_click=lambda _: print(self.page.route)),
                                IconButton(icon=icons.CLOSE_ROUNDED, on_click=lambda _: self.page.window_close()),
                            ]
                        )
                    )
                ),
                Container(
                    content=Column(
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            Container(
                                alignment=alignment.center,
                                content=Icon(name=icons.MEDICAL_SERVICES_ROUNDED, size=48.0)
                            ),
                            Text('Medical', size=48.0, weight='bold'),
                        ]
                    )
                ),
                Divider(height=5, color=colors.TRANSPARENT),
                self.username,
                self.password,
                self.register(),
                Divider(height=10, color=colors.TRANSPARENT),
                self.btn
            ]
        )
        self.page.update()
        
    def username(self):
        return TextField(
            width=300,
            label='Tên đăng nhập',
            border_radius=8,
            content_padding=10,
            on_change=lambda _: self.validate()
        )
        
    def password(self):
        return TextField(
            label='Mật khẩu',
            width=300,
            border_radius=8,
            content_padding=10,
            password=True,
            can_reveal_password=True,
            on_change=lambda _: self.validate()
        )
    
    def register(self):
        return TextButton(
            text='Chưa có tài khoản? Đăng ký ngay!',
            on_click=lambda _: self.registry()
        )
        
    def btnLogin(self):
        return ElevatedButton(
            bgcolor='#16ffa0',
            width=300,
            height=50,
            text='Đăng nhập',
            disabled=True,
            on_click=lambda _: self.submit()
        )
    
    def validate(self):
        
        if all([self.username.value, self.password.value]) == True:
            self.btn.disabled=False
        else:
            self.btn.disabled=True
        self.page.update()
    
    def registry(self):
        self.page.controls[0] = Register(self.page)
        self.page.update()
    
    def submit(self): 
        
        
        container = Container(
            expand=True,
            bgcolor=colors.GREEN_300,
            content=Row(
                vertical_alignment=CrossAxisAlignment.START,
                spacing=0,
                controls=[
                    self.page.side_bar,
                    self.page.router.route['/dashboard']
                ]
            )
        )
        
        for account in self.account_list:
            if account.username == self.username.value and account.password == self.password.value:
                if account.role.startswith('US'):
                    self.page.clean()
                    self.page.window_title_bar_hidden=False
                    self.page.window_title_bar_buttons_hidden=False
                    self.page.window_width = 1200
                    self.page.window_height = 800
                    self.page.add(self.page.router.route['/entry'])
                    self.page.update()
                    return                
                self.page.clean()
                self.page.window_title_bar_hidden=False
                self.page.window_title_bar_buttons_hidden=False
                self.page.window_width = 1200
                self.page.window_height = 800
                self.page.add(container)
                self.page.content = self.page.controls[0].content.controls
                self.page.window_center()
                self.page.update()
                return
            
        self.page.show_snack_bar(SnackBar(Text('Tài khoản hoặc mật khẩu không đúng!'), bgcolor=colors.RED_300, duration=1000))
        self.page.update()
        
        
    
    def build(self):
        return self
    
    
class Register(Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.expand = True
        self.bgcolor='#e6faf2'
        self.username=TextField(
            width=300,
            label='Tên đăng nhập',
            border_radius=8,
            content_padding=10,
        )
        self.password=TextField(
            label='Mật khẩu',
            width=300,
            border_radius=8,
            content_padding=10,
            password=True,
            can_reveal_password=True,
        )
        self.confirm_password=TextField(
            label='Nhập lại mật khẩu',
            width=300,
            border_radius=8,
            content_padding=10,
            password=True,
            can_reveal_password=True,
        )
        
        self.content=Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                ListTile(title=Text('Đăng ký tài khoản', size=24.0, weight='bold')),
                self.username,
                self.password,
                self.confirm_password,
                Divider(height=10, color=colors.TRANSPARENT),
                ElevatedButton(
                    bgcolor='#16ffa0',
                    width=300,
                    height=50,
                    text='Đăng ký',
                    on_click=lambda _: self.submit()
                )
            ]
        )
        
    def submit(self):
        if self.password.value != self.confirm_password.value:
            self.page.show_snack_bar(SnackBar(Text('Mật khẩu không khớp!'), bgcolor=colors.RED_300, duration=1000))
            self.page.update()
            return
        if self.username.value == '' or self.password.value == '':
            self.page.show_snack_bar(SnackBar(Text('Vui lòng nhập đầy đủ thông tin!'), bgcolor=colors.RED_300, duration=1000))
            self.page.update()
            return
        for account in accounts.get_accounts():
            if self.username.value == account.username:
                self.page.show_snack_bar(SnackBar(Text('Tài khoản đã tồn tại!'), bgcolor=colors.RED_300, duration=1000))
                self.page.update()
                return
        self.page.show_snack_bar(SnackBar(Text('Đăng ký thành công!'), bgcolor=colors.GREEN_300, duration=1000))
        accounts.add_account(Account(self.username.value, self.password.value, f'US{int(accounts.get_accounts()[-1].role[2:])+1}'))
        self.page.controls[0] = Login(self.page)
        self.page.update()
        
    def build(self):
        return self