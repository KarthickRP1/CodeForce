a,b=map(int,input().split())
z=0
if(a%2==0):
    c=a//2
else:
    c=(a+1)//2
if c>=b:
    #odd number
    print((b*2)-1)
else:
    z=b-c
    print(z*2)
