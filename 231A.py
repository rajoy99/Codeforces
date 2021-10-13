
cnt=0

for i in range(int(input())):

    a=list(map(int,input().split()))
    if sum(a)>=2:
        cnt+=1
    
print(cnt)
