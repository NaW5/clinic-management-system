from .connection_pool import ODBCConnectionPool
from .patientsDAO import PatientsDAO
from .accountsDAO import AccountsDAO
from .doctorsDAO import DoctorsDAO
from .appointmentsDAO import AppointmentsDAO
from .medicinesDAO import MedicinesDAO
from .billsDAO import BillsDAO
from .servicesDAO import ServicesDAO
from .departmentsDAO import DepartmentsDAO
from .equipmentsDAO import EquipmentsDAO
from .employeesDAO import EmployeesDAO
from .providersDAO import ProvidersDAO

database = 'clinic'
server = '.'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}}; SERVER={server}; DATABASE={database}; Trusted_Connection=yes;'
connection_pool = ODBCConnectionPool(connection_string)

