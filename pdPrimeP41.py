from brandonsEP import isPrime
from brandonsEP import lsToNum
import itertools

def search(perms):
    found = []
    nextp = perms.next()
    while nextp:
        nextp = list(nextp)
        num = lsToNum(nextp)
        if isPrime(num):
            print num
            return True
        nextp = next(perms, None)
    return False

for i in range(9,0,-1):
    if search(itertools.permutations(range(i,0,-1))): break
