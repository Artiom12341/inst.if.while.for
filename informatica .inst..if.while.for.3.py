n=eval(input("Dati n="))
m=eval(input("Dati m="))
a=0
while m<n :
    a=a+1
    if (m**a==n):
        print("N este o putere a lui M")
        break   
    else:
        print("N  nu este o putere a lui M")
        break