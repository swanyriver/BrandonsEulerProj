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

def fact(x):
    for i in range(x-1,0,-1): x*=i
    return x

def numCombs(n,r):
    return int(fact(n)/(fact(r)*fact(n-r)))
def numCombsWRep(n,r):
    return int(fact(n+r-1)/(fact(r)*fact(n-1)))
def numPerms(n,r):
    return int(fact(n)/fact(n-r))

def digits(x):
    result = []
    while x:
        a = divmod(x,10)
        result.append(a[1])
        x = a[0]
    result.reverse()
    return result

def contains(sortedlist,num):
    if len(sortedlist) == 1:
        return num == sortedlist[0]
    else:
        mid = len(sortedlist)//2
        if num < sortedlist[mid]: 
            return contains(sortedlist[:mid], num)
        else:
            return contains(sortedlist[mid:], num) 