from character import Character


def main():

    name = input("What's the character's name? ")
    level = int(input("What's their level? "))
    bonus = int(input('What is the general bonus to the attacks? '))
    add_weapon = False
    weapon_ask = input("Want to add some weapons?(y/n)")
    if weapon_ask != 'y' and weapon_ask != 'Y' and weapon_ask != 'n' and weapon_ask != 'N':
        raise Exception("Error: invalid response")
    if weapon_ask == "y" or weapon_ask == 'Y':
        add_weapon = True
    weapons = []
    while add_weapon:
        weapon_name = input('Please input a weapon name: ')
        weapons.append(weapon_name)
        weapon_ask = input("Want to add another weapon?(y/n) ")
        if weapon_ask != 'y' and weapon_ask != 'Y' and weapon_ask != 'n' and weapon_ask != 'N':
            raise Exception("Error: invalid response")
        if weapon_ask == "n" or weapon_ask == 'N':
            add_weapon = False
    add_spell = False
    spell_ask = input("Want to add some spells?(y/n) ")
    if spell_ask != 'y' and spell_ask != 'Y' and spell_ask != 'n' and spell_ask != 'N':
        raise Exception("Error: invalid response")
    if spell_ask == "y" or spell_ask == 'Y':
        add_spell = True
    spells = []
    while add_spell:
        spell_name = input('Please input a weapon name: ')
        spells.append(spell_name)
        spell_ask = input("Want to add another spell?(y/n) ")
        if spell_ask != 'y' and spell_ask != 'Y' and spell_ask != 'n' and spell_ask != 'N':
            raise Exception("Error: invalid response")
        if spell_ask == "n" or spell_ask == 'N':
            add_spell = False
    print("Current Game systems: \"D&D\", \"Pathfinder\", \"World of Darkness\", \"DC20\"")
    system = input('Which one would you like? ')
    new_character = Character(name, level, bonus, weapons, spells, system)
    while True:
        spell_or_attack = input("Is this a (s)pell or an (a)ttack? ")
        if spell_or_attack == "a":
            target = int(input('What\'s your target? '))
            print ("Your weapons:")
            for w in weapons:
                print(w)
            weapon = input("What weapon are you using? ")
            die = input("What is the damage die? (use d# format) ")
            print(new_character.attack(weapon, bonus, target, die))
        if spell_or_attack == "s":
            target = int(input('What\'s your target? '))
            print("Your spells:")
            for w in weapons:
                print(w)
            weapon = input("What spell are you using? ")
            die = input("What is the damage die? (use d# format) ")
            print(new_character.attack(weapon, bonus, target, die))
        again = input("Want to find another possible move? (y/n) ")
        if again != 'y' and again != 'Y' and again != 'n' and again != 'N':
            raise Exception("Error: invalid response")
        elif again == "y" and again == "Y":
            continue
        else:
            break


if __name__ == "__main__":
    main()
