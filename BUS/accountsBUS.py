from DAO import connection_pool, AccountsDAO
from DTO import Account

class AccountsBUS:
    def __init__(self, connection_pool):
        self.connection_pool = connection_pool
        self.accountsDAO = AccountsDAO(self.connection_pool)
        
    def get_accounts(self):
        return [
            Account(
                role=account[0],
                username=account[1],
                password=account[2]
            ) for account in self.accountsDAO.get_accounts()
        ]
    
    def add_account(self, account):
        self.accountsDAO.add_account(account)
    
accounts = AccountsBUS(connection_pool)