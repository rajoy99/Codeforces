import sys
n=int(input())

if n in range(0,10):
    print(n)
    sys.exit(0)

msk_array=[0 for i in range(len(str(n))-1)]
msk_array.insert(0,1)

msk_num=int(''.join(map(str,msk_array)))

maxval=0
if msk_num==n:
    print(9**(len(str(n))-1))
    sys.exit(0)



for number in range(n+1,n+1-msk_num,-1):

    
    number=list(map(int,str(number)))
    # print(number)
    product=1
    for i in number:
        product*=i 
        

    if product>maxval:
        maxval=product
        the_numb=int(''.join(map(str,number)))
    # print(product)

    
print(maxval)
# print('magic_number : ',the_numb)
