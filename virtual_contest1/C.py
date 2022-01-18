t=int(input())

for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    
    isin=[False for i in range(n)]

    for i in arr:
        x=i
        while x>n or isin[x]==False:
            x=x//2 
            

    i=0


    print("YES")
    print(arr) 
            



    





