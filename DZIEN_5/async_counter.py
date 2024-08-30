import time
import asyncio


def licz():
    print("start synchro")
    time.sleep(2)
    print("koniec synchro")
async def count():
    print("start")
    await asyncio.sleep(2)
    print("koniec")

async def main():
    await asyncio.gather(count(),count(),count())

def mm():
    for _ in range(3):
        licz()


if __name__ == '__main__':
    print("pomiar wykonania synchronicznego....")
    s = time.perf_counter()
    mm()
    elapsed = time.perf_counter() - s
    print(f'{__file__} wykonany w czasie: {elapsed:.2f} s')
    print("pomiar wykonania asynchronicznego....")
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f'{__file__} wykonany w czasie: {elapsed:.2f} s')
