import game_system
from game_system import System, DungeonPath
from character import Character


def main():
    john = Character("John", 1, 3, ['dagger'], system='DC20')
    target = int(input('What\'s your target? '))
    print(john.attack('dagger', 4, difficulty=target))


if __name__ == "__main__":
    main()
