#find the minimum and maximum in a list

lst = [4,9,1,7,3]

minimum = lst[0]
maximum = lst[0]

for i in range(len(lst)):
    if lst[i]>maximum:
        maximum = lst[i]
    if lst[i]<minimum:
        minimum = lst[i]
    
print('min:',minimum)
print('max:',maximum)

#count how many time each element apperas

lst = [1,2,2,2,3,3,3]
freq = {}

for i in lst:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i]+=1
print(freq)

#find the first repeated element in a list
lst = [4,5,2,4,3,5]

seem = set()
first_repeated = None

for i in lst:
    if i in seem:
        first_repeated = i
        break
    seem.add(i)
print('first repeated: ',first_repeated)

#find the sum of even and odd numbers

lst = [1,2,3,4,5,6]

even_sum = 0
odd_sum = 0

for num in lst:
    if num%2 == 0:
        even_sum+=num
    else:
        odd_sum+= num
print('odd sum: ',odd_sum)
print('even sum: ',even_sum)

#check if a string is palindrome using a loop

s = 'madam'
is_palindrome = True

for i in range(len(s) // 2):
    if s[i] != s[-i - 1]:
        is_palindrome = False
        break
print('palindrom: ', is_palindrome)

# find the longest word in a list of words

words = ['apple','banna','kiwi','watermelon']

longest = ''

for word in words:
    if len(word) >len(longest):
        longest = word

print('longest word: ',longest)

#count uppercase and lowercase letters in a string

s = 'HelloWorld'
upper = 0 
lower = 0

for ch in s:
    if ch.isupper():
        upper+=1
    else:
        lower+=1
print(upper,lower)

#find common elements between two lists using loops

a = [1,2,3,4]
b = [3,4,5,6]
common = []

for i in a:
    if i in b:
        common.append(i)
print('common: ',common)

#remove all occurences of a specific elements

lst = [1,2,3,2,4,2]
target = 2

result = []

for i in lst:
    if i != target:
        result.append(i)
print('after removing: ',result)

#find the difference between consecutive elements

lst = [10,7,5,3]

diff = []

for i in range(len(lst)-1):
    diff.append(lst[i]-lst[i+1])

print(diff)

#zip()
#iterate two lists together and print paired values

a = [1,2,3]
b = ['a','b','c']
for a,b in zip(a,b):
    print(a,b)

#add two lists element-wise using zip()

a = [1,2,3]
b = [4,5,6]
c = []
for x,y in zip(a,b):
    c.append(x+y)
print(c)

c = [x+y for x,y in zip(a,b)]
print(c)

#multiply corresponding elements of two lists

a = [2,3,4]
b = [5,6,7]

c = [x*y for x,y in zip(a,b)]
print(c)

#compare two lists and print elements that are equal

a = [1,2,3,4]
b = [1,5,3,8]

for x,y in zip(a,b):
    if x == y:
        print(x,'==',y)

#create a dictionary from two list using zip()

a = [1,2,3,4]
b = ['a','b','c','x','e']
c = {}

for k,v in zip(a,b):
    c[k]=v
print(c)

#unzip a list of tuples using zip(*iterable)
pairs = [(1,'a'),(2,'b'),(3,'c')]

nums,chars = zip(*pairs)

print(nums)
print(chars)

#loop through three lists at the same time 

names = ['A','B','C']
ages = [20,21,22]
cities = ['blr','mum','del']

for a,b,c in zip(names,ages,cities):
    print(a,b,c)

#find the mismatched elements

a = [1,2,3,4]
b = [1,9,3,8]

for x,y in zip(a,b):
    if x != y:
        print(x,'!=',y)

#combine two list into list of tuples

a = [1,2,3]
b = ['x','y','z']

result = list(zip(a,b))
print(result)

#Transpose a matrix using zip

matrix = [
    [1,2,3],
    [4,5,6]
]

transposed = list(zip(*matrix))
print(transposed)

#iterate two strings together

s1 = 'abc'
s2 = '123'

for x,y in zip(s1,s2):
    print(x,y)

#count matching positions in two lists

a = [1,2,3,4]
b = [1,9,3,8]

count = 0

for x,y in zip(a,b):
    if x == y:
        count += 1

print('matches:',count)

#merge two lists into formatted output 

keys = ['name','age']
values = ['bhushan',21]

for k,v in zip(keys,values):
    print(f'{k}:{v}')

#identity list

a = [1,2,3]
b = [1,2,3]

is_same = True

for x,y in zip(a,b):
    if x != y:
        is_same = False
        break
print('identical: ',is_same)

#update selected keys in a dictionary using zip

d = {'name':'old','age':0,'city':'unknown'}

keys = ['name','age']
values = ['bhushan',21]

for k,v in zip(keys,values):
    d[k] = v
print(d)