t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    flag = False
    a.sort(reverse=True)
    if len(a) == 1:
        print("YES")
        continue
    for i in range(1, len(a)):
        if abs(a[i] - a[i - 1]) > 1:
            flag = True
    print("YES") if flag == False else print("NO")
