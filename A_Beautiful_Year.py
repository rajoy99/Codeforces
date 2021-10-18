y=int(input())

def is_distinct(s):
    if len(set(s))==len(s):
        return True
    else:
        return False


i=y+1

while True:
    i_string=str(i)

    if is_distinct((i_string)):
        print(i)
        break
    i+=1 


