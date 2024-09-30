class user:
    def __init__(self,Fname, Lname,username, Age, Gender,height, weight, Email ):
        
        self.Fname=Fname
        self.Lname=Lname
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

class workout_plan:
    def _init_(self,Fname,duration):
        pass


class nutrition_plan:
    def __init__(self) -> None:
       pass
     
        
class progress:
    def __init__(self) -> None:
        pass
