
inp=input()

st=set()

for i in inp:
    if 65<=ord(i)<=90 or 97<=ord(i)<=122:
        st.add(i)

print(len(st))


