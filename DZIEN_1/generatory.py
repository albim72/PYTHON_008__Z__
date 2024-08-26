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

#przykład 2
def wznowienia(n,k):
    print("wstrzymanie działania 0")
    yield 3004
    print("wznowienie działania 1")

    print("wstrzymanie działania 1")
    yield n+k
    print("wznowienie działania 2")

    n = 8*k-4
    print("wstrzymanie działania 2")
    yield n-k
    print("wznowienie działania 3")

    print("wstrzymanie działania 3")
    yield n*k
    print("wznowienie działania 4")

    print("wstrzymanie działania 4")
    yield n/k
    print("wznowienie działania 5")

print(wznowienia(7,5))
print(tuple(wznowienia(7,5)))
for i in wznowienia(7,5):
    print("_"*50)
    print(type(i))
    print(f'zwrócono wartośc {i}')
