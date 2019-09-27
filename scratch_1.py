import itertools

def codebook(n):
    pool = '0', '1'
    o = open('binarylength' + str(n) + '.txt', 'w')
    for item in itertools.product(pool, repeat=n):
        o.write(str(item) + "\n")
    return item

codebook(5)

def weight(n, s):
    empty = []
    for i in range(s):
        empty.append(0)
    for i in range(n+s):
        empty.append(1 + empty[i] + empty[i+1])
    for i in range(s):
        empty.remove(0)
    return empty

weight(5, 2)

#program computing the moment of a given codeword

def moment(s, x):
    w = weight(len(x), s)
    moment = 0
    for i in range(len(x)):
        moment += (x[i]*w[i])
    print moment

moment(2, [0,1,1,0,1,0,0,0])
moment(2, [0,1,1,1,1])

#Generate helberg codebook n = 5, s = 2, a = 0. Should have moment 0 or 20.

def helbergcodebook(n, s, a):
    file = codebook(n)
    w = weight(n, s)
    num = w[n]    #This is printing out as 33, when it should be 20.
    print num       #w[n] prints out 20
    for t in file:
        m = moment(s, t) #This is not working because the moment program only works if the number is a list of ints while the codebook program gives strings
        print m
        if m == a:
            print t
        if m == (num+a):
            print t
        else:
            pass

helbergcodebook(5, 2, 0)