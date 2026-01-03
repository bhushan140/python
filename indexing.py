s = 'python'
print(s[0])
print(s[-1])

#substring 'yth' form 'python' using slicing.

s = 'python'
print(s[1:-2])

#what happen if you do

# lst = [10,20,30]
# print(lst[5])      ##out of range

#what this slice return

nums = [1,2,3,4,5]
print(nums[1:4])

#revers a string using slicing

s = 'python'
rs = s[::-1]
print(rs)

#what is the output

s = 'interview'
print(s[2:8:2])

#predict the result:

a = [0,1,2,3,4,5]
print(a[-5:-1])

#what does thid produce

s = 'abcdef'
print(s[:])
print(s[::])

#what is the output

lst = [1,2,3,4,5]
print(lst[::-2])

#how do you extract every 3rd charcter from a string

s = '1234567890'
print(s[2::3])

#what is the output

a = 'abcdefgh'
print(a[-2:2:-1])

#explain why this returns an empty list

lst = [1,2,3,4,5]
print(lst[4:1])

#what is the output

s = 'python slicing'
print(s[3:100])

#what is the output

a = [10,20,30,40,50]
a[1:4] = [99]
print(a)

#given 

s = '0123456789'
print(s[::-2])

#explain the logic behind this

lst = [1,2,3,4,5]
print(lst[10:2:-1])
print(lst[None:None])

#what is the output

s = 'banana'
print(s[s.index('n'): s.rindex('n')+1])

#whithout using loops, extract all vowels from a string using slicing+indexing tricks

s = 'beautiful day in bengaluru'
vowels = ''.join(filter('aeiouAEIOU'.__contains__,s))
print(vowels)

#given nested list extract the diagonal
x = [[1,2,3],[4,5,6],[7,8,9]]
dig = [x[i][i] for i in range(len(x))]
print(x[:2])
print(dig)

#slicing 

lst = [1,2,3,4,5,6]
print(lst[3:3])
print(lst[3:3:-1])

#indexing

s = ['python','java','c']
print(s[1][-1])