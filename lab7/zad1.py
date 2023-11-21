def usun_duplikaty(x):
    nowa_lista = []
    for el in x:
        if el not in nowa_lista:
            nowa_lista.append(el)
    return nowa_lista


x = 1
lista = []
print("Jesli chcesz skonczyc, dodaj 0")
while True:
    e = input(f"Podaj {x} element: ")
    if e == "0":
        break
    lista.append(e)
    x = x + 1

print("Lista poczatkowa: ", lista)
print("Lista po usunieciu duplikatow: ", usun_duplikaty(lista))
