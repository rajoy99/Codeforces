import math
t=int(input())

for i in range(t):
    n=int(input())

    if n in {0,1,2}:
        print(0)
    else:
        print(math.ceil(n/2)-1)