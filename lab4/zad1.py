x = input("Podaj pierwsze slowo: ")
y = input("Podaj drugie slowo: ")
dl1 = len(x)
dl2 = len(y)
if dl1 > dl2:
    print("Pierwsze slowo jest dluzsze")
elif dl2 > dl1:
    print("Drugie slowo jest dluzsze")
else:
    print("Slowa sa rownej dlugosci")
