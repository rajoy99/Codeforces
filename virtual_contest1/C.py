def isPermutation(n,arr):

    li=list(range(1,n+1))
    arr.sort()
    return li==arr 


print(isPermutation(4,[4,3,1,2]))

t=int(input())

for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    ideal=list(range(1,n+1))

    for i in range()


