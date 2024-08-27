from libcalls.calls import CallCounter,RangeValidator

#prezentacja licznika wywołań funkcji
counter = CallCounter()
counter()
counter()
counter()
counter()

#prezentacja walidatora

valid = RangeValidator(2,16)
valid(3)
valid(2)
valid(19)
