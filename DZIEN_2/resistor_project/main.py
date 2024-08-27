from oldresistor import OldResistor

print("__________ klasa OldResistor ___________")
r0 = OldResistor(10.2E2)
print(r0)
# print(r0._ohms)
# r0._ohms = 0.45E3
# print(r0._ohms)
print(r0.get_ohms())
r0.set_ohms(0.45E3)
print(r0.get_ohms())
