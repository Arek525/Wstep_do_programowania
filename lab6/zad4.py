biblioteka = {}


def dodaj_ksiazke():
    autor = input("Podaj autora: ")
    tytul = input("Podaj tytuł: ")
    wydawnictwo = input("Podaj wydawnictwo: ")
    rok_wydania = input("Podaj rok wydania: ")

    ksiazka = {
        'autor': autor,
        'tytul': tytul,
        'wydawnictwo': wydawnictwo,
        'rok_wydania': rok_wydania
    }

    biblioteka[(autor, tytul)] = ksiazka
    print("Dodano ksiazke do bazy danych")


def usun_ksiazke():
    autor = input("Podaj autora książki do usunięcia: ")
    tytul = input("Podaj tytuł książki do usunięcia: ")
    if (autor, tytul) in biblioteka:
        del biblioteka[(autor, tytul)]
        print("Usunieto ksiazke")
    else:
        print("Nie znaleziono podanej ksiazki")


def modyfikuj_ksiazke():
    autor = input("Podaj autora książki do modyfikacji: ")
    tytul = input("Podaj tytuł książki do modyfikacji: ")

    if (autor, tytul) in biblioteka:
        nowy_autor = input("Podaj nowego autora (jeśli bez zmian, wciśnij Enter): ")
        nowy_tytul = input("Podaj nowy tytuł (jeśli bez zmian, wciśnij Enter): ")
        nowe_wydawnictwo = input("Podaj nowe wydawnictwo (jeśli bez zmian, wciśnij Enter): ")
        nowy_rok_wydania = input("Podaj nowy rok wydania (jeśli bez zmian, wciśnij Enter): ")

        if nowy_autor:
            biblioteka[(autor, tytul)]['autor'] = nowy_autor
        if nowy_tytul:
            biblioteka[(autor, tytul)]['tytul'] = nowy_tytul
        if nowe_wydawnictwo:
            biblioteka[(autor, tytul)]['wydawnictwo'] = nowe_wydawnictwo
        if nowy_rok_wydania:
            biblioteka[(autor, tytul)]['rok_wydania'] = nowy_rok_wydania

        print("Książka zaktualizowana.")
    else:
        print("Książka nie istnieje w bazie danych.")


def przeszukaj_baze():
    fraza = input("Podaj frazę do wyszukania: ")

    znalezione_ksiazki = []
    for (autor, tytul), ksiazka in biblioteka.items():
        if fraza.lower() in f"{ksiazka['autor']} {ksiazka['tytul']} {ksiazka['wydawnictwo']} {ksiazka['rok_wydania']}".lower():
            znalezione_ksiazki.append(ksiazka)

    if znalezione_ksiazki:
        print("Znalezione książki:")
        for ksiazka in znalezione_ksiazki:
            for i in ksiazka:
                print(i)
    else:
        print("Brak pasujących książek.")


def wyswietl_baze():
    print("Baza danych książek:")
    for (autor, tytul), ksiazka in biblioteka.items():
        print(f"Autor: {ksiazka['autor']}, Tytuł: {ksiazka['tytul']}, Wydawnictwo: {ksiazka['wydawnictwo']}, Rok wydania: {ksiazka['rok_wydania']}")


def wyswietl_menu():
    print("""
    MENU:
    1.Dodaj ksiazke
    2.Usun ksiazke
    3.Modyfikuj ksiazke
    4.Przeszukaj baze
    5.Wyswietl baze
    6.Wyjdz
    """)


while True:
    wyswietl_menu()
    wybor = input("Wybierz dzialanie: ")

    if wybor == "1":
        dodaj_ksiazke()
    elif wybor == "2":
        usun_ksiazke()
    elif wybor == "3":
        modyfikuj_ksiazke()
    elif wybor == "4":
        przeszukaj_baze()
    elif wybor == "5":
        wyswietl_baze()
    elif wybor == "6":
        break
    else:
        print("Nie ma opcji o podanym numerze")