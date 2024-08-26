def czytaj_liste(lista):
    for i,j in enumerate(lista):
        print(f'elmement listy {i+1} -> wartosc: {j}')

def czytaj_slownik(slownik):
    for x,y in slownik.items():
        print(f'klucz: {x} -> wartosc: {y}')
