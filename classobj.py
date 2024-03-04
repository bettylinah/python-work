class person:
    name="john"
    age = 18
    gender ="male"
    marital_status ="divorced"
print(person.name)
print(person.age)
print(person.gender)
print(person.marital_status)
person.age =20
print(person.age)

class employees:
    firstname ="val"
    lastname ="mbeki"
    salary =100000
    gender =("female")
    age =33
print(f"{employees.firstname} {employees.lastname} your age is {employees.age} and you earn a salary of {employees.salary} and you are of gender {employees.gender}.")
print(f"{employees.lastname} you are a {employees.gender} who earn {employees.salary}")
print(f"{employees.firstname} is a {employees.gender} of age {employees.age}")

# class parent:
#     firstname ="ariana"
#     lastname ="grande"
#     print(firstname)
#     print(lastname)
class parent:
    def __init__(self,firstname,lastname,age):
        self.firstname =firstname
        self.lastname =lastname
        self.age =age
parent1 =parent("arina",' grande',21)
parent2 =parent("nicki","minaj",40)
parent3 =parent("megan","stallion",29)
print(parent1.firstname)
print(parent2.firstname)
print(parent3.firstname)
print(parent1.lastname)
print(parent2.lastname)
print(parent3.lastname)

class cars:
    def __init__(self,make,model,year):
        self.make =make
        self.model =model
        self.year =year
car1 =cars("ford","ranger",2022)
car2 =cars("toyota","axis",2014)
car3 =cars("nissan","sunny",1999)
print(car1.make)
print(car2.make)
print(car3.make)
print(f"my car is{car1.make} {car1.model}")
print(f"{car1.make},{car2.make} and {car3.make} are all manufactured in year {car3.year}")

class students:
    def __init__(self,firstname,lastname,score):
        self.firstname =firstname
        self.lastname =lastname
        self.score =score
student1 =students("jane","njenga",306)
student2 =students("ariana","grande",365)
student3 =students("jason","derulo",401)
print(f"{student1.firstname} {student1.lastname} has scored {student1.score}"f" {student2.firstname} {student2.lastname} has scored {student2.score} "f"{student3.firstname} {student3.lastname} has scored {student3.score}. "
      )

class magari:
    def __init__(self,make,model,price,year):
        self.make =make
        self.model =model
        self.price =price
        self.year =year
    def describe(self):
        print(f"my favourite car is {self.make} and it is a model {self.model} and it cost {self.price}")

obj1 =magari("ford","ranger",300000,2024)
obj2 =magari("toyota","axis",400000,2013)
obj3 = magari('nissan', "sunny", 500000, 2012)
print(f"my favourite car is {obj1.make} and it is a model {obj1.model} and it cost {obj1.price}")
print(obj1.describe())
print()

class Person:
    def __init__(self,firstname,lastname,gender,age):
        self.firstname =firstname
        self.lastname =lastname
        self.gender =gender
        self.age =age
    def fullname(self):
        print(f"{self.firstname} {self.lastname}")
    def person_age(self):
        print(self.age)
    def display_gender(self):
        print(self.gender)
    def one_lastname(self):
        print(f"my last name is {self.lastname}")
    def increment_age(self):
        self.age +=10
per1 =Person("val","mbeki","female",16)
print(per1.fullname())
print(per1.person_age())
print(per1.display_gender())
print(per1.one_lastname())
