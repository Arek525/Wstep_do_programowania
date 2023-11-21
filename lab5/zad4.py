lista = [i for i in range(1, 101)]
lista2 = [i for i in lista if i % 3 == 0]
for i in lista2:
    print(i, end=" ")
