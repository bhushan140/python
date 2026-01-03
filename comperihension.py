#list comprehension
#numbers divisible by 3 or 5

result = [x for x in range(1,101) if x%3 == 0 or x % 5 == 0]
print(result)

#extract digits from a string

s = '1234kskd'

digits = [ch for ch in s if ch.isdigit()]
print(digits)

#reverse each word

sen = 'hi this is python developer'

rev = [w[::-1] for w in sen.split()]
print(rev)

#prime numbers 1 - 100

def is_prime(n):
    return n>1 and all(n%i !=0 for i in range(2, int(n**0.5)+1))
prime = [x for x in range(1,101) if is_prime(x)]
print(prime)

#convert a list of integers into their string equivalents using list comprehension

lst = [1,2,3,4]
st = [str(x) for x in lst]
print(st)

#from a list of words,create a list of words that start with a vowel

w_lst = ['apple','banana','elephant']
vowel = 'aeiou'
o_lst = [w for w in w_lst if w[0] in vowel]
print(o_lst)

#extract all characters from a string except vowels using list comprehension

s = 'python is easy'
lst = [ch for ch in s if ch not in vowel]
print(lst)

#given a list of tuples,extract only the second element of each tuple

lst = [(1,2,3),(4,5,6)]
ex = [s[1] for s in lst ]
print(ex)

#from a list of numbers,replace:
#even numbers 'E' and odd number 'o'

lst = [1,2,3,4,5]
e_o = ['E' if x%2==0 else 'O' for x in lst]
print(e_o)

d = {1:'hi',2:'hello'}
k_v = [f'{k}={v}'for k,v in d.items()]
print(k_v)

#from a list of sentences, extract the first word of each sentence

s_lst = ['hello world','hi everyone']
first = [w.split()[0] for w in s_lst ]
print(first)

#given a list of list,creata a list of the sum of each inner list

nes_list = [[1,2,3],[4,5,6]]
su = [sum(l) for l in nes_list]
print(su)

#flatten a list of lists but only include elements greater than 10

ls = [[1,2,3],[2,3,4]]
fla = [num for l in ls for num in l]
print(fla)

#generate all (i,j) pairs where i is from list A and j is from list B but only if i < j

A =[1,2,3]
B = [4,5,6]

ls = [(i, j) for i in A for j in B if i<j]
print(ls)




#given a list of strings,extract only those strings that contain digits

ls = ['12python','32hi','hello23']
sd = [w for w in ls if w.isalnum()]
print(sd)

#reverse each word in a sentence but keep the word order same using list comprehension

s = 'welcome to python world'
rew = [w[::-1] for w in s.split()]
print(rew)

#given a list of numbers,create a list of (num,num2,num3) tuples

lsnum = [1,2,3]
t_l = [(num,num**2,num**3) for num in lsnum]
print(t_l)

#extract unique charcters from a string using list comprehension + set

stri = 'apple banna'
uniq = set([(ch) for ch in stri])
print(uniq)

#set comprehension
#create a set of squares from 1 to 10

squares = {x*x for x in range(1,11)}
print(squares)

#extract unique vowels from a string

text = 'comprehension interview'
vowel = {ch for ch in text if ch in 'aeiou'}
print(vowel)

#find common elements between two lists using set comprehension

a = [1,2,3,4]
b = [3,4,5,6]
common = {x for x in a if x in b}
print(common)

#create a set of even numbers from a list

nums = [1,2,2,3,4,6,6]
evens = {n for n in nums if n%2 == 0}
print(evens)

#remove duplicates and convert all words to lowercase

words = ['Apple','Banna','apple','Cherry']
uniq_valu = {w.lower() for w in words}
print(uniq_valu)

#set comprehension with nested loops

pairs = {(i,j) for i in range(3) for j in range(3) if i<j}
print(pairs)

#extract uique lengths of words
sentence = 'set comprehension interview'
lengths = {len(word) for word in sentence.split()}
print(lengths)

#flatten a list of list using set comprehension

lst = [[1,2],[2,3],[3,4]]
flat = {x for sub in lst for x in sub}
print(flat)

#dictionary comprehension
#create a dictionary of numbers and their squares

squares = {x:x**2 for x in range(1,6)}
print(squares)

#swap keys and values
data = {'a':1 ,'b':2,'c':3}
swap = {v:k for k,v in data.items()}
print(swap)

#filter dictionary items
nums ={'a':1,'b':2,'c':3}
evens = {k:v for k,v in nums.items() if v%2 == 0}
print(evens)

#convert list to dictionary

names = ['rams','shyam','geeta']
leng = {name:len(name) for name in names}
print(leng)

#count frequency of characters

text = 'banan'
freq = {ch:text.count(ch) for ch in text}
print(freq)

#nested dictionary comprehension

matrix = {i:{j: i*j for j in range(1,4)} for i in range(1,4)}
print(matrix)

#dictionary from two lists

key = ['name','age','city']
values = ['bhushan','age','city']
result = {k:v for k,v in zip(key,values)}
print(result)

#conditional value assignment
nums = range(1,6)
status = {n:('even' if n%2==0 else 'odd') for n in nums}
print(status)

#multiple conditions

filtered = {x: x*x for x in range(20) if x%2 == 0 if x>10}
print(filtered)

#nested loops

pairs = {(i, j): i+j for i in range(3) for j in range(3)}
print(pairs)

