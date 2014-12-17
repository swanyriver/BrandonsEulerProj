months = [31,28,31,30,31,30,31,31,30,31,30,31]

day = 1
sundays = 0

for y in range(1900,2001):
    for m in range(12):
        if day == 0 and y>1900: sundays+=1

        day = (day + months[m])%7
        if(m==1) and ((not y%4 and y%100) or not y%400):
            day = (day+1)%7

print sundays