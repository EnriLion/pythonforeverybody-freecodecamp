# -Using re.search() like find()-
# import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # if re.search('From:', line) :
    if re.search('^From:', line):
        print(line)
#We fine-tune what is matched by adding special characters to the string
