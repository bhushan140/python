#determine if a number is 'automorphic'
#a number is automorphic if its square ends with the number itself
#ex 5 = 25

num = int(input())
sq = str(num **2)
st = len(str(num))

if int(sq[-st:]) == num:
    print('automorphic')
else:
    print('not automorphic')

#simulate a basic billing system with discounts


bill = int(input())

if bill>5000:
    discount = '20%'
    bill-=bill*20/100
elif bill>3000:
    discount = '15%'
    bill-=bill*15/100
elif bill>1000:
    discount = '10%'
    bill-=bill*10/100
else:
    discount = 'no discount'
    bill = bill
bill_after_discount = bill
discount = discount
print(discount,bill_after_discount)

#classify a persom based on BMI

weight = float(input())
height = float(input())**2

BMI = weight/height

if BMI < 18.5:
    print('underweight')
elif 18.5<BMI<24.9:
    print('Normal')
elif 25<BMI<29.9:
    print('Overweight')
elif BMI>= 30:
    print('Obese')

#determine if a number is 'spy number'
#sum of digit = product of digits

spy = 1124

sum = sum(int(ch) for ch in str(spy))
product = 1
tem = spy
while tem>0:
    product*=tem%10
    tem = tem//10

if sum == product:
    print('spy number')

#simulate a grading system with attendance

attendance = input()

if attendance>=90:
    print('A')
elif attendance>=80:
    print('B')
elif attendance>= 70:
    print('C')
elif attendance<75:
    print('not eligibal')
else:
    print('D')

#pangram checker

s = input().lower()
letters = set()

for ch in s:
    if 'a' <= ch <= 'z':
        letters.add(ch)
if len(letters) == 26:
    print('pangram')
else:
    print('not pangram')

#validate a Date(DD/MM/YYY) - no datatime

date = input('enter the date(dd/mm/yyyy): ')

try:
    d,m,y = map(int,date.split('/'))
    #month check

    if m<1 or m>12:
        print('invalid date')
    else:
        #days in each month
         month_days = [31, 29 if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) else 28,
                      31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if 1 <= d <= month_days[m-1]:
        print('valid date')
    else:
        print('invalid date')
except:
    print('invalid format')

#am/pm compatibility

t1 = input('time 1 (HH:MM): ')
t2 = input('time 2 (HH:MM): ')

h1 = int(t1.split(':')[0])
h2 = int(t2.split(':')[0])

def period(h):
    if h == 12:
        return 'PM'
    elif h == 0:
        return 'AM'
    elif h < 12:
        return 'AM'
    else:
        return "PM"
    
if period(h1) == period(h2):
    print('same period')
else:
    print('different period')

#perfect/Abundent/Deficient Number

n = int(input())

s = 0
for i in range(1,n):
    if n % i == 0:
        s += 1

if s == n:
    print('perfect')
elif s>n:
    print('abundat')
elif s == 1:
    print('prime number')
else:
    print('deficient')

#validate 12 - hour Time format

time = input('enter the (HH:MM AM/PM): ')

try:
    part,mer = time.split()
    h, m = map(int, part.split(":"))
    mer = mer.upper()

    if mer not in ('AM',"PM"):
        print('invalid')
    elif not(1<= h<= 12):
        print('invalid')
    elif not(0<= m <= 59):
        print('invalid')
    else:
        print('valid time')
except:
    print('invalid format')