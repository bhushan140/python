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

#harshas number

n = int(input())

s = sum(int(d) for d in str(n))

if n % s == 0:
    print('harshas number')
else:
    print('not harshed')

#kaprekar number

n = int(input())
sq = str(n*n)
l = len(str(n))

right = int(sq[-l:]) if sq[-l:] else 0
left = int(sq[:-l]) if sq[:-l] else 0

if left + right == n:
    print('kaprekar')
else:
    print('not kaprekar')

#mini calculator

a = float(input())
b = float(input())
op = input()

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a*b)
elif op == '/':
    try:
        a/b
    except ZeroDivisionError:
        print('cant divid by zero')
    else:
        print(a/b)
else:
    print('invalid')

#almost strong password

pwd = input()
rules_failes = 0

if len(pwd) < 8:
    rules_failes += 1
if not any(ch.isupper() for ch in pwd):
    rules_failes += 1
if not any(ch.islower() for ch in pwd):
    rules_failes += 1
if not any(ch.isdigit() for ch in pwd):
    rules_failes += 1
if not any(ch in '!@#$%^&*()-_+=[]{}:;' for ch in pwd):
    rules_failes += 1

if rules_failes == 0:
    print('strong')
elif rules_failes == 1:
    print('almost strong')
else:
    print('week')    