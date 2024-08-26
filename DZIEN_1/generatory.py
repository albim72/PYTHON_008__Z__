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


print("%"*12)

k = wznowienia(7,5)
next(k)
next(k)

print("%"*12)

#przykład 3

def sendgen():
    x = 0
    while True:
        y = yield x
        if y is None:
            x=x+1
        else:
            x = y*3


g = sendgen()
print("_"*60)
print(next(g))
print(next(g))
print(next(g))
print(g.send(132))
print(next(g))
print(next(g))
print(next(g))
print(g.send(88))
print(next(g))
print(next(g))

