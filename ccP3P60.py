import brandonsEP
from itertools import combinations
from itertools import permutations
from mydigitInt import digitInt
import sys
isP = brandonsEP.isPrime
cc = brandonsEP.concatNums

LENGTH = 4

def doubleCC(a,b): return isP(cc(a,b)) and isP(cc(b,a))

p = brandonsEP.sieve(10**6)
groups = []
success = []

for n in p:
    for group in groups:
        if all(doubleCC(a,b) for a,b in combinations(group+[n],2)):
            group.append(n)
            if len(group) == LENGTH:
                print group, sum(group)
                #sys.exit()
                success.append(group)
    groups.append([n])

print "finished, found ", len(success)


#p = [digitInt(x) for x in p]
#p = [x for x in p if len(x)==3]

#shortlist = [(a,b) for a,b in combinations(p,2) if isP(cc(a,b)) and isP(cc(b,a))]

#print shortlist
#print len(shortlist)

#p = sieve(100)

