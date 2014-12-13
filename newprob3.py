BIGNUM = 600851475143
largest_possibe_factor = BIGNUM/2
largest = 0;

primes = [2,3]

def isPrime(x):
    for a in primes:
        if not x%a:
            return False
    return True

scaleFactor = 10000
scale = 0

for b in xrange(4,largest_possibe_factor):
    if isPrime(b):
        primes.append(b)
        scale += 1
        if(scale == scaleFactor):
            scale = 0
            print "new prime: ", b, round(float(b/float(largest_possibe_factor)),5)
        if not BIGNUM%b:
            print " isfactor"
            largest = b

print "larges factor is: ", largest