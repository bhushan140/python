def fact(num):

    if num == 1:
        return 1
    
    return num * fact(num - 1)

print(fact(5))

#inner function
def outer():
    print('in outer function')

    def inner():
        print('in inner function')
    
    return inner

something = outer()

def greet():
    def message():
        print('welcome to python')
    return message

s = greet()
s()

#decorator

def detail(func):
    def wrapper():
        print(f'start: {func.__name__}')
        func()
        print(f'ending: {func.__name__}')
    return wrapper
@detail
def process_data():
    print('processing some data..')
@detail
def uploding_data():
    print('uploding some data')

process_data()
uploding_data()

#lambda

lis = [1,2,3,4,5,6]

result = list(filter(lambda x: x%2 ==0,lis))
print(result)

#find even or odd using bitwise operator

def check_even_odd(nums):
    return 'odd' if nums & 1 else "even"

print(check_even_odd(3))

#counter

from collections import Counter

n = Counter([1,2,3,33,3,3,3,3])
print(n)

#missing number

nums = [1,2,3,5]

n = 5
missing = n* (n +1)//2 - sum(nums)
print(missing)
