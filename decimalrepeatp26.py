#from decimal import Decimal

#decs = [(x,str(Decimal(1/float(x)))[2:]) for x in range(2,100)]
#decs = [(x,str(1/float(x))[2:]) for x in range(2,100)]

#print decs
#for n in decs: print n

LIMIT = 10000

def longdiv(x):
    answer = []
    div = 10
    while len(answer)<=LIMIT:
        d = divmod(div,x)
        answer.append(d[0])
        div = d[1] * 10
        if not div: return None
    return answer

#reps = [(i,longdiv(i)) for i in range(2,1001) if longdiv(i)]

#print reps[:16]
#print len(reps)
#for x in reps: print x[0],x[1][:20]

def recur(decl):
    for size in range(1, len(decl)//2):
        if decl[-size:] == decl[-(size*2):-size]: return size
    return 0

def repsearch(x):
    answer = []
    div = 10
    while len(answer)<=LIMIT:
        d = divmod(div,x)
        answer.append(d[0])
        div = d[1] * 10
        if not div: return 0  #terminating decimal
        recurance = recur(answer)
        if recurance: return recurance
    return 0

#for i in range(2,16): print repsearch(i)

reps=[(i,repsearch(i)) for i in range(2,1000)]
reps=sorted(reps, reverse=True, key=lambda x:x[1])
print reps[0]
print reps[:20]