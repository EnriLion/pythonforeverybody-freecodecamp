# print('The chapter6')

# print('Strings')

# name = input('Enter:')

# print(name)

# name = input('Enter: ')

# # x = apple - 10

# x = int(apple) =10

#  print(x)

# print('Looking inside strings')

# fruit = 'banana'

# letter = fruit[1]

# print(letter)

# x = 3

# w = fruit[x-1]

# print(w)

# print('Len function')

# fruit = 'banana'
# print(len(fruit))


# print('Looping through Strings')

# # fruit = 'banana'
# # index = 0

# # while index < len(fruit):
# #     letter = fruit[index]
# #     print(index, letter)
# #     index = index + 1

# fruit = 'banana'
# for letter in fruit:
#     print(letter)

# print('Looping and Counting')

# word = 'banana'
# count = 0
# for letter  in word :
#     if letter == 'a' :
#         count = count + 1
# print(count)

# print("Slicing Strings")

# s = 'Monty Python'
# print(s[0:4])
# print(s[6:7])
# print(s[6:20])
# print(s[:2])
# print(s[8:])
# print(s[:])

# print("String Concatenation")

# a = 'Hello'

# b = a + 'There'

# print(b)

# c = a + ' ' + 'There'

# print(c)

# print("Using 'in' as a logical Operator")

# fruit = 'banana'
# 'n' in fruit
# 'm' in fruit
# 'nan' in fruit
# if 'a' in fruit :
#     print('Found it!')

print('String comparisons')

# word = input('Enter:')

# if word == 'banana' :
#     print('All right, bananas.')
# if word < 'banana' :
#     print('Your word,' + word + ', comes before banana.')
# elif word > 'banana' :
#     print('Your word,' + word + ', comes after banana.')
# else :
#     print('All right, bananas.')

# print('String library')

# greet = 'Hello Bob'
# zap = greet.lower()
# print(zap)
# print(greet)
# print('Hi There'. lower())

# greet = 'Hello Bob'
# type(greet)
# dir(greet)

# print('String Library')

# str.capitalize()
# str.center(width[, fillchar])
# str.endswith(suffix[, start[, end]])
# str.find(sub[, start[, end]])
# str.lstrip([chars]])
# str.replace(old[, new[, count]])
# str.lower()
# str.rstrip([chars])
# str.strip([chars])
# str.upper()

# print('Search and Replace')
# greet = 'Hello Bob'
# nstr = greet.replace('Bob', 'Jane')
# print(nstr)
# nstr = greet.replace('o','X')
# print(nstr)


# print('Search and Replace')

# greet = '  Hello Bob  '
# print (greet.lstrip(), 'space')
# print (greet.rstrip(), 'space')
# print (greet.strip(), 'space')


# print('Prefixes')
# line = 'Please have a nice day'
# line.startswith('Please')
# line.startswith('p')

# print('Parsing and Extracting')

# data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

# atpos = data.find('@')
# print(atpos)

# sppos = data.find(' ', atpos)
# print(sppos)

# host = data[atpos+1 : sppos]
# print(host)

