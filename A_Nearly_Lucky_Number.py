import sys
n=input()
s=str(n)

no_of_lucky_digits=0
for i in s:
    if i=='4' or i=='7':
        no_of_lucky_digits+=1

# print(str(no_of_lucky_digits))
st=set([4,7])

for i in str(no_of_lucky_digits):
    
    if int(i) not in st:
        print('NO')
        sys.exit(0)
        


print('YES')