import brandonsEP
from itertools import combinations
from itertools import permutations
from mydigitInt import digitInt
isP = brandonsEP.isPrime
cc = brandonsEP.concatNums
#ps = [3,7,109,673]

#print all(brandonsEP.isPrime(brandonsEP.concatNums(a,b)) for a,b in permutations(ps,2))

p = brandonsEP.sieve(10**4)
p = [digitInt(x) for x in p]
p = [x for x in p if len(x)==4]
p = [x for x in p if x[0] == 3 or x[-1] == 3 or x[0] == 7 or x[-1] == 7]
p = [x for x in p if isP(x[1:]) or isP(x[:-1])]
#p = [x for x in p if x[0]!=2]
p = [x for x in p if x[1]]

#print p
#print len(p)

left3 = {}
right3 = {}

for num in p:
    l = num[:3]
    c = left3.get(l,0)
    left3[l]=c+1

    r = num[1:]
    c = right3.get(r,0)
    right3[r]=c+1

lv = sorted(list(left3.items()),key=lambda x: x[0])
rv = sorted(list(right3.items()),key=lambda x: x[0])

print rv
print lv

# #lv.sort(key=lambda x: x[1], reverse=True)


lv = [x for x in lv if x[1]>1]
rv = [x for x in rv if x[1]>1]

#print lv
#print rv

rv = [x[0] for x in rv]

candidates = [x[0] for x in lv if x[0] in rv]

print candidates
shortlist = []

for a,b in combinations(candidates, 2):
    if isP(cc(a,b)) and isP(cc(b,a)):
        shortlist.append((a,b))

print shortlist


# for a,b in combinations(candidates, 2):
#     if brandonsEP.isPrime(brandonsEP.concatNums(a,b)) and brandonsEP.isPrime(brandonsEP.concatNums(a,b)):
#         print a, b
#         bignums = (a,b)

# ip = brandonsEP.isPrime
# cc = brandonsEP.concatNums

for a,b in shortlist:
    print a,b
    print isP(cc(a,3)) and isP(cc(3,a))
    print isP(cc(a,7)) and isP(cc(7,a))
    print isP(cc(b,3)) and isP(cc(3,b))
    print isP(cc(b,7)) and isP(cc(7,b))








