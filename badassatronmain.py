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
    print('Now, we need to create your character. ')
    characterselection()

#Phase 1: Character Selection (with traits and strengths)
import json #store info?
def characterselection():
    print('Where do you lie, (choices) ') #put choices of character class warrior minor officer etc.
                                        #make like hw 3 


#Phase 2: Establish Inventory (dictionary with items and traits)
import json




if __name__== '__main__': #so the program will run, dont delete
    mainmenu()


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
        elif character_class == "Warrior"
            self.attack = 20
        elif character_class == "Tank"
            self.shield = 20
        elif character_class == "Aerial"
            self.agility = 20
        else:
            print("Invalid character class")

    def show_profile(self):
        return f"Name: {self.name}, Class: {self.character_class}, HP: {self.health}, 
        Attack: {self.attack}, Heal: {self.heal}, Shield: {self.shield}, Agility: {self.agility}, Inventory: {self.inventory}"
#Phase 2: Establish Inventory (dictionary with items and traits)

#Phase 3: First Event Sequence
#Phase 4: Event Path 1
#Phase 5: Event Path 2
#Phase 6: Event Path 3
#Phase 7: Event Path 4
#Game End with Stats -> Reset and Restart