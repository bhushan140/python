#convert this list of strings to integers

data = ['10','20','30']

ints = list(map(int,data))
print(ints)

#convert this nested list to flat list

data = [[1,2],[3,4],[5]]
flat = []
for sub in data:
    for x in sub:
        flat.append(x)
print(flat)

#using sum
flat = sum(data,[])
print(flat)

#list comprehension

flat =[x for sub in data for x in sub]
print(flat)

#convert list to dictionary

pairs = [('a',1),('b',2),('c',3)]
print(dict(pairs))

# using loop

d = {}
for k,v in pairs:
    d[k] =v

print(d)

#convert two separete list to dict

keys = ['a','b','c']
values = [1,2,3]

d = dict(zip(keys, values))

# to remove duplicates while preserving order

items = [1,2,3,3,3,4,8,7,3]
seen = set()
listed = []

for x in items:
    if x not in seen:
        seen.add(x)
        listed.append(x)

print(listed)

#using dict

result = list(dict.fromkeys(items))
print(result)

#predict the output
a = True + True + False
print(a)

#what is the output

s = '123'
print(type(int(s)))
print(type(s))

#convert the list to set

nums = [1,2,3,3,3,2]
print(set(nums))
print(nums)

# s = {[1,2,4],4}

# what is the output

t = (1,2,[3,4])
t[2].append(5)
print(t)

#what is the output

a = (1,2,3)
b = (1,2,3)
print(a is b)

#what is the output

x = 256
y = 256
print(x is y)

x = 1000
y = 1000
print(x is y)

#what is the output
print([] == [])
print([] is [])

#what is the output

x = 'python'
print(id(x))
x += '3'
print(id(x))
print(x)

# what is the difference

a = (1,2,3)
b = tuple([1,2,3])
print(b is a)
print(a == b)