class Osoba:
    def __init__(self,imie,nazwisko,wiek,waga,wzrost):
        self._imie = imie
        self._nazwisko = nazwisko
        self._wiek = wiek
        self._waga = waga
        self._wzrost = wzrost

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self,nowywiek):
        self._wiek = nowywiek

    @property
    def bmi(self):
        return self._waga/(self._wzrost/100)**2



os = Osoba("Jan","Kowal",30,89,173)
print(os)
print(os.wiek)
os.wiek = 45
print(os.wiek)
print(os.bmi)
