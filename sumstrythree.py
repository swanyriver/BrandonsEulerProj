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

#print addto(100)-1

#############################################################
############################someone elses code###############
#############################################################
def counting_summations(n):
    costs=[1]+[0]*(n)

    for i in range(1,n):
        #print costs
        for j in range(i, n+1):
            costs[j]+=costs[j-i]  # Where did this come from?

    res=costs[n]

    print costs[n]


counting_summations(100)