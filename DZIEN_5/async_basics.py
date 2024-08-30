import asyncio

async def function_async():
    for i in range(5):
        print("kod dostępu: A ->")
        print("734857238547438")
    return 0

loop = asyncio.get_event_loop()
loop.run_until_complete(function_async())

print("druga opcja A")
print("druga opcja B")
print("_"*50)

async def function_a2():
    for i in range(100_000):
        if i%50_000 == 0:
            print("kod dostępu dla B:")
            print("7886654324")
            await asyncio.sleep(0.01)
    return 0

async def function_b2():
    print("\ndruga opcja ABC\n")
    return 0

async def main():
    f1 = asyncio.create_task(function_a2())
    f2 = asyncio.create_task(function_b2())
    await asyncio.wait([f1,f2])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("_"*70)
