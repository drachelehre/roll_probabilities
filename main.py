from game_system import System, DungeonPath
import character


def main():
    dungeons = DungeonPath("Dungeons and Dragons")
    print(dungeons.roll('d4'))


if __name__ == "__main__":
    main()
