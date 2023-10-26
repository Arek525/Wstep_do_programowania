x = int(input("Podaj liczbe naturalna: "))
tab = [[0 for i in range(x)] for j in range(x)]

for i in range(x):
    for j in range(x):
        if j % 2 == 0:
            tab[i][j] = 1
        else:
            tab[i][j] = 0

for rzad in tab:
    for element in rzad:
        print(element, end="")
    print()