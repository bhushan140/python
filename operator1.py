#list mulitiplicantion

a = [1,2,3,[1,[1,2]]] *3
a[-1][1].append(9)
print(a)


#arithmetic operators

a = 5
b = 2
print(a/b,a//b,a%b)

#assignment operators

x = 10
x += 3
x *= 2
x -= 4
print(x)

#comparison operators

print(3<4<5)
print(3<4>2)
print(3<4>10)

#logical operators

a = True
b = False
print(a and b or a)

#identity vs equality

x = [1,2,3]
y = [1,2,3]
print(x == y, x is y)

# membership operators

s = 'hello world'
print('wo' in s, 'he' not in s)

# bitwise operators

a = 12
b = 5

print(a&b, a|b,a^b)

#bitwise shift

x = 7
print(x << 2, x>>1)

#operator precedence

print(2 + 3 * 4 **2)

#boolen + integer

print(True + True + False)

#swap to numbers without using a third variable

a = 10
b = 20
a = a^b
b = a^b
a = a^b
print(a,b)

#evaluate the tricky expression

print(10>5 == True) #chained comparison

#operator overloding

print('5' *3)
print([1,2] * 2)

#short - circuit evaluation

def f():
    print('called')
    return True
print(False and f())
print(True or f())

#difference between is and == for small integers

a = 256
b = 256
print(a is b)

a= 257
b = 257
print(a is b)

#operator precedence with not

print(not True == False)

#what is the output

print(~5)

#evalute this expression

print(3 * 3 ** 3 >> 2)