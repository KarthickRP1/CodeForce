a=int(input())
b=['I','love','that']
c=['I','hate','that']
e=['I','love','it']
f=['I','hate','it']
d=''
for i in range(a):
    if a-1==i:
        if i%2==0:
            for i in f:
                d=d+i+' '
        else:
            for i in e:
                d=d+i+' '
        
    elif i%2==0:
        for i in c:
            d=d+i+' '
    else:
        for i in b:
            d=d+i+' '
print(d)
            
            
