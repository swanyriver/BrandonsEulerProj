import brandonsEP

primes = set(brandonsEP.sieve(10**6))

def toNum(digits):
    result = 0
    for digit in digits:
        result *=10
        result +=digit
    return result

def rotations(num):
    digs = brandonsEP.digits(num)
    result = [digs[x:] + digs[:x] for x in range(len(digs))]
    return [toNum(x) for x in result]
    #return list(set(result))

numCircs =0
for p in primes:
    if all([x in primes for x in rotations(p)]): 
        numCircs+=1
        print p, "is TRUE"


print numCircs



#in is uncesarily slow,  primes list is sorted