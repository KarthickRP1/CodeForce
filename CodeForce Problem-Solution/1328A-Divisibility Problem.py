a=int(input())
for i in range(a):
    b,c=map(int,input().split())
    if b%c==0:
        print("0")
    elif b<c:
        print(c-b)
    else:
        print(c-(b%c))
        
