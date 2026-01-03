#square pattern

for i in range(3):
    for j in range(3):
        print("*",end='')
    print()

#increasing triangel

for i in range(1,5):
    for j in range(i):
        print('*',end='')
    print()

#number pattern

for i in range(1,4):
    for j in range(1,4):
        print(j,end=" ")
    print()

#matrix traversal

matrix = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end='')
    print()

#what is the output

for i in range(3):
    for j in range(i):
        print(i,j)

#print the pattern

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

#multiplication table

for i in range(1,6):
    for j in range(1,6):
        print(i*j,end='\t')
    print()

#count pairs(i,j)

count = 0
for i in range(5):
    for j in range(5):
        count += 1
print(count)

#print a hollow square
n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*',end=' ')
        else: 
            print(' ',end=' ')
    print()

i = 0
while i < n:
    j = 0
    while j < n:
        if i == 0 or i == n-1 or j == 0 or j == n -1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
        j += 1
    print()
    i += 1

#print a 4x4 solid square using nested loop

for i in range(4):
    for j in range(4):
        print('*',end=' ')
    print()

#print this pattern

for i in range(1,4):
    for j in range(i):
        print('*',end=' ')
    print()

#print numbers in a grid(3x3):

for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
    print()

#print this pattern

for i in range(1,4):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

#print a hollo square of size 5

n = 5
i = 0
while i<n:
    j = 0
    while j<n:
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
        j+=1
    print()
    i+=1

#print this pattern

for i in range(4,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

#hollow rectangle

rows = 4
cols = 8

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#alphabet pattern

for i in range(1,5):
    for j in range(i):
        print(chr(65+ j),end= ' ')
    print()
