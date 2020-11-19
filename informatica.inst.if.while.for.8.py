a= float(input("Dati a="))
b= float(input("Dati b="))
c= float(input("Dati c="))
if ((a>0) and (b>0) and (c>0)):
    if ((a+b>c) and (a+c>b) and (b+c>a)):
        if ((a==b) and (a==c) and (b==c)):
            print ("triunghi -Echilateral")
        elif ((a==b) or (a==c) or (b==c)):
            print("triunghi -Isoscel")
        else:
            print("triunghi -Scalen")
    else:
        print("Nu exista triunghi cu laturile date")
else :
    print ("Introdu numerele reale POZITIVE")