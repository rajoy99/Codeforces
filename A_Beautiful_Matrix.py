mat=[[0 for i in range(5)]for j in range(5)]

for i in range(5):
    mat[i]=list(map(int,input().split()))


for i in range(5):
    for j in range(5):
        if mat[i][j]==1:
            pos=(i,j)

ans=abs(2-pos[0])+abs(2-pos[1])

print(ans)



