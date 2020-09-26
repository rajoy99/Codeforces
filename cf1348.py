t=int(input())

for i in range(t):
    n=int(input())
    pos=n//2 # 3,4 ....
    left=0
    right=0
    for i in range(pos,pos+pos):
        left+=1<<i
        
    for i in range(1,n+1):
        right+=1<<i
    ans=right-2*left
    print(ans)
