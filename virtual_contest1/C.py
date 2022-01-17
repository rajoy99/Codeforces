def isPermutation(n,arr):

    li=list(range(1,n+1))
    arr.sort()
    return li==arr 


print(isPermutation(4,[4,3,1,2]))


