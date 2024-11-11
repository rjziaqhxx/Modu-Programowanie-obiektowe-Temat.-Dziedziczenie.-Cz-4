class Device:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.ofon = False

    def switch(self):
        if self.ofon == False:
            self.ofon = True
            print('Device is on')
        else:
            self.ofon = False
            print('Device is off')
    
    def getinfo(self):
        print(f'Device name - {self.name}, device power - {self.power}, is device on - {self.ofon}')

class CoffeeMachine(Device):
    def __init__(self, name, power, water_tank):
        super().__init__(name, power)
        self.water_tank = water_tank
        self.coffee_made = 0

    def make_coffee(self):
        if self.ofon:
            self.coffee_made += 1
            print(f'Coffee made, coffee made: {self.coffee_made}')
        else:
            print(f'{self.name} is off')

    def getinfo(self):
        base_info = super().getinfo()
        return f"{base_info}, water tank capacity - {self.water_tank}"

class Blender(Device):
    def __init__(self, name, power, speed_levels):
        super().__init__(name, power)
        self.speed_levels = speed_levels

    def blend(self):
        if self.ofon:
            print(f'Blende with {self.speed_levels} speed level')
        else:
            print(f'{self.name} is off')

    def getinfo(self):
        base_info = super().getinfo()
        return f"{base_info}, speed levels - {self.speed_levels}"
    
class MeatGrinder(Device):
    def __init__(self, name, power, capacity):
        super().__init__(name, power)
        self.capacity = capacity

    def grind(self):
        if self.ofon:
            print(f'Meat grinded, machine capacity - {self.capacity}')
        else:
            print(f'{self.name} is off')
    
    def getinfo(self):
        base_info = super().getinfo()
        return f'{base_info}, capacity - {self.capacity}'
    
coffee_machine = CoffeeMachine("Ekspres do kawy", 1500, 1.5)
blender = Blender("Blender", 800, 5)
meat_grinder = MeatGrinder("Maszynka do miesa", 1200, 3)

print(coffee_machine.getinfo())
coffee_machine.switch()
coffee_machine.make_coffee()
coffee_machine.switch()

print(blender.getinfo())
blender.switch()
blender.blend()
blender.switch()

print(meat_grinder.getinfo())
meat_grinder.switch()
meat_grinder.grind()
meat_grinder.switch()