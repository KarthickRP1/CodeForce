x=0
a=int(input())
for i in range(a):
    b=str(input())
    if b[0]=='+' or b[1]=='+':
        x+=1
    else:
        x-=1
print(x)
