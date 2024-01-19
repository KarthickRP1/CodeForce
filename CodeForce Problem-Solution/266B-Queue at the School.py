z,b=map(int,input().split())
a=list(input())
word=''
c=''
for j in range(1,b+1):
    for i in range(len(a)-1):
        for k in range(len(a)-1):
            if a[i]=="B" and a[len(a)-1-k]=="G":
                c=a[len(a)-1-k]
                for z in range(len(a)-1-k,0,-1):
                    
                    a[z]=a[z-1]
                a[0]="G"
                
            else:
                continue;
        break;
    break
for i in a:
    word=word+i
            
print(word)
