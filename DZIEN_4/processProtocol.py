from typing import Protocol,List,Any
import numpy as np

class DataProcessor(Protocol):
    def process(self,data:List[Any])->List[Any]:
        pass

class NumberProcessor:
    def process(self, data: List[Any]) -> List[Any]:
        return [item*2 for item in data if isinstance(item,int) or isinstance(item,float)]

class StringProcessor:
    def process(self, data: List[Any]) -> List[Any]:
        return [item.upper() for item in data if isinstance(item,str)]

#funckja przyjmująca obiekt zgodny z protokołem DataProcessor
def process_data(processor:DataProcessor,data:List[Any])->List[Any]:
    return processor.process(data)

number_processor = NumberProcessor()
string_processor = StringProcessor()


data_to_process = [1,2,3,4,5,6.74,0.53,"hej","zielony","456","d",[4,6,"coś"]]
array_tonp = [4,7,3,7,3,8,9,51,6,-35,0,2.33,4.44]
array_tonp = np.array(array_tonp,dtype=float)
print(type(array_tonp))
proc_nb = process_data(number_processor,data_to_process)
proc_str = process_data(string_processor,data_to_process)

print(f'wynik dla liczb: {proc_nb}')
print(f'wynik dla tekstu: {proc_str}')
print(f"TEST DLA NUMPY --->")
proc_nbnp = process_data(number_processor,array_tonp)
proc_strnp = process_data(string_processor,array_tonp)

print(f'wynik dla liczb: {proc_nbnp}')
print(f'wynik dla tekstu: {proc_strnp}')
