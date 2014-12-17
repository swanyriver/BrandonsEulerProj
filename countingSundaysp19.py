days = ["sun","mon","tues","wed","thur","fri","sat"]
months = [31,28,31,30,31,30,31,31,30,31,30,31]

year = 1900
day = 1
dofM = 1
month = 1
sundays = 0

for y in range(year,2001):
    print y, ":",
    for m in range(12):
        if day == 0 and y>1900: sundays+=1

        print days[day],",",
        #print "Month: ", m

        #d =0
        #while(d<months[m]):
            #print "Week"
            #for dm in range(7):
                #print days[(d+day)%7], ":",d+1," ",
                #d+=1

        day = (day + months[m])%7
        if(m==1):
            if (not y%4 and y%100) or not y%400:
                #print "leap year:", y
                day = (day+1)%7
    print ""

print sundays