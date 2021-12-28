k,l,m,n,d = [int(input()) for i in range(5)]

hmap = {i: False for i in range(1,d+1)}

for i in range(1,d+1):
    if i%k==0 or i%l==0 or i%m==0 or i%n==0:
        hmap[i]=True 


counter=0 

for i in range(1,d+1):
    if hmap[i]==True:
        counter+=1 


print(counter)
