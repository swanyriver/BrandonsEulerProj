import brandonsEP

primes = brandonsEP.sieve(10**6)

#From Rosseta Code
def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low <= high: 
        mid = (low+high)//2
        if l[mid] > value: high = mid-1
        elif l[mid] < value: low = mid+1
        else: return True
    return False

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
    if all([binary_search(primes,x) for x in rotations(p)]): 
        numCircs+=1
        #print p, "is TRUE"


print numCircs



#in is uncesarily slow,  primes list is sorted