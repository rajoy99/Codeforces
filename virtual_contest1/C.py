t=int(input())

for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    
    isin=[False for i in range(n+1)]

    flag=True
    for i in arr:
        x=i
        while x>n or isin[x]:
            x=x//2 
        if x>0:
            isin[x]=True
        else:
            flag=False 


    print("YES") if flag else print("NO")



    





