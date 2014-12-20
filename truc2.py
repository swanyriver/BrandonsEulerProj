import brandonsEP
import math

primes = brandonsEP.sieve(10**6)
oneDPrimes = [2,3,5,7]
del primes[:4]

primesofDigit = [[]] * 7
primesofDigit[1] = oneDPrimes

digits = 1
beginIndex = 0
for i in range(len(primes)):
    if int(math.log10(primes[i]))>digits:
        digits +=1
        primesofDigit[digits] = primes[beginIndex:i]
        beginIndex = i
primesofDigit[digits+1] = primes[beginIndex:]

reducedPrimes = primes[:]

for i in range(1,7):
    print i, len(primesofDigit[i])


def valid(num, digits): 
    rightTrunc = False
    leftTrunc = num%(10**digits) in primesofDigit[digits] 
    if leftTrunc: 
        rightTrunc = num//10**(int(math.log10(num))-digits+1) in primesofDigit[digits]
    return rightTrunc and leftTrunc

winers = []
for x in range(1,6):
    reducedPrimes = [p for p in reducedPrimes if valid(p,x)]
    print x, " remaining:", len(reducedPrimes)
    winers.extend([p for p in reducedPrimes if p in primesofDigit[x+1]])

print winers
print sum(winers)


