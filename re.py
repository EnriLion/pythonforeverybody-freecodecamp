from re import search

with open('mbox-short.txt', 'r') as hand:
    for line in hand:
        line = line.rstrip()
        if search('^From:.*', line):
            print(line)

hand.close()

