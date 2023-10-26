x = int(input("Podaj liczbe, z ktorej oblicze silnie: "))
suma = 1
for i in range(2, x+1):
    suma *= i

print(x, "silnia wynosi: ", suma)