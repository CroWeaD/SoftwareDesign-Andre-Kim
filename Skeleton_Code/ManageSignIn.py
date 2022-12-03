import Data_Storage

class ManageSignIn:
    def __init__(self, data):
        self.signInInfo = data
        
    def validateSignIn(self):
        Data_Storage.DataStorage.select([])
        for account in Data_Storage.DataStorage.account:
            if account[0] == self.signInInfo[0]:
                if account[1] == self.signInInfo[1]:
                    return True
        
        for account in Data_Storage.DataStorage.account:
            print(account)
        
        return False
                    
            
            
            
