# import dane
# import dane as dn
from dane import nrfilii as nf
from dane import book as bk

from funkcje.bfunkcje import czytaj_liste,czytaj_slownik
from klasy.classdata import CDane

print("______________ wyswietlenie bezpośrednie ________________")
print(nf)
print(bk)

print("______________ wyswietlenie za pomocą funkcji ________________")
czytaj_liste(nf)
czytaj_slownik(bk)

print("______________ wyswietlenie za pomocą modelu ________________")

cd = CDane(nf,bk)
cd.czytaj_l()
cd.czytaj_s()

