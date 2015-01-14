import brandonsEP

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

n = 10
ways = 0

while (ways<5000):
    n+=1
    ways = addto(n)

print n, brandonsEP.isPrime(n), ways