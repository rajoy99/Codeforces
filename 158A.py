n,k=map(int,input().split())

li=list(map(int,input().split()))

kth_score=li[k-1]
cnt=0
for i in range(n):
    if li[i]>=kth_score and li[i]>0:
        cnt+=1
    else:
        break
print(cnt)


