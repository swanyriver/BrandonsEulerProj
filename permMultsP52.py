import brandonsEP

i = 0
while  True:
	i+=1
	ds = sorted(brandonsEP.digits(i))
	for x in range(2,7):
		if sorted(brandonsEP.digits(i*x)) != ds:
			break
	else:
		print i
		for x in range(2,7): print i*x,
		break

