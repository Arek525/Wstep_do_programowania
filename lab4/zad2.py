x = input("Podaj zdanie: ")
if x[0].isupper() == False:
    print("Zdanie nie zaczyna sie wielka litera")
    exit()
if x[-1] != '.':
    print("Zdanie nie konczy sie kropka")
    exit()
if x[0].isupper() and x[-1] == '.':
    print("Zdanie jest prawidlowe")
