
count = 0

denoms = [200,100,50,20,10,5,2,1]

def find(x,subdem):
    global count

    if not x:
        count +=1
        return

    for i in range(len(subdem)):
        if x>=subdem[i]:
            find(x-subdem[i],subdem[i:])

find(200,denoms)

print count