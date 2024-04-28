from flet import Container, Text, Column, ListTile, TextField, Dropdown, alignment, CrossAxisAlignment, Row, ResponsiveRow, colors, SnackBar, Divider, dropdown, ElevatedButton
from BUS import patients, doctors, appointments, services, medicines, employees, departments, equipments, bills, providers
from DTO import Patient, Doctor, Appointment, Service, Medicine, Employee, Department, Equipment, Bill


class PageForm(Container):
    def __init__(self, page, data, form_data=None):
        super().__init__()
        self.page = page
        self.expand = True
        self.title_list = {
            "BacSi" : f"{'Cập nhật' if form_data else 'Thêm'} bác sĩ",
            "BenhNhan" : f"{'Cập nhật' if form_data else 'Thêm'} bệnh nhân",
            "LichKham" : f"{'Cập nhật' if form_data else 'Thêm'} lịch khám",
            "DichVu" : f"{'Cập nhật' if form_data else 'Thêm'} dịch vụ",
            "Thuoc" : f"{'Cập nhật' if form_data else 'Thêm'} thuốc",
            "PhongKhoa" : f"{'Cập nhật' if form_data else 'Thêm'} phòng khám",
            "NhanVien" : f"{'Cập nhật' if form_data else 'Thêm'} nhân viên",
            "HoaDon" : f"{'Cập nhật' if form_data else 'Thêm'} hóa đơn",
            "ThietBi" : f"{'Cập nhật' if form_data else 'Thêm'} thiết bị",
            "BaoCao" : "Báo cáo"
        }
        self.title=Container(
            padding=20,
            content=Text(self.title_list[data], size=42.0, weight='bold')
        )
        self.form = FormDetail(page, data, form_data)
        self.content=Column(
            scroll=True,
            controls=[
                self.title,
                self.form
            ]
        )
    
    def build(self):
        return self

