n=int(input())

count=0
string=''

for i in range(n):
    s=input()
    if s=='01':
        string+='x'
    else:
        string+='y'


for i in range(1,n):
    if string[i]!=string[i-1]:
        count+=1 
    
print(count+1)


        



    





