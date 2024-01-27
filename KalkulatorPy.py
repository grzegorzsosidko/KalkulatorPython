def kalkulator():
    print("Prosty Kalkulator")

    liczba1 = float(input("Wprowadź pierwszą liczbę: "))
    liczba2 = float(input("Wprowadź drugą liczbę: "))

    print("Wybierz operację, którą chcesz wykonać:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")

    wybor = input("Wybierz (1/2/3/4): ")

    if wybor == '1':
        print(f"Wynik: {liczba1 + liczba2}")
    elif wybor == '2':
        print(f"Wynik: {liczba1 - liczba2}")
    elif wybor == '3':
        print(f"Wynik: {liczba1 * liczba2}")
    elif wybor == '4':
        if liczba2 != 0:
            print(f"Wynik: {liczba1 / liczba2}")
        else:
            print("Błąd: Dzielenie przez zero!")
    else:
        print("Nieprawidłowy wybór")

kalkulator()
