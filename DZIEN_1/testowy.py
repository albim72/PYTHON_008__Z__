print("to jest pierwszy skrypt testowy!")
print("programowanie funkcyjne!")

#przykład 1
def witaj(imie:str)->str:
    return f'Miło mi Cię widzie {imie}'

def konkurs(imie,punkty,miejsce):
    return f'uczestnik konkursu: {imie}, liczba punktów: {punkty}, miejsce: {miejsce}'

def bonus(punkty,bonus):
    if punkty >=51:
        return punkty + bonus
    else:
        return punkty

print(witaj("Anna"))
print(witaj(4343.556))

def osoba(funkcja,*args):
    return funkcja(*args)

print(osoba(witaj,"Leon"))
print(osoba(konkurs,"Iwona",56,7))

print(osoba(bonus,67,10))
