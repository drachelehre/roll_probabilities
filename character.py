import game_system
from game_system import D20Sys, D6Sys, D100Sys, DungeonCoach


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
                return D20Sys(system, game_system.dice_list)
            case 'Pathfinder':
                return D20Sys(system, game_system.dice_list)
            case 'World of Darkness':
                return D6Sys(system, game_system.dice_list)
            case 'Call of Cthulhu':
                return D100Sys(system, game_system.dice_list)
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

    def calculate_hit_probability_inverse(self, die_size, difficulty):
        successful_outcomes = 0
        total_outcomes = die_size
        for outcome in range(1, die_size + 1):
            if outcome + self.bonus < difficulty:
                successful_outcomes += 1
        return successful_outcomes / total_outcomes

    # attacks or spells that have the attacker roll
    def attack(self, weapon, num_attacks, difficulty, die=None):
        system_used = self.use_system(self.system)
        if weapon not in self.weapons:
            raise ValueError('Error: weapon not held by character')
        hit_count = 0
        damage_count = 0

        # attacks that use systems that use 20-sided dice
        if isinstance(system_used, D20Sys):
            die_size = game_system.dice_list.get('d20')
            hit_probability = self.calculate_hit_probability(die_size, difficulty)
            for i in range(num_attacks):
                roll = system_used.roll(die)
                result = roll[0] + self.bonus
                if result >= difficulty:
                    damage_count += roll[1]
            probability = hit_probability**num_attacks
            return f'{probability:.2f}% chance to hit, potential {damage_count} damage from {num_attacks} {weapon} attacks (Hit probability per attack: {hit_probability:.2%})'

        # attacks using systems that use six-sided dice
        if isinstance(system_used, D6Sys):
            die_size = game_system.dice_list.get('d6')
            hit_probability = self.calculate_hit_probability(die_size, difficulty)
            for i in range(num_attacks):
                roll = system_used.roll(die)
                result = roll[0] + self.bonus
                if result >= difficulty:
                    damage_count += roll[1]
            probability = hit_probability ** num_attacks
            return f'{probability:.2f}% chance to hit, potential {damage_count} damage from {num_attacks} {weapon}'

        if isinstance(system_used, D100Sys):
            die_size = game_system.dice_list.get('d6')
            hit_probability = self.calculate_hit_probability_inverse(die_size, difficulty)
            for i in range(num_attacks):
                roll = system_used.roll(die)
                result = roll[0] + self.bonus
                if result <= difficulty:
                    damage_count += roll[1]
            probability = hit_probability ** num_attacks
            return f'{probability:.2f}% chance to hit, potential {damage_count} damage from {num_attacks} {weapon}'

        # DC20 system
        if isinstance(system_used, DungeonCoach):
            die_size = game_system.dice_list.get('d20')
            hit_probability = self.calculate_hit_probability(die_size, difficulty)
            for i in range(num_attacks):
                roll = system_used.roll()
                result = roll + self.bonus
                if result >= difficulty:
                    hit_count += 1
            probability = hit_probability**num_attacks
            return f'{probability:.2f}% chance to hit all {num_attacks} {weapon} attacks (Hit probability per attack: {hit_probability:.2%})'

    def cast_spell(self, spell, difficulty):
        system_used = self.use_system(self.system)
        if spell not in self.spells:
            raise ValueError('Error: spell not known by character')

        # spells that use systems that use 20-sided dice
        if isinstance(system_used, D20Sys) or isinstance(system_used, DungeonCoach):
            die_size = game_system.dice_list.get('d20')
            hit_probability = self.calculate_hit_probability_inverse(die_size, difficulty)
            return f'{hit_probability:.2f}% chance to hit {spell})'

        if isinstance(system_used, D100Sys):
            die_size = game_system.dice_list.get('d20')
            hit_probability = self.calculate_hit_probability_inverse(die_size, difficulty)
            return f'{hit_probability:.2f}% chance to hit {spell})'

        if isinstance(system_used, D6Sys):
            die_size = game_system.dice_list.get('d20')
            hit_probability = self.calculate_hit_probability_inverse(die_size, difficulty)
            return f'{hit_probability:.2f}% chance to hit {spell})'
