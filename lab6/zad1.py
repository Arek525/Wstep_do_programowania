import math


def sito(n):
    tab = [1 for i in range(n+1)]
    tab[0] = tab[1] = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if tab[i] == 1:
            for j in range(i*i, n+1, i):
                tab[j] = 0
    return tab

n = int(input("Podaj ilosc liczb: "))
liczby = set(range(1, n+1))
print(liczby)

tablica = sito(n)
for i in range(n+1):
    if tablica[i] == 1:
        print(i, end=" ")
