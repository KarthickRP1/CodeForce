a=int(input())
z=['4','7']
b=str(a)
count=0
flag=0
if flag==0:
    for i in b:
        if i in z:
            count+=1
        
    if count==len(b):
        flag=0
        print('YES')
    else:
        flag=1
if flag==1:        
    if a%7==0 or a%4==0 or a%47==0 or a%74==0:
        print('YES')
    else:
        print('NO')
