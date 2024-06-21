from game_system import System, DungeonPath


class Character:
    def __init__(self, name, level=1, bonus=None, weapons=None, spells=None, system=None):
        self.name = name
        self.level = level
        self.bonus = bonus
        self.weapons = weapons
        self.spells = spells
        self.system = system


    def use_system(self,system):
        match system:
            case 'D&D':
                return DungeonPath(system)

    def attack(self, weapon, num_attacks, die):
        game_system = self.use_system(self.system)
        if weapon not in self.weapons:
            raise ValueError('Error: weapon not held by character')
        difficulty = int(input("Target: "))
        hit_count = 0
        damage_count = 0
        for i in range(num_attacks):
            roll = game_system.roll(die) + self.bonus
            if roll[0] >= difficulty:
                hit_count += 1
                damage_count += roll[1]
        probability = (hit_count / num_attacks) * 100
        return f'{probability}% for {damage_count} from {weapon}'


