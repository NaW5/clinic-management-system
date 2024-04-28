
from flet import Container, Text, Column, Row, DataTable, DataColumn, DataCell, DataRow, CircleAvatar, IconButton, TextField, TextAlign, MainAxisAlignment, AlertDialog, TextButton, icons, colors, TextStyle, NumbersOnlyInputFilter
from math import ceil
from BUS import patients, doctors, appointments, services, medicines, departments, employees, equipments, bills
from .page_form import PageForm

class PageList(Container):
    def __init__(self, page, data):
        super().__init__()
        self.page = page
        self.expand = True
        self.table = Table(self.page, data)
        self.title_list = {
            "BacSi" : "Danh sách bác sĩ",
            "BenhNhan" : "Danh sách bệnh nhân",
            "LichKham" : "Danh sách lịch khám",
            "DichVu" : "Danh sách dịch vụ",
            "Thuoc" : "Danh sách thuốc",
            "PhongKhoa" : "Danh sách phòng khám",
            "NhanVien" : "Danh sách nhân viên",
            "HoaDon" : "Danh sách hóa đơn",
            "ThietBi" : "Danh sách thiết bị",
        }
        self.title=Container(
            padding=20,
            content=Text(f'{self.title_list[data]}', size=42.0, weight='bold')
        )
        self.content = Column(
            scroll=True,
            spacing=0,
            controls=[
                self.title,
                self.table
            ]
        )
        
    def build(self):
        return self
    
