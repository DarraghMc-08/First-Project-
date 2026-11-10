import math

class Resistor:
    def __init__(self, resistance_ohms):
        self.r = resistance_ohms

    def voltage(self, current):
        return self.r * current

    def current(self, voltage):
        return voltage / self.r 

class Thermistor(Resistor):
    def __init__(self, resistance_ohms, A=0.001, B=0.0002):
        super().__init__(resistance_ohms)
        self.A = A
        self.B = B
    def temperature(self):
        return 1.0 / (self.A + self.B * math.log(self.r))

therm = Thermistor(10000)
print(f"temperature: {therm.temperature():.2f} K")
print(f"current for 5v: {therm.current(5):.5f} A")
