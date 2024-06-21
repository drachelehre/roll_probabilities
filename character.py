from game_system import System, DungeonPath


class Character:
    def __init__(self, name, level=1, weapons=None, spells=None, system=None):
        self.name = name
        self.level = level
        self.weapons = weapons
        self.spells = spells
        self.system = system


    def use_system(self,system):
        match system:
            case 'D&D':
                return DungeonPath(system)


    def attack(self, weapon, num_attacks, die, system):
        game_system = self.use_system(system)
        if weapon not in self.weapons:
            raise ValueError('Error: weapon not held by character')
        difficulty = input("Target")
        probability = 1
        for i in range(num_attacks):
            roll = game_system.roll(die)


