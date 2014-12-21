def dig(d):
    n = (10**d) - sum([9*(10**x)*(x+1) for x in range(d-1)])
    div = divmod(n, d)
    quotient, remainder = div[0], div[1]
    

    quotient+= 10**(d-1)
    return int(str(quotient+1)[remainder-1])

print reduce(lambda x,y: x*y, [dig(i) for i in range(2,7)])
#print [dig(i) for i in range(1,7)]