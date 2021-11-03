n=int(input())

a=list(map(int,input().split()))

total=n*100 

portion=sum(a)

print(portion*100/total)