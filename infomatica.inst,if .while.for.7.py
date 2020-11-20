n=eval(input("dati n de ani ="))
a=0
c=1
for i in range(1,n+1):
    c=c*2
    a=c+i
#Punct B
if a>=100:
    print("Varsta =",i)
print("Nr. de dolari=",a,"$")
