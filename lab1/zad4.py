import math
print("Podaj dwie liczby typu zmiennoprzecinkowego: ")

liczba1 = float(input("Pierwsza liczba: "))
liczba2 = float(input("Druga liczba: "))

dodawanie = liczba1+liczba2
odejmowanie = math.floor(liczba1-liczba2)
mnozenie = math.floor(liczba1*liczba2)
dzielenie = math.floor(liczba1/liczba2)

print("Dodawanie: " + str(dodawanie))
print("Odejmowanie: " + str(odejmowanie))
print("Mnozenie: " + str(mnozenie))
print("Dzielenie: " + str(dzielenie))
