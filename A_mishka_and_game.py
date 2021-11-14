n=int(input())

mcount=0
ccount=0

for i in range(n):
    m,c=map(int,input().split())

    if m>c:
        mcount+=1
    elif m<c:
        ccount+=1 
    
if mcount==ccount:
    print('Friendship is magic!^^')
elif mcount>ccount:
    print('Mishka')
else: 
    print('Chris')