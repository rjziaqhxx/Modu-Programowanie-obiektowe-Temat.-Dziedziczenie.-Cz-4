class Ship:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def get_info(self):
        return f'{self.name} - Length - {self.length}'

class Frigate(Ship):
    def __init__(self, name, length, weapon_system):
        super().__init__(name, length)
        self.weapon_system = weapon_system

    def fire_weapon(self):
        print(f'{self.name} is firing weapons - {self.weapon_system}')

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}, weapon System - {self.weapon_system}'

class Destroyer(Ship):
    def __init__(self, name, length, radar_system):
        super().__init__(name, length)
        self.radar_system = radar_system

    def activate_radar(self):
        print(f'{self.name} is activating radar system - {self.radar_system}')

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}, radar System - {self.radar_system}'

class Cruiser(Ship):
    def __init__(self, name, length, defense_system):
        super().__init__(name, length, )
        self.defense_system = defense_system

    def activate_defense(self):
        print(f'{self.name} is activating defense system - {self.defense_system}')

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}, defense System - {self.defense_system}'



frigate = Frigate('ship1', 123, 'weapon')
destroyer = Destroyer('ship2', 155, 'radar')
cruiser = Cruiser('ship3', 186, 'defense')

print(frigate.get_info())
frigate.fire_weapon()
print(destroyer.get_info())
destroyer.activate_radar()
print(cruiser.get_info())
cruiser.activate_defense()