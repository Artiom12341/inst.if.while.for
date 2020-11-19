n=eval(input("Dati n="))
m=eval(input("Dati m="))
k=0
a=0
while n>k:
    a=a+1
    k=m**a
    if n==k:
        print("N este puterea lui m")
    elif n<k:
        print("N nu este puterea lui m")
