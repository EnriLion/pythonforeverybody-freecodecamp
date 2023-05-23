import re

hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip() # strip and start all the lines
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) # look at the lines that start.
    if len(stuff) != 1 : continue #if the numbers of the items of the list not in the list inside the stuff is not equap to 1 continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
