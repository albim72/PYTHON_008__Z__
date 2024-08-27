from oldresistor import OldResistor
from resistor import Resistor

print("__________ klasa OldResistor ___________")
r0 = OldResistor(10.2E2)
print(r0)
# print(r0._ohms)
# r0._ohms = 0.45E3
# print(r0._ohms)
print(r0.get_ohms())
r0.set_ohms(0.45E3)
print(r0.get_ohms())

print("__________ klasa Resistor ___________")
r1 = Resistor(5.5E3)
print(r1)
r1.ohms = 18.9
print(f'układ elektryczny:\nopornośc: {r1.ohms} omów\n'
      f'napięcie prądu: {r1.voltage} mV\nnateżenie prądu: {r1.current} mA')
