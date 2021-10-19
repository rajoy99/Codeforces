n=int(input())
s=input()

ant=s.count('A')
dnk=s.count('D')

if ant>dnk:
    print('Anton')
elif ant<dnk:
    print('Danik')
else:
    print('Friendship')
