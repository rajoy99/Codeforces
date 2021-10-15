k,n,w=map(int,input().split())

needed=0

needed=k*w*(w+1)//2

if needed-n>0:
    print(needed-n)
else:
    print(0)
