from DAO import connection_pool,ServicesDAO
from DTO import Service, Department

class ServicesBUS:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.servicesDAO = ServicesDAO(connection_pool)
        
    def get_services(self):
        return [Service(
            id=service[0],
            name=service[1],
            description=service[2],
            charge=service[3],   
            department=Department(
                id=service[4],
                name=service[5],
                description=service[6],
                status=service[7]
            )
        ) for service in self.servicesDAO.get_services()]
    
    def get_service(self, service_id):
        id, name, description, charge, department_id, department_name, description, status=self.servicesDAO.get_service(service_id)
        return Service(
            id=id,
            name=name,
            description=description,
            charge=charge,
            department=Department(
                id=department_id,
                name=department_name,
                description=description,
                status=status
            )
        )
    
    def add_service(self, service):
        self.servicesDAO.add_service(service)
        
    def delete_service(self, service_id):
        self.servicesDAO.delete_service(service_id)
        
    def delete_services(self, service_ids):
        self.servicesDAO.delete_services(service_ids)
        
    def update_service(self, service):
        self.servicesDAO.update_service(service)
        
        
services = ServicesBUS(connection_pool)