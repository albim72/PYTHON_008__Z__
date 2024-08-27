from dataclasses import dataclass

class Liczba:
    def __init__(self,x,y):
        self.x = x
        self.y = y

liczba = Liczba(5,2)
print(liczba.x)
print(liczba)

@dataclass
class DLiczba:
    x:int
    y:int
    z:float

dl = DLiczba(6,3,7)
print(dl.x)
print(dl)

@dataclass
class Dane:
    nazwa:str
    licznik:int=0
    cena:float=0.0

    @property
    def licznik(self):
        return self._licznik

    @licznik.setter
    def licznik(self,nl):
        self._licznik = nl

p=Dane("pudełko",4,11.45)
print(f'produkt: {p.nazwa} -> cena: {p.cena} zł -> licznik: {p.licznik}')

p.licznik = 89
print(f'produkt: {p.nazwa} -> cena: {p.cena} zł -> licznik: {p.licznik}')
