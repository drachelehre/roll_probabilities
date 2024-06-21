from random import randint


class System:
    def __init__(self, name, dice):
        self.name = name
        self.dice = dice

    def roll(self, die):
        raise NotImplementedError

    def __repr__(self):
        return f'System(name={self.name!r})'


dice_list = {
    'd4': 4,
    'd6': 6,
    'd8': 8,
    'd12': 12,
    'd20': 20,
    'd100': 100
}


class DungeonPath(System):
    def __init__(self, name, dice):
        super().__init__(name, dice)

    def roll(self, die):
        hit = randint(1, 20)
        if die not in dice_list:
            raise ValueError('Error: Not a valid die')
        damage = randint(1, dice_list[die])
        return hit, damage


class SixSiders(System):
    def __init__(self, name, dice):
        super().__init__(name, dice)

    def roll(self, die):
        hit = randint(1, 6)
        if die not in dice_list:
            raise ValueError('Error: Not a valid die')
        damage = randint(1, dice_list[die])
        return hit, damage


class FireMasque(System):
    def __init__(self, name, dice):
        super().__init__(name, dice)

    def roll(self, die):
        hit = randint(1, 100)
        if die not in dice_list:
            raise ValueError('Error: Not a valid die')
        damage = randint(1, dice_list[die])
        return hit, damage


class DungeonCoach(System):
    def __init__(self, name):
        super().__init__(name, None)  # No dice needed for DungeonCoach

    def roll(self):
        hit = randint(1, 20)
        return hit