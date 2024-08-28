class Dzial:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.pracownicy = []

    def dodaj_pracownika(self, pracownik):
        self.pracownicy.append(pracownik)

    def usun_pracownika(self, pracownik):
        if pracownik in self.pracownicy:
            self.pracownicy.remove(pracownik)
        else:
            print(f"Pracownik {pracownik.imie} {pracownik.nazwisko} nie istnieje w dziale {self.nazwa}.")

    def wyswietl_pracownikow(self):
        if not self.pracownicy:
            print(f"Dział {self.nazwa} nie ma przypisanych pracowników.")
        else:
            print(f"Pracownicy w dziale {self.nazwa}:")
            for pracownik in self.pracownicy:
                print(f" - {pracownik}")

    def __str__(self):
        return f"Dział: {self.nazwa}, Liczba pracowników: {len(self.pracownicy)}"
