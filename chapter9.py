print('Dictionaries')

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse)


print('Comparing Lists and Dictionaries')

print('\n','Lists')
lst = list()
lst.append(21)
lst.append(183)
print(lst)
lst[0] = 23
print(lst)

print('\n','Dictionaries')
ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)

print('\n','Dictionary Literals(Constants)')

jjj = {'chuck' : 1,  'fred' : 42, 'jan' : 100}
print(jjj)

ooo= { }
print(ooo)


