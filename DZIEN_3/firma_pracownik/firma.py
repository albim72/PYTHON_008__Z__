class Firma:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.dzialy = []

    def dodaj_dzial(self, dzial):
        self.dzialy.append(dzial)

    def usun_dzial(self, dzial):
        if dzial in self.dzialy:
            self.dzialy.remove(dzial)
        else:
            print(f"Dział {dzial.nazwa} nie istnieje w firmie {self.nazwa}.")

    def wyswietl_dzialy_i_pracownikow(self):
        if not self.dzialy:
            print(f"Firma {self.nazwa} nie ma przypisanych działów.")
        else:
            print(f"Działy i pracownicy w firmie {self.nazwa}:")
            for dzial in self.dzialy:
                print(f"\n{dzial}")
                dzial.wyswietl_pracownikow()
