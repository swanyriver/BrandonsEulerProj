def sieve(MAX):
    MAX +=1
    primes = []
    candidates = [True] * MAX

    for i in xrange(2,MAX):
        if candidates[i]: primes.append(i)
        for factor in range(i*i,MAX,i):candidates[factor]=False
    return primes