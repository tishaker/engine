class Engine_new:
    def __init__(self, name, aura, power):
        self.name = name
        self.aura = aura
        self.power = power
    def engine_strength_output(self):
        print(f"{self.name} has an aura of {self.aura} and a power of {self.power}.")
        print(f"The engine strength output is: {self.aura * self.power}")
        return self.aura * self.power
    
engine1 = Engine_new("Engine1", 10, 5)
engine1.engine_strength_output()
