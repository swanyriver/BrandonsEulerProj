import brandonsEP

digsums = []

for a in range(1,100):
	for b in range(1,100):
		digsums.append(sum(brandonsEP.digits(a**b)))
print max(digsums)
