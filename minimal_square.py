t=int(input())

for i in range(t):
    a,b=map(int,input().split())
    c=max(a,b)
    d=min(a,b)

    if c==d:
        print(4*c**2)
    elif 2*d>=c:
        print(4*d**2)
    else:
        print(c**2)
