n,k=map(int,input().split())
a=list(map(int,input().split()))
p=0
for i in range(n):
    if a[k-1]==0 and a[k-1]>=a[i]:
        p=p+0
    elif a[k-1]<=a[i]:
        p=p+1
        
print(p)               

