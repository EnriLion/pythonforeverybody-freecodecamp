han = open('mbox-short.txt')

# for line in han:
#     line = line.rstrip()
#     # print('Line', line)
#     wds = line.split()
#     # print('Words:',wds)

#     # Guardian pattern a bit stronger
#     if len(wds) < 3 : #makes the guardian a bit stronger cause if he sees 3 lists will continue
#         continue
#     if wds[0] != 'From' :
#         # print('Ignore')
#         continue
#     print(wds[2])

##Another way to do this

for line in han:
    line = line.rstrip()
    # print('Line', line)
    wds = line.split()
    # print('Words:',wds)

    # Guardian in a compound statement
    if len(wds) < 3 or wds[0] != 'From' : # if there are 3 lines in words or if the first word is not From, the only way to do this is in this order cause will work if we flipped it did not work
        # print('Ignore')
        continue
    print(wds[2])

#If we flipped(it'll give us a traceback)

# for line in han:
#     line = line.rstrip()
#     # print('Line', line)
#     wds = line.split()
#     # print('Words:',wds)

#     # Guardian in a compound statement
#     if lwds[0] != 'From' or len(wds) < 3  : # if there are 3 lines in words or if the first word is not From, the only way to do this is in this order cause will work if we flipped it did not work
#         # print('Ignore')
#         continue
#     print(wds[2])


# for line in han:
#     line = line.rstrip()
#     print('Line', line)
#     wds = line.split()
#     if line == '':
#         # print('Skip Blank')
#         continue
#     if wds[0] != 'from' :
#         # print('Ignore')
#         continue
#     print(wds[2])

