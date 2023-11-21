import itertools

n = int(input("Ile elementow ma byc w zbiorze?: "))
zbior = set()
for i in range(n):
    x = input(f"Podaj {str(i+1)} element: ")
    zbior.add(x)

potegowy = set()
for i in range(1, n+1):
    potegowy.update(itertools.combinations(zbior, i))

for i in potegowy:
    print(i)
