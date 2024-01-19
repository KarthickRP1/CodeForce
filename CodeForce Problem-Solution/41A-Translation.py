a=input()
c=input()
b=''
for i in range(len(a)):
    b=a[i]+b
if b==c:
    print('YES')
else:
    print('NO')
