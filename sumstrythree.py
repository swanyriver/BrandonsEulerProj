def addto(n, min = 1, sofar = []):

    # only for debug
    if n==0: print sofar

    if n<=0: return not n

    total = 0
    for part in range(min,n+1):
        sofar.append(part)
        total += addto(n-part, min=part, sofar=sofar[:])
        sofar.pop()

    return total - 1

print addto(6)