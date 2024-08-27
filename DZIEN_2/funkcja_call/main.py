from libcalls.calls import CallCounter,RangeValidator,CacheFunction

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

#prezentacja obsługi cache

def efunction(x,y):
    return x**y + y**x

#obiekt CacheFunction
ce_func = CacheFunction(efunction)

print(ce_func(2,3))
print(ce_func(2,2))
print(ce_func(2,3))
print(ce_func(13,1))
print(ce_func(13,3))
print(ce_func(13,3))
print(ce_func(2,3))
