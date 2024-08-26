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
