from brandonsEP import allDivisors
import itertools

MAX = 28123

def findAbundants(limit=MAX):
    result = []
    for num in range(12,limit+1):
        if sum(allDivisors(num))>num: result.append(num)
    return result

abunts = findAbundants()

abuntsums = [False] * (MAX+1)

for pair in itertools.combinations_with_replacement(abunts,2):
    s = pair[0]+pair[1]
    if s < MAX+1: abuntsums[s] = True

print sum([x for x in range(MAX+1) if not abuntsums[x]])
