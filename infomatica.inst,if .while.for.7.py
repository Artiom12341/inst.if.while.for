n=eval(input("dati n de ani ="))
b=0
c=1
a=0
for i in range(1,n+1):
    i=i+1
    c=c*2
    b=c+i
    a=a+b
    s=1+a
#Punct B
    if s>100:
        print("Varsta =",i-1)
print("Nr. de dolari=",s,"$")
