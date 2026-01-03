def outer():

    print('hello')
    def inner():
        print('hi')
        return 'hi'
    return inner()

print(outer())

def decorator(func):
    def wrapper(*args,**kwargs):
        print('before function')
        func(*args,*kwargs)
        print('after function')
    return wrapper

@decorator
def hello(name):
    print('hello!',name)

hello('bhushan')

def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
        return x
    return inner()

print(outer())

#closures 
#inner function remember outer variables

def outer(x):
    def inner(y):
        return x +y
    return inner

add5 = outer(5)
print(add5(10))

#reverse string recursively

def rev(s):
    if len(s) == 0:
        return s
    return rev(s[1:]) + s[0]

print(rev('bhushan'))

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

#fibonacci example

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n -2)

print(fib(6))

#passing fuctions as arguments

def square(x):
    return x*x
def apply(func,val):
    return func(val)

print(apply(square,5))