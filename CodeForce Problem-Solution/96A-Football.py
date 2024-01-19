a=input()
count=0
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        count+=1
        if count==6:
            break
    else:
        count=0
if count==6:
    print("YES")
else:
    print("NO")
