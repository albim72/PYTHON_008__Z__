from errorclasses import IntFloatValueError, KeyValueConstructorError

class CustomIntFloatDict(dict):
    empty_dict = {}

    def get_dict(self):
        return self.empty_dict

    def __init__(self,key=None,value=None):
        if key is None or value is None:
            self.get_dict()
        elif not isinstance(key,(tuple,list,)) or not isinstance(value,(tuple,list,)):
            raise KeyValueConstructorError(key,value)
        else:
            zipped = zip(key,value)
            for k,val in zipped:
                if not isinstance(val,(int,float)):
                    raise IntFloatValueError(val)
                dict.__setitem__(self,k,val)

test_1 = CustomIntFloatDict()
print(test_1)

test_2 = CustomIntFloatDict(('a','b'))
print(test_2)

# test_3 = CustomIntFloatDict({'a','b'},[5,8])
# print(test_3)

# test_4 = CustomIntFloatDict(('x','y','z'),(10,'twenty',30))
# print(test_4)

test_5 = CustomIntFloatDict(('x','y','z'),(10,20,30))
print(test_5)
