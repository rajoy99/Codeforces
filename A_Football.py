string = input()

zcount=0
maxcount=0 

for i in range(1,len(string)):
    if string[i-1]==string[i]:
        zcount+=1
        maxcount=max(zcount,maxcount) 
    else:
        zcount=0

if maxcount>=7:
    print("YES")
else:
    print("NO")


     