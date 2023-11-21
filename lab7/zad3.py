def szyfr_cezara(slowo, n):
    zaszyfrowane = ""
    for i in range(len(slowo)):
        if ord(slowo[i].lower()) + n > ord('z'):
            zaszyfrowane = zaszyfrowane + chr(ord(slowo[i]) + n - 26)
        else:
            zaszyfrowane = zaszyfrowane + chr(ord(slowo[i]) + n)

    return zaszyfrowane


slowo = input("Podaj slowo: ")
n = int(input("Podaj liczbe: "))
print(slowo, "Zaszyfrowane kluczem", n, " to :", szyfr_cezara(slowo, n))
