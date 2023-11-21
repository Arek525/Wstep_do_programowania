a = int(input("Podaj pierwsza liczbe naturalna: "))
b = int(input("Podaj druga liczbe naturalna: "))

zbior1 = set()
zbior2 = set()

for i in range(1, a*b):
    zbior1.add(i*a)
    zbior2.add(i*b)
    nww = zbior1.intersection(zbior2)
    if len(nww):
        print(nww)
        break
