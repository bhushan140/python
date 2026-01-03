#print all even numbers from 1 to 100 using loop

for i in range(1,10):
    if i % 2 == 0:
        print(i)

#count the number of vowels in a string using a loop

strign = 'aeiou'
count = 0
for i in strign:
    if i in 'aeiou':
        count+=1
    
else:
    print(count)

#reverse a string using a loop

strn = 'i love python'
rev = ''
for i in range(len(strn)-1,-1,-1):
    
    rev += strn[i] 
print(rev)

#find the factorial of a number using a loop

num = 5
fact = 1
for i in range(1,6):
    fact*= i
else:

    print(fact)

#print a pattern like

for i in range(1,4):
    print('*'*i)

#check if a number is prime using a loop

num = 10
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count += 1
if count<=2:
    print('prime number')
else:
    print('not prime')

#remove duplicate from a list using a loop

lst = [1,2,3,2,2,2,2]
relst = []

for v in lst:
    if v not in relst:
        relst.append(v)
print(relst)

#flatten a nested list using loop

lst = [[1,2,4],[1,2,4]]
flaten = []
for v in lst:
    for i in v:
        flaten.append(i)
print(flaten)

#write a loop to find the secound largest number in a list

lst = [1,2,4,4,5,5]

lar = float()
sec = float()

for num in lst:
    if num>lar:
        sec = lar
        lar = num
    elif num<sec and num != lar:
        sec = num
print(sec)


#print all number divisible by 3 and 5 between 1 and 100

i = 1
while i<=100:
    if i %3 == 0 and i % 5 == 0:
        print(i)
    i += 1
    
#count how many digits,letters and special characters are in a string

st = '@123python'
dcount = 0
lcount = 0
spcount = 0

for ch in st:
    if ch.isdigit():
        dcount+=1
    elif ch.isalpha():
        lcount += 1
    else:
        spcount +=1
        
print(dcount,lcount,spcount)

#find the largest and second largest number in a list

lst = [1,2,3,4,5]
larg = float()
secr = float()

for i in lst:
    if i>larg:
        secr = larg
        larg = i
    elif i<secr and i !=larg:
        secr = i

print(secr)

# reverse a string without using slicing

stri = 'python is powerfull lang'
revs = ''
for i in stri:
    revs = i + revs
print(revs)

#check if a number is prime using a loop

n = 7
count = 0
for i in range(1,n+1):
    if n%i == 0:
        count+=1
if count==2:
    print('prime')
else:
    print('not prime')

#count vowels and consonants in a string

st = 'a apple is a fruits'
v_count = 0
c_count = 0

for ch in st:
    if ch in 'aeiou':
        v_count+=1
    elif ch.isalpha():
        c_count+=1
print(v_count,c_count)

#sum of digits of a number

n = 1234
sum = 0
while n>0:
    digit = n%10
    sum+=digit
    n//=10
print(sum)

#print fibonacci series up to N terms

n = 10
a = 0
b = 1
for i in range(n):
    print(a,end=' ')
    c = a
    a = b
    b = c+a

#find the frequency of each character in a string

string = 'i have a pen in my hand'
d = {}
for ch in string:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch]+=1
print(d)

#find the sum of all elements in a list without using sum()

lst = [1,2,3,4,5]
sum = 0
for i in lst:
    sum+=i
print(sum)

#print numbers from 1 to 50 but skip multiples by 7

for num in range(1,51):
    if num % 7 == 0:
        continue
    print(num)

#stop the loop when the number 13 apperas in the list

for num in range(15):
    if num == 13:
        break
    print(num)

#print the index and value of each element in a list

lst = ['10','30','20','69']

for i , v in enumerate(lst):
    print(i,v)
else:
    print(i+1,int(v)+1)

#find the product of all numbers in a list

lst = [1,2,4,5]
prod = 1
for i in lst:
    prod*=i
print(prod)

#print the pattern
rows = 5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end='')
    print()

#write a loop to check if a list is sorted

lst = [1,2,3,4,5]
short = True

for i in range(len(lst)-1):
    
    if lst[i]>lst[i + 1]:
        short = False
        break
if short:
    print('short')
print(i)