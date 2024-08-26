#przykład 2
def rejestracja(oplata):
    def lista(nr):
        return f'jesteś na liście zawodników pod numerem: {nr}'
    def brak():
        return f'brak opłaty. Doknaj jak najszybciej!'
    def error():
        return f'błąd! ponów proces zapisu...'

    if oplata == 1:
        return lista
    elif oplata == 0:
        return brak
    else:
        return error

print(rejestracja(1)(645))
print(rejestracja(0)())
print(rejestracja(453)())

#przykład 3 -> prosty dekorator

def startstop(funkcja):
    def wrapper(*args):
        print("*"*50)
        print("startowanie procesu...")
        funkcja(*args)
        print("kończenie procesu...")
    return wrapper

def zawijanie(w_co):
    print(f"zawijanie czekoladek w {w_co}")

zw = startstop(zawijanie)
zw("sreberka")

@startstop
def dmuchanie(czego):
    print(f'dmuchanie {czego} na urodziny!')

dmuchanie("baloników")

#przykład 4

liczby = [45,67,890,-345,0,11,478,25,9,-233,-4,4,35,27,-21,3,100,-56]

parzyste = list(filter(lambda x:x%2==0,liczby))
print(parzyste)

cube = list(map(lambda x:x**3,liczby))
print(cube)

#list comprehension
dane = [i**2 for i in range(10_000)]
print(dane)
