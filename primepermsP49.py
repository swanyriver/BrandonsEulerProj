import math, brandonsEP
from collections import defaultdict
import itertools

def nlen(x):
    return int(math.log10(x))+1

fourDPs = brandonsEP.sieve(10**4)

fourDPs = [x for x in fourDPs if nlen(x)==4]

print len(fourDPs)

sets = defaultdict(list)

for p in fourDPs:
    l = sets[brandonsEP.lsToNum(sorted(brandonsEP.digits(p), reverse=True))]
    l.append(p)

 #{brandonsEP.lsToNum(sorted(brandonsEP.digits(d), reverse=True)):d for d in fourDPs}

for k,v in sets.items():
    if len(v)<3: del sets[k]

#print sets, len(sets)

def search(Ps):
    for num in Ps:
        diffs = []
        for num2 in Ps:
            dif = abs(num-num2)
            if dif in diffs:
                return (Ps[diffs.index(dif)],num,num2)
            diffs.append(dif)
    return None


for v in sets.values():
    a = search(v)
    if a:
        print a
        print str(a[0])+str(a[1])+str(a[2])