class Table(Container):
    def __init__(self, page, data):
        super().__init__()
        self.page = page
        self.padding = 20
        self.nav_data = {
            'BenhNhan': self.PatientTable,
            'BacSi': self.DoctorTable,
            'LichKham': self.AppointmentTable,
            'DichVu': self.ServiceTable,
            'Thuoc': self.MedicineTable,
            'PhongKhoa': self.DepartmentTable,
            'NhanVien': self.EmployeeTable,
            'ThietBi': self.EquipmentTable,
            'HoaDon': self.BillTable,
        }
        self.table = self.nav_data[data]()
        self.scroll_table = Row(scroll=True, tight=True, controls=[self.table])
        self.navigation = self.tableNavigation()
        self.search = self.searchTable()
        self.content = Container(
            padding=10,
            bgcolor=colors.GREEN_100,
            border_radius=10,
            content=Column(
                controls=[
                    self.search,
                    self.scroll_table,
                    self.navigation
                ]
            )
        )
    
    def load(self):
        self.table = self.nav_data[self.table.data]()
        self.scroll_table = Row(scroll=True, tight=True, controls=[self.table])
        self.navigation = self.tableNavigation()
        self.search = self.searchTable()
        self.content = Container(
            padding=10,
            bgcolor=colors.GREEN_100,
            border_radius=10,
            content=Column(
                controls=[
                    self.search,
                    self.scroll_table,
                    self.navigation
                ]
            )
        )
        self.page.update()
    
    def DelDiaLog(self, type, func, num = 1):
        
        multi = f'{num} ' if num > 1 else ''
        obj = {
            'BenhNhan': 'bệnh nhân',
            'BacSi': 'bác sĩ',
            'LichKham': 'lịch khám',
            'DichVu': 'dịch vụ',
            'Thuoc': 'thuốc',
            'PhongKhoa': 'phòng khám',
            'NhanVien': 'nhân viên',
            'HoaDon': 'hóa đơn',
            'ThietBi': 'thiết bị',
        }
        
        def close_dlg(e):
            dialog.open = False
            self.page.update()
        
        def confirmed(e):
            close_dlg(e)
            func()
        
        dialog = AlertDialog(
            modal=True,
            title=Text('Xác nhận'),
            content=Text(f'Bạn có chắc chắn muốn xóa {multi}{obj[type]} này không?'),
            actions=[
                TextButton('Hủy', on_click=close_dlg),
                TextButton('Xóa', on_click=confirmed),
            ],
            actions_alignment=MainAxisAlignment.END
        )
        return dialog
    
    def toggle_del_btn(self):
        if any(row.selected for row in self.data):
            if self.search.content.controls[-1].icon != icons.DELETE_ROUNDED:
                self.search.content.controls.append(IconButton(
                    icon=icons.DELETE_ROUNDED,
                    on_click=lambda _: self.multi_delete_click(),
                ))
        else:
            if self.search.content.controls[-1].icon == icons.DELETE_ROUNDED:
                self.search.content.controls = self.search.content.controls[:-1]
        self.page.update()
            
    def select_changed(self,e):
        e.control.selected = not e.control.selected
        self.toggle_del_btn()
            
            
    def delete_click(self, id):
        def confirmed():
            # self.data.remove(next(row for row in self.data if row.data == id))
            # self.cur_rows_change(self.data)
            # self.toggle_del_btn()
            match self.table.data:
                case 'BenhNhan':
                    patients.delete_patient(id)
                case 'BacSi':
                    doctors.delete_doctor(id)
                case 'LichKham':
                    appointments.delete_appointment(id)
                case 'DichVu':
                    services.delete_service(id)
                case 'Thuoc':
                    medicines.delete_medicine(id)
                case 'PhongKhoa':
                    departments.delete_department(id)
                case 'NhanVien':
                    employees.delete_employee(id)
                case 'HoaDon':
                    bills.delete_bill(id)
                case 'ThietBi':
                    equipments.delete_equipment(id)
            self.load()
        
        dialog = self.DelDiaLog(self.table.data, confirmed)
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        
        
            
        
    def multi_delete_click(self):
        selected_ids = tuple(row.data for row in self.data if row.selected)
        def confirmed():
            match self.table.data:
                case 'BenhNhan':
                    patients.delete_patients(selected_ids)
                case 'BacSi':
                    doctors.delete_doctors(selected_ids)
                case 'LichKham':
                    appointments.delete_appointments(selected_ids)
                case 'DichVu':
                    services.delete_services(selected_ids)
                case 'Thuoc':
                    medicines.delete_medicines(selected_ids)
                case 'PhongKhoa':
                    departments.delete_departments(selected_ids)
                case 'NhanVien':
                    employees.delete_employees(selected_ids)
                case 'HoaDon':
                    bills.delete_bills(selected_ids)
                case 'ThietBi':
                    equipments.delete_equipments(selected_ids)
            self.load()
    
        dialog = self.DelDiaLog(self.table.data, confirmed, len(selected_ids))
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        
    def edit_click(self, data):
        self.page.content[1] = PageForm(self.page, self.table.data, data)
        self.page.update()
        
    def cur_rows_change(self, rows):
        self.cur_rows=rows
        self.table.rows = self.cur_rows[:min(10, len(self.cur_rows))]
        self.num_page = ceil(len(self.cur_rows)/10)
        self.navigation.content.controls[3].value=f'of {self.num_page}'
    
    def searchTable(self):
        
        def search_change(e):
            search_result = []
            for row in self.data:
                if any(search_input.value.lower().strip() in str(cell.content.value).lower() if hasattr(cell.content, 'value') else '' for cell in row.cells[:-1]):
                    search_result.append(row)
            self.cur_rows_change(search_result)
            self.page.update()
        
        def on_refresh(e):
            # self.table = self.nav_data[self.table.data]()
            # self.scroll_table = Row(scroll=True, tight=True, controls=[self.table])
            # self.navigation = self.tableNavigation()
            # self.search = self.searchTable()
            # self.content = Container(
            #     padding=10,
            #     bgcolor=colors.GREEN_100,
            #     border_radius=10,
            #     content=Column(
            #         controls=[
            #             self.search,
            #             self.scroll_table,
            #             self.navigation
            #         ]
            #     )
            # )
            # self.page.update()
            self.load()
            
        def on_add(e):
            self.page.content[1] = self.page.router.route[f'/page_form/{self.table.data}']
            self.page.update()
        
        search_input = TextField(
            expand=True,
            label='Search',
            border_radius=8,
            content_padding=10,
            on_change=search_change
        )
        
        return Container(
            height=50,
            padding=5,
            content=Row(
                controls=[
                    search_input,
                    IconButton(icon=icons.ADD_ROUNDED, on_click=on_add),
                    IconButton(icon=icons.REFRESH_ROUNDED, on_click=on_refresh),
                ]
            )
        )
    
    # Bảng bệnh nhân    
    def PatientTable(self):
        
        patientData = lambda patient: DataRow(
            data=patient.id,
            cells=[
                DataCell(Text(patient.name)),
                DataCell(Text(patient.gender)),
                DataCell(Text(str(patient.birth))),
                DataCell(Text(patient.address)),
                DataCell(Text(patient.phone)),
                DataCell(
                    Row(
                        controls=[
                            IconButton(icon=icons.EDIT_ROUNDED, on_click=lambda _,data=patient: self.edit_click(data)),
                            IconButton(icon=icons.DELETE_ROUNDED, on_click=lambda _,id=patient.id: self.delete_click(id))
                        ]
                    )
                )
            ],
            on_select_changed=self.select_changed,
        )
        
        self.data = [patientData(patient) for patient in patients.get_patients()]
        self.cur_rows = self.data
        
        return DataTable(
            data='BenhNhan',
            heading_text_style=TextStyle(size=16.0, weight='bold'),
            border_radius=8,
            show_checkbox_column=True,
            columns=[
                DataColumn(label=Text('Họ tên')),
                DataColumn(label=Text('Giới tính')),
                DataColumn(label=Text('Ngày sinh')),
                DataColumn(label=Text('Địa chỉ')),
                DataColumn(label=Text('Số điện thoại')),
                DataColumn(label=Text('Thao tác')),
            ],
            rows=self.cur_rows[:10]
        )
        
    # Bảng bác sĩ    
    def DoctorTable(self):
        
        doctorData = lambda doctor: DataRow(
            data=doctor.id,
            cells=[
                DataCell(CircleAvatar(foreground_image_src=doctor.image, content=Text(doctor.name.split()[0][0] + doctor.name.split()[-1][0]))),
                DataCell(Text(doctor.name)),
                DataCell(Text(doctor.gender)),
                DataCell(Text(doctor.department.name)),
                DataCell(Text(doctor.degrees)),
                DataCell(Text(doctor.email)),
                DataCell(Text(doctor.phone)),
                DataCell(
                    Row(
                        controls=[
                            IconButton(icon=icons.EDIT_ROUNDED, on_click=lambda e,data=doctor: self.edit_click(e,data)),
                            IconButton(icon=icons.DELETE_ROUNDED, on_click=lambda e,id=doctor.id: self.delete_click(e,id))
                        ]
                    )
                )
            ],
            on_select_changed=self.select_changed,
        )
        
        self.data = [doctorData(doctor) for doctor in doctors.get_doctors()]
        self.cur_rows = self.data
                
        return DataTable(
            data='BacSi',
            heading_text_style=TextStyle(size=16.0, weight='bold'),
            border_radius=8,
            show_checkbox_column=True,
            columns=[
                DataColumn(label=Text('Hình ảnh')),
                DataColumn(label=Text('Họ tên')),
                DataColumn(label=Text('Giới tính')),
                DataColumn(label=Text('Khoa')),
                DataColumn(label=Text('Bằng cấp')),
                DataColumn(label=Text('Email')),
                DataColumn(label=Text('Số điện thoại')),
                DataColumn(label=Text('Thao tác')),
            ],
            rows=self.cur_rows[:10]
        )
    
    # Bảng lịch khám
    def AppointmentTable(self):
        
        appointmentData = lambda appointment: DataRow(
            data=appointment.id,
            cells=[
                DataCell(Text(appointment.patient.name)),
                DataCell(Text(appointment.doctor.name)),
                DataCell(Text(appointment.service.name)),
                DataCell(Text(str(appointment.date))),
                DataCell(Text(str(appointment.time))),
                DataCell(Text(str(appointment.condition))),
                DataCell(Text(appointment.status)),
                DataCell(
                    Row(
                        controls=[
                            IconButton(icon=icons.EDIT_ROUNDED, on_click=lambda e,data=appointment: self.edit_click(e,data)),
                            IconButton(icon=icons.DELETE_ROUNDED, on_click=lambda e,id=appointment.id: self.delete_click(e,id))
                        ]
                    )
                )
            ],
            on_select_changed=self.select_changed,
        )
        
        self.data = [appointmentData(appointment) for appointment in appointments.get_appointments()]
        self.cur_rows = self.data
        
        return DataTable(
            data='LichKham',
            heading_text_style=TextStyle(size=16.0, weight='bold'),
            border_radius=8,
            show_checkbox_column=True,
            columns=[
                DataColumn(label=Text('Bệnh nhân')),
                DataColumn(label=Text('Bác sĩ')),
                DataColumn(label=Text('Dịch vụ')),
                DataColumn(label=Text('Ngày')),
                DataColumn(label=Text('Giờ')),
                DataColumn(label=Text('Triệu chứng')),
                DataColumn(label=Text('Trạng thái')),
                DataColumn(label=Text('Thao tác')),
            ],
            rows=self.cur_rows[:10]
        )
    
    # Bảng dịch vụ
    def ServiceTable(self):
            
        serviceData = lambda service: DataRow(
            data=service.id,
            cells=[
                DataCell(Text(service.name)),
                DataCell(Text(service.department.name)),
                DataCell(Text(service.description)),
                DataCell(Text(f'{int(service.charge)}đ')),
                DataCell(
                    Row(
                        controls=[
                            IconButton(icon=icons.EDIT_ROUNDED, on_click=lambda _,data=service: self.edit_click(data)),
                            IconButton(icon=icons.DELETE_ROUNDED, on_click=lambda _,id=service.id: self.delete_click(id))
                        ]
                    )
                )
            ],
            on_select_changed=self.select_changed,
        )
        
        self.data = [serviceData(service) for service in services.get_services()]
        self.cur_rows = self.data
        
        return DataTable(
            data='DichVu',
            heading_text_style=TextStyle(size=16.0, weight='bold'),
            border_radius=8,
            show_checkbox_column=True,
            columns=[
                DataColumn(label=Text('Tên dịch vụ')),
                DataColumn(label=Text('Khoa')),
                DataColumn(label=Text('Mô tả')),
                DataColumn(label=Text('Giá')),
                DataColumn(label=Text('Thao tác')),
            ],
            rows=self.cur_rows[:10]
        )
    
    # Bảng nhân viên
    def EmployeeTable(self):
            
        employeeData = lambda employee: DataRow(
            data=employee.id,
            cells=[
                DataCell(CircleAvatar(foreground_image_src=employee.image, content=Text(employee.name.split()[0][0] + employee.name.split()[-1][0]))),
                DataCell(Text(employee.name)),
                DataCell(Text(employee.gender)),
                DataCell(Text(employee.address)),
                DataCell(Text(employee.email)),
                DataCell(Text(employee.phone)),
                DataCell(
                    Row(
                        controls=[
                            IconButton(icon=icons.EDIT_ROUNDED, on_click=lambda e,data=employee: self.edit_click(e,data)),
                            IconButton(icon=icons.DELETE_ROUNDED, on_click=lambda e,id=employee.id: self.delete_click(e,id))
                        ]
                    )
                )
            ],
            on_select_changed=self.select_changed,
        )
        
        self.data = [employeeData(employee) for employee in employees.get_employees()]
        self.cur_rows = self.data
        
        return DataTable(
            data='NhanVien',
            heading_text_style=TextStyle(size=16.0, weight='bold'),
            border_radius=8,
            show_checkbox_column=True,
            columns=[
                DataColumn(label=Text('Hình ảnh')),
                DataColumn(label=Text('Họ tên')),
                DataColumn(label=Text('Giới tính')),
                DataColumn(label=Text('Địa chỉ')),
                DataColumn(label=Text('Email')),
                DataColumn(label=Text('Số điện thoại')),
                DataColumn(label=Text('Thao tác')),
            ],
            rows=self.cur_rows[:10]
        )
    
    # Bảng phòng khoa
    def DepartmentTable(self):
                
        departmentData = lambda department: DataRow(
            data=department.id,
            cells=[
                DataCell(Text(department.name)),
                DataCell(Text(department.description, width=700)),
                DataCell(Text('Hoạt động' if department.status else 'Không hoạt động')),
                DataCell(
                    Row(
                        controls=[
                            IconButton(icon=icons.EDIT_ROUNDED, on_click=lambda e,data=department: self.edit_click(e,data)),
                            IconButton(icon=icons.DELETE_ROUNDED, on_click=lambda e,id=department.id: self.delete_click(e,id))
                        ]
                    )
                )
            ],
            on_select_changed=self.select_changed,
        )
        
        self.data = [departmentData(department) for department in departments.get_departments()]
        self.cur_rows = self.data
        
        return DataTable(
            data='PhongKhoa',
            heading_text_style=TextStyle(size=16.0, weight='bold'),
            border_radius=8,
            show_checkbox_column=True,
            columns=[
                DataColumn(label=Text('Tên phòng')),
                DataColumn(label=Text('Mô tả')),
                DataColumn(label=Text('Trạng thái')),
                DataColumn(label=Text('Thao tác')),
            ],
            rows=self.cur_rows[:10]
        )
    
    # Bảng thuốc
    def MedicineTable(self):
                        
        medicineData = lambda medicine: DataRow(
            data=medicine.id,
            cells=[
                DataCell(Text(medicine.name)),
                DataCell(Text(medicine.type)),
                DataCell(Text(medicine.provider.name)),
                DataCell(Text(f'{int(medicine.unit_price)}đ')),
                DataCell(Text(medicine.quantity)),
                DataCell(Text(str(medicine.buy_date))),
                DataCell(Text(str(medicine.expire_date))),
                DataCell(
                    Row(
                        controls=[
                            IconButton(icon=icons.EDIT_ROUNDED, on_click=lambda e,data=medicine: self.edit_click(e,data)),
                            IconButton(icon=icons.DELETE_ROUNDED, on_click=lambda e,id=medicine.id: self.delete_click(e,id))
                        ]
                    )
                )
            ],
            on_select_changed=self.select_changed,
        )
        
        self.data = [medicineData(medicine) for medicine in medicines.get_medicines()]
        self.cur_rows = self.data
        
        return DataTable(
            data='Thuoc',
            heading_text_style=TextStyle(size=16.0, weight='bold'),
            border_radius=8,
            show_checkbox_column=True,
            columns=[
                DataColumn(label=Text('Tên thuốc')),
                DataColumn(label=Text('Loại')),
                DataColumn(label=Text('Nhà cung cấp')),
                DataColumn(label=Text('Đơn giá')),
                DataColumn(label=Text('Số lượng')),
                DataColumn(label=Text('Ngày mua')),
                DataColumn(label=Text('Hạn sử dụng')),
                DataColumn(label=Text('Thao tác')),
            ],
            rows=self.cur_rows[:10]
        )
        
    
    # Bảng hóa đơn     
    def BillTable(self):
                        
        billData = lambda bill: DataRow(
            data=bill.id,
            cells=[
                DataCell(Text(bill.patient.name)),
                DataCell(Text(bill.doctor.name)),
                DataCell(Text(str(bill.date))),
                DataCell(Text(f'{bill.discount}%')),
                DataCell(Text(f'{int(bill.total)}đ')),
                DataCell(Text(f'{int(bill.real_total)}đ')),
                DataCell(
                    Row(
                        controls=[
                            IconButton(icon=icons.EDIT_ROUNDED, on_click=lambda e,data=bill: self.edit_click(e,data)),
                            IconButton(icon=icons.DELETE_ROUNDED, on_click=lambda e,id=bill.id: self.delete_click(e,id))
                        ]
                    )
                )
            ],
            on_select_changed=self.select_changed,
        )
        
        self.data = [billData(bill) for bill in bills.get_bills()]
        self.cur_rows = self.data
        
        return DataTable(
            data='HoaDon',
            column_spacing=95,
            heading_text_style=TextStyle(size=16.0, weight='bold'),
            border_radius=8,
            show_checkbox_column=True,
            columns=[
                DataColumn(label=Text('Bệnh nhân')),
                DataColumn(label=Text('Bác sĩ')),
                DataColumn(label=Text('Ngày tạo')),
                DataColumn(label=Text('Giảm giá')),
                DataColumn(label=Text('Tổng tiền')),
                DataColumn(label=Text('Thực thu')),
                DataColumn(label=Text('Thao tác')),
            ],
            rows=self.cur_rows[:10]
        )
    
    # Bảng thiết bị
    def EquipmentTable(self):
                                    
        equipmentData = lambda equipment: DataRow(
            data=equipment.id,
            cells=[
                DataCell(Text(equipment.name)),
                DataCell(Text(equipment.type)),
                DataCell(Text(equipment.provider.name)),
                DataCell(Text(str(equipment.buy_date))),
                DataCell(Text(f'{int(equipment.price)}đ')),
                DataCell(Text(equipment.quantity)),
                DataCell(
                    Row(
                        controls=[
                            IconButton(icon=icons.EDIT_ROUNDED, on_click=lambda e,data=equipment: self.edit_click(e,data)),
                            IconButton(icon=icons.DELETE_ROUNDED, on_click=lambda e,id=equipment.id: self.delete_click(e,id))
                        ]
                    )
                )
            ],
            on_select_changed=self.select_changed,
        )
        
        self.data = [equipmentData(equipment) for equipment in equipments.get_equipments()]
        self.cur_rows = self.data
        
        return DataTable(
            data='ThietBi',
            column_spacing=80,
            heading_text_style=TextStyle(size=16.0, weight='bold'),
            border_radius=8,
            show_checkbox_column=True,
            columns=[
                DataColumn(label=Text('Tên thiết bị')),
                DataColumn(label=Text('Loại')),
                DataColumn(label=Text('Nhà cung cấp')),
                DataColumn(label=Text('Ngày mua')),
                DataColumn(label=Text('Giá')),
                DataColumn(label=Text('Số lượng')),
                DataColumn(label=Text('Thao tác')),
            ],
            rows=self.cur_rows[:10]
        )

    
    def tableNavigation(self):
        self.num_page = ceil(len(self.cur_rows)/10)
        self.cur_page = 1
        
        def page_change():
            start = (self.cur_page - 1) * 10
            end = min(len(self.cur_rows), start + 10)
            self.table.rows = self.cur_rows[start:end]
            nav_txt.value = self.cur_page
            self.page.update()
        
        def pre_page(e):
            self.cur_page = max(1, self.cur_page - 1)
            page_change()
        def next_page(e):
            self.cur_page = min(self.num_page, self.cur_page + 1)
            page_change()
        def on_submit(e):
            e.control.value = self.cur_page = min(self.num_page, int(e.control.value))
            page_change()
        nav_txt = TextField(value=self.cur_page, width=30, height=30, content_padding=0, text_align=TextAlign.CENTER, input_filter=NumbersOnlyInputFilter(), border_color='transparent', on_submit=on_submit)
        return Container(
            content=Row(
                controls=[
                    IconButton(icon=icons.CHEVRON_LEFT_ROUNDED, on_click=pre_page),
                    IconButton(icon=icons.CHEVRON_RIGHT_ROUNDED, on_click=next_page),
                    nav_txt,
                    Text(f'of {self.num_page}'),
                ]
            )
        )
        
    def build(self):
        return self