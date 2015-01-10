import brandonsEP
from math import factorial

limit = 10**6
length = 59
count = 0

facts = map(factorial, range(10))

recordedLength = {}


def sumfact(num):
    return sum(map(lambda x:facts[x], brandonsEP.digits(num)))
#    return sum(map(factorial,brandonsEP.digits(num)))

def ind(seris):
    i = len(seris)-2
    while i:
        if seris[i]==seris[-1]: return (False, i)
        i-=1
    return (True, None)


def serisLength(x):

    if recordedLength.has_key(x): return recordedLength[x]

    seris = [x] + [sumfact(x)]
    indexRep = ind(seris)

    while indexRep[0]:
        seris.append(sumfact(seris[-1]))
        if recordedLength.has_key(seris[-1]):
            st = recordedLength[seris[-1]]
            recordedLength.update(map(lambda x:(x[1],x[0]), enumerate(reversed(seris), start=st)))
            return st
        indexRep = ind(seris)


    st = len(seris) - indexRep[1] - 1
    recordedLength.update(map(lambda x:(x[1],x[0]), enumerate(reversed(seris[:indexRep[1]+1]), start=st)))

    return len(seris)-1

#cyclers = [145,169,363601,1454,871,872,45361,45362]



for x in range(1,limit):
    #print x
    if serisLength(x)==length:
        count +=1

print count

#dict1 = dict(map(lambda x:(x[1],x[0]), enumerate(reversed(a), start=1)))
