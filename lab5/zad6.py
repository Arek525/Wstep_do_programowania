v1, v2 = [], []
ile = int(input("Ilo wymiarowe beda twoje wektory: "))

for i in range(1, ile+1):
    x = int(input("Podaj "+str(i)+" wspolrzedna 1 wektora: "))
    v1.append(x)

for i in range(1, ile+1):
    x = int(input("Podaj "+str(i)+" wspolrzedna 2 wektora: "))
    v2.append(x)

iloczyn = 0
for i in range(0, ile):
    iloczyn += (v1[i] * v2[i])
print("Iloczyn skalarny tych wektorow wynosi", iloczyn)
