suma = 0
while True:
    skladnik = float(input("Podaj liczbe: "))
    if skladnik == 0:
        print("Laczna suma wynosi: " + str(suma))
        exit()
    else:
        suma += skladnik
