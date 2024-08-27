from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance

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

print("__________ klasa VoltageResistance ___________")
r2 = VoltageResistance(1E3)
print(f'początkowe natężenie prądu: {r2.current} A')
r2.voltage = 50.5
print(f'napięcie prądu: {r2.voltage} V')
print(f'natężenie prądu: {r2.current} A')
