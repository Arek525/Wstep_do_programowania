def nwd(a, b):
    while b != 0:
        pom = b
        b = a % b
        a = pom
    return a


x = int(input("Podaj pierwsza liczbe: "))
y = int(input("Podaj druga liczbe: "))
print("NWD tych liczb wynosi:", nwd(x, y))
