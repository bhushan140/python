#weird grading system

m = int(input())

if m < 0 or m >100:
    print('invalid marks')
else:
    if m < 38:
        print(m,'-fail')
    else:
        next_multiple = m + (5 - m % 5)
        if next_multiple - m < 3:
            m = next_multiple
        print(m, '-pass')

#movie ticket pricing(age + time)

age = int(input())
show_time = int(input('enter the show time: '))

if show_time<0 or age <0 or show_time>23:
    print('invalid')
else:
    price = 200
    if age<12:
        price = price-price*50/100
    elif age>= 60:
        price = price- price*40/100

    if 18 <= show_time <= 23:
        price = price+price*20/100

    print('final ticket:',round(price))

#uber fare calculator with surge + waiting

distance_km = float(input())
time_min = int(input())
is_peak = input('enter the yes/no:').lower()
Waiting_min = int(input)    

if distance_km< 0 or time_min < 0 or is_peak<0 or Waiting_min<0 :
    print('Invalid')
else:
    fare = 50 + (10 * distance_km) +(2*time_min)
    
    if Waiting_min>5:
        fare += 3*(Waiting_min-5)
    
    if is_peak == 'yes':
        fare*=1.5
    
    if fare<50:
        fare = 50
    
    print(round(fare))

#Employee bonus system

salary = int(input())
years_of_service = int(input())
performance_rating = input().upper()

if years_of_service < 1:
    print('salary: ',salary)
else:
    base_bonus = salary*0.05*years_of_service
    if base_bonus>salary*0.5:
        base_bonus = base_bonus*0.5

    if performance_rating =='A':
        bonus = base_bonus*1.5
    if performance_rating == 'B':
        bonus = base_bonus*1.2
    if performance_rating == 'C':
        bonus = base_bonus
    else:
        bonus = 0

    print(f'bonus:{bonus}')
    print(f'total bonuse: {bonus+salary}')

#e - commerce shipping and coupon system

cart_total = int(input())
has_coupon = input().lower()
is_prime = input().lower()

if cart_total<0:
    print('invalid')

if has_coupon == 'yes':
    if cart_total >= 500:
        discount = cart_total*0.10
    else:
        discount = 50
    cart_after_discount = cart_total - discount

    if is_prime == 'yes':
        shipping = 0
    else:
        if cart_total>=1000:
            shipping = 0
        else:
            shipping = 100

    final_amount = cart_after_discount+shipping
    print(f'final amount: {final_amount},discount: {discount}')

#exam malpractice decision

marks = int(input())
cheating = input().lower()
severity = input().lower()

if cheating == 'no':
    if marks >= 90:
        print('distinction')
    elif marks>= 60:
        print('pass')
    else:
        print('fail')
elif cheating == 'yes':
    if severity == 'low':
        marks -= 20
    elif severity == 'medium':
        marks = 0
    elif severity == 'high':
        print('Disqualified')
        marks = None
    else:
        print('invalid data')

print(f'final marks:{marks}')

#multi - level login system

username = input()
password = input()
otp = int(input())

fali = 0
for i in range(3):
    if username != 'admin':
        fali+=1
        print('invalid username')
    elif password != 'Secret@123':
        fali+=1
        print('invalid password')
    elif otp != '4567':
        fali+=1
        print('invalid otp')
    else:
        print('login successful')
        break

    if fali == 3:
        print('account locked')
        break