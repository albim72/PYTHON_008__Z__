class Resistor:
    def __init__(self,ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

    def __repr__(self):
        return f"obiekt klasy {self.__class__.__name__}"

    def __str__(self):
        return f"komunikat tekstowy - opisujący obiekt klasy {self.__class__.__name__}"

