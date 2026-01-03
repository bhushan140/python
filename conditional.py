#basic
#check if the number is positive,negative, or zero 

num = 5 #int(input('enter the number: '))

if num > 0:
    print('positive')
elif num < 0:
    print('negative')
else:
    print('zero')

#check if a number is even or odd

n = 3 #int(input('enter a number: '))

if n % 2 == 0:
    print('even')
else:
    print('odd')

#ternary operator 

print('even') if n % 2 == 0 else print('odd') 

#find the largest of two numbers

a = 23 #int(input('A: '))
b = 24 #int(input('B: '))

if a > b:
    print('A is largest')
else:
    print('B is largest')

#ternary operator

print('A is largest') if a > b else print('B is largest')

#check if a year is a leap year 

year = 2024 #int(input('year: '))

if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print('leap year')
else:
    print('not a leap year')

#grade calculator

marks = 85 # int(input('marks: '))

if marks >= 90:
    print('A')
elif marks >= 75:
    print('B')
elif marks >= 60:
    print('C')
else:
    print('D')

#check if character is vowel or consonant

ch = 'w' #input('enter a character: ').lower()

if ch in 'aeiou':
    print('vowel')
else:
    print('Consonant')

#ternary operator

print('vowel') if ch in 'aeiou' else print('consonant')

#FizzBuzz
#if number divisible by 3 -> Fizz
#if divisble by 5 -> Buzz
#if divisible by both => FizzBuzz

n = 15 # int(input('enter the number: '))
 
if n %3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)

# check if a number is in a range

n = 35 #int(input('enter the number: '))

if 10 <= n <= 50:
    print('in rnage')
else:
    print('out of range')

#login system(simple)

username = 'admin' #input('username: ')
password = '1234' #input('password: ')

if username == 'admin' and password == '1234':
    print('login successful')
else: 
    print('invalid credentials')

#ternary operator

print('login successful') if username == 'admin' and password == '1234' else print('invalid credentials')

#nested condition

age = 18 # int(input('enter the age: '))

if age >= 18:
    citizen = 'yes' #input('Are you a citizen of india ?(yes/no): ')
    if citizen == 'yes':
        print('eligibal')
    else:
        print('not eligibal')
else:
    print('underage')

#find the second larget number amoung three numbers

num1 = 3 # int(input('enter the number A: '))
num2 = 4 #int(input('enter the number B: '))
num3 = 5 #int(input('enter the number C: '))

if num1>num2>num3:
    print('secound largest:',num2)
elif num2>num1>num3:
    print('secound largest:',num1)
else:
    print('secound largest: ',num3)

#atm withdrawal logic

balance = 10000
choise = input('say yes to withdrawal: ')

if choise == 'yes':
    amount = int(input('enter the ammout to withdraw: '))
    if amount<= balance and amount%100 == 0:
        balance-= amount
        print('withdraw is succeful')
        print(f'current balance : {balance}')
    else:
        print('please enter the valid amount to witdraw')
else:
    print('thank you for using atm')

#electricity bill calculator

units = int(input('enter the units of current: '))
if units <= 100:
    price = 5*units
elif units <= 200:
    price = 7*units
elif units <=300:
    price = 10 * units
elif units>300:
    price = 15*units

total_bill = price
print(f'total bill : {price}')

#validate a strong password

pwd = input('enter the password to check: ')

has_upper = any(ch.isupper() for ch in pwd)
has_digit = any(ch.isdigit() for ch in pwd)
has_lower = any(ch.islower() for ch in pwd)
has_spl = any(ch in '!@#$%^&*()?' for ch in pwd)

if len(pwd) >= 8 and has_upper and has_digit and has_spl and has_lower:
    print('strong')
else:
    print('week')

#check if a string is a valid identifier

s = input()
space = any(ch in ' !@#$%^&*()' for ch in s)

if s[0] not in '0123456789' and not space:
   print('valid')
else:
    print('invalid')

#traffic light system

color = input().lower()

if color == 'red':
    print('stop')
elif color == 'yellow':
    print('ready')
elif color == 'green':
    print('go')
else:
    print('invalid color')

#triangle classification

a,b,c = map(int,input().split())

if a + b > c and a + c >b and b + c >a:
    if a == b == c:
        print('equilateral')
    elif a == b or b == c or a == c:
        print('Isosceles')
    else:
        print('scalene')
else:
    print('not a triangle')

#point inside a rectangle

x1,y1 = 0,0
x2,y2 = 10,10
px,py = map(int,input().split())

if x1 <= px <=x2 and y1 <= py <= y2:
    print('insde')
else:
    print('outside')

#24 - hour => 12-hour format

time = input() #hh:mm
 
h,m = map(int,time.split(':'))

if h == 0:
    print(f'12:{m:02d} AM')
elif h == 12:
    print(f'12:{m:02d} PM')
elif h < 12:
    print(f'{h}:{m:02d} AM')
else:
    print(f'{h-12}:{m:02d} PM')

#check given number is even or odd using bitwise operatoer

num = int(input('enter a number: '))

if num & 1 == 0:         #num &1 extract the last bit
    print('even number')  #if last bit is 0 num is even and
else:                      #if last bit is 1 num is odd
    print('odd number')

#ternary operator

print('even' if num & 1 == 0 else 'odd')