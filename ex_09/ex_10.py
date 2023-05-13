fname = input('Enter File:')

if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        # print('**',w,di.get(w,-99))# di.get(w,-99) the -99 explains if is in there count if not not count(ex. the word 'the' is not in the dictionary and that is why will be -99) and we are going to see the same before will be 1 and allows us to get

        # oldcount = di.get(w,0) #look up if the oldcount in the dictionary we will count as 0
        # print('**',w,di.get(w,-99))#the first time we see the word will count -99
        # oldcount = di.get(w,0) #look up in this dictionary and get is the function of the dictionary look up the w(word) and if i don't get it give me back 0/ using the get an if we don't find it we assing the 0
        # print(w,'old',oldcount)# print the old count
        # newcount = oldcount + 1 # the newcount exist and we count the old(0) with 1 
        # di[w] = newcount #we add the new count to the dictionary 

        #idiom: retrieve/create/update counter  
        di[w] = di.get(w,0) + 1 ## this convines all the previous lines in one 
        # print(w,'new',di[w])

        # print(w,'old',oldcount) #we are going to print it as old  
        # newcount = oldcount + 1 # the new count we count the same only we count the 0 + 1 = 1
        # di[w] = newcount
        # print(w,'new',oldcount) #we are going to print it as old  

        # if w in di:
        #     di[w] = di[w] + 1 #the string is adding the w to count +1
        #     # print('**EXISTING***')
        # else:
        #     di[w] = 1 #Adding only one
            # print('**NEW**')
        # print(w,di[w])
# print(di)

# x = sorted(di.items()) # give us a key value pairs using sorted to sort the key value pairs of the dictionary
# print(x[:5]) # showing only the first 5

tmp = list()
for k,v in di.items() :
    # print(k,v)
    newt = (v,k)
    tmp.append(newt)

# print('Flipped',tmp)

tmp = sorted(tmp, reverse=True)#is sorted by tuple
# print('Sorted',tmp[:5])#not including the 5 

for v,k in tmp[:5] :
    print(k,v)

