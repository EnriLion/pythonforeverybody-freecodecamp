print('Tuples')
x = ('Gleen', 'Sally', 'Joseph')
print(x[2])
y = ( 1, 9, 2)
print(y)
print(max(y))
for iter in y:
    print(iter)

print('but... Tuples are "immutable"')

x = [9, 8, 7]
x[2] = 6
print(x)

# y = 'ABC'
# # y[2] ='D'

# z =(5, 4, 3)
# z[2] = 0

print('Things not to do with tuples')
x = (3, 2, 1)
# x.sort()
# x.append()
# x.reverse()
print('A tale of two Sequences')
l = list()
print(dir(l))
print("\n")
t = tuple()
print(dir(t))
print("\n")
print('Tuples and Assignment')
(x, y) = (4, 'fred')
print(y)
(a, b) = (99, 98)
print(a)
print("\n")
print('Tuples and Dictionaries')
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k, v)
tups = d.items()
print(tups)
print('Tuples are Comparable')
print((0, 1, 2) < (5, 1, 2))
print((0, 1, 2000000) < (0, 3, 4))
print(('Jones', 'Sally') < ('Jones', 'Sam'))
print(('Jones', 'Sally') > ('Adams', 'Sam'))
print('Sorting Lists of tuples')
d = {'a':10, 'b':1, 'c':22}
print(d.items())
print(sorted(d.items()))
print('Using sorted()')
t = sorted(d.items())
print(t)
for k, v in sorted(d.items()):
    print(k, v)
print('Using sorted()')
c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k, v in sorted(d.items()):
    tmp.append( (v, k) )

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

