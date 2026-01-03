#most asked python practical interview questions

#reverse a string without using slicing

def reverse(string):
    rev = ''
    for ch in string:
        rev = ch + rev
    return rev

print(reverse("hello"))

#check if a string is a palindrome

def is_palindrome(string):
    string = string.replace(" ","").lower()
    return string == string[::-1]

print(is_palindrome("madam"))

#find the second largest number in a list

def second_largest(num):
    first = second = float('-inf')
    for i in num:
        if i > first:
            second = first
            first = i
        if i > second and i != first:
            second = i
    return second

lst = [13,43,1.2,12,49,18,100,50]
print(second_largest(lst))

#count frequency of ecah charcter in a string

def frequency(string):
    d = {}
    for ch in string:
        d[ch] = d.get(ch,0)+1
    return d

print(frequency("banana"))

from collections import Counter

text = "banana"
print(Counter(text))

#remove duplicates from a list without using set()

def unique_list(lst):
    seen = []
    for i in lst:
        if i not in seen:
            seen.append(i)

    return seen

lst = [1,2,2,3,4,4,5]
print(unique_list(lst))

#fizzbezz

def fizzbuzz():
    for i in range(1,101):
        if i%3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        
fizzbuzz()

#find missing number in a sequence

def missing(nums):
    n = len(nums) + 1
    
    expected = n * (n+1)//2
    actual_sum = sum(nums)
    return expected - actual_sum

print(missing([1,2,3,5]))

#check if Two strings are anagrams

def anagram(str1,str2):
     
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()


    if len(str1) != len(str2):
        return False
   
    return sorted(str1) == sorted(str2)

print(anagram("listen ","Silent"))

#factorial without recursion

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact

print(factorial(5))

#factorial with recursion

def factorial(n):
    return 1 if n<1 else n*factorial(n-1)

print(factorial(5))

#find prime numbers up to N

def prime_number(n):
    primes = []
    for num in range(2,n+1):
        is_prime = True
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

print(prime_number(10))
