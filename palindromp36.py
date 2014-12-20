from brandonsEP import digits

def isPalindrome(num):
    num = str(num)
    return num == num[::-1]

#binary test isPalindrome(bin(x)[2:])

sumb = 0
for i in range(1,1000):
    podd = i
    peven = i
    digs = digits(i, reverse=True)
    for i in range(len(digs)):
        peven *= 10
        peven += digs[i]
        if i:
            podd *= 10
            podd += digs[i]
    if isPalindrome(bin(podd)[2:]): sumb+=podd
    if isPalindrome(bin(peven)[2:]): sumb+=peven



print sumb