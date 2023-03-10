# print("What is a Handle?")

# fhand = open('mbox.txt')
# print(fhand)

# fhand = open('stuff.txt')

#print("The newline Character")

#stuff = 'Hello\nWorld!'
##stuff
#print(stuff)
#stuff = 'X\nY'
#print(stuff)
#print(len(stuff))


# print("File Handle as a Sequence\n")

# xfile = open('mbox.txt')
# for cheese in xfile:
#     print(cheese)


# print("Counting Lines in a File")
# fhand = open('mbox.txt')
# count = 0
# for line in fhand:
#     count = count + 1
# print('Line Count:', count)


# print("Reading the Whole file")

# fhand = open('mbox.txt')
# inp = fhand.read()
# print(len(inp))
# print(inp[:20])

# print("Searching through a file")

# fhand = open("mbox-short.txt")
# for line in fhand:
#     if line.startswith('From:'):
#         print(line)


# print("Search throug a file(fixed)")

# fhand = open("mbox-short.txt")
# for line in fhand:
#     line = line.rstrip()
#     if line.startswith('From:') :
#         print(line)

# print("Skippin with continue")

# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:') :
#         continue
#     print(line)

# print("Using in to select lines")

# fhand = open('mbox-short.txt')
# for line in fhand: 
#     line = line.rstrip()
#     if not '@uct.ac.za' in line :
#         continue
#     print(line)

# print('Enter the file name: ')

# fname = input('Enter the file name: ')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:') :
#         count = count + 1
# print('There were', count, 'subject lines in', fname)

print("Bad File Names")

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)


