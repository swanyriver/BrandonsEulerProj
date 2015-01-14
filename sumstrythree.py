def debugaddto(n, min = 1, sofar = []):

    # only for debug
    if n==0: print sofar

    if n<=0: return not n

    total = 0
    for part in range(min,n+1):
        sofar.append(part)
        total += debugaddto(n-part, min=part, sofar=sofar[:])
        sofar.pop()

    return total

def addto(n, min = 1):
    if n<=0: return not n

    total = 0
    for part in range(min,n+1):
        total += addto(n-part, min=part)
    return total

print addto(100)-1