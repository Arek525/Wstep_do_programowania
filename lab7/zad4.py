import random

def trans(a, b, tab):
    wynik = [[0 for i in range(b)] for j in range(a)]
    for i in range(b):
        for j in range(a):
            wynik[j][i] = tab[i][j]
    return wynik

a = int(input("Podaj 1 wymiar macierzy: "))
b = int(input("Podaj 2 wymiar macierzy: "))
tab = [[random.randint(1, 100) for i in range(a)] for j in range(b)]
print("Macierz przed transpozycja:")
for row in tab:
    print(row)

print("Macierz po transpozycji:")
druga = trans(a, b, tab)
for row in druga:
    print(row)