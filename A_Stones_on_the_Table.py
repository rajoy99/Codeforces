n=int(input())
s=input()
s=list(s)
cnt=0

for i in range(0,len(s)-1):
    if s[i]==s[i+1]:
        cnt+=1
print(cnt)


# orglength=len(s)
# res=''
# while len(s)>=2:
#     a=s.pop(-1)
#     b=s.pop(-1)
#     print(a,b)
#     if a!=b:
#         res+=a
    
# if len(s)>0:
#     res+=s[0] 
# print(res)
# print(orglength-len(res))

