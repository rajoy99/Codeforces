t=int(input())

for i in range(t):
    a,b,c=map(int,input().split())

    new_a=b-(c-b)
    if new_a>=a and new_a%a==0 and new_a!=0:
        print("YES")
        continue

    new_b=c-0.5*(c-a)
    if new_b>=b and new_b%b==0 and new_b!=0:
        print('YES')
        continue

    new_c=b+(b-a)
    if new_c>=c and new_c%c==0 and new_c!=0:
        print("YES")
        continue

    print("NO")