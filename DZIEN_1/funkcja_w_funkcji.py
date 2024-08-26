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
