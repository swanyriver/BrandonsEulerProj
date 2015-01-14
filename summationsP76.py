import itertools
import brandonsEP

def ex(ls,ls2): 
    ls.extend(ls2)
    return ls

def toParts(iter,x):
    result = []
    for p in reversed(iter):
        result.append(x-p)
        x=p
    result.append(x)
    return result

def wholeDeal(iter,x):
    return brandonsEP.lsToNum(sorted(toParts(iter,x)))


def waystosum(x):
    partitions =reduce(ex, [list(itertools.combinations(range(1,x), r)) for r in range(1,x)])
    partitions = set(map(lambda a:wholeDeal(a,x), partitions))
    print partitions, len(partitions)


