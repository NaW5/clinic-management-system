from DAO import connection_pool,EmployeesDAO
from DTO import Employee

class EmployeesBUS:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.employeesDAO = EmployeesDAO(connection_pool)
        
    def get_employees(self):
        return [Employee(*employee) for employee in self.employeesDAO.get_employees()]
    
    def get_employee(self, employee_id):
        return Employee(*self.employeesDAO.get_employee(employee_id))
    
    def add_employee(self, employee):
        self.employeesDAO.add_employee(employee)
        
    def delete_employee(self, employee_id):
        self.employeesDAO.delete_employee(employee_id)
        
    def delete_employees(self, employee_ids):
        self.employeesDAO.delete_employees(employee_ids)
        
    def update_employee(self, employee):
        self.employeesDAO.update_employee(employee)
        
        
employees = EmployeesBUS(connection_pool)