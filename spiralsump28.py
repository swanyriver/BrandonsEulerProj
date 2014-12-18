sumup = 1
location = 1
for x in range(2,1002,2):
    #print [location + x*i for i in range(1,5)]
    sumup += sum([location + x*i for i in range(1,5)])
    location+=x*4

print sumup