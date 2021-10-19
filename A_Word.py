s=input()

upcnt,lowcnt=0,0

for i in s:
    if ord(i)>=65 and ord(i)<=90:
        upcnt+=1
    else:
        lowcnt+=1
if upcnt>lowcnt:
    print(s.upper())
else:
    print(s.lower())
