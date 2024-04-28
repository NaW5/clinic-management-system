
from GUI import Router, SideBar
from flet import Page, Theme, ThemeMode, app
def main(page: Page):
    page.theme_mode=ThemeMode.LIGHT
    page.theme=Theme(color_scheme_seed='#16a064')
    page.padding=0
    page.side_bar = SideBar(page)
    page.router = Router(page)
    page.add(page.router.route['/login'])

if __name__ == '__main__':
    app(target=main, assets_dir='assets')