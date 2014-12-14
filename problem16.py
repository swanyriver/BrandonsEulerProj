x = pow(2,1000)
#x= pow(2,15)

t = 0

while x>0:
    a = divmod(x,10)
    t+= a[1]
    x = a[0]

print t