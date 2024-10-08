from resistor import Resistor

class VoltageResistance(Resistor):

    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0
        
    @property
    def voltage(self):
        return self._voltage
    
    @voltage.setter
    def voltage(self,voltage):
        self._voltage = voltage
        self.current = self._voltage/self.ohms
