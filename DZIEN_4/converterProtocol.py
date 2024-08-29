from typing import Protocol,Union

#protokół
class Convertible(Protocol):
    def convert(self,data:str) -> Union[int,float]:
        pass

#implementacje protokołu
class IntegerConverter:
    def convert(self,data:str)->int:
        return int(data)

class FloatConverter:
    def convert(self,data:str)->float:
        return float(data)

class BoolConverter:
    def convert(self,data:str)->bool:
        data = float(data)
        return bool(data)

def convert_data(converter:Convertible,data:str) -> Union[int,float]:
    return converter.convert(data)


int_conv = IntegerConverter()
flt_conv = FloatConverter()
bl_conv = BoolConverter()

res_int = convert_data(int_conv,"756")
res_float = convert_data(flt_conv,"6.876")
res_bool = convert_data(bl_conv,"1")
res_bool2 = convert_data(bl_conv,"0")

print(f'konwersja na int: {res_int} -> typ: {type(res_int)}')
print(f'konwersja na float: {res_float} -> typ: {type(res_float)}')
print(f'konwersja na bool: {res_bool} -> typ: {type(res_bool)}')
print(f'konwersja na bool: {res_bool2} -> typ: {type(res_bool2)}')
