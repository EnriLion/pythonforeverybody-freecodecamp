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
        if w in di:
            di[w] = di[w] + 1
            print('**EXISTING***') 
        else:
            di[w] = 1
            print('**NEW**') 
        print(w,di[w])
