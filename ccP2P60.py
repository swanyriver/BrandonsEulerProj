import brandonsEP
from itertools import combinations
from itertools import permutations
from mydigitInt import digitInt
isP = brandonsEP.isPrime
cc = brandonsEP.concatNums

p = brandonsEP.sieve(10**6)
p = [digitInt(x) for x in p]
p = [x for x in p if len(x)>2]

p = [x for x in p if all(isP(cc(a,b)) for a,b in permutations([x,3,7],2))]

shortlist =[]

for a,b in combinations(p, 2):
    if isP(cc(a,b)) and isP(cc(b,a)): shortlist.append((a,b))

#print shortlist

shorterlist = set()

for a,b in shortlist:
    shorterlist.add(a)
    shorterlist.add(b)
shorterlist = sorted(list(shorterlist))
#print shorterlist

for trip in combinations(shorterlist, 3):
    if all(isP(cc(a,b)) for a,b in permutations(trip,2)):
        print trip, sum(trip) + 3 + 7

#found 109 and 673 as only possibility

#s = [3,7,109,673]
#for a in p:
#    if all(isP(cc(a,b)) and isP(cc(b,a)) for b in s):
#        print a, sum(s)+a