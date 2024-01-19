h=int(input())
e=0
f=0
m=0
for i in range(h):
    a,b,c=map(int,input().split())
    e+=a
    f+=b
    m+=c
if e==0 and f==0 and m==0:
    print("YES")
else:
    print("NO")
    
    
