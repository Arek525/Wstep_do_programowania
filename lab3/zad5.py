slowo = input("Podaj slowo: ")
znak = input("Podaj znak: ")
dlugosc = len(slowo)
ile_razy = 0
for i in range(0, dlugosc):
    if slowo[i] == znak:
        ile_razy += 1
print("W slowie", slowo, "podany znak wystepuje", ile_razy, "razy")
