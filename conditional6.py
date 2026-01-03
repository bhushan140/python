#railway ticket booking system

pas_age = int(input())
gender = (input())
travel_cls = input()
s_cititz = input().lower()
t_booking = input().lower()

#base fares:

if travel_cls == '1AC':
    base_fare = 2000
elif travel_cls == '2AC':
    base_fare = 1500
elif travel_cls == 'sleeper':
    base_fare = 800

#senior citizen:

if s_cititz == 'yes':
    if gender == 'male' and pas_age>=60:
        s_discount =  base_fare*0.40
    elif gender == 'female' and pas_age>=58:
        s_discount = base_fare*0.50

#tatkal booking:

if t_booking == 'yes':
    t_discount=base_fare*.30
else:
    t_discount = 0

#children:

if pas_age<5:
    c_discount = 0
elif 5<pas_age<12:
   c_discount=base_fare*.50


if 5<pas_age<12:
    base_fare -= c_discount
    print('final fare:',base_fare)
    exit()
elif pas_age <5:
    base_fare -= c_discount
    print('final fare:',base_fare)
    exit()


if t_booking == 'yes':
    base_fare += t_discount
if s_cititz == 'yes':
    base_fare -= s_discount
print('final price:',base_fare)


#collage admission system

per = float(input('enter your 12th percentage: '))
score = int(input('enter your entrance exam score: '))
category = input('enter category(general/obc/sc/st): ').lower()
sports = input('sports quota(yes/no): ').lower()

#sports quota
if sports == 'yes':
    per = per+5

#minimum eligibility

if category == 'general' and per >= 75:
    eligibility = True
elif category == 'obc' and per >= 70:
    eligibility = True
elif (category == 'sc' or category == 'st') and per>=65:
    eligibility = True
else:
    eligibility = False

#entrance exam score:
 
if score <50:
    eligibility = False

if eligibility :
    if per + score >= 140:
        print('selected')
    else:
        print('waitlist')
else:
    print('rejected')
