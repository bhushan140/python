#greeating example

def outer(name):
    def inner():
        return (f'helllo, {name}!')
    return inner()

print(outer('bhushan'))

#sum calcualtor

def sum(a,b):
    c=3
    def inner():
        return a+b+c
    return inner()

print(sum(1,2))

#closure with multiplier

def multiplier(n):
    def inner(x):
        return x *n
    return inner

time5 = multiplier(5)
print(time5(10))

time2 = multiplier(2)
print(time2(10))

time3 = multiplier(3)
print(time3(10))

#counter function

def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

c = counter()
print(c())

#returning two functions

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    def reset():
        nonlocal count
        count = 0
        return count
    
    return increment, reset

#usage

inc,reset = counter()
print(inc())
print(inc())
print(reset())
print(inc())

#single function with command

def counter():
    count = 0
    def inner(command = 'inc'):
        nonlocal count
        if command == 'inc':
            count += 1
            return count
        elif command == 'reset':
            count = 0
            return count
    return inner

c = counter()
print(c())
print(c())
print(c('reset'))
print(c)

#object like 

def counter():
    count = 0
    def inner(aciton = 'inc'):
        nonlocal count
        if aciton == 'inc':
            count += 1

        elif aciton == 'reset':
            count = 0
        return count
    return inner

c = counter()
for _ in range(3):
    print(c())

print(c('reset'))
print(c())

#function factory

def operation_factory(op):
    def inner(a,b):
        if op == '+':
            return a+b
        elif op == '-':
            return a-b
        elif op == '*':
            return a*b
    return inner

sum = operation_factory('+')
print(sum(2,5))

#decotator with nested function

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(start)
        print(end)
        print(f'execution time: {end-start:.5f} seconds')
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return 'done!'

print(slow_function())

#modified decorator

import functools

def timer(func):
    @functools.wraps(func)

    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'function {func.__name__} executed in {end-start:.5f} seconds')  
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    return 'done!'

print(slow_function())

#state machine toggle create a nested function that toggles between 'on' and 'of' each time it's called

def toggle_machine():
    state = 'off'

    def toggle():
        nonlocal state
        state = 'on' if state == 'off' else 'off'
        return state
    
    return toggle
switch = toggle_machine()
print(switch())
print(switch())
print(switch())  

#example 2

def traffic_light():
    states = ['red','green','yellow']
    index = 0

    def next_state():
        nonlocal index
        index = (index+1) % len(states)
        return states[index]
    
    return next_state

ligth = traffic_light()
print(ligth())
print(ligth())

#memorization with nested function

def fib():
    cache = {}
    def inner(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            cache[n] = n
        else:
            cache[n] = inner(n-1) + inner(n-2)
        return cache[n]
    return inner
    
f = fib()
print(f(10))

#decorator 

def simple_decorator(func):
    def wrapper(*args,**kwargs):
        print('before function runs')
        result = func(*args,**kwargs)
        print(('after function runs'))
        return result
    return wrapper

@simple_decorator
def greet(name):
    print(f'hello,{name}!')

greet('bhushan')

#authentication decorator

def require_login(func):
    def wrapper(user,*args,**kwargs):
        if not user.get('is_logged_in'):
            print('access denied.please log in')
            return None
        return func(user,*args,**kwargs)
    return wrapper

@require_login
def view_profile(user):
    print(f'profile: {user['name']}')

user1 = {'name':'bhushan','is_logged_in': True}
user2 = {'name':'guest','is_logged_in':False}

view_profile(user1)
view_profile(user2)