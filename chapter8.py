# print("List Constants")

# # print([1, 24, 76])
# # print(['red', 'yellow', 'blue'])
# # print(['red', 24, 98.6])
# # print([ 1, [5,6], 7])
# # print([])


# print("We already use lists!")

# for i in [5, 4, 3, 2, 1] :
#     print(i)
# print('Blastoff!')

# print('Lists and definite loops - best pals')

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends :
#     print('Happy New Year:', friend)
# # print('Done!')

# z = ['Joseph', 'Glenn', 'Sally']
# for x in z:
#     print('Happy New Year:', x)
# print('Done!')


# print('Looking inside Lists')

# friends = ['Joseph', 'Glenn', 'Sally']
# print(friends[1])

# print('Lists are Mutable')

# fruit = 'Banana'
# # fruit[0] = 'b'

# x = fruit.lower()
# print(x)

# lotto = [2, 14, 26, 41, 63]
# print(lotto)
# lotto[2] = 28
# print(lotto)

# print("How Long is a List?")

# greet = 'Hello Bob'
# print(len(greet))
# x = [ 1, 2, 'joe', 99]
# print(len(x))


print("Using the range function")

# print(range(4))

# friends =['Joseph', 'Glenn', 'Sally']
# print(len(friends))
# print(range(len(friends)))

# print('A tale of two loops...')

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends :
#     print('Happy New Year:', friend)

# for i in range(len(friends)) :
#     friend = friends[i]
#     print('Happy New Year:', friend)
# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends :
#     print('Happy New Year:', friend)

# print(len(friends))

# print(range(len(friends)))

# print('Concatenating lists using ')

# a = [1, 2, 3]
# b = [4 ,5, 6]
# c = a+b
# print(c)
# print(a)


# print('Lists can be sliced using:')

# t = [9, 41, 3, 74, 15]
# print(t[1:3])
# print(t[:4])
# print(t[3:])
# print(t[:])


# print('List Methods')

# x = list()
# print(type(x))
# print(dir(x))

# print('List Methods')

# stuff = list()
# stuff.append('book')
# stuff.append(99)
# print(stuff)
# stuff.append('cookie')
# print(stuff)



# print('Is Something in a List?')

# some = [1, 9, 21, 10, 16]

# print(9 in some)
# print(15 in some)
# print(20 not in some)


# print('Lists are in Order')

# friends = ['Joseph', 'Glenn', 'Sally']
# friends.sort()
# print(friends)
# print(friends[1])

# print('Built-in Functions and Lists')
# nums = [3, 41, 12, 9, 74, 15]


# print(len(nums))

# print(max(nums)) 

# print(min(nums))

# print(sum(nums))

# print(sum(nums)/len(nums))


# total = 0
# count = 0
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     total = total + value
#     count = count + 1

# average = total / count
# print('Average:', average)


#There is the other way to do it with list() functions

# numlist = list()
# while True :
#     inp = input('Ente a numer: ')
#     if inp == 'done' : break 
#     value = float(inp)
#     numlist.append(value)

# average = sum(numlist) / len(numlist)
# print('Average:', average)

print('Best Friends: Strings and Lists')

abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

print("\n")
for w in stuff:
    print(w)

print("\n Another example")

line = 'A lot             of  spaces'
etc = line.split()
print(etc)

line = 'first;second;third'

thing = line.split()

print(thing)

print(len(thing))

thing = line.split(';')

print(thing)

print(len(thing))


print('\nAnother example using emails')

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])
# ////////////////////


print('\nAnother example spliting an email')

line = 'From stephen.marquard@uxt.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words)

