import math
a = int(input("Podaj liczbe a:"))
b = int(input("Podaj liczbe b:"))
c = int(input("Podaj liczbe c:"))
delta = (b*b)-(4*a*c)
if delta > 0:
    x1 = (-1*b-math.sqrt(delta))/(2*a)
    x2 = (-1*b+math.sqrt(delta))/(2*a)
    print("Rozwiazania to: "+str(x1)+" oraz "+str(x2))
elif delta == 0:
    x0 = -b/(2*a)
    print("Rozwiazanie to: "+str(x0))
else:
    print("Rownanie nie ma rozwiazan")
