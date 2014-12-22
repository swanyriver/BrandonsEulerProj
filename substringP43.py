from brandonsEP import digits

primes = [17,13,11,7,5,3,2]

factcors = {}

for p in primes:
    factcors[p]=[tuple(digits(i*p)) for i in xrange(100//p+1,1000//p)]
    factcors[p]=[(a,b,c) for a,b,c in factcors[p] if a!=b and b!=c and a!=c]

for p in primes: print p, factcors[p]
