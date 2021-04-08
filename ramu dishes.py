t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    ty=[]
    for j in l:
        if j not in ty:
            ty.append(j)
    o=[]
    for m in ty:
        c=0
        f=0
        for n in l:
            if(f==0 and m==n):
                f=1
                c=c+1
            else:
                f=0  
        o.append(c)
    m=max(o)
    for k in range(len(o)):
        if(o[k]==m):
            print(ty[k])
            break
      
                    
            
