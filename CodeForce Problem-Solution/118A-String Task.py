a=input()
a=a.lower()
b=['a','e','i','o','u','y']
r=str()
for i in a:
    h=i
    if h in b:
        continue
    if i not in b:
        r=r+'.'+i
print(r)
        
