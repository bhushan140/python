#spy numbers
#product of numbers is equal to sum of number

# spy = 1124

# sum = sum(int(ch) for ch in str(spy))
# product = 1
# tem = spy
# while tem>0:
#     product*=tem%10
#     tem = tem//10

# if sum == product:
#     print('spy number')

num = 1124
sum = 0
prod = 1
while num>0:
    digi = num%10
    sum += digi
    prod *= digi
    num//=10

print('spy number') if sum == prod else print('not spy')

#prime number

num = 7
count = 0
for i in range(1,num+1):
    if num%i == 0:
        count += 1
if count<=2:
    print('prime')

#factorial of the number
num = 5
fact = 1
for i in range(1,num+1):
    fact*=i
print(fact)

#strong number 
#if sum of  factor of the digi in numbers is equal to the digit

dig = 145
sum_fact = 0
temp = dig
while temp>0:
    digit = temp%10
    fact = 1
    
    for i in range(1,digit+1):
        fact*=i
    
    sum_fact+=fact
    temp//=10
if sum_fact == dig:
    print('strong number')
else:
    print('not strong')

#armstrong number or not
#if sum of digit to the power of number of num in the digit is eqaul to digit

num = 153
power = len(str(num))
sum_of = 0
temp = num
while temp>0:
    dig = temp%10
    sum_of+=dig**power
    temp//=10
if num == sum_of:
    print('armstron')
else:
    print('not armstrong')

#neon number
#sum of digit of squar of the number is equal to number itself
num = 9
squar = num ** 2
sum_squar = 0
temp = squar
while temp>0:
    dig = temp%10
    sum_squar+= dig
    temp//=10

if num == sum_squar:
    print('neon number')
else:
    print('not neon')

#palindrom number

num = 898
temp = num
rev = 0
while temp>0:
    dig = temp%10
    rev = rev*10+dig
    temp =temp//10
if num == rev:
    print('palidrom')
else:
    print('not palidrom')