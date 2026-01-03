#output of the following

a = "10"
b = 5
c = 2.5

result = int(a) + b * float(a) / c + bool(a)
print(result)

#Basic casting 

print(int('25'))
print(float('3.14'))
print(str(45))
print(int(True))
print(bool(0))

#predict the output

a = '20'
b = 3
c = 2.5

result = int(a) + b * float(a)/c
print(result)

#collection casting
# convert between list,tuple,set
a = [1,2,2,3]
print(set(a))

b = (4,5,6)
print(list(b))

c = {7,8,9}
print(tuple(c))

s = 'python'
print(list(s))

#boolean casting

print(bool('hello'))
print(bool(''))
print(bool(0))
print(bool(2.15))
print(bool([]))
print(bool(()))
print(bool({}))

#error handling

try:
    value = '1.3' 
    num = int(value)
except ValueError:
    print('invalid value')

#real - world practical
#convert user inpur safely
# try:
#     age = int(input('enter the age: '))
# except ValueError:
#     print('invalid age')
# else:
#     print(f'your age is {age}')

# tricky cases

print(int(3.9999999))
print(int(True) + float(False))
print(list(str(12345)))
print(tuple({1,2,3}))
print(bool('False'))

#class and object
class student:
    def __str__(self):
        return 'student object'
    def __int__(self):
        return 1000
s = student()
print(str(s))
print(int(s))

a = 5
b = a
a = 6
print(b)