import brandonsEP

primes = brandonsEP.sieve(10**3)
#len = 168
#search space = 168**2

#Invairants:
#   B must be in set primes less than 1000
#   A must be odd (does not narrow search space though)
#   |A| must be <1000
#   1+A+B must be in set primes less than 1000

def testFormula(a,b):
    i = 0
    while True:
        num = i**2 + a*i + b
        if num>0 and brandonsEP.isPrime(num): i+=1
        else: break
    return i

print testFormula(1, 41)      #expected result:40
print testFormula(-79, 1601)  #expected result:80

longest = (0,0,0)

for b in primes:
    for a in [p-b-1 for p in primes]:
        score = testFormula(a, b)
        if score > longest[0]: 
            longest = (score,a,b)

print longest
print longest[1]*longest[2]