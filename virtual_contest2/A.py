t=int(input())

for i in range(t):
    n=int(input())

    if n%2==0: 
        print(0) 
    else:
        s=str(n)
        flag=False
        for i in range(len(str(n))):
            if int(s[i])%2==0:
                print(i+1)
                flag=True
                break 
        
        if flag==False:
            print(-1)
        
    
    


    

