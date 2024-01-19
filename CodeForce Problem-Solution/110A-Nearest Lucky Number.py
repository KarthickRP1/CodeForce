a=input()
b=['4','7']
c=0
for i in range(len(a)):
    if a[i] in b:
        c+=1

if c==7  or c==4:
    print("YES")
else:
    print("NO")
