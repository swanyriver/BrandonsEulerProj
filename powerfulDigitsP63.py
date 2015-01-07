import brandonsEP

def search(n):
    count = 0
    m = 1
    x = m**n
    l = brandonsEP.lengthNum(x)

    while l<=n:
        if brandonsEP.lengthNum(x)== n: 
            count+=1
            print m,"^",n, ":" ,x
        m+=1
        x = m**n
        l = brandonsEP.lengthNum(x)

    return count

n=1
total = 0
nextcount = 1
while nextcount:
    nextcount=search(n)
    total+=nextcount
    print n, nextcount, total
    n+=1

print total