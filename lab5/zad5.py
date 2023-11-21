naukowcy = (
    ("Einstein", "Albert"),
    ("Bohr", "Niels"),
    ("Oppenheimer", "J. Robert"),
    ("Newton", "Isaac"),
    ("Turing", "Alan")
)
nazwisko = input("Podaj nazwisko naukowca: ")
for i in naukowcy:
    if i[0] == nazwisko:
        print(i[1])
        break
