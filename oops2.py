#libraray simualtion

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed = []

    def borrow(self, book):
        if book.available:
            book.available = False
            self.borrowed.append(book)
            print(f"{self.name} borrowed {book.title}")
        else:
            print("Book not available")

    def return_book(self, book):
        if book in self.borrowed:
            book.available = True
            self.borrowed.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print("You didn’t borrow this book")

# Dry-run
b1 = Book("Python 101", "Guido")
m1 = Member("Bhushan")
m1.borrow(b1)   # Bhushan borrowed Python 101
m1.return_book(b1)  # Bhushan returned Python 101

#operator overloading

class vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return vector(self.x + other.x , self.y + other.y)
    
    def __str__(self):
        return f'({self.x},{self.y})'
    
v1 = vector(2,3)
v2 = vector(4,5)
print(v1+v2)
        
#multiple inheritance

class teacher:
    def role(self):
        print('teaching students')

class researcher:
    def role(self):
        print('conducting research')

class professor(teacher,researcher):
    pass

p = professor()
p.role()
print(professor.__mro__)

#statci and class methods

class student:
    shcool_name = 'abc school'

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod
    def change_school(cls, new_name):
        cls.shcool_name = new_name

    @staticmethod
    def is_adult(age):
        return age>= 18
    

s1 = student('bhushan',20)
print(student.shcool_name)

student.change_school('xyz school')
print(student.shcool_name)

print(student.is_adult(17))
        