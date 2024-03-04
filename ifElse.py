age=int(input("how old are you? "))
if age >=68:
    print("you are olD enough to move retire")
elif age <65 and age >=50:
    print("you are almost going to retire")
elif age <50 and age>=40:
    print("you are still active")
elif age<40 and age>=18:
    print("your considered youthful")
else:
    print("you are still young")


marks=float(input("enter your marks"))
if marks >=80 and marks <=100:
    print('you have an A')
elif marks >=60 and marks <=79:
    print('you have a B')
elif marks >=50 and marks <=59:
    print('you have a C')
elif marks >=40 and marks<=49:
    print('you have a D')
elif marks >=0 and marks<=39:
    print('you have a E')
else:
    print('enter valid marks')

temp=float(input("enter your temperature? "))
if temp >30:
    print("have a vest on")
elif temp <=30 and temp>=20:
    print("put on a sweater")
elif temp <20:
    print("put on a jacket")



