def hello():
    print('hi')

def bye():
    print('se yo')

function = 'bye'
globals()[function]()

#write a program to check if a number is even or odd using conditionals

num = 2

if num % 2 == 0 :
    print('even')
else:
    print('odd')

#print the sum of difits of a given number using a loop

num = 123
sum = 0

for i in str(123):
    sum += int(i)

print(sum)

#write a program to reverse a strin without using slicing

stri = 'abcd'
rev = ''

for i in stri:
    rev = i + rev

print(rev)

#find the largest of three numbers using nested if

num1,num2,num3 = 3,3,3
lar = num1

if num1>=num2: 
    if num1>num3:
        lar = num1
    else:
        lar = num3
else:
    if num2 >=num3:
        lar = num2
    else:
        lar = num3

print(f'largest = {lar}')

#generate the first 10 fibonacci numbers using a loop

a,b = 0,1
n = 10
for _ in range(10):
    print(a,end=",")
    a,b = b,a+b
print()

#write a function to check if a string is a palindrome

def check_palindrome(a):
    return a == a[::-1]

stri = 'toot'
print(check_palindrome(stri))

#implement a program to count the frequency of each word in a sentence using a dictionary

sen = 'python is good lang and python'

s = sen.split()

d = {}
for word in s:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)

#write a function that returns the second largest number in a list

num_list = [3,5,19,199,399,37]

def sec_lar(a):
    first =  float('-inf')
    second = float('-inf')
    for num in a :
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second
    
print(sec_lar(num_list))

# implement a program to merge two sroted list one sorted list

def merge_sorted_lists(list1,list2):
    i, j = 0,0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

lis1 = [1,2,3,4,23,32]
lis2 = [3,4,6,74]

print(merge_sorted_lists(lis1,lis2))

#write a function to calculate the factorial of a number using recursion

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(5))

#create a Bankaccount class with methods deposit.withdraw,and check_balance

class Bankaccount:
    def __init__(self,name,balance):
        self.name = name
        self.__bal = balance

    def depo(self,ammount):
        if ammount >0:
            self.__bal += ammount
        else:
            print('invalid')
    
    def withdraw(self,ammount):
        if ammount < self.__bal:
            self.__bal -= ammount
        else:
            print('invalid')

    @property
    def check_balance(self):
        return self.__bal
    
user = Bankaccount('bhushan',10000)
user.depo(1009)
user.withdraw(10000)
print(user.check_balance)

#write a program to read a file and count the number of lines, words , and charcters

try:
    with open('notes.txt','r') as f:
        r = f.readlines()
        f.seek(0)
        w = f.read()

        wo = w.split()
        print(len(wo))
        print(len(r))
        ch = 0
        for i in w:
            ch += 1
        print(ch)
except Exception as e:
    print(e)

#implement a decorator that logs the execution time of a function

import time

def cal(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(f'time : {end - start:.6f} secounds')
    return wrapper

@cal
def a():
    time.sleep(1)
    print('hello')
a()

#write a closure that generates a function to multiply numbers by a fixed factor

def multipler(factor):
    def multiple_by(num):
        return factor * num
    return multiple_by

tiem3 = multipler(3)
print(tiem3(10))

#tracffic signal state machine

states = ['red','green','yellow']

def traffic_signal(cycles = 3, delay = 1):
    state_index = 0

    for _ in range(cycles * len(states)):
        current_state = states[state_index]
        print(f'signal: {current_state}')
        time.sleep(delay)

        state_index = (state_index + 1) % len(states)

traffic_signal(cycles=2)

#write a program to check if two strings are anagrams without using bulit-in function like sorted()

def is_anagrams(s1,s2):
    # if the len is dif they cant be anagram

    if len(s1) != len(s2):
        return False
    
    #dictionary to count characters

    freq1 = {}
    freq2 = {}

    #count character in s1

    for ch in s1:
        freq1[ch] = freq1.get(ch,0) +1

    #count character in s2

    for ch in s2:
        freq2[ch] = freq2.get(ch,0) + 1

    return freq1 == freq2

print(is_anagrams('listen','silent'))
print(is_anagrams('hello','world'))


#given a list of integers,find all pairs that sum to a targert value

def find_pair_bruteforce(num,target):
    pairs = []
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i] + num[j] == target:
                pairs.append((num[i],num[j]))
    return pairs

print(find_pair_bruteforce([1,2,3,4,5],6))

#- Implement a function to generate all permutations of a string.

def permute(s, step=0):
    if step == len(s):
        print("".join(s))   # base case: one permutation
    else:
        for i in range(step, len(s)):
            # swap current index with step
            s_copy = [c for c in s]
            s_copy[step], s_copy[i] = s_copy[i], s_copy[step]
            # recurse on next step
            permute(s_copy, step+1)

# Example
permute(list("abc"))