from DAO import connection_pool,ProvidersDAO
from DTO import Provider

class ProvidersBUS:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.providersDAO = ProvidersDAO(connection_pool)
        
    def get_providers(self):
        return [Provider(*provider) for provider in self.providersDAO.get_providers()]
    
    def get_provider(self, provider_id):
        return Provider(*self.providersDAO.get_provider(provider_id))
    
    def add_provider(self, provider):
        self.providersDAO.add_provider(provider)
        
    def delete_provider(self, provider_id):
        self.providersDAO.delete_provider(provider_id)
        
    def delete_providers(self, provider_ids):
        self.providersDAO.delete_providers(provider_ids)
        
    def update_provider(self, provider):
        self.providersDAO.update_provider(provider)
        
        
providers = ProvidersBUS(connection_pool)