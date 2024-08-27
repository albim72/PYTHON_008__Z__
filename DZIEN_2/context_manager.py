class ContextManager(object):
    def __init__(self):
        print("inicjacja funkcji init()")

    def __enter__(self):
        print("inicjacja funkcji enter()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("incjacja funkcji exit...")

with ContextManager() as manager:
    print("działanie wewnątrz instrukcji with")
