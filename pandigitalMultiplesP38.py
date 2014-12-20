#possible combos are, 2,2,2,3 / 3,3,3 / 4,5
# ranges               (25-33] 100-334  >5000

from brandonsEP import digits
from brandonsEP import lsToNum

panDig = range(1,10)
largest = 0

def search(beg, end):
    global largest
    for i in range(beg,end):
        mult = 1
        concat = []
        while len(concat)<9:
            concat.extend(digits(i*mult))
            mult+=1
        check = sorted(concat)
        if check == panDig:
            print concat, i
            num = lsToNum(concat)
            if num > largest: largest = num


search(3, 10)
search(25,34)
search(100, 335)
search(5000, 9999)

print largest