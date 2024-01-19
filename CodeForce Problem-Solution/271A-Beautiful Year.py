a=int(input())
s=0
for i in range(a+1,9020):
    b=str(i)
    for x in b:
        if b.count(x)==1:
            s+=1
            if s==4:
                print(i)
                break
            
        else:
            s=0
            break
    if s==4:
        break
    
        
        
