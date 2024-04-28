import datetime
from flet import Container, Column, Row, ResponsiveRow, padding, colors, icons, TextStyle, BoxShadow, Text, PieChart, LineChart, PieChartEvent, PieChartSection, LineChartData, LineChartDataPoint, ListTile, Icon, Card, ChartAxis, ChartAxisLabel, Border, BorderSide
from BUS import accounts, patients, doctors, employees, departments, services, medicines, equipments, bills, appointments
class DashBoard(Container):
    
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.expand = True
        self.general_info = GeneralInfo(self.page)
        self.clinic_report = ClinicReport(self.page)
        self.content = Column(
            scroll=True,
            spacing=0,
            controls=[
                self.general_info,
                self.clinic_report,
            ]
        )
        
    def build(self):
        return self

class State:
    toggle = True

class ClinicReport(Container):
    
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.padding = padding.only(top=0, right=20, bottom=20, left=20)
        self.state = State()
        self.pie_chart = self.PieChart()
        self.line_chart = self.LineChart()
        self.content = Row(
            spacing=20,
            controls=[
                self.pie_chart,
                self.line_chart   
            ]
        )
        
        
    def PieChart(self):
        
        appointment_list = appointments.get_appointments()
        completed_appointments = [appointment for appointment in appointment_list if appointment.status == 'Hoàn thành']
        department_count = {}

        for appointment in completed_appointments:
            department = departments.get_department(appointment.service.department).name
            department_count[department] = department_count.get(department, 0) + 1
    
        
        normal_radius = 60
        hover_radius = 70
        normal_txt_style = TextStyle(size=16.0, weight='bold')
        hover_txt_style = TextStyle(size=22.0, weight='bold', shadow=BoxShadow(blur_radius=5, color=colors.BLACK12))
        
        section = lambda value, color: PieChartSection(
            value=value,
            title=value,
            title_style=normal_txt_style,
            color=color,
            radius=normal_radius,
        )
        
        def on_piechart_event(e: PieChartEvent):
            for i, sect in enumerate(pie_chart.sections):
                if i == e.section_index:
                    sect.radius = hover_radius
                    sect.title_style = hover_txt_style
                else:
                    sect.radius = normal_radius
                    sect.title_style = normal_txt_style
            pie_chart.update()
        
        color = ['RED_300', 'BLUE_300', 'GREEN_300', 'YELLOW_300', 'PURPLE_300', 'CYAN_300', 'ORANGE_300', 'PINK_300', 'INDIGO_300', 'TEAL_300', 'LIME_300', 'BROWN_300', 'AMBER_300', 'DEEP_ORANGE_300', 'DEEP_PURPLE_300', 'LIGHT_BLUE_300', 'LIGHT_GREEN_300', 'BLUE_GREY_300', 'GREY_300']
        
        department_color = tuple(zip(department_count, color[:len(department_count)]))
        
        pie_chart = PieChart(
            height=300,
            sections=[
                section(department_count[key], getattr(colors, color)) for key, color in department_color
            ],
            on_chart_event=on_piechart_event,
            center_space_radius=50,
            sections_space=0
        )
        
        indicator = lambda name, color: ListTile(
            leading=Icon(name=icons.CIRCLE, color=getattr(colors, color)),
            title=Text(name, weight='bold', size=12.0),
            content_padding=0,
            dense=True,
            col=6
        )
        
        return Container(
            padding=10,
            bgcolor=colors.GREEN_100,
            border_radius=10,
            expand=1,
            content=Column(
                controls=[
                    Text('Bệnh nhân theo khoa', size=24.0, weight='bold'),
                    pie_chart,
                    ResponsiveRow(
                        controls=[
                            indicator(key, color) for key, color in department_color
                        ],
                    )
                ]                
            )
        )
        
    def LineChart(self):
        
        bill_list = bills.get_bills()
        
        max_income = max([bill.real_total for bill in bill_list])
        
        month = datetime.datetime.now().month - 1
        
        data_1 = [
            LineChartData(
                data_points=[
                    LineChartDataPoint(x=int(bill.date.day), y=bill.real_total) for bill in bill_list if bill.date.month == month
                ],
                stroke_width=4,
                color=colors.with_opacity(0.8, colors.PINK_500),
                stroke_cap_round=True,
                below_line_bgcolor=colors.with_opacity(0.5, colors.PINK_500),
            ),
        ]

        chart = LineChart(
            height=485,
            data_series=data_1,
            border=Border(
                bottom=BorderSide(4, colors.with_opacity(0.5, colors.ON_SURFACE))
            ),
            left_axis=ChartAxis(
                labels=[
                    ChartAxisLabel(value=i, label=Text(f'{i:,}', weight='bold') if i % 2 == 0 else None) for i in range(0, int(max_income) + 100000, 200000)
                ],
                labels_size=80,
            ),
            bottom_axis=ChartAxis(
                labels=[
                    ChartAxisLabel(value=i, label=Text(f'{i}', weight='bold') if not i & 1 else None) for i in range(1, 32)
                ],
                labels_size=52,
            ),
            # tooltip_bgcolor=colors.with_opacity(0.8, colors.BLUE_500),
            min_y=0,
            max_y=max_income + 100000,
            min_x=1,
            max_x=31 if month in [1, 3, 5, 7, 8, 10, 12] else 30 if month in [4, 6, 9, 11] else 28 if month == 2 else 31,
            animate=5000,
        )
        
        return Container(
            bgcolor=colors.GREEN_100,
            border_radius=10,
            padding=10,
            expand=2,
            content=Column(
                controls=[
                    Text('Doanh thu theo tháng', size=24.0, weight='bold'),
                    chart
                ]
            )
        )
        
    def build(self):
        return self
    
    
    
