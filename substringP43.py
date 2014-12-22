from brandonsEP import digits
from brandonsEP import lsToNum

primes = [17,13,11,7,5,3,2]

factcors = {}

for p in primes:
    #factcors[p]=[tuple(digits(i*p)) for i in xrange(100//p+1,1000//p)]
    #factcors[p]=[(a,b,c) for a,b,c in factcors[p] if a!=b and b!=c and a!=c]
    total = p
    factcors[p] = []
    while total<1000:
        num = digits(total)
        if total<100: num.insert(0, 0)
        if total>9 and num[0] != num[1] != num[2] != num[0]:
            factcors[p].append(tuple(num))
        total+=p


def findPD(primesIndex,currentnum,numsremaining,result):
    if primes[primesIndex] == 2:
        result.append(numsremaining+currentnum)
        numsremaining.reverse()
        result.append(numsremaining+currentnum)
        return

    #print "nums remaing:", numsremaining, " currentnum:", currentnum

    ##print currentnum, currentnum[:2], factcors[primes[primesIndex]][3][1:]
    test = tuple(currentnum[:2])
    #print test
    possibles = [x[0] for x in factcors[primes[primesIndex]] if x[1:]==test]
    #print "posibles", possibles

    for num in [x for x in numsremaining if x in possibles]:
        findPD(primesIndex+1, [num]+currentnum, [x for x in numsremaining if x != num], result)



def findB(primesIndex,currentnum,numsremaining,result):
    if primes[primesIndex] == 2:
        if not currentnum[1]&1:
            result.append(numsremaining+currentnum)
            numsremaining.reverse()
            result.append(numsremaining+currentnum)
        return

    for n in numsremaining:
        if not lsToNum([n]+currentnum[:2])%primes[primesIndex]:
            findB(primesIndex+1, [n]+currentnum, [x for x in numsremaining if x != n], result)



pandigitals = []
for x in xrange(17,1000,17):
    dig = digits(x)
    if len(dig)<3: dig.insert(0, 0)
    a,b,c = dig[0],dig[1],dig[2]
    if a != b != c !=a:
        findB(1, dig, [x for x in range(10) if x not in dig], pandigitals)

#print factcors[primes[1]]
#test = (2,8)
#print "filtered", [x for x in factcors[primes[1]] if x[1:]==test]
#findB(1, [2,8,9], [x for x in range(10) if x not in [2,8,9]], pandigitals)

print pandigitals
print [1,4,0,6,3,5,7,2,8,9] in pandigitals
print len(pandigitals)
a= [lsToNum(x) for x in pandigitals]

b = [1430952867 ,  1460357289 ,  1406357289 , 4130952867 , 4160357289 , 4106357289]

print [x for x in a if x not in b]

print "sum=",sum(a)
#for p in primes: 
#recursive function needed here


###GETS THE WRONG ANSWER!!!