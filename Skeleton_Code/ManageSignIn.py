import Data_Storage

class ManageSignIn:
    def __init__(self, data):
        self.signInInfo = data
        
    def validateSignIn(self):
        print("_validateSignIn()")
        Data_Storage.DataStorage.select([])
        print("_return")
        for account in Data_Storage.DataStorage.account:
            if account[0] == self.signInInfo[0]:
                if account[1] == self.signInInfo[1]:
                    print("_result (True or False)")
                    return True
        
        for account in Data_Storage.DataStorage.account:
            print(account)
            print("_result (True or False)")
        return False
                    
            
            
            
