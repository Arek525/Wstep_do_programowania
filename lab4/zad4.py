x = input("Podaj zdanie: ")
x = x.lower()
ile_a, ile_e, ile_i, ile_o, ile_u, ile_y = 0, 0, 0, 0, 0, 0
for c in x:
    if c == 'a':
        ile_a += 1
    elif c == 'e':
        ile_e += 1
    elif c == 'i':
        ile_i += 1
    elif c == 'o':
        ile_o += 1
    elif c == 'u':
        ile_u += 1
    elif c == 'y':
        ile_y += 1
print("a:", ile_a)
print("e:", ile_e)
print("i:", ile_i)
print("o:", ile_o)
print("u:", ile_u)
print("y:", ile_y)
