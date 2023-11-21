x = input("Podaj ciag znakow: ")

dl = len(x)
for i in range(dl):
    for j in range(i+1, dl+1):
        substring = ""
        for k in range(i, j):
            substring += x[k]
        print(substring)
