import brandonsEP
from itertools import combinations
from itertools import permutations
from mydigitInt import digitInt
import sys

fours = [[11, 23, 743, 1871],
[7, 19, 97, 3727],
[23, 47, 1481, 4211],
[89, 107, 1061, 4973],
[467, 587, 617, 6323],
[3391, 3433, 3643, 6607],
[5023, 5443, 6841, 7039],
[1283, 1619, 4127, 7949],
[5197, 5701, 6733, 8389],
[43, 97, 1381, 8521],
[6569, 6689, 6779, 8537],
[19, 31, 181, 9679],
[3547, 3643, 5449, 9817],
[3917, 4019, 4211, 10181],
[2267, 2729, 10973, 12659],
[9619, 10039, 11971, 13831],
[3373, 3631, 8923, 14083],
[2687, 3023, 8069, 14447],
[11527, 12073, 12703, 14737],
[4201, 4759, 14797, 16729],
[6323, 6491, 8237, 17333],
[659, 947, 5009, 18233],
[5209, 5419, 9241, 18427],
[6047, 6203, 7643, 19727],
[373, 661, 1237, 20011],
[15359, 15737, 18401, 20333]]
fours.sort(key=sum)

isP = brandonsEP.isPrime
cc = brandonsEP.concatNums

def doubleCC(a,b): return isP(cc(a,b)) and isP(cc(b,a))

p = brandonsEP.sieve(10**6)

def search(four):
    print four
    for a in p:
        #if all(doubleCC(a,b) for a,b in combinations(four+[num],2)):
        #    print num, sum(four)+num
        for b in four:
            if not doubleCC(a, b): break
        else:
            print a, sum(four)+a


search([5197, 5701, 6733, 8389])
#for x in fours: search(x)

