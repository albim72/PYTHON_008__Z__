from trojkat import Trojkat
from prostokat import Prostokat
from trapez import Trapez

tr = Trojkat(5.6,8.7)
print(f'pole figury {tr.__class__.__name__} wynosi {tr.policz_pole():.2f} cm2')
print('_'*50)

pr1 = Prostokat(4,6.4)
print(f'pole figury {pr1.__class__.__name__} wynosi {pr1.policz_pole():.2f} cm2')
print('_'*50)

pr2 = Prostokat(5.1,5.1)
print(f'obiekt klasy: {type(pr2)}!')
print(f'pole figury {pr2.__class__.__name__} wynosi {pr2.policz_pole():.2f} cm2')
print('_'*50)

trp = Trapez(8.3,5.8,4.6)
print(f'pole figury {trp.__class__.__name__} wynosi {trp.policz_pole():.2f} cm2')
print('_'*50)
