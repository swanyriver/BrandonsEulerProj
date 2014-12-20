def sievevP(MAX):
    primes = []
    candidates = [True] * MAX

    for i in xrange(2,MAX,1):
        if candidates[i]:
            print i,
            for factor in range(i*i,MAX,i):candidates[factor]=False
    return primes

sievevP(10**9)