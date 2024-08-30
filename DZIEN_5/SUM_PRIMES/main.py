import time
import concurrent.futures
from funkcja_prime import znajdz_sume_liczb_pierwszych

numbers = [(1,10_000),(3,50_000),(5_000,100_000),(4,900),(8_000,15_0000),(95_000,133_500),(255,67_760)]

def synchronicznie():
    starttime = time.time()
    for pair in numbers:
        st = time.time()
        prime_suma = znajdz_sume_liczb_pierwszych(*pair)
        et = time.time()
        print(f'wynik = {prime_suma}, czas wykonania: {et-st} s')
    endtime = time.time()

    print(f'całkowity czas wyznaczenia sum (synchronicznie): {endtime-starttime} s')

def main():
    synchronicznie()

if __name__ == '__main__':
    main()
