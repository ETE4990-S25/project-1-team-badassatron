#game start 
#Game Title: War for Cybertron
#Game Description: Turn based RPG played as a Cybertronian in the midst of the Autobot and Decepticon War.
#Phase 1: Character Selection (with traits and strengths)
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
        elif character_class == "warrior"
            self.attack = 20

    def show_profile(self):
        return f"Name: {self.name}, Class: {self.character_class}, HP: {self.health}, Attack: {self.attack}, Heal: {self.heal}"
#Phase 2: Establish Inventory (dictionary with items and traits)

#Phase 3: First Event Sequence
#Phase 4: Event Path 1
#Phase 5: Event Path 2
#Phase 6: Event Path 3
#Phase 7: Event Path 4
#Game End with Stats -> Reset and Restart