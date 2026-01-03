class BankAccount:
    def __init__(self,number,name,balance):
        self.num = number
        self.name = name
        self.__bal = balance
    def deposit(self,amount):
        self.__bal+=amount
    def withdraw(self,amount):
        if amount>self.__bal:
            print('invalid')
        self.__bal-=amount
    def display_balance(self):
        return self.__bal
        
user = BankAccount(1234,'bhushan',1000)
user.deposit(1000)
user.withdraw(200)
print(user.display_balance())

#inheritance and method overriding

class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def start(self):
        print('vehicle started')
class Car(Vehicle):
    def start(self):
        print('car started')   

o1 = Car('tesla',1)
o1.start()  

o2 = Vehicle('tesla',2)
o2.start()

#encapsulation

class Student:
    def __init__(self,marks):
        self.__marks = marks
    def set_marks(self,new):
        if new >0:
            self.__marks = new
        else:
            print('invalid')
    def get_marks(self):
        return self.__marks
    
s1 = Student(100)
s1.set_marks(75)
print(s1.get_marks())

#multiple inheritance

class Flyer:
    def fly(self):
        print('it fly')
class swimmer:
    def swim(self):
        print('it swim')
class Duck(Flyer,swimmer):
    pass

b = Duck()
b.fly()
b.swim()
print(Duck.__mro__)

#operator overloading

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector(self.x + other.x,self.y + other.y)
    
    def __str__(self):
        return f'vector({self.x},{self.y})'
    
v1 = Vector(2,3)
v2 = Vector(4,5)
print(v1+v2)
        
#abstract classes

from abc import ABC,abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangel(shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

class Circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
shapes = [Rectangel(4,5),Circle(3)]
for s in shapes:
    print(s.area())      
        
#class vs static methods

class MathUtils:
    @staticmethod
    def add(a,b):
        return a +b
    
    @classmethod
    def info(cls):
        print(f'this is class: {cls.__name__}')

print(MathUtils.add(5,6))
MathUtils.info()
        
#class and object Basics

class Car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def display(self):
        print(self.brand,self.model,self.year)
car1 = Car('tesla',20,2020)
car2 = Car('tesla',14,2023)
car2.year = 2023
car1.year = 2024
car1.display()
car2.display()

#inheritance

class Shape:
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.len = length
        self.wid = width

    def area(self):
        return self.len * self.wid
    
class circle(shape):
    def __init__(self,radius):
        self.rad = radius
    
    def area(self):
        return math.pi * self.rad**2
    
re = Rectangel(2,3)
print(re.area())

ci = circle(2)
print(ci.area())

#encapsulation

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    
    def balance(self,new):
        self.__balance = new

    @property
    def get_balance(self):
        return self.__balance
    
b1 = BankAccount('bhuahan',200)
b1.balance(1000)
print(b1.get_balance)
        
#abstraction

class payment(ABC):
    @abstractmethod
    def make_payment(self,amount):
        pass

class CreditCardPayment(payment):
    def make_payment(self, amount):
        print(f'paid {amount} using credit card')

class Upipayment(payment):
    def make_payment(self, amount):
        print(f'paid {amount} using upi') 

p1 = CreditCardPayment()
p2 = Upipayment()
p1.make_payment(500)
p2.make_payment(200)       
        
        