class FormDetail(Container):
    def __init__(self, page, data, form_data=None):
        super().__init__()
        self.page = page
        self.padding = 20
        self.nav_data={
            'BenhNhan': self.PatientForm,
            'BacSi': self.DoctorForm,
            'LichKham': self.AppointmentForm,
            'DichVu': self.ServiceForm,
            'Thuoc': self.MedicineForm,
            'NhanVien': self.EmployeeForm,
            'PhongKhoa': self.DepartmentForm,
            'ThietBi': self.EquipmentForm,
            'HoaDon': self.BillForm
        }
        self.appointment_list=appointments.get_appointments()
        self.doctor_list=doctors.get_doctors()
        self.patient_list=patients.get_patients()
        self.service_list=services.get_services()
        self.department_list=departments.get_departments()
        self.form_data=form_data
        
        self.sub_btn = ElevatedButton(
            text='Cập nhật' if self.form_data else 'Thêm', bgcolor=colors.GREEN_300, width=120, height=40, disabled=True,
            on_click=(lambda _:self.submit_update(self.form.data)) if self.form_data else (lambda _: self.submit_add(self.form.data)))
        self.cancel_btn = ElevatedButton(text='Hủy', bgcolor=colors.RED_300, width=120, height=40, on_click=lambda _: self.return_page())
        
        self.form=self.nav_data[data]()
        self.content = Container(
            padding=10,
            border_radius=10,
            bgcolor=colors.GREEN_100,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    self.form,
                    Container(
                        alignment=alignment.center_right,
                        content=Row(
                            tight=True,
                            spacing=20,
                            controls=[
                                self.sub_btn,
                                self.cancel_btn
                            ]
                        )
                    )
                ]
            )
        )
    
    
    def return_page(self):
        self.page.content[1] = self.page.router.route[f'/page_list/{self.form.data}']
        self.page.update()
    
    def get_form_data(self, data):
        obj = {}
        
        match data:
            case 'BacSi' | 'DichVu':
                department_list = {x.name: x for x in self.department_list}
                for control in self.form.controls[1].content.controls:
                    if control.data == 'department':
                        obj[control.data] = department_list[control.value]
                    else:
                        obj[control.data] = control.value
                                    
            case 'Thuoc' | 'ThietBi':
                provider_list = {x.name: x for x in employees.get_employees()}
                for control in self.form.controls[1].content.controls:
                    if control.data == 'provider':
                        obj[control.data] = provider_list[control.value]
                    else:
                        obj[control.data] = control.value            
            
            case 'LichKham':
                service_list = {x.name: x for x in self.service_list}
                doctor_list = {x.name: x for x in self.doctor_list}
                for control in self.form.controls[0].controls[1].content.controls:
                    obj[control.data] = control.value
                patient=Patient(id=f'BN{int(self.patient_list[-1].id[2:])+1}',**obj)
                patients.add_patient(patient)
                obj = {}
                obj['patient'] = patient
                for control in self.form.controls[3].content.controls:
                    if control.data == 'service':
                        obj[control.data] = service_list[control.value]
                    elif control.data == 'doctor':
                        obj[control.data] = doctor_list[control.value]
                    else:
                        obj[control.data] = control.value
            
            case 'HoaDon':
                patient_list = {x.name: x for x in self.patient_list}
                doctor_list = {x.name: x for x in self.doctor_list}
                for control in self.form.controls[1].content.controls:
                    if control.data == 'patient':
                        obj[control.data] = patient_list[control.value]
                    elif control.data == 'doctor':
                        obj[control.data] = doctor_list[control.value]
                    else:
                        obj[control.data] = control.value
            
            case _:
                for control in self.form.controls[1].content.controls:
                    obj[control.data] = control.value

        return obj
        
    def submit_add(self, data):
        match data:
            case 'BenhNhan':
                patient = Patient(id=f'BN{int(self.patient_list[-1].id[2:])+1}',**self.get_form_data(data))
                patients.add_patient(patient)
            case 'BacSi':
                doctor = Doctor(id=f'BS{int(self.doctor_list[-1].id[2:])+1}',**self.get_form_data(data))
                doctors.add_doctor(doctor)
                
            case 'LichKham':
                appointment = Appointment(id=f'LK{int(self.appointment_list[-1].id[2:])+1}',**self.get_form_data(data))
                appointments.add_appointment(appointment)
            case 'DichVu':
                service = Service(id=f'DV{int(self.service_list[-1].id[2:])+1}',**self.get_form_data(data))
                services.add_service(service)
            case 'Thuoc':
                medicine = Medicine(id=f'T{int(medicines.get_medicines()[-1].id[1:])+1}',**self.get_form_data(data))
                medicines.add_medicine(medicine)
            case 'NhanVien':
                employee = Employee(id=f'NV{int(employees.get_employees()[-1].id[2:])+1}',**self.get_form_data(data))
                employees.add_employee(employee)
            case 'PhongKhoa':
                department = Department(id=f'PK{int(self.department_list[-1].id[2:])+1}',**self.get_form_data(data))
                departments.add_department(department)
            case 'ThietBi':
                equipment = Equipment(id=f'TB{int(equipments.get_equipments()[-1].id[2:])+1}',**self.get_form_data(data))
                equipments.add_equipment(equipment)
            case 'HoaDon':
                bill = Bill(id=f'HD{int(bills.get_bills()[-1].id[2:])+1}',**self.get_form_data(data))
                bills.add_bill(bill)
        self.page.show_snack_bar(SnackBar(Text('Thêm thành công'), bgcolor=colors.GREEN_300, duration=1000))
        self.return_page()
                
    def submit_update(self, data):
        match data:
            case 'BenhNhan':
                patient = Patient(id=self.form_data.id,**self.get_form_data(data))
                patients.update_patient(patient)
            case 'BacSi':
                doctor = Doctor(id=self.form_data.id,**self.get_form_data(data))
                doctors.update_doctor(doctor)
            case 'LichKham':
                appointment = Appointment(id=self.form_data.id,**self.get_form_data(data))
                appointments.update_appointment(appointment)
            case 'DichVu':
                service = Service(id=self.form_data.id,**self.get_form_data(data))
                services.update_service(service)
            case 'Thuoc':
                medicine = Medicine(id=self.form_data.id,**self.get_form_data(data))
                medicines.update_medicine(medicine)
            case 'NhanVien':
                employee = Employee(id=self.form_data.id,**self.get_form_data(data))
                employees.update_employee(employee)
            case 'PhongKhoa':
                department = Department(id=self.form_data.id,**self.get_form_data())
                departments.update_department(department)
            case 'ThietBi':
                equipment = Equipment(id=self.form_data.id,**self.get_form_data())
                equipments.update_equipment(equipment)
            case 'HoaDon':
                bill = Bill(id=self.form_data.id,**self.get_form_data())
                bills.update_bill(bill)
                
        self.page.show_snack_bar(SnackBar(Text('Cập nhật thành công'), bgcolor=colors.GREEN_300, duration=1000))
        self.return_page()
    
    def sub_btn_validate(self, form):
        required_fields = []
        match form.data:
            case 'BenhNhan':
                required_fields = ['name', 'gender', 'birth', 'address', 'phone']
            case 'BacSi':
                required_fields = ['name', 'gender', 'department', 'phone', 'degrees', 'email']
            case 'LichKham':
                required_fields = ['patient', 'doctor', 'service', 'date', 'time', 'status']
            case 'DichVu':
                required_fields = ['name', 'department', 'charge', 'description']
            case 'Thuoc':
                required_fields = ['name', 'type', 'provider', 'unit_price', 'quantity', 'buy_date', 'expire_date']
            case 'NhanVien':
                required_fields = ['name', 'gender', 'address', 'email', 'phone']
            case 'PhongKhoa':
                required_fields = ['name', 'description', 'status']
            case 'ThietBi':
                required_fields = ['name', 'type', 'provider', 'buy_date', 'price', 'quantity']
            case 'HoaDon':
                required_fields = ['patient', 'doctor', 'date', 'discount', 'total', 'real_total']
        
        require_controls = filter(lambda x: x.data in required_fields, form.controls)

        
        if all([control.value for control in require_controls]) == True:
            if form.data == 'HoaDon':
                patient, doctor = form.controls[0:2]
                if (patient, doctor) in [(appointment.patient.name, appointment.doctor.name) for appointment in self.appointment_list]:
                    self.sub_btn.disabled=False
                else:
                    self.sub_btn.disabled=True
            else:
                self.sub_btn.disabled=False
        else:
            self.sub_btn.disabled=True
        self.update()

    
    def input_field(self, control, data_type, label, col, parent, list=None):
        
            match control():
                case Dropdown():
                    return control(data=data_type, label=label, border_radius=10, content_padding=10, col=col, options=list, on_change=lambda _:self.sub_btn_validate(parent), value=(
                        getattr(self.form_data, data_type).name if (self.form_data and hasattr(getattr(self.form_data, data_type), 'name')) else getattr(self.form_data, data_type)   
                    ) if self.form_data else None)
                case _:
                    return control(data=data_type, label=label, border_radius=10, content_padding=10, col=col, on_change=lambda _:self.sub_btn_validate(parent), value=(
                            getattr(self.form_data, data_type).name if (self.form_data and hasattr(getattr(self.form_data, data_type), 'name')) else getattr(self.form_data, data_type)   
                        ) if self.form_data else None)
    
    def PatientForm(self):
        
        parent = ResponsiveRow(
            data='BenhNhan',
            spacing=60,
            run_spacing=50
        )
        
        input_fields = [
            self.input_field(TextField, 'name', 'Họ và tên', 6, parent),
            self.input_field(TextField, 'phone', 'Số điện thoại', 6, parent),
            self.input_field(TextField, 'birth', 'Ngày sinh', 6, parent),
            self.input_field(Dropdown, 'gender', 'Giới tính', 6, parent, [dropdown.Option('Nam'), dropdown.Option('Nữ')]),
            self.input_field(TextField, 'address', 'Địa chỉ', 12, parent),
            self.input_field(TextField, 'medical_history', 'Tiền sử bệnh án', 12, parent)
        ]
        
        parent.controls = input_fields
        
        return Column(
            data=parent.data,
            controls=[
                ListTile(title=Text('Thông tin bệnh nhân', size=24.0, weight='bold')),
                Container(
                    padding=30,
                    alignment=alignment.center,
                    content=parent
                )
            ]
        )
        
    def DoctorForm(self):
        
        parent = ResponsiveRow(
            data='BacSi',
            spacing=60,
            run_spacing=50
        )
        
        input_fields = [
            self.input_field(TextField, 'name', 'Họ và tên', 6, parent),
            self.input_field(Dropdown, 'gender', 'Giới tính', 6, parent, [dropdown.Option('Nam'), dropdown.Option('Nữ')]),
            self.input_field(Dropdown, 'department', 'Khoa', 6, parent, [dropdown.Option(department.name) for department in self.department_list]),
            self.input_field(TextField, 'phone', 'Số điện thoại', 6, parent),
            self.input_field(TextField, 'degrees', 'Bằng cấp', 6, parent),
            self.input_field(TextField, 'email', 'Email', 6, parent),
            self.input_field(TextField, 'image', 'Ghi tạm path hình vào đây đê', 12, parent),
        ]
        
        parent.controls = input_fields
        
        return Column(
            data=parent.data,
            controls=[
                ListTile(title=Text('Thông tin bác sĩ', size=24.0, weight='bold')),
                Container(
                    padding=30,
                    alignment=alignment.center,
                    content=parent
                )
            ]
        )
        
    def AppointmentForm(self):
        
        parent = ResponsiveRow(
            data='LichKham',
            spacing=60,
            run_spacing=50,
        )
        
        input_fields = [
            self.input_field(Dropdown, 'service', 'Dịch vụ', 6, parent, [dropdown.Option(service.name) for service in self.service_list]),
            self.input_field(Dropdown, 'doctor', 'Bác sĩ', 6, parent, [dropdown.Option(doctor.name) for doctor in self.doctor_list]),
            self.input_field(TextField, 'date', 'Ngày khám', 6, parent),
            self.input_field(TextField, 'time', 'Giờ khám', 6, parent),
            self.input_field(TextField, 'condition', 'Triệu chứng', 12, parent),
            self.input_field(TextField, 'status', 'Trạng thái', 12, parent)
        ]
        
        parent.controls = input_fields
        
        return Column(
            data=parent.data,
            controls=[                
                self.PatientForm(),
                Divider(height=10, color=colors.TRANSPARENT),
                ListTile(title=Text('Thông tin lịch khám', size=24.0, weight='bold')),
                Container(
                    padding=30,
                    alignment=alignment.center,
                    content=parent
                )
            ]
        )

    def ServiceForm(self):
        
        parent = ResponsiveRow(
            data='DichVu',
            spacing=60,
            run_spacing=50
        )
        
        input_fields = [
            self.input_field(TextField, 'name', 'Tên dịch vụ', 6, parent),
            self.input_field(Dropdown, 'department', 'Khoa', 6, parent, [dropdown.Option(department.name) for department in self.department_list]),
            self.input_field(TextField, 'price', 'Giá', 12, parent),
            self.input_field(TextField, 'description', 'Mô tả', 12, parent),
        ]
        
        parent.controls = input_fields
        
        return Column(
            data=parent.data,
            controls=[
                ListTile(title=Text('Thông tin dịch vụ', size=24.0, weight='bold')),
                Container(
                    padding=30,
                    alignment=alignment.center,
                    content=parent
                )
            ]
        )
    
    def MedicineForm(self):
        
        parent = ResponsiveRow(
            data='Thuoc',
            spacing=60,
            run_spacing=50
        )
        
        input_fields = [
            self.input_field(TextField, 'name', 'Tên thuốc', 6, parent),
            self.input_field(TextField, 'type', 'Loại', 6, parent),
            self.input_field(Dropdown, 'provider', 'Nhà cung cấp', 6, parent, [dropdown.Option(provider.name) for provider in providers.get_providers()]),
            self.input_field(TextField, 'unit_price', 'Giá', 6, parent),
            self.input_field(TextField, 'quantity', 'Số lượng', 6, parent),
            self.input_field(TextField, 'buy_date', 'Ngày mua', 6, parent),
            self.input_field(TextField, 'expire_date', 'Ngày hết hạn', 6, parent),
        ]
        
        parent.controls = input_fields
        
        return Column(
            data=parent.data,
            controls=[
                ListTile(title=Text('Thông tin thuốc', size=24.0, weight='bold')),
                Container(
                    padding=30,
                    alignment=alignment.center,
                    content=parent
                )
            ]
        )
        
    def EmployeeForm(self):
        
        parent = ResponsiveRow(
            data='NhanVien',
            spacing=60,
            run_spacing=50
        )
        
        input_fields = [
            self.input_field(TextField, 'name', 'Họ và tên', 6, parent),
            self.input_field(Dropdown, 'gender', 'Giới tính', 6, parent, [dropdown.Option('Nam'), dropdown.Option('Nữ')]),
            self.input_field(TextField, 'address', 'Địa chỉ', 12, parent),
            self.input_field(TextField, 'email', 'Email', 6, parent),
            self.input_field(TextField, 'phone', 'Số điện thoại', 6, parent),
            self.input_field(TextField, 'image', 'Hỉnh ảnh', 6, parent),
        ]
        
        parent.controls = input_fields
        
        return Column(
            data=parent.data,
            controls=[
                ListTile(title=Text('Thông tin nhân viên', size=24.0, weight='bold')),
                Container(
                    padding=30,
                    alignment=alignment.center,
                    content=parent
                )
            ]
        )    
    
    def DepartmentForm(self):
        
        parent = ResponsiveRow(
            data='PhongKhoa',
            spacing=60,
            run_spacing=50
        )
        
        input_fields = [
            self.input_field(TextField, 'name', 'Tên phòng', 6, parent),
            self.input_field(Dropdown, 'status', 'Trạng thái', 6, parent, [
                    dropdown.Option('Hoạt động'),
                    dropdown.Option('Không hoạt động'),
            ]),
            self.input_field(TextField, 'description', 'Mô tả', 12, parent),
        ]
        
        parent.controls = input_fields
        
        return Column(
            data=parent.data,
            controls=[
                ListTile(title=Text('Thông tin phòng khoa', size=24.0, weight='bold')),
                Container(
                    padding=30,
                    alignment=alignment.center,
                    content=parent
                )
            ]
        )
        
    def EquipmentForm(self):
        
        parent = ResponsiveRow(
            data='ThietBi',
            spacing=60,
            run_spacing=50
        )
        
        input_fields = [
            self.input_field(TextField, 'name', 'Tên thiết bị', 6, parent),
            self.input_field(TextField, 'type', 'Loại', 6, parent),
            self.input_field(TextField, 'provider', 'Nhà cung cấp', 6, parent),
            self.input_field(TextField, 'buy_date', 'Ngày mua', 6, parent),
            self.input_field(TextField, 'price', 'Giá', 6, parent),
            self.input_field(TextField, 'quantity', 'Số lượng', 6, parent),
        ]
        
        parent.controls = input_fields
        
        return Column(
            data=parent.data,
            controls=[
                ListTile(title=Text('Thông tin thiết bị', size=24.0, weight='bold')),
                Container(
                    padding=30,
                    alignment=alignment.center,
                    content=parent
                )
            ]
        )
        
    def BillForm(self):
        
        parent = ResponsiveRow(
            data='HoaDon',
            spacing=60,
            run_spacing=50
        )
        
        input_fields = [
            self.input_field(TextField, 'patient', 'Bệnh nhân', 6, parent),
            self.input_field(Dropdown, 'doctor', 'Bác sĩ', 6, parent, [dropdown.Option(doctor.name) for doctor in self.doctor_list]),
            self.input_field(TextField, 'date', 'Ngày tạo', 6, parent),
            self.input_field(TextField, 'discount', 'Giảm giá', 6, parent),
            self.input_field(TextField, 'total', 'Tổng tiền', 6, parent),
            self.input_field(TextField, 'real_total', 'Tổng thu', 6, parent)
        ]
        
        parent.controls = input_fields
        
        return Column(
            data=parent.data,
            controls=[
                ListTile(title=Text('Thông tin hóa đơn', size=24.0, weight='bold')),
                Container(
                    padding=30,
                    alignment=alignment.center,
                    content=parent
                )
            ]
        )
        
    
    def build(self):
        return self
    