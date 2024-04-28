from flet import *
from .chatbot import ChatBot
from BUS import departments, services, appointments, patients
from DTO import Appointment, Patient

class Entry(Container):
    def __init__(self, page:Page):
        super().__init__()
        self.page = page
        self.department_list = departments.get_departments()
        self.service_list = services.get_services()
        self.appointment_list = appointments.get_appointments()
        self.patient_list = patients.get_patients()
        self.page.on_resize=self.on_resize
        self.chatbot = ChatBot()
        self.content=Stack(
            width=self.page.window_width,
            height=self.page.window_height - 40,
            expand=True,
            controls=[
                Column(
                    controls=[
                        Container(
                            expand=True,
                            image_src='/clinic.png',
                            image_fit=ImageFit.COVER,
                            content=ResponsiveRow(
                                vertical_alignment=CrossAxisAlignment.CENTER,
                                height=600,
                                controls=[
                                    Container(
                                        alignment=alignment.center,
                                        padding=20,
                                        content=Text('Chào mừng bạn đến với phòng khám Medical', size=64.0, weight='bold', color=colors.WHITE),
                                        col=8
                                    ),
                                    self.AppointmentForm()
                                ]
                            )
                        )
                    ]
                ),
                FloatingActionButton(
                    bottom=22,
                    right=22,
                    icon=icons.MESSAGE_ROUNDED,
                    bgcolor=colors.GREEN_300,
                    on_click=self.show_chatbot
                ),
                self.chatbot
            ],
        )
        
    def get_form_data(self, form):
        service_list = {service.name: service for service in self.service_list}
        data = {}
        pattient_attr = {}
        for control in form.controls:
            if control.data:    
                if control.data.startswith('patient'):
                    pattient_attr[control.data.split('.')[1]] = control.value
                elif control.data == 'service':
                    data[control.data] = service_list[control.value]
                else:
                    data[control.data] = control.value
        patient = Patient(id=f'BN{int(self.patient_list[-1].id[2:])+1}',**pattient_attr)
        patients.add_patient(patient)
        data['patient'] = patient
        return data
    
    def send(self,form):
        appointments.add_appointment(Appointment(id=f'LK{int(self.appointment_list[-1].id[2:])+1}', status='Chờ xác nhân',**self.get_form_data(form)))
        
        
    def show_chatbot(self,e):
        self.chatbot.visible = not self.chatbot.visible
        self.page.update()
       
    def on_resize(self,e):
        self.content.width=self.page.window_width
        self.content.height=self.page.window_height - 40
        self.page.update()
     
    def AppointmentForm(self):
        
        self.service_list = services.get_services()
        self.department_list = departments.get_departments()
        def department_change(options):
            service.options = options
            self.update()
        
        parent = ResponsiveRow(
            controls=[
                Text('Đăng ký khám', size=32.0, weight='bold', col=12),
                Text('vui lòng điền thông tin vào form bên dưới để đăng ký khám bệnh theo yêu cầu', col=12),
            ]
        )
        
        
        service = Dropdown(
            data='service',
            dense=True,
            hint_text='Dịch vụ',
            options=[dropdown.Option(service.name) for service in self.service_list],
            col=6
        )
        
        department = Dropdown(
            dense=True,
            hint_text='Khoa khám',
            options=[dropdown.Option(department.name) for department in self.department_list],
            on_change=lambda _: department_change([dropdown.Option(service.name) for service in self.service_list if service.department.name == department.value]),
            col=6
        )
        
        input_fields = [
            TextField(
                data='patient.name',
                dense=True,
                hint_text='Họ và tên',
                col=6
            ),
            TextField(
                data='patient.phone',
                dense=True,
                hint_text='Số điện thoại',
                col=6
            ),
            TextField(
                data='patient.birth',
                dense=True,
                hint_text='Ngày sinh',
                col=6
            ),
            Dropdown(
                data='patient.gender',
                dense=True,
                hint_text='Giới tính',
                options=[dropdown.Option('Nam'), dropdown.Option('Nữ')],
                col=6
            ),
            TextField(
                data='patient.address',
                dense=True,
                hint_text='Địa chỉ',
                col=12
            ),
            department,
            service,
            TextField(
                data='date',
                dense=True,
                hint_text='Ngày khám',
                col=6
            ),
            TextField(
                data='time',
                dense=True,
                hint_text='Giờ khám',
                col=6
            ),
            TextField(
                data='condition',
                dense=True,
                hint_text='Triệu chứng',
                col=12
            ),
        ]
        
        send_btn = ElevatedButton(
            text='Gửi',
            on_click=lambda _: self.send(parent),
        )
        
        parent.controls.extend(input_fields)
        
        return Container(
            padding=20,
            content=Column(
                controls=[
                    parent,
                    send_btn
                ]
            ),
            bgcolor=colors.with_opacity(0.8, colors.GREEN_100),
            blur=10,
            border_radius=10,
            col=4,
        )
    
    
    def ClinicService(self):
        return Column(
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Text('Dịch vụ', size=40.0, weight='bold'),
                
            ]
        )
        
    
    def build(self):
        return self
    