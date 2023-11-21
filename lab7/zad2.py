n = int(input("Podaj liczbe naturalna do 10: "))
tab = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        tab[i][j] = (j+1) * (i+1)

for row in tab:
    for e in row:
        print(e, "\t", end="")
    print()