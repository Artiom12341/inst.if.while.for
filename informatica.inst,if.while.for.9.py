n= eval(input("Dati n ="))
for i in range(1,n+1):
    s=0
    for a in range(1,i):
        if (i%a==0):
            s=s+a
    if (s==i):
        print("numar prim=",i,end=' ')
 

