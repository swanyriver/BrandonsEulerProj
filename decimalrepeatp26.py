from decimal import Decimal

decs = [str(Decimal(1/float(x)))[2:] for x in range(2,10)]

print decs