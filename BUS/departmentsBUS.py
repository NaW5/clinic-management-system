from DAO import connection_pool,DepartmentsDAO
from DTO import Department

class DepartmentsBUS:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.departmentsDAO = DepartmentsDAO(connection_pool)
        
    def get_departments(self):
        return [Department(*department) for department in self.departmentsDAO.get_departments()]
    
    def get_department(self, department_id):
        return Department(*self.departmentsDAO.get_department(department_id))
    
    def add_department(self, department):
        self.departmentsDAO.add_department(department)
        
    def delete_department(self, department_id):
        self.departmentsDAO.delete_department(department_id)
        
    def delete_departments(self, department_ids):
        self.departmentsDAO.delete_departments(department_ids)
        
    def update_department(self, department):
        self.departmentsDAO.update_department(department)
        
        
departments = DepartmentsBUS(connection_pool)