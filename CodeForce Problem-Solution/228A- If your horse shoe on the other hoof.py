b=list(map(int,input().split()))
c=0
for i in b:
    c=c+b.count(i)
if c==6:
    print(1)
elif c==10:
    print(2)
elif c==16:
    print(3)
else:
    print(0)
        
