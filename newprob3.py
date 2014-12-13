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

for b in xrange(11,largest_possibe_factor):
    if not b%10000:
        print largest_possibe_factor-b, " remaining"
    if isPrime(b):
        if not BIGNUM%b:
            largest = b

print "largest factor is: ", largest