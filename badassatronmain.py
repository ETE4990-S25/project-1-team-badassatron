#game start

import random

def mainmenu():
    print('-----Savior of Cybertron----')
    print('Hello citizen, Crybertron needs your help. ')
    print('We are sending you on a mission to discover the who has been messing with the core of our home')
    print('The instructions are simple, choose as you see fit, and see where destiny sends you.')
    print('During interactions, you will take turns attacking until one is victorious.')
    print('')
    player = input('First, please tell us who you are: ')
    print('')
    Prelude()

#Phase 1: Prelude
#You are miner, given freedom(context), chose your path
def Prelude():
    print('Young {player}, Minerbot69420, your producton of energon has been lacking and Sentinel Prime is counting on you.')
    print(' ')
    print('As a miner you')
    print("   - work 14 hour work days")
    print('   - cannot transform ')
    print(' ')
    print("Sentinel Prime just announced a higher quota for this week, like a cog in a machine am I right? ")
    print('You are approached by another bot about a rumor. Fellow miner, Orion Pax, has decided to revolt!')
    print('Please {player}, choose the path you wish to take...')
    print('   1. Revolt with Orion Pax and choose your destiny')
    print('   2. Continue to work in the mines.')
    option = input()
    if option == '1':
        character_selection()
    else:
        endgame_boring()

#Phase 2: Character Selection (with traits and strengths)
#put in function character_selection
def character_selection(): #move above menu so it can be called out 
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
            print(f"{enemy.name} has {enemy.health}")
            

#Phase 3: Establish Inventory (dictionary with items and traits)
class Item:
    def __init__(self, name, durability, blank):
        self.name = name 
        self.durability = durability
        self.blank = blank #create item traits

    def use(self):
        if self.durability > 0:
            self.durability -= 1
            print (f'Used {self.name}, item health now {self.durability}')
        else:
            print(f'{self.name} is broken')
class Weapon(Item):
    def __init__(self,name, durability, blank, damage):
        super().__init__(name, durability, blank) #Will add functions after we figure out more story
        self.damage = damage
class Wearable(Item):
    def __init__(self,name, durability, blank):
        super().__init__(name, durability, blank) #Will add functions after we figure out more story

class Inventory:
    def __init__(self):
        self.items = [] #when player chooses character, items automatically added to inventory

    def add_item_to_pack(self, item):
        self.items.append(item)
        print(f'{item.name} has been added to your pack')

    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
            print(f'{item.name} has been removed from your pack')
        else:
            print(f'{item.name} is not in your pack.')

    def use_item(self,item):
        if item in self.items:
            item.use()
            item.durability  -= 10
        else:
            print(f'{item.name} is not in your pack.')

player_inventory = Inventory()

#item list
Allspark= Item("Allspark", 1000000, None)
Matrix_of_Leadership= Item("Matrix of Leadership",1000000, None)
Axe= Weapon("Axe", 20, 100, None)
Sword= Weapon("Sword", 30, 100, None)
Bazooka= Weapon("Bazooka", 40, 100, None)
Handheld_Turret= Weapon("Handheld Turret", 40, 100, None)
Zapper= Weapon("Zapper", 20, 100, None)
Shield= Item("Shield", 200, None)
Energon= Item("Energon", 100000, None)
Medpack= Item("Medpack", 100, None)
Jetpack= Wearable("Jetpack", 200, None )
Add_Changer= Wearable("Transformer", 1000000, None)

def endgame_boring():
    print("Ending: You continue to work in the mines. Orion Pax's revolt is crushed before it even begins and more miners are succumbing to the harsh conditions.")
    print("As time goes on, the energon reserves are depleted and the planet is dying. You are one of the last surviving Cybertronians.")
    print("It is revealed that Sentinel Prime was offloading the energon to the Quintessons, enemies to the planet of Cybertron.")
    print("Sentinel Prime, in his greed to claim leadership from the 13 Primes, has doomed the planet and its inhabitants.")

def ending_prime():
    print("Because of your integrity and bravery, you have been chosen to be the next Prime. You have saved Cybertron from the brink of destruction.")
    print("You have been granted the Matrix of Leadership. With it, the planet can now flow energon freely and the inhabitants can thrive once more.")
    print("Miner bots rejoice and hail you as 'Omega Prime'.")

def ending_autobot():
    print('You have chosen to take Sentinel Prime into custody and take him to trial for his crimes against Cybertron.')
    print('It is admirable you have chose this path. You make a good recruit alongside the Autobots.')
    print('With Orion Pax as the new Prime, the Autobots will lead Cybertron to a new era of peace and prosperity.')

def ending_decepticon():
    print('Revenge is the only answer, welcome to the decepticons. Megatron is pleased that you have ended the reign of Sentinel Prime.')
    print('Orion Pax is weak and will not be able to lead Cybertron to a new era of peace and prosperity.')
    print('The Decepticons will rule Cybertron with an iron fist.')

def ending_megatron():
    print('Inspired by the fallen leader, Megatronus Prime, you have taken the name Megatron.')
    print('')

if __name__== '__main__': #so the program will run, dont delete
    mainmenu()


#Phase 4: Event Path 1 Sneaking into the Iacon 5000

#Phase 5: Event Path 2 Escape from Sublevel 50 with B-127

#Phase 6: Event Path 3 Captured by the Cybertronian High Guard

#Phase 7: Event Path 4 Exposing Sentinel to the city

#Game End with Stats -> Reset and Restart