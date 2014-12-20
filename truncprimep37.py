import brandonsEP
import math

primes = brandonsEP.sieve(10**6)
oneDPrimes = [2,3,5,7]
twoDPrimes = [x for x in primes if int(math.log10(x))==1]
threeDPrimes = [x for x in primes if int(math.log10(x))==2]
fourDPrimes = [x for x in primes if int(math.log10(x))==3]
fiveDPrimes = [x for x in primes if int(math.log10(x))==4]
del primes[:4]
print primes[-100:]

winers = []
#filter first and last number
#primes = [x for x in primes if x%10 in [2,3,5,7]]
#primes = [x for x in primes if x//10**int(math.log10(x)) in oneDPrimes]

primes = [x for x in primes if x%10 in oneDPrimes and x//10**int(math.log10(x)) in oneDPrimes]
winers.extend([x for x in primes if int(math.log10(x))==1])
print "two ", winers

primes = [x for x in primes if x%100 in twoDPrimes and x//10**(int(math.log10(x))-1) in twoDPrimes]
winers.extend([x for x in primes if int(math.log10(x))==2])
print "three ", winers

primes = [x for x in primes if x%1000 in threeDPrimes and x//10**(int(math.log10(x))-2) in threeDPrimes]
winers.extend([x for x in primes if int(math.log10(x))==3])
print "four", winers

primes = [x for x in primes if x%10000 in fourDPrimes and x//10**(int(math.log10(x))-3) in fourDPrimes]
winers.extend([x for x in primes if int(math.log10(x))==4])
print "five", winers

primes = [x for x in primes if x%100000 in fiveDPrimes and x//10**(int(math.log10(x))-4) in fiveDPrimes]
winers.extend([x for x in primes if int(math.log10(x))==5])
print "five", winers


print winers
print len(winers)
print sum(winers)



