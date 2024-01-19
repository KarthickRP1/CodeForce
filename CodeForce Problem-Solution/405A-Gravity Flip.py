a=int(input())
b=list(map(int,input().split()))
b.sort()
c=''
for i in b:
    c+=str(i)+' '
print(c)
