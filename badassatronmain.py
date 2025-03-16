#game start

def mainmenu():
    print('-----Savior of Cybertron----')
    print('Hello citizen, Crybertron needs your help. ')
    print('We are sending you on a mission to discover the who has been messing with the core of our home')
    print('The instructions are simple, choose as you see fit, and see where destiny sends you.')
    print('During interactions, you will take turns attacking until one is victorious.')
    print('')
    playername = input('First, please tell us who you are: ')
    print('')

#Phase 1: Prelude
#You are miner, given freedom(context), chose your path
def Prelude():
    print


    character_selection()

#Phase 2: Character Selection (with traits and strengths)

#put in function character_selection
class Player:
    def _init_(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100 #default health
        self.attack = 0 #default attack
        self.heal = 0 #default heal
        self.shield = 0 #default shield
        self.agility = 0 #default agility
        self.inventory = [] #Inventory starts empty
        self.set_attributes(character_class)

    def set_attributes(self, character_class):
        if character_class == "Medic":
            self.heal = 20
        elif character_class == "Warrior":
            self.attack = 20
        elif character_class == "Tank":
            self.shield = 20
        elif character_class == "Aerial":
            self.agility = 20
        else:
            print("Invalid character class")

    def show_profile(self):
        return f"Name: {self.name}, Class: {self.character_class}, HP: {self.health}, Attack: {self.attack}, Heal: {self.heal}, Shield: {self.shield}, Agility: {self.agility}"
    
    def combat (player, enemy):
        print(f"{player.name} faces {enemy.name} in combat!")

        while player.health > 0 and enemy.health > 0:
            action = input ("What will you do? (attack, heal, shield)")
            if action == "attack":
                enemy.health -= player.attack
            # Player attacks with a weapon
            # if player.inventory:
            #    weapon = next((item for item in player.inventory if isinstance(item, Weapon)), None)
            #   if weapon:
            #      enemy.health -= weapon.damage
            #     print(f"{player.name} attacks {enemy.name} for {weapon.damage} damage.")
            #else:
            #   print(f"{player.name} has no weapons!")
            #else:
            #   print(f"{player.name} has no items to attack with!")
                print(f"{player.name} attacks {enemy.name} for {player.attack} damage")
            elif action == "heal":
                player.health += player.heal
                print(f"{player.name} heals for {player.heal} health")
            elif action == "shield":
                player.health += player.shield
                print(f"{player.name} shields for {player.shield} health")
            else:
                print("Invalid action")
# Enemy attacks
        if enemy.health > 0:
            damage = random.randint(5, 10)
            player.health -= damage
            print(f"{enemy.name} attacks {player.name} for {damage} damage!")
            print(f"{player.name} has {player.health} health left")
            print(f"{enemy.name} has {enemy.health}

#Phase 2: Establish Inventory (dictionary with items and traits)
class Item:
    def __init__(self, name, damage, durability, blank):
        self.name = name 
        self.damage = damage
        self.durability = durability
        self.blank = blank #create item traits

    def use(self):
        if self.durability > 0:
            self.durability -= 1
            print (f'Used {self.name}, item health now {self.durability}')
        else:
            print(f'{self.name} is broken')
    
class Inventory:
    def __init__(self):
        self.items = []

    def add_item_to_bag(self, item)
        self.items.append(item)
        print()

Allspark=
Matrix_of_Leadership=
Axe= #warrior
Sword=
Bazooka=
Handheld_Turret=
Zapper= 
Shield= #tank
Energon=
Medpack= #medic
Jetpack= #aerial
Add_Changer= #gives new transformation


if __name__== '__main__': #so the program will run, dont delete
    mainmenu()


#Phase 3: First Event Sequence
#Phase 4: Event Path 1
#Phase 5: Event Path 2
#Phase 6: Event Path 3
#Phase 7: Event Path 4
#Game End with Stats -> Reset and Restart