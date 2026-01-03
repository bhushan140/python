#determine the type of a password

pwd = input()

has_upper = any(ch.isupper() for ch in pwd)
has_lower = any(ch.islower() for ch in pwd)
has_digit = any(ch.isdigit() for ch in pwd)
has_special = any(ch in '!@#$%^&*()_+:"?' for ch in pwd)
only_letter = pwd.isalpha()

if len(pwd)>=12 and has_lower and has_upper and has_special and has_digit:
    print('very strong')
elif has_special and has_digit and has_upper and has_lower:
    print('strong')
elif has_digit and has_lower or has_upper:
    print('medium')
elif only_letter:
    print('week')
else:
    print('invalid')

#simualte a simple Banking system

current_balance = int(input('enter the balance: '))
print('1.deposit\n2.withdraw')
chois = input('enter your choose: ')

if chois == '1':
    print('as you want to deposit')
    amount = int(input('enter the amount to deposit: '))
    if amount>0:
       print('depositing your amount')
       current_balance += amount
       print(f'balance after deposit: {current_balance}')
    else:
        print('invalid')
elif chois == '2':
    print('as you want to withdraw')
    amount = int(input('enter the amount to withdraw: '))
    if 0<amount<= current_balance:
        print('withdrawing your amount')
        current_balance-=amount
        print(f'balance after withdraw: {current_balance}')
    else:
        print('invalid')
else:
    print('invalid choise')

#parking lot fee system

hours = int(input())

if hours < 0:
    print('invalid hours')
else:
    if hours<2:
        fee = 50
    elif hours<=5:
        fee = 50 + (hours-2)*30
    else:
        fee = 50 + 3 * 30 + (hours - 5) *20
    
    if fee > 500:
        fee = 500
    print('parking fee: ',fee)

#anagram - compatible strings

s1 = input().replace(' ','').lower()
s2 = input().replace(' ','').lower()

valid = True

# check for special characters

for ch in s1 + s2:
    if not (ch.isalpha()):
        valid = False
        break

if not valid:
    print('invalid input')
else:
    unique1 = ''
    unique2 = ''

    for ch in s1:
        if ch not in unique1:
            unique1 += ch
    
    for ch in s2:
        if ch not in unique2:
            unique2 += ch

    if sorted(unique1) == sorted(unique2):
        print('Anagran Compatible')
    else:
        print('not compatible')

#evil or odious number(no bin())

n = int(input())
 
count = 0
x = n
while x > 0:
    if x % 2 == 1:
        count += 1
    x //= 2
if count % 2 == 0:
    print('Evil number')
else:
    print('odious number')

#classify an ip address

ip = input().split('.')

if len(ip) != 4:
    print('invalid ip')
else:
    valid = True
    nums = []

    for part in ip:
        if not part.isdigit():
            valid = False
            break
        n = int(part)
        if n < 0 or n>255:
            valid = False
            break
        nums.append(n)
    if not valid:
        print('invalid ip')
    else:
        first = nums[0]
        if 1<=first<= 126:
            print('class A')
        elif 128<= first<= 191:
            print('class B')
        elif 192 <= first <= 223:
            print('Class C')
        elif 224 <= first <= 239:
            print('class D')
        elif 240 <= first <= 255:
            print('class E')
        else:
            print('invalid ip')

#Rock-paper-scissors winner

p1 = input().lower()
p2 = input().lower()

choices = ['rock','paper','scissors']

if p1 not in choices or p2 not in choices:
    print('invalid choise')
elif p1 == p2:
    print('draw')
elif (p1 == 'rock' and p2 == 'scissors') or \
     (p1 == 'paper' and p2 == 'rock') or  \
     (p1 == "scissors" and p2 == 'rock'):
    print('player 1 win')
else:
    print('player 2 win')