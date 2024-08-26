#przykład 1

def liczby():
    wynik = []
    for i in range(21):
        wynik.append(i*2)
    return wynik

print(liczby())

def liczbygen():
    for i in range(21):
        yield i*2

print(liczbygen())
print(list(liczbygen()))

for p in liczbygen():
    print(p)

