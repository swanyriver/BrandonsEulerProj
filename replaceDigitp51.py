import brandonsEP
import itertools

primes = brandonsEP.sieve(10**8)

def replace(diglist, a, b):
    found = 0
    mutate = diglist[:]
    for i in range(10):
        mutate[a],mutate[b] = i,i
        if brandonsEP.binary_search(primes, brandonsEP.lsToNum(mutate)):
            found+=1
    return found

def search():
    for p in primes[primes.index(101):]:
        dig = brandonsEP.digits(p)
        for a,b in itertools.combinations(range(len(dig)), 2):
            if dig[a]==dig[b]:
              score = replace(dig, a, b)
              #print score
              #print a,b, p, score,  dig[a],dig[b], dig
              if score==8: return p

#print replace([5,6,0,0,3], 2, 3)
print search()