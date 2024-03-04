print("you are hungry")
print('you are hungry')

def function():
    print('you are hungry')
    print('you are hungry')
    print('you are hungry')
function()
function()
def karibu(name):
    print(name)
    print(name)
    print(name)
karibu('john')

def num(nambari):
    print(nambari)
    print(nambari)
num(56)
num(43)
def salutation(first_name):
    print('Hi '+first_name + ' good morning')
salutation('esther')
def miaka(age):
    print('hello,you are ' + str(age) +' years old')
miaka(18)

def my_name(first_name,last_name):
    print(first_name + '' + last_name + " is the student")
my_name('val ',' mbeki')


def sentence(first_name,last_name,age):
    print(first_name + ''+ last_name +' is ' +str(age) + ' years old')
sentence('john ',' kamau',13)

def employees(first_name,age):
    if age >=20:
        print(first_name + 'you are' + str(age) + 'years old')
    elif age<20 and age>=15:
        print(first_name + ' you are ' + str(age) + ' years old')
    elif age<15 and age>=10:
        print(first_name + ' you are ' + str(age) + ' years old')
    else:
        print(first_name + 'you are' + str(age) + 'years old')
employees('mbuthia ',23)
employees('otieno ',9)
employees('cheptoo ',13)

def age_calculator(age):
    new_age = age +10
    return new_age
print(age_calculator(18))

def marks_calculator(*subjects):
    total_marks = sum(subjects)
    return total_marks
print(marks_calculator(23,45,67))
print(marks_calculator(2,56,68,90))
print(marks_calculator(34,56))





def v(first_name,last_name,age):
    print(first_name + last_name + ' is a student and she is ' + str(age) +' years old')
v('val',' mbeki',17)
def marks(*languages):
    overall_total = sum(languages)
    return overall_total
print(marks(66,77))
print(marks(87,55))

def  my_post(location,age):
    if age <60:
        print(str(age) +" posted to" + location)
    elif age <60 and age >50:
        print(str(age) + 'posted to' + location)
    elif age <40 and age >30:
        print(str(age) + ' posted to' + location)
    elif age >30:
        print(str(age) + ' posted to' + location)
    else:
        print(str(age) + ' posted to' + location)
my_post(' kisumu',61)
my_post(' nakuru',54)
my_post(' mombasa',31)











