
a=input()
b=str()
for i in range(len(a)):
    if i==0:
        b=b+a[i].upper()
    else:
        b=b+a[i]
print(b)
