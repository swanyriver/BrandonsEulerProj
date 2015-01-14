import brandonsEP
import itertools

p = brandonsEP.sieve(100)
bsi = brandonsEP.binary_search_index

def pslice(min, max):
    return p[bsi(p,min):bsi(p,max)+1]

def addto(n, min = 1):
    if n<=0: return not n

    total = 0
    for part in pslice(min,n):
        total += addto(n-part, min=part)
    return total

for n in itertools.count(start=11):
    if addto(n)>5000:
        print n
        break