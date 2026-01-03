#lambda function is a anoymous function which accepts multiple arguments and has only one expresion

#square numbers with map

lst = [1,2,3,4]
sqr = map(lambda x: x*x,lst)
print(list(sqr))

#filter even numbers

lst = [2,4,5,6,7,8]
even_num = filter(lambda x : x % 2 == 0, lst)
print(list(even_num))

#sort words by length using lamba

words = ['apple','kiwi','banana','grape']
sort_word = sorted(words,key=lambda w: len(w))
print(sort_word)

#filter palindromes

lst = ['madam','apple','racecar','python']
palindrom = filter(lambda x: x ==x[::-1],lst)
print(list(palindrom))

#map to extract first character of each word

lst = ['hello','world','python']
first_ch = map(lambda x: x[0],lst)
print(list(first_ch))

#filter numbers divisible by both 3 and 5

x = range(1,51)
fizzbuzz = filter(lambda x: x%3 == 0 and x%5 == 0,x)
print(list(fizzbuzz))

#sort list of tuples by secound element

lst = [(1,5),(2,3),(4,1)]
sort_lst = sorted(lst, key= lambda x: x[1])
print(sort_lst)

#filter words containin vowels only

lst = ['aeiou','sky','queue','try']
only_ovel = filter(lambda x : all(ch in 'aeiou' for ch in x.lower()),lst)
print(list(only_ovel))

#filter perfect squares
import math
nums = range(1,51)

perfect_squar = filter(lambda x: int(math.sqrt(x))**2 == x,nums)
print(list(perfect_squar))