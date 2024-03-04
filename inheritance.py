class Employees:
    def __init__(self,name,salary):
        self.name =name
        self.salary =salary
class Receptionist(Employees):
    def __init__(self, name, salary,gender):
        super().__init__(name,salary)
        self.gender =genderReceptionist1=Receptionist
class front_end_developer(Employees):
    def __init__(self,name,salary,programming):
        super().__init__(name,salary)
        self.programming =programming
Receptionist1=Receptionist("susan",30000,"female")
Employees1=Employees('felix',20000)
print(Receptionist1.name)
print(Employees1.name)