class GeneralInfo(Container):

    def __init__(self, page):
        super().__init__()
        self.page = page
        self.padding = 20
        self.content = ResponsiveRow(
            spacing=20,
            run_spacing=20,
            controls=[
                self.CardInfo('Bệnh nhân', len(patients.get_patients()), icons.PERSON_ROUNDED, 'BenhNhan'),
                self.CardInfo('Bác sĩ', len(doctors.get_doctors()), icons.PERSON_ROUNDED, 'BacSi'),
                self.CardInfo('Nhân viên', len(employees.get_employees()), icons.PERSON_ROUNDED, 'NhanVien'),
                self.CardInfo('Khoa', len(departments.get_departments()), icons.PERSON_ROUNDED, 'PhongKhoa'),
                self.CardInfo('Dịch vụ', len(services.get_services()), icons.PERSON_ROUNDED, 'DichVu'),
                self.CardInfo('Thuốc', len(medicines.get_medicines()), icons.PERSON_ROUNDED, 'Thuoc'),
                self.CardInfo('Thiết bị', len(equipments.get_equipments()), icons.PERSON_ROUNDED, 'ThietBi'),
                self.CardInfo('Hóa đơn', len(bills.get_bills()), icons.PERSON_ROUNDED, 'HoaDon'),
            ]
        )
        
    def page_change(self, data):
        self.page.content[1] = self.page.router.route[f'/page_list/{data}']
        self.page.update()
        
    def CardInfo(self, title, value, icon, data):
        return Container(
            on_click=lambda _: self.page_change(data),
            content=Card(
                margin=0,
                color=colors.GREEN_100,
                content=Container(
                    padding=10,
                    content=Column(
                        controls=[
                            Icon(name=icon, size=42.0),
                            Text(title, size=24.0, weight='bold'),
                            Text(value, size=16.0, weight='bold'),
                        ]
                    ),
                ),
            ),
            col={ 'xs': 12, 'sm': 6, 'md': 4, 'lg': 3 }
        )
   

    def build(self):
        return self