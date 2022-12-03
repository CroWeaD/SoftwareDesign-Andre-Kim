import Data_Storage

class ManageSignUp:
    def __init__(self, data):
        self.signUpInfo = data
        
    def validateSignUp(self):
        for account in Data_Storage.DataStorage.account:
            if account[0] == self.signUpInfo[0]:
                return False
        
        Data_Storage.DataStorage.insert(self.signUpInfo)
        Data_Storage.DataStorage.account.append(self.signUpInfo)
        
        for account in Data_Storage.DataStorage.account:
            print(account)
        
        return True
                    
            
            
            
