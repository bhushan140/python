#secound largest number in the list using function

def sec_lar(a = []):

    lst = a
    lar = a[0]
    sec = a[0]
    for i in lst:
        if i>lar:
            sec = lar 
            lar = i
        elif i<sec and i != lar:
            sec = i
    return sec

print(sec_lar([1,2,3,4,5]))

#write a function is_sorted(lst) that returns true/false

def is_sorted(lst):

    sort = True
    for i in range(1,len(lst)-1):
        if lst[i]>lst[i+1]:
            sort = False
    if sort:
        return True
    else:
        return False
    
print(is_sorted([1,2,3,5,3]))

#write a function that takes *args and returns the maximum

def maximum(*args):

    maxi = args[0]
    for i in args:
        if i > maxi:
            maxi = i
    return maxi

print(maximum(1,2,3,4,5))

#docstring 

def test(a,b):
    """
    Docstring for test
    
    :param a: first number
    :param b: secound number
    retrun: sum of two
    """
    return a+b

print(test.__doc__)
print(test(2,4))

#write a function is_even(n) that returns true if a number is even,else false

def is_even(n):

    if n % 2== 0:
        return True
    else:
        return False
    
print(is_even(3))

#write a function factorial(n) that calculates the factorial of number using recursion

def factorial(n):

    fact = 1
    for i in range(1,n):
        fact += fact*i
    return fact

print(factorial(5))

#write a function reverse_string(s) that returns the reversed string

def reverse_string(s):
    return s[::-1]

print(reverse_string('i hello'))

#write a function sum_list(lst) that return the sum of all elements in a list

def sum_list(lst):

    sum = 0
    for i in lst:
        sum+=i
    return sum

print(sum_list([1,2,3,4]))

#write a function max_of_three(a,b,c) that returns the largest of three numbers

def max_of_three(a,b,c):

    if a>b>c:
        return a
    elif b>a>c:
        return b
    else:
        return c
    
print(max_of_three(4,5,1))

#write a function is_palindreome(s) that checkd if a sting is a palindrome

def is_palindrome(s):

    if s == s[::-1]:
        return True
    else:
        return False
    
print(is_palindrome('heeh'))

# write a function count_vowels(s) that counts the number of vowels in a string

def count_vowels(s):
    
    count = 0
    vowels = 'aeiou'
    for i in s:
        if i in vowels:
            count += 1
    return count

print(count_vowels('hi its python vowels'))

#write a function unique_elsements(lst) that returns a list of unique elements

def unique_elements(lst):
    
    return set(lst)

print(list(unique_elements([1,2,3,4,4,4,4,])))

#write a function fibonacci(n) that returs the first n fibonacci numbers

def fibonacci(n):

    a = 0
    b = 1

    for i in range(1,n):
        print(a,end=' ')
        c = a
        a = b
        b = c+b

fibonacci(10)

#write a function prime_numbers(limit) that returns all prime numbers up to a given limit

def prime_numbers(limit):

    prime = []
    
    for num in range(2,limit+1):
        for j in range(1,num+1):
            if num % j == 0:
                break
        else:
            prime.append(num)
            
    return prime

print(prime_numbers(100))


#write a fuction word_frequency(text) that returns a dictionary of word counts

def word_frequency(text):

    d = {}
    for word in text.split():
        if word not in d:
            d[word] = 1
        else:
            d[word]+=1
    return d

print(word_frequency('hi hi hi hi'))

#write a function matrix_tranpose(matrix) that returns the transpose of a 2d list

def matrix_transpodse(matrix):
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end='')
        print()

(matrix_transpodse([[1,2,3],[1,2,3],[1,2,3]]))

#write a function longest_word(sentence) that returns the longest word in a sentence

def longest_word(sentence):

    lst = sentence.split()
    longest_word = lst[0]

    for word in lst:
        if len(word) > len(longest_word):
            longest_word = word
        
    return longest_word

print(longest_word('hi hello'))

#write a function anagram(s1,s2) that checkes if two strings are anagrams

def anagram(s1,s2):
    
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(anagram('hi ','ih '))


#write a function flatten_list(nested_list) that flattens a list of lists into a single list

def flatten_list(nested_list):
    return [num for i in nested_list for num in i]

print(flatten_list([[1,2,3],[4,5,6]]))

#write a function find_duplicated(lst) that returns all duplicate elements in a list

def find_duplicated(lst):
    seen = set()
    dup = []
    for i in lst:
        if i in seen:
            dup.append(i)
        else:
            seen.add(i)
    return dup

print(find_duplicated([1,2,3,4,4,5,3,5]))

#rotate list

def rotate_list(lst,k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_list([1,2,3,4,5],k = 2))

#factorial using recurtion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

