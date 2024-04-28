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

connection_string = 'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=tcp:NaWW,1433; DATABASE=clinic; Trusted_Connection=yes;'
connection_pool = ODBCConnectionPool(connection_string)

