def fact(x):
    if x==1:
        return x
    else:
        return x * fact(x-1)

x = fact(100)

total = 0

while x!=0:
    div = divmod(x,10)
    total += div[1]
    x=div[0]
print total