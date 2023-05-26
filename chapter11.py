import re
import socket
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

y = re.findall('[AEIOU]+',x)
print(y)

# ...............
#import re
x = 'From: Using the: character'
y = re.findall('^F.+:',x)
print(y)
print("\nNo-Greedy Matching\n")
#import re
x = 'From: Using the: character'
y = re.findall('^F.+?:',x)
print(y)
x = 'From stephen.marquez@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('\S+@\S+',x)
print(y)
print("\n")
y = re.findall('^From (\S+@\S+)',x)
print(y)
print("\nAnother example\n")
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)
print("\nThe Double Split Pattern\n")
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
print("\nThe Regex Version\n")
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin)
print(y)
y = re.findall('^From.*@([^ ]*)',lin)
print(y)
print("\nEscape Character\n")
x = 'We just received $10.00 for cookies'
y = re.findall('\$[0-9.]+',x)
print(y)
print("\nSockets in Python\n")
# import socket
mysock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )
print("\nApplication Protocols\n")
