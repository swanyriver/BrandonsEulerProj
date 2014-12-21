LIMIT = 1000

def pythagPrims(Numlevels):
    matrixA = ((1,-2,2), (2,-1,2),(2,-2,3))
    matrixB = ((1,2,2), (2,1,2),(2,2,3))
    matrixC = ((-1,2,2), (-2,1,2),(-2,2,3))

    matricies = (matrixA,matrixB,matrixC)

    trips = [(3,4,5)]
    for i in range(Numlevels):
        #print i, trips[:-3**i]
        for discvovered in trips[-3**i:]:
            for m in matricies:
                trips.append(tuple(sum(k*v for k,v in zip(row,discvovered)) for row in m))


    return trips


prims = filter(lambda x: sum(x)<LIMIT, pythagPrims(4))
print prims
print len(prims)


sums = [0] *LIMIT

for trip in prims:
    tsum = sum(trip)
    total = tsum
    while total<LIMIT:
        sums[total] +=1
        total+=tsum

print max(enumerate(sums), key = lambda x:x[1])



#####close,  but missing co-prime detection
#m and n >0
#m>n
####TODO,  TURN INTO GENERATOR WITH BELOW M,N
# def ptrip(m,n):
#     return (m**2 - n**2, 2*m*n, m**2+n**2)


# primitiveTrips =[]
# for m in range(1,10):
#     for n in range((m&1)+1,m, 2): print m,n, ptrip(m, n)
