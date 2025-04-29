import random
class player:
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
    
class Medic(player):
    def __init__(self, name):
        super().__init__(name)
        self.heal = 20

    def heal(self):
        self.health += self.heal_amount
        print(f"{self.name} heals for {self.heal_amount}. Health is now {self.health}.")

class Warrior(player):
    def __init__(self,name):
        super().__init__(name)
        self.attack_power = 20

class Tank(player):
    def __init__(self,name):
        super().__init__(name, health = 150)
        self.attack_power = 12
        self.armor = 5

    def take_damage(self, amount):
        reduced = max(amount-self.armor, 0) 
        super().take_damage(reduced)
        print(f"{self.name} armor reduces damge by {self.armor}.")   

class Aerial(player):
    def __init__(self,name):
        super().__init__(name)
        self.attack_power = 15
        self.agility = 20


def combat (player, enemy):
    print(f"\n {player.name} faces {enemy.name} in combat!")

    while player.alive() and enemy.alive():
        print("\n"+ player.show_profile())
        print(enemy.show_profile())

        action = input ("What will you do? (attack, heal)")

        if action == "attack":
            player.attack(enemy)
        elif action == "heal":
            player.heal()
        else:
            print("Invalid action")
# Enemy attacks
    if enemy.alive():
        damage = random.randint(5, 10)
        player.take_damage(damage)
        print(f"{enemy.name} counterattacks {player.name} for {damage} damage!")

print(f"\n Battle Over! {"You won!" if player.alive() else "You Lost!"}")
   