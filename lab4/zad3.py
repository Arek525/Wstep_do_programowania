x = input("Podaj zdanie: ")
x = x.replace(" ", "")
x = x.lower()

ile = int(len(x) / 2)
koniec = len(x)-1

for i in range(ile):
    if x[i] != x[koniec]:
        print("Zdanie nie jest palindromem")
        exit()
    koniec -= 1

print("Zdanie jest palindromem")
