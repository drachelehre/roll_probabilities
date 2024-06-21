import random


class System:
    def __init__(self, name):
        self.name = name

    def roll(self):
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


class DungeonPath:
    def __init__(self, name):
        super().__init__()

    def roll(self, die):
        hit = int(random.random(1, 20))
        if die not in dice_list:
            raise ValueError('Error: Not a valid die')
        damage = int(random.random(1, dice_list[die]))
        return hit, damage

