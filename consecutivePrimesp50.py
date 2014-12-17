from brandonsEP import sieve

import timeit
timein = timeit.time.time()

LIMIT = 10**6

primes = sieve(LIMIT)
pset = set(primes)

#0.264675140381 seconds
def search1(sliceSize):
    #search from 0-s to n-s to n
    for i in range(len(primes)-sliceSize+1):
        s = sum(primes[i:i+sliceSize])
        if s>primes[-1]: return None
        if s in pset: return s
    return None

# 0.128955125809  seconds
def search2(sliceSize):
    s = sum(primes[:sliceSize])
    for i in range(len(primes)-sliceSize+1):
        if s>primes[-1]: return None
        if s in pset: return s

        s = s - primes[i] + primes[i+sliceSize]

    return None

search=search2


# all summed obviously wont total to one within them
# sum of one element cant be another
# n-1 elements to 2 elements tested
greatest = 0
numprimes = 0
size=20
while sum(primes[:size])<=primes[-1]:
    size+=1
    s = search(size)
    if s and s>greatest: greatest,numprimes = s, size

print "%d is the sum of %d consecutive primes"%(greatest,numprimes)

print "completed in :", timeit.time.time()-timein, " seconds"