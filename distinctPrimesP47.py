import math
import brandonsEP

def primeFactors(num):

	orig = num

	pFactors =[]
	
	#factors of 2
	if not num&1: pFactors.append(2)

	while not num&1:
		num = num>>1

	for i in range(3,orig):
		div = divmod(num, i)
		if not div[1]: pFactors.append(i)
		while div[0] and not div[1]:
			num = div[0]
			div = divmod(num, i)
		if not div[1]:
			if brandonsEP.isPrime(num): pFactors.append(num)

	return pFactors


import brandonsEP

def pfact2(num, primes):
	factors = []
	for p in primes:
		if p>num: return factors
		if not num%p: factors.append(p)


mPrimes = brandonsEP.sieve(10**6)

queSize =0
for i in xrange(10,10**6):
	if len(pfact2(i,mPrimes))==4:
		queSize+=1
	else: queSize=0

	if queSize == 4: 
		print i-3
		break



