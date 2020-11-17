n=eval(input("dati n="))
s1=0
s2=0
b=0
for i in range (0,n+1):
    i=i+1
    s1=s1+(i**3)
for i in range(0,n+1):
    i=i+1
    b=b+i
    s2=b**2
if s1 > s2:
    print("s1 mai mare ca s2")
if s1 < s2:
    print("s1 mai mic ca s2")
if s1 == s2:
    print("s1=s2")
#Punctul B
for i in range(0,n+1):
    i=i+1
    b=b+(i**2)
    s1=3*b
for i in range(0,n+1):
    i=i+1
    b=b+i
    s2=n**3+n**2+b
if s1 > s2:
    print("s1 mai mare ca s2")
if s1 < s2:
    print("s1 mai mic ca s2")
if s1 == s2:
    print("s1=s2")
