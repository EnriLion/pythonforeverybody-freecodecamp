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


print('\nMay Counters with a Dictionary')

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)

ccc['cwen'] = ccc['cwen'] + 1

print(ccc)

print('\nWhen we see a new name')

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)


print('\nThe get method for dictionaries')

counts = dict()

names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
if name in counts:
    x = counts[name]
else:
    x = 0

x = counts.get(name, 0)
print(counts)

print('\nSimplified counting with get()')

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names : 
    counts[name] = counts.get(name, 0) + 1
print(counts)


print('\n')
print('Retrieving lists of Keys and Values')

jjj = { 'chuck' :1, 'fred': 42, 'jan':100 }
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

print('\n')
print('Bonus:Two Iteration Variables!')
jjj = { 'chuck' :1, 'fred': 42, 'jan':100 }
for aaa, bbb in jjj.items():
    print(aaa, bbb)

