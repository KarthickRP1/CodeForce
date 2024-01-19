f=input()
f=f.lower()
s=input()
s=s.lower()
if f==s:
    print("0")
    print(f.__sizeof__())
elif f>s:
    print("1")
else:
    print("-1")
