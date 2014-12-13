import math

BIGNUM = 600851475143
largest_possibe_factor = BIGNUM/2
largest = 0;


def isPrime(x):
    if not x%3:
        return False
    r = int(math.sqrt(x))
    f = 5
    while f<=r:
        if not x%f or not x%(f+2):
            return False
        f+=6
    return True

for b in xrange(2,largest_possibe_factor):
    if not BIGNUM%b:
        div = BIGNUM/b
        if isPrime(div):
            largest = div
            break

print "largest factor is: ", largest