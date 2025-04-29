class Player:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health
        self.attack_power = 10

    def alive(self):
        return self.health > 0
    
    def attach(self,target):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")
        target.take_damage(self.attack_power)
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Health is now {self.health}.")

    def show_profile(self):
        return f"Name: {self.name}, Class: {self.character_class}, HP: {self.health}, Attack: {self.attack}, Heal: {self.heal}, Shield: {self.shield}, Agility: {self.agility}"
    
class Medic(Player):
    def __init__(self, name):
        super().__init__(name)
        self.heal = 20

    def heal(self):
        self.health += self.heal_amount
        print(f"{self.name} heals for {self.heal_amount}. Health is now {self.health}.")

class Warrior(Player):
    def __init__(self,name):
        super().__init__(name)
        self.attack_power = 20

class Tank(Player):
    def __init__(self,name):
        super().__init__(name, health = 150)
        self.attack_power = 12
        self.armor = 5

    def take_damage(self, amount):
        reduced = max(amount-self.armor, 0) 
        super().take_damage(reduced)
        print(f"{self.name} armor reduces damge by {self.armor}.")   

class Aerial(Player):
    def __init__(self,name):
        super().__init__(name)
        self.attack_power = 15
        self.agility = 20


def combat (player, enemy):
    print(f"\n {player.name} faces {enemy.name} in combat!")

    while player.health > 0 and enemy.health > 0:
        action = input ("What will you do? (attack, heal, shield)")
        if action == "attack":
            enemy.health -= player.attack
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
   