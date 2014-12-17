from brandonsEP import sieve

LIMIT = 10**6

primes = sieve(LIMIT)
pset = set(primes)

def search(sliceSize):
    #search from 0-s to n-s to n
    for i in range(len(primes)-sliceSize+1):
        s = sum(primes[i:i+sliceSize])
        if s>primes[-1]: return None
        if s in pset: return s
    return None


# all summed obviously wont total to one within them
# sum of one element cant be another
# n-1 elements to 2 elements tested
for sliceSize in xrange(len(primes),2,-1):
    pfound = search(sliceSize)
    if pfound:
        print "%d is the sum of %d consecutive primes"%(pfound,sliceSize)
        break
