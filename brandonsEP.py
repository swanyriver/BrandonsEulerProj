def sievev1(MAX):
    MAX +=1
    primes = []
    candidates = [True] * MAX

    for i in xrange(2,MAX):
        if candidates[i]:
            primes.append(i)
            for factor in range(i*i,MAX,i):candidates[factor]=False
    return primes

def sievev2(MAX):
    MAX +=1
    primes = []
    candidates = [True] * MAX

    for i in xrange(4,MAX,2): candidates[i]=False
    primes.append(2)

    for i in xrange(3,MAX,2):
        if candidates[i]:
            primes.append(i)
            for factor in range(i*i,MAX,i):candidates[factor]=False
    return primes


sieve = sievev2

def allDivisors(n):
    from math import sqrt
    divisors = [1]
    for factor in xrange(2,int(sqrt(n))+1):
        div = divmod(n,factor)
        if not div[1]:
            divisors.append(factor)
            divisors.append(div[0])
    if len(divisors)>1 and divisors[-1] == divisors[-2]: divisors.pop()
    return divisors