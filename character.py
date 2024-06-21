import game_system
from game_system import System, DungeonPath, SixSiders, FireMasque, DungeonCoach

class Character:
    def __init__(self, name, level=1, bonus=0, weapons=None, spells=None, system=None):
        self.name = name
        self.level = level
        self.bonus = bonus
        self.weapons = weapons if weapons is not None else []
        self.spells = spells if spells is not None else []
        self.system = system

    @staticmethod
    def use_system(system):
        match system:
            case 'D&D':
                return DungeonPath(system, game_system.dice_list)
            case 'Pathfinder':
                return DungeonPath(system, game_system.dice_list)
            case 'World of Darkness':
                return SixSiders(system, game_system.dice_list)
            case 'DC20':
                return DungeonCoach(system)
            case _:
                raise ValueError('Error: Not a valid system')

    def calculate_hit_probability(self, die_size, difficulty):
        successful_outcomes = 0
        total_outcomes = die_size
        for outcome in range(1, die_size + 1):
            if outcome + self.bonus >= difficulty:
                successful_outcomes += 1
        return successful_outcomes / total_outcomes

    def attack(self, weapon, num_attacks, difficulty, die=None):
        system_used = self.use_system(self.system)
        if weapon not in self.weapons:
            raise ValueError('Error: weapon not held by character')
        hit_count = 0
        damage_count = 0
        die_size = game_system.dice_list.get(die, 20)  # Default to d20 if die is None
        hit_probability = self.calculate_hit_probability(die_size, difficulty)

        if not isinstance(system_used, DungeonCoach):
            for i in range(num_attacks):
                roll = system_used.roll(die)
                result = roll[0] + self.bonus
                if result >= difficulty:
                    damage_count += roll[1]
            probability = hit_probability**num_attacks
            return f'{probability:.2f}% chance to hit, potential {damage_count} damage from {num_attacks} {weapon} attacks (Hit probability per attack: {hit_probability:.2%})'
        else:
            for i in range(num_attacks):
                roll = system_used.roll()
                result = roll + self.bonus
                if result >= difficulty:
                    hit_count += 1
            probability = hit_probability**num_attacks
            return f'{probability:.2f}% chance to hit all {num_attacks} {weapon} attacks (Hit probability per attack: {hit_probability:.2%})'

