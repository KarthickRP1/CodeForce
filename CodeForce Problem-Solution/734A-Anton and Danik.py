b=int(input())
a=input()
A=0
D=0
for i in a:
    if i=='A':
        A=A+1
    else:
        D+=1
if A==D:
    print("Friendship")
elif A>D:
    print("Anton")
else:
    print("Danik")
          
