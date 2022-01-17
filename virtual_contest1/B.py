t=int(input())

for i in range(t):
    a,b,c=map(int,input().split())

    if b<a and b<c:
        d1,d2=a-b,c-b 
        m=1
        while True:
            if (a-b)*m==0.5*abs(a-c):
                print("YES")
                break  
            elif (a-b)*m>0.5*abs(a-c):
                print("NO")
                break 
            else:
                m+=1


    