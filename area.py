class Rectangle:
    def __init__(self,width,length):
        self.width =width
        self.length =length
        self.area =length*width
area1 =Rectangle(44,56)
print(area1.area)


class Circle:
    def __init__(self,one,radius):
        self.one =one
        self.radius =radius
        self.area =one*(radius*radius)
area2 =Circle(22/7,21)
print(area2.area)

class Bankaccount:
    def __init__(self,account_number,balance,date_of_opening,customer_name):
        self.account_number =account_number
        self.balance =balance
        self.date_of_opening =date_of_opening
        self.customer_name =customer_name
    def deposit(self):
        deposit =int(input("Enter amount you would like to deposit"))
        balance=self.balance+deposit
        print(f"dear{self.customer_name}your new balance is{balance}")
    def withdraw(self):
        withdraw =int(input("enter amount you would like to withdraw"))
        balance=self.balance-withdraw
        print(f"{self.customer_name}your new balance is{balance}")

obj4=Bankaccount(234,40000,24,"natasha")
obj4.withdraw()
obj4.deposit()