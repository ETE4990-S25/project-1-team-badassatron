#game start
import json

def mainmenu():
    print('-----Savior of Cybertron----')
    print('Hello citizen, Crybertron needs your help. ')
    print('We are sending you on a mission to discover the who has been messing with the core of our hom')
    playername = input('First, please tell us who you are: ')
    print('Now, we need to create your character. ')
    characterselection()

def characterselection():
    print('Where do you lie, (choices) ') #put choices of character class warrior minor officer etc.
                                        #make like hw 3

if __name__== '__main__':
    mainmenu()
#Phase 1: Character Selection (with traits and strengths)
#Phase 2: Establish Inventory (dictionary with items and traits)
#Phase 3: First Event Sequence
#Phase 4: Event Path 1
#Phase 5: Event Path 2
#Phase 6: Event Path 3
#Phase 7: Event Path 4
#Game End with Stats -> Reset and Restart