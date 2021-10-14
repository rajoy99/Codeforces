s=input()

l=list(map(int,s.split('+')))

l.sort()

lw=''.join(map(str,l))

print('+'.join(lw))
