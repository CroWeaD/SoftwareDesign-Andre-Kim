import Data_Storage

class ManageProfile:
    def __init__(self, data):
        self.updateinfo = data
        
    def updateProfile(self, user):
        i = 0
        for account in Data_Storage.DataStorage.account:
            if account[0] == user[0]:
                    break
            
            i+=1
        
        pop = Data_Storage.DataStorage.account.pop(i)
        
        if (self.updateinfo[0] == "") and (self.updateinfo[1] == "") and (self.updateinfo[2] == ""):
            req = input("delete?(Y/N)>> ")
            
            if req == "Y" or req == "y":
                Data_Storage.DataStorage.update(user)   #수정될 가능성 높음
                return "Deleted " + str(user)
                
            elif req == "N" or req == "n":
                Data_Storage.DataStorage.account.append(pop)
                return "Not changed"
            else:
                print("Invalid input!")
                Data_Storage.DataStorage.account.append(pop)
                return "Not changed"
        
        else:
            new_profile = []
            
            new_profile.append(user[0])
            
            if (self.updateinfo[0] != ""):
                new_profile.append(self.updateinfo[0])
            else:
                new_profile.append(pop[1])
            
            if (self.updateinfo[1] != ""):
                new_profile.append(self.updateinfo[1])
            else:
                new_profile.append(pop[2])
            
            if (self.updateinfo[2] != ""):
                new_profile.append(self.updateinfo[2])
            else:
                new_profile.append(pop[3])
                
            Data_Storage.DataStorage.account.append(new_profile)
            
            Data_Storage.DataStorage.update(user)   #수정될 가능성 높음
        
        return "Changed " + str(new_profile)
                    
            
            
            
