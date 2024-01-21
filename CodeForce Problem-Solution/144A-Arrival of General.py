b=int(input())
a=list(map(int,input().split()))
z=max(a)
y=min(a)
count=0
while(a[0]!=z):
    for i in range(len(a)):
        if a[i]==z:
            temp=a[i-1]
            a[i-1]=a[i]
            a[i]=temp
            count+=1
            break
    
while(a[len(a)-1]!=y):
    for i in range(len(a)-1,0,-1):
        if a[i]==y:
            temp=a[i+1]
            a[i+1]=a[i]
            a[i]=temp
            count+=1
            break
    
        
print(count)
