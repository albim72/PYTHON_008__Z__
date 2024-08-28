class Pracownik:
    def __init__(self, imie, nazwisko, stanowisko, wynagrodzenie, id_dzialu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.wynagrodzenie = wynagrodzenie
        self.id_dzialu = id_dzialu

    def __str__(self):
        return (f"Pracownik: {self.imie} {self.nazwisko}, Stanowisko: {self.stanowisko}, "
                f"Wynagrodzenie: {self.wynagrodzenie} zł")
