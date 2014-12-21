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

def isPrime(x):
    from math import sqrt
    if not x&1: return False
    if x < 2: return False
    if x == 2 or x==3: return True
    if not x%3:
        return False
    r = int(sqrt(x))
    f = 5
    while f<=r:
        if not x%f or not x%(f+2):
            return False
        f+=6
    return True

def allDivisors(n, inclusive = False):
    from math import sqrt
    divisors = [1]
    for factor in xrange(2,int(sqrt(n))+1):
        div = divmod(n,factor)
        if not div[1]:
            divisors.append(factor)
            divisors.append(div[0])
    if len(divisors)>1 and divisors[-1] == divisors[-2]: divisors.pop()
    if inclusive: divisors.append(n)
    return divisors

def fact(x):
    if x==0: return 1
    for i in range(x-1,0,-1): x*=i
    return x

def numCombs(n,r):
    return int(fact(n)/(fact(r)*fact(n-r)))
def numCombsWRep(n,r):
    return int(fact(n+r-1)/(fact(r)*fact(n-1)))
def numPerms(n,r):
    return int(fact(n)/fact(n-r))

def digits(x, reverse = False):
    result = []
    while x:
        a = divmod(x,10)
        result.append(a[1])
        x = a[0]
    if not reverse: result.reverse()
    return result

def lsToNum(digList):
    result = 0
    for digit in digList:
        result *=10
        result +=digit
    return result

#def contains(sortedlist,num):
    #This function is slower than python "in" wich i assumed was linear
    #is it stack frame genearation, or the list slices
#    if len(sortedlist) == 1:
#        return num == sortedlist[0]
#    else:
#        mid = len(sortedlist)//2
#        if num < sortedlist[mid]: 
#            return contains(sortedlist[:mid], num)
#        else:
#            return contains(sortedlist[mid:], num)

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

#for c<300
primitivePythagTriples =[ (3, 4, 5),   (5, 12, 13), (8, 15, 17), (7, 24, 25),
(20, 21, 29),    (12, 35, 37),    (9, 40, 41), (28, 45, 53),
(11, 60, 61),    (16, 63, 65),    (33, 56, 65),    (48, 55, 73),
(13, 84, 85),    (36, 77, 85),    (39, 80, 89),    (65, 72, 97),
(20, 99, 101),  (60, 91, 109),   (15, 112, 113),  (44, 117, 125),
(88, 105, 137),  (17, 144, 145),  (24, 143, 145),  (51, 140, 149),
(85, 132, 157),  (119, 120, 169), (52, 165, 173),  (19, 180, 181),
(57, 176, 185),  (104, 153, 185), (95, 168, 193),  (28, 195, 197),
(84, 187, 205),  (133, 156, 205), (21, 220, 221),  (140, 171, 221),
(60, 221, 229),  (105, 208, 233), (120, 209, 241), (32, 255, 257),
(23, 264, 265),  (96, 247, 265),  (69, 260, 269),  (115, 252, 277),
(160, 231, 281), (161, 240, 289), (68, 285, 293)]