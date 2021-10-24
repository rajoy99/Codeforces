
n=int(input())

arr=list(map(int,input().split()))
hm={}
for i in range(n):
    hm[i+1]=arr[i]

hm={k:v for v,k in hm.items()}


for i in sorted(hm):
    
    print(hm[i],end=' ')

