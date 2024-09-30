class User:
    def __init__(self,FirstName, LastName,username, Age, Gender,height, weight, Email ):
        
        self.FirstName=FirstName
        self.LastName=LastName
        self.username=username
        self.Age=Age
        self.Gender=Gender
        self.Email=Email
        self.height=height
        self.weight=weight
    def BMI(bd):
        if bd.weight is None or bd.height is None or bd.height==0:
            return None   
        val=(bd.weight)/(bd.height**2)
        return round(val,2)
    
    def login(self):
        pass
    
    def signup(self):
        pass
    def choose_Wp(self):
        pass

class Wplan:
    def _init_(self,FirstName,duration):
        pass
