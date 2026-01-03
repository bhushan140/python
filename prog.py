#write a program to find the second largest number in a list without unsing sorthed()

def secound_largest(nums):
    first = secound = float('-inf')
    for n in nums:
        if n>first:
            secound,first = first,n
        elif n> secound and n != first:
            secound = n
    return secound

print(secound_largest([1,2,3,4,22,33,22,1]))

#check if a list is strictly increasing

def is_strictly_increasing(lst):
    for i in range(len(lst)-1):
        if lst[i]>=lst[i+1]:
            return False
    return True
    
print(is_strictly_increasing([1,2,3,4]))
print(is_strictly_increasing([1,2,2,3]))

#or

def is_strictly_increasing(lst):
    return all(x < y for x,y in zip(lst,lst[1:]))

print(is_strictly_increasing([1,2,3,65]))

#to print all numbers from 1-100

for i in range(1,100):
    if  i %3 == 0 and i % 5 ==0:
        print('fizz-buzz')
    elif i%3 == 0:
        print('buzz')
    elif i%5 == 0:
        print('fizz')
    else:
        print(i)

#reverse a string without using slicing([::-1])

def reverse(stri):
    rev = ''
    for ch in stri:
        rev = ch + rev
    return rev

print(reverse('python'))

#check if two strings are anagrams

def is_anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    
    freq1 = {}
    freq2 = {}

    for i in str1:
        freq1[i] = freq1.get(i,0)+1

    for j in str2:
        freq2[j] = freq2.get(j,0)+1

    return freq1 == freq2

print(is_anagram('asdaa','dsaaa'))

#function 
#implement a decorator that logs the execution time of function

import time

def exe(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'time ={end-start:.2f}')

    return wrapper

@exe
def mess():
    print('hello')

mess()

#stat machine

states = ['red','green','yellow']

def traffic_signal(cycles = 3, delay = 1):
    state_index = 0

    for _ in range(cycles * len(states)):
        current_state = states[state_index]
        print(f'signal: {current_state}')
        time.sleep(delay)

        state_index = (state_index + 1) % len(states)

traffic_signal(cycles=2)


#closer to rember the last  3 value passed to it

def lst_three_closure():
    history = []

    def inner(value):
        nonlocal history
        history.append(value)
        if len(history) > 3:

            history.pop(0)
        return history
    
    return inner
tracker = lst_three_closure()
print(tracker(10))
print(tracker(20))

#reverse words in a string

def reverse_words(s):
    return ' '.join(s.split()[::-1])

print(reverse_words('python is fun'))

#remove duplicates from a list

def remove_duplicates(lst):
    seen = set()
    result = []

    for n in lst:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result

print(remove_duplicates([1,3,3,3,2,2,3]))

#find factorial using recursion

def fact(n):
    return 1 if n ==1 else n*fact(n-1)

print(fact(5))

#find common element in two lists

def common_element(lis1,lis2):
    return list(set(lis1)&set(lis2))

print(common_element([1,2,43,23],[1,2,33,45,5]))

#fibonacci series

def fib(n):
    a,b = 0,1
    series = []
    for _ in range(n):
        series.append(a)
        a,b = b,a+b

    return series

print(fib(10))

#find the first non repeting character

def first_non_rep(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch,0)+1

    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

print(first_non_rep('swiss'))

#rotate a list

def rotate_list(nums,k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

print(rotate_list([2,3,4,5],3))