class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f'{self.name} scored {self.marks} marks'

s = student('bhushan',95)
print(s.name)
print(s.marks)
print(s)

#operator overloding

class Vector:
    def __init__(self,x,y):
        self.x,self.y = x,y
    
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)

    def __repr__(self):
        return f'vector({self.x},{self.y})'

v1 = Vector(2,3)
v2 = Vector(4,5)
print(v1+v2)        