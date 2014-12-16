LIMIT = 10**6

def cobalt(n):
    if not n%2:
        return n/2
    else:
        return 3*n+1


distances = {1:0}

for num in range(2,LIMIT):
    seq = [num]
    while num not in distances:
        num = cobalt(num)
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

#for k in distances:
    #print k, " distance:",distances[k],"->",
    #num = k
    #while num!=1:
        #print num, "-->",
        #num = cobalt(num)
    #print 1