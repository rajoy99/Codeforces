n=int(input())

flag=False

val=list(map(int,input().split()))
for i in range(n):
    
    flag=flag or val[i] 

if flag==False:
    print("EASY")
else:
    print("HARD")