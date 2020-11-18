import fractions
n=eval(input("Dati n="))
n1=eval(input("Dati n1="))
b=eval(input("Dati b="))
b1=eval(input("Dati b1="))
s= fractions.Fraction(n,n1)+  fractions.Fraction(b,b1)
p=  fractions.Fraction(n,n1)*  fractions.Fraction(b,b1)
print("Suma fractiilor =",s)
print("produsul fractiilor=",p)
