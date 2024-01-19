a=int(input())
b=list()
c=1
for i in range(a):
    b.append(input())
for i in range(len(b)-1):
    if b[i]!=b[i+1]:
        c+=1
print(c)
             
