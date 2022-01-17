import math

# def isPermutation(n,arr):

#     li=list(range(1,n+1))
#     arr.sort()
#     return li==arr 


# print(isPermutation(4,[4,3,1,2]))

t=int(input())

for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    ideal=list(range(1,n+1))

    i=0
    while i<n:
        while arr[i]>i+1:
            arr[i]=math.floor(arr[i]/2) 
            if arr[i]<i+1:
                print("NO")
                break 
        i+=1

    print("YES")
    print(arr) 
            



    





