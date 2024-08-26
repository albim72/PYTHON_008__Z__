import time

#przykład 1
def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.time()
        funkcja()
        endtime = time.time()
        wynik = endtime - starttime
        print(f'czas wyskonania funkcji: {wynik} s')
    return wrapper

def usypiacz(funkcja):
    def wrapper():
        time.sleep(3)
        return funkcja()
    return wrapper

@usypiacz
@pomiarczasu
def big_lista():
    sum([i**5 for i in range(10_000_000)])

big_lista()

#przykład 2

def debug(funkcja):
    def wrapper(*args):
        print(f'wołana funkcja: {funkcja.__name__}')
        funkcja(*args)
    return wrapper

@debug
def info(i):
    print(f'zadany kod: {i}')

info("kod: absbdBS")
info(45348765)
