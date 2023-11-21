lista = []
while True:
    x = input("Podaj wyraz: ")
    if x == "0":
        break
    lista.append(x)
lista.sort()
for i in lista:
    print(i, end=" ")