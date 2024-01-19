a,b,c=map(int,input().split())
z=0

for i in range(1,c+1):
    h=i*a
    z=z+h
if z>b:
    print(z-b)
else:
    print(0)
