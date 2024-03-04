height=float(input("enter your height in meters"))
weight=float(input("enter your weight in kilograms"))
Bmi=float(weight)/float(height*height)
print (Bmi)
if Bmi <18:
    print("you are underweight")
elif Bmi <25 and Bmi >18:
    print("your normal")
elif Bmi <30 and Bmi >25:
    print("you are overweight")
elif Bmi >30:
    print("you are obese")

