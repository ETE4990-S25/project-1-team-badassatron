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
        self.health = 100
        self.attack = 0
        self.heal = 0
        self.inventory = []
        self.set_attributes(character_class)

    def set_attributes(self, character_class):
        if character_class == "medic":
            self.heal = 20
        elif character_class == "warrior":
            self.attack = 20

    def show_profile(self):
        return f"Name: {self.name}, Class: {self.character_class}, HP: {self.health}, Attack: {self.attack}, Heal: {self.heal}"
    

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

#Phase 2: Establish Inventory (dictionary with items and traits)

#Phase 3: First Event Sequence
#Phase 4: Event Path 1
#Phase 5: Event Path 2
#Phase 6: Event Path 3
#Phase 7: Event Path 4
#Game End with Stats -> Reset and Restart