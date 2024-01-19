a=int(input())

b=list(map(int,input().split()))

if b.count(1)==0:
    print('EASY')
else:
    print('HARD')
