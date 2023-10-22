def kalkulator(wybor, a, b):
    if wybor == "1":
        return a+b
    elif wybor == "2":
        return a-b
    elif wybor == "3":
        return a*b


print("1. Dodawanie\n2. Odejmowanie\n3. Mnożenie")

dzialanie = input("Wybierz dzialanie: ")
x = float(input("Podaj pierwsza liczbe: "))
y = float(input("Podaj druga liczbe: "))
print("Wynik to:", kalkulator(dzialanie, x, y))
