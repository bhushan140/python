file = open('notes.txt','w')
con = file.writelines('line1,\nline2,\nline3')

file.close()

with open('notes.txt','r') as f:
    con = f.read()
    print(con)
    print(f.tell())

#read 

with open('hello.txt','w') as f:
    f.write('hello python')

with open('hello.txt','r') as f:
    cont =f.read()

lis = cont.split()
print(len(lis))

#append

with open('notes.txt','a') as f:
    f.write('\nthis is an extra line')

with open('notes.txt','r') as f:
    count = f.readlines()
    print(len(count))

#numbers.txt

try:
    with open('numbers.txt','w') as f:
        f.write('1\n2\n\n3')
    with open('numbers.txt','r') as f:
        num = f.readlines()
        som = sum(num)
        avg = som/len(som)
    with open('numbers.txt','w') as f:
        f.write(som,avg)
except (FileNotFoundError, TypeError) as e:
    print(e)

#copying a data into new file

with open('source.txt','r') as src:
    data = src.read()

with open('copy.txt','w') as dest:
    dest.write(data)

#read a file and count the word

count = 0 
with open('paragraph.txt','r') as f:
    for line in f:
        words = line.split()
        count += words.count('python')

print('occurences of python :',count)

#remove duplicate line

with open('input.txt','r') as f:
    lines = f.readlines()

un_l = list(set(lines))

with open('unique.txt','w') as f:
    f.writelines(un_l)

with open(r'C:\Users\Bhushan\OneDrive\Desktop\pyton\hello.txt ','r') as f:
    print(f.read())