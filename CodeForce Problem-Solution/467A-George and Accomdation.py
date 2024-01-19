a=int(input())
count=0
for i in range(a):
    a,b=map(int,input().split())
    if b-a>=2:
        count+=1
print(count)
