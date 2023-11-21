x = input("Podaj zdanie: ")
ile_slow = 0
for c in x:
    if c == ' ':
        ile_slow += 1
print("Wystapilo slow:", ile_slow+1)#+1 bo po ostatnim slowie raczej nie wystepuje spacja, a slowo sie liczy