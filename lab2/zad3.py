import os
print("Jesli wcisniesz x, to przestane sie wyswietlac: ")
while True:
    znak = input()
    if znak == "x":
        os.system('cls')
        exit()
