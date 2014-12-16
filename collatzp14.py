LIMIT = 10**6

#seconds: 3.7091960907
def collatza(n):
    if not n%2:
        return n/2
    else:
        return 3*n+1

#seconds: 3.58166313171
def collatzb(n):
    if not n&1:
        return n >> 1
    else:
        return 3*n+1

collatz = collatzb

import timeit
timein = timeit.time.time()

distances = {1:0}

for num in range(2,LIMIT):
    seq = [num]
    while num not in distances:
        num = collatz(num)
        seq.append(num)
    #reached 1 or found previously known distance
    d = distances[seq.pop()]
    while len(seq):
        d+=1
        distances[seq.pop()]=d

#find max value:
greatest = 0
key = 0
for k in distances:
    if distances[k]>greatest:
        greatest = distances[k]
        key = k

print key, "distance:", greatest

print "seconds:", timeit.time.time()-timein

#print distances

#for k in distances:
    #print k, " distance:",distances[k],"->",
    #num = k
    #while num!=1:
        #print num, "-->",
        #num = cobalt(num)
    #print 1