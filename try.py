#read the file

with open('students.txt','r') as f:
    lines = f.readlines()

#process data into a list of tuple(name,score)

students = []

for line in lines:
    name,socre = line.strip().split(',')
    students.append((name,int(socre)))

#find the highest and lowest
print(students)

highest = max(students, key=lambda x : x[1])
lowest = min(students, key=lambda x : x[1])

#calculate average

total_score = sum(socre for _, socre in students)
average = total_score/len(students)

with open('result.txt','w') as f:
    f.write(f'highest: {highest[0]} ({highest[1]})\n')
    f.write(f'lowest: {lowest[0]}({lowest[1]})\n')
    f.write(f'average: {average: .1f}\n')


with open(r'C:\Users\Bhushan\OneDrive\Desktop\pyton\hello.txt ','r') as f:
    print(f.read())

import sys

data = [1,23,4,3]

print(sys.getsizeof(data))

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    name = 'user'

print('heloo',name)

print(not True)