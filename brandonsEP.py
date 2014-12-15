def sieve(MAX):
    MAX +=1
    primes = []
    candidates = [True] * MAX

    for i in xrange(2,MAX):
        if candidates[i]:
            primes.append(i)
            for factor in range(i*i,MAX,i):candidates[factor]=False
    return primes

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