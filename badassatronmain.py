#game start

def mainmenu():
    print('-----Savior of Cybertron----')
    print('Hello citizen, Crybertron needs your help. ')
    print('We are sending you on a mission to discover the who has been messing with the core of our home')
    print('The instructions are simple, choose as you see fit, and see where destiny sends you.')
    print('During interactions, you will take turns attacking until one is victorious.')
    print('')
    player.name = input('First, please tell us who you are: ')
    print('')
    Prelude()

#Phase 1: Prelude
#You are miner, given freedom(context), chose your path
def Prelude():
    print('Young {player.name}, Minerbot69420, your producton of energon has been lacking and Sentinel Prime is counting on you.')
    print(' ')
    print('As a miner you')
    print("   - work 14 hour work days")
    print('   - cannot transform ')
    print(' ')
    print("Sentinel Prime just announced a higher quota for this week, like a cog in a machine am I right? ")
    print('You are approached by a fellow miner about a rumor. Fellow miner, Orion Pax, has decided to revolt!')
    print('Please {player.name}, choose the path you wish to take...')
    print('   1. Revolt with Orion Pax and choose your destiny')
    print('   2. Continue to work in the mines.')
    option = input()
    if option == '1':
        character_selection()
    else:
        endgame_boring()

#Phase 2: Character Selection (with traits and strengths)
#put in function character_selection
def character_selection():
    class Player:
        def _init_(self, name, character_class):
            self.name = name
            self.character_class = character_class
            self.health = 100 #default health
            self.attack = 0 #default attack            self.heal = 0 #default heal
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
    

#Phase 3: Establish Inventory (dictionary with items and traits)
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

def endgame_boring():

if __name__== '__main__': #so the program will run, dont delete
    mainmenu()


#Phase 4: Event Path 1
#Phase 5: Event Path 2
#Phase 6: Event Path 3
#Phase 7: Event Path 4
#Game End with Stats -> Reset and Restart