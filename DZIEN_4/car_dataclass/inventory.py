from dataclasses import dataclass,field
from typing import List
from car import Car

@dataclass
class CarInventory:
    cars:List[Car] = field(default_factory=list)
    
    def add_car(self,car:Car) -> None:
        """dodawanie samochodu do inwentarza"""
        self.cars.append(car)
        print(f"dodano samochód do inwentarza: {car.car_description()}")
        
    def remove_car(self,car:Car) -> None:
        """usuwanie samochodu z inwentarza"""
        if car in self.cars:
            self.cars.remove(car)
            print(f"usunięto samochód z inwentarza: {car.car_description()}")
        else:
            print("Samochód nie znaleziony w inwentarzu!")
            
    def list_inventory(self)->None:
        "wypisuje wszystkie samochody wpisane do inwnetarza"
        print("Inwentarz samochodów salonu EasyCar")
        for car in self.cars:
            print(car.car_description())
            
    def find_cars_by_mark(self,mark:str)->List[Car]:
        """filtowanie wszytskich samochodów wybranej marki"""
        return [car for car in self.cars if car.mark.lower() == mark.lower()]
