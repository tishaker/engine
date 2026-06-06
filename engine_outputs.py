class Engine_Output:
    def __init__(self, name, aura, power):
        self.name = name
        self.aura = aura
        self.power = power
    def engine_strength_output(self):
        print(f"{self.name} has an aura of {self.aura} and a power of {self.power}.")
        print(f"The engine strength output is: {self.aura * self.power}")
        return self.aura * self.power
    
class Engine_fap(Engine_Output):
    def __init__(self, name, aura, power, cum_amount):
        super().__init__(name, aura, power)
        self.cum_amount = cum_amount
    def engine_strength_output(self):
        super().engine_strength_output()
        print(f"{self.name} did huge cum work of {self.cum_amount}. kg")
        print(f"The total engine output with cum is: {(self.aura * self.power) + self.cum_amount}")
        return (self.aura * self.power) + self.cum_amount
