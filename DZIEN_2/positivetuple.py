class PositiveTuple(tuple):
    def __new__(cls, *numbers):
        skipped = 0
        pos_numbers = []
        for x in numbers:
            if x>=0:
                pos_numbers.append(x)
            else:
                skipped += 1
        instance = super().__new__(cls,pos_numbers)
        instance._skipped = skipped
        return instance

posnb = PositiveTuple(9,-4,56,-9,0,19,-234,568,0,32,-45,-556,987,9,1,4,8,16,4,-5)
print(type(posnb))
print(posnb)
print(posnb._skipped)
