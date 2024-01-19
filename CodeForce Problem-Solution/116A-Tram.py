a=int(input())
count=0
som=0
for i in range(a):
    a,b=map(int,input().split())
    som=som-a+b
    if som>count:
        count=som
print(count)
