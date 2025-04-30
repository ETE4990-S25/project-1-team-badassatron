import random
class Player:
    def __init__(self, name, health = 100, attack_power =10):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.character_class = self.__class__.__name__

    def __str__(self):
        return self.show_profile()
    
    def alive(self):
        return self.health > 0
    
    def attack(self,target):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")
        target.take_damage(self.attack_power)
    
    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Health is now {self.health}.")

    def show_profile(self):
        return f"Name: {self.name}, Class: {self.character_class}, HP: {self.health}, Attack: {self.attack_power}"
    
class Medic(Player):
    def __init__(self, name):
        super().__init__(name, health = 80, attack_power = 8)
        self.heal_amount = 10

    def heal(self):
        self.health += self.heal_amount
        print(f"{self.name} heals for {self.heal_amount}. Health is now {self.health}.")

class Warrior(Player):
    def __init__(self,name):
        super().__init__(name, health = 100, attack_power = 20)

class Tank(Player):
    def __init__(self,name):
        super().__init__(name, health = 150, attack_power = 12)
        self.armor = 5

    def take_damage(self, amount):
        reduced = max(amount-self.armor, 0) 
        super().take_damage(reduced)
        print(f"{self.name} armor reduces damge by {self.armor}.")   

class Aerial(Player):
    def __init__(self,name):
        super().__init__(name, health = 100, attack_power = 15)
        self.agility = 20


def combat (player, enemy):
    print(f"\n {player.name} faces {enemy.name} in combat!")

    while player.alive() and enemy.alive():
        print(f"\n"+ player.show_profile())
        print(enemy.show_profile())

        action = input ("What will you do? (attack, heal):  ").strip().lower()

        if action == "attack":
            player.attack(enemy)
        elif action == "heal":
            if hasattr(player, "heal"):
                player.heal()
            else:
                print("You cannot heal...")
        else:
            print("You cannot heal...")

        # Enemy attacks
        if enemy.alive():
            damage = random.randint(5, 10)
            player.take_damage(damage)
            print(f"{enemy.name} counterattacks {player.name} for {damage} damage!")

    if enemy.health <= 10:
        print(f"{enemy.name} is critically wounded.")

    print(f"\n Battle Over! {'You won!' if player.alive() else 'You Lost!'}")     

#Phase 1: Start    
def mainmenu():
    global player
    print('-----Savior of Cybertron----')
    print('\n Hello citizen, Crybertron needs your help. ')
    print('We are sending you on a mission to discover the who has been messing with the core of our home')
    print('The instructions are simple, choose as you see fit, and see where destiny sends you.')
    print('During interactions, you will take turns attacking until one is victorious.')

    player_name= input('\n First, please tell us who you are: ').strip()
    player = character_selection(player_name)
    Prelude(player)

def character_selection(name):
    classes = {
        "Medic": Medic,
        "Warrior" : Warrior,
        "Tank" : Tank,
        "Aerial" : Aerial
    }

    print("\n Please choose your path: ")
    for class_name in classes:
        print(f"- {class_name}")

    while True:
        choice = input("Enter class: ").strip()
        if choice in classes:
            player = classes[choice](name)
            print(f"You have chosen {player.character_class}")
            return player
        else:
            print("Invalid choice")

#Phase 2: Prelude
def Prelude(player):
    print('-----------------------------------------------------------------------------------')
    print(f'\n Young {player.name}, Minerbot69420, your producton of energon has been lacking and Sentinel Prime is counting on you.')
    print('\n As a miner you')
    print("   - work 14 hour work days")
    print('   - cannot transform ')
    print("\n Sentinel Prime just announced a higher quota for this week, like a cog in a machine am I right? ")
    print('You are approached by another bot about a rumor. Fellow miner, Orion Pax, has decided to revolt!')
    print(f'\n Please {player.name}, choose the path you wish to take...')
    print('   1. Revolt with Orion Pax and choose your destiny')
    print('   2. Continue to work in the mines.')
    option = input().strip()
    if option == '1':
        print(player.show_profile())
        sneak_into_iacon_5000(player.name)
    elif option == '2':
        ending_boring(player.name)
    else:
        print("Invalid input. Please choose option 1 or 2.")
        Prelude(player)

#Phase 3: Establish Inventory (dictionary with items and traits)

class Item:
    def __init__(self, name, durability, traits=None):
        self.name = name 
        self.durability = durability
        self.traits = traits if traits else [] #create item traits

    def use(self):
        if self.durability > 0:
            self.durability -= 1
            print (f'Used {self.name}, item durability now {self.durability}')
        else:
            print(f'{self.name} is broken!')

class Weapon(Item):
    def __init__(self,name, durability, traits=None, damage=0):
        super().__init__(name, durability, traits) #Will add functions after we figure out more story
        self.damage = damage

        def use(self):
            if self.durability > 0:
                self.durability -= 1
                print (f'Attacked with {self.name}, damage: {self.damage}, durability now {self.durability}')
                return self.damage
            else:
                print(f'{self.name} is broken!')
                return 0
            
class Wearable(Item):
    def __init__(self,name, durability, traits=None):
        super().__init__(name, durability, traits) #Will add functions after we figure out more story

class Inventory:
    def __init__(self):
        self.items = [] #when player chooses character, items automatically added to inventory

    def add(self, item):
        self.items.append(item)
        print(f'{item.name} has been added to your invertory.')

    def remove(self,item):
        if item in self.items:
            self.items.remove(item)
            print(f'{item.name} has been removed.')
        else:
            print(f'{item.name} not found in inventory.')

    def use(self,item_name):
        for item in self.items:
            if item.name == item_name.lower():
                item.use()
                return
        print(f'{item_name} not found in inventory.')

    def list_items(self):
        if not self.items:
            print("Your inventory is empty.")
            return
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} (Durability: {item.durability})")

player_inventory = Inventory()

#item list
Allspark = Item("Allspark", 1_000_000)
Matrix_of_Leadership = Item("Matrix of Leadership", 1_000_000)
Axe = Weapon("Axe", 20, damage=15)
Sword = Weapon("Sword", 30, damage=20)
Bazooka = Weapon("Bazooka", 40, damage=50)
Handheld_Turret = Weapon("Handheld Turret", 40, damage=35)
Zapper = Weapon("Zapper", 20, damage=25)
Shield = Item("Shield", 200)
Energon = Item("Energon", 100_000)
Medpack = Item("Medpack", 100)
Jetpack = Wearable("Jetpack", 200)
Add_Changer = Wearable("Transformer", 1_000_000)

def ending_boring(name):
    print('-----------------------------------------------------------------------------------')
    print("Boring Ending:")
    print("You continue to work in the mines. Orion Pax's revolt is crushed before it even begins and more miners are succumbing to the harsh conditions.")
    print("As time goes on, the energon reserves are depleted and the planet is dying. You are one of the last surviving Cybertronians.")
    print("It is revealed that Sentinel Prime was offloading the energon to the Quintessons, enemies to the planet of Cybertron.")
    print("Sentinel Prime, in his greed to claim leadership from the 13 Primes, has doomed the planet and its inhabitants.")
    game_end() #send to end menu to view stats and have restart option

def game_end():
    print("\nThank you for playing Savior of Cybertron!")
    choice = input("Would you like to play again? (yes/no): ").lower()
    if choice == "yes":
        mainmenu()
    elif choice == "no":
        print("Stay safe warrior!")
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
    exit()

def ending_prime():
    print('-----------------------------------------------------------------------------------')
    print("Because of your integrity and bravery, you have been chosen to be the next Prime. You have saved Cybertron from the brink of destruction.")
    print("You have been granted the Matrix of Leadership. With it, the planet can now flow energon freely and the inhabitants can thrive once more.")
    print("Miner bots rejoice and hail you as 'Omega Prime'.")

def ending_autobot():
    print('-----------------------------------------------------------------------------------')
    print('You have chosen to take Sentinel Prime into custody and take him to trial for his crimes against Cybertron.')
    print('It is admirable you have chose this path. You make a good recruit alongside the Autobots.')
    print('With Orion Pax as the new Prime, the Autobots will lead Cybertron to a new era of peace and prosperity.')

def ending_decepticon():
    print('-----------------------------------------------------------------------------------')
    print('Revenge is the only answer, welcome to the decepticons. Megatron is pleased that you have ended the reign of Sentinel Prime.')
    print('Orion Pax is weak and will not be able to lead Cybertron to a new era of peace and prosperity.')
    print('The Decepticons will rule Cybertron with an iron fist.')

def ending_megatron():
    print('-----------------------------------------------------------------------------------')
    print('Inspired by the fallen leader, Megatronus Prime, you have taken the name Megatron.')
    print('Through your actions, you have shown that the Autobots are not to be trusted with the fate of Cybertron.')
    print('You attempt to take the Matrix of Leadership, but it rejects you. You are bitter towards Orion Pax, for who you believe is too weak to lead Cybertron.')

#Phase 4: Event Path 1 Sneaking into the Iacon 5000
def sneak_into_iacon_5000(player):
    print('-----------------------------------------------------------------------------------')
    print("\n Welcome to the Iacon 5000, the best race in all of Cybertron!")
    print("You have an important decision to make.")
    print("Orion Pax has a plan to sneak into the Iacon 5000 and make a name for the minerbots.")

    choice = input("\n Join Orion Pax and equip a jet pack? (Yes/No): ").strip().lower()

    if choice == "yes":
        print("\n You decided to join Orion Pax and equip a jet pack for the race.")
        print("With your jet pack, you fly past the competition, winning the race!")
        print("The crowd goes wild that two minerbots have won the Iacon 5000 without the ability to transform.")
    elif choice == "no":
        print("\n You decided not to join Orion Pax and watch from the sidelines.")
        print("You still enter the race, but without the jet pack, you fall terribly behind!")
        print("Your loss is a disappointment and the transformers laugh at you and Orion Pax for trying to race")
    else:
        print("\n Invalid input. Please type 'yes' or 'no'.")
        while True:
                choice = input("Do you want to join Orion Pax and equip a jet pack" "yes/no): ").lower()
                if choice in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
                    continue
    escape_from_sublevel_50(player)

#Phase 5: Event Path 2 Escape from Sublevel 50 with B-127
    
def escape_from_sublevel_50(player_name):
    print('-----------------------------------------------------------------------------------')
    print("\nYou and Orion Pax are kicked down to Sublevel 50 by one of Sentinel Prime's guards.")
    print("As you tumble down, you land in the depths of Cybertron, in a dark and eerie sector filled with old mining equipment.")
    
    print("\nHere, you meet B-127, a friendly miner bot in charge of all the scrap metal. B-127 explains that he's been working here alone, building sculptures out of old parts.")
    print("As you interact with B-127, you accidentally knock into one of his friends and their head falls off, popping out a disc.")
    
    print("\nB-127 plays the disc for you. It's a **distress message** from the legendary **Alpha Trion**. The message reveals that the Primes are on a mission and they were told to meet in a cave, "
          "with coordinates pointing to the surface of Cybertron.")
    
    print("\nThis discovery fills you with determination. You and Orion Pax decide to set course for the surface to uncover the truth behind what happened to the Primes.")
    print("On your way out of Sublevel 50, you encounter another robot named **Elita**, a warrior who shares your interest in finding out the truth.")
    
    print("\nNow, the three of you venture out of your comfort zones to unravel the mysteries of Cybertron and the disappearance of the Primes.")
    print("You hop aboard a cargo train carrying loads of **Energon** on a path to the surface of Cybertron.")

    print("\nBut as the train speeds through the tunnels, your group is suddenly attacked by **random invaders**! They think you're looting the energon!")

    battle_choice(player_name)

def battle_choice(player):
        print(' ')
        print("\nYou are now being attacked by random invaders while on the cargo train!")
        print("Choose an item from your inventory to use in the battle:")
    
        # Display available inventory items
        for i, item in enumerate(player_inventory.items, 1):
            print(f"{i}. {item.name} Durability: {item.durability}")
    
        # Ask player to choose an item
        try:
            choice = int(input("\nEnter the number of the item you wish to use: "))
            if 1 <= choice <= len(player.inventory.items):
                selected_item = player.inventory.items[choice - 1]
                print(f"\nYou used {selected_item.name}!")
                selected_item.use()
            else:
                print("\nInvalid choice!")
        except ValueError:
            print("\nPlease enter a number.")

#Phase 6: Event Path 3 Captured by the Cybertronian High Guard

if __name__== '__main__': #so the program will run, dont delete
    mainmenu()

def battle_choice2(player_name):
    print("\nYou are captured by the Cybertronian High Guard. You must decide what to do next.")
    print("Do you fight Starscream to create a batallion or give your respect to the High Guard?")
    
    choice = input("Choose an option:\nA) Fight Starscream and create a batallion.\nB) Give your respect to the High Guard and let someone else take charge.\nEnter A or B: ").lower()

    if choice == "a":
        print("\nYou chose to fight Starscream and create a batallion.")
        print("You rally the Cybertronian High Guard to your cause, promising that together, you will overthrow Sentinel Prime.")
        print("Starscream, seeing the growing rebellion, challenges you to a final showdown!")
        
        # Simulate the outcome of the battle
        battle_result = random.choice(["win", "lose"])
        
        if battle_result == "win":
            print("\nYour resolve and leadership inspire the High Guard. You defeat Starscream, and the batallion stands for you!")
            print("The tide begins to turn as more Cybertronians join your cause.")
        else:
            print("\nDespite your efforts, Starscream's ruthless tactics overpower you, and you are crushed.")
            print("The resistance is scattered, and you are forced to retreat.")
    
    elif choice == "b":
        print("\nYou chose to give your respect to the High Guard and let someone else take charge.")
        print("You acknowledge the wisdom of the High Guard and trust them to lead the way back to Iacon City.")
        print("Together, you manage to stay out of Sentinel Prime's reach, and the journey back begins.")
        print("However, the fight against Sentinel’s rule is far from over. The High Guard will need time to gather strength.")
    else:
        print("\nInvalid choice! Please select 'A' or 'B'.")

def cybertronian_high_guard_encounter():
    print("You arrive at the cave where the truth is revealed.")
    print("As you and your group carefully step inside, you see the **deactivated Alpha Trion** alongside the **corpses of the 12 other Primes**.")
    print("Your heart sinks at the sight of the fallen heroes of Cybertron.")
    
    print("\nYou manage to reactivate Alpha Trion using some **Energon** you saved from the cargo train you narrowly escaped earlier.")
    print("As his systems power back online, Alpha Trion looks at you with weary eyes.")
    
    print("\nAlpha Trion reveals the truth: **Sentinel Prime** was the cause of the Primes' demise. He set them up in a cruel trap to steal the **Matrix of Leadership** and take control of Cybertron for himself.")
    print("Sentinel, however, was unworthy to wield the Matrix, and as a result, it rejected him, becoming lost in the chaos. With no Primes left to lead, the planet stopped producing Energon.")
    
    print("\nThis loss of Energon prompted Sentinel to devise a sickening plan to remove the cogs from many Transformers and reprogram them as **miner bots**, forcing them to harvest the remaining Energon reserves deep within the planet.")
    print("\nYou are filled with anger at this realization, and before you can speak, you hear the sound of **Sentinel Prime's guards** closing in on your location.")
    
    print("\nAlpha Trion, realizing the urgency, quickly hands you, Orion Pax, B-127, and Elita the **cogs of the fallen Primes**. He urges you to escape before it's too late.")
    
    print("\nYou make your way out of the cave, but as you try to hide, you run into the **Cybertronian High Guard**—a group of warriors thought to be long gone alongside the Primes.")
    print("They are scared of what Sentinel would do to them and the invading **Quintessons** if they are discovered. The High Guard captures your group and are in a stalement on what to do with 4 puny minerbots.")

    # Let the player make a choice for the next course of action
    battle_choice2()

#Phase 7: Event Path 4 Exposing Sentinel to the city
import random

# Define player and enemy stats
player_health = 100
arachnid_health = 150
sentinel_health = 100

# Define a function for the battle with Arachnid (3 rounds)
def battle_arachnid():
    global player_health, arachnid_health
    
    print("\nYour group has made their way to Iacon City. It is here where you face off against Arachnid!")
    print(f"Arachnid's Health: {arachnid_health} | Your Health: {player_health}")
    print("\nArachnid is a fierce opponent, quick to strike and relentless in combat.")
    
    rounds = 3
    for round in range(1, rounds + 1):
        print(f"\nRound {round} begins!")
        print(f"Arachnid's Health: {arachnid_health} | Your Health: {player_health}")
        
        # Let the player choose an item from their inventory
        print("\nChoose an item from your inventory to use in this round:")
        for i, item in enumerate(player_inventory.items, 1):
            print(f"{i}. {item}")
        choice = int(input("\nEnter the number of the item you wish to use: "))
        
        if choice == 1:
            print("\nYou equip the Laser Sword and charge at Arachnid!")
            damage = random.randint(15, 30)
            arachnid_health -= damage
            print(f"You hit Arachnid for {damage} damage!")
        elif choice == 2:
            print("\nYou equip the Energy Shield and brace for Arachnid's attack!")
            damage = random.randint(5, 15)
            player_health -= damage
            print(f"Arachnid attacks you for {damage} damage!")
        elif choice == 3:
            print("\nYou use the Repair Kit to heal yourself!")
            heal = random.randint(10, 20)
            player_health += heal
            print(f"You heal for {heal} health!")
        elif choice == 4:
            print("\nYou use the Holo-map to strategize your next move!")
            damage = random.randint(10, 20)
            arachnid_health -= damage
            print(f"You use the Holo-map to outsmart Arachnid and deal {damage} damage!")
        elif choice == 5:
            print("\nYou use the Jet Pack to dodge Arachnid's attacks!")
            damage = random.randint(5, 10)
            arachnid_health -= damage
            print(f"You evade and strike back with a quick attack, dealing {damage} damage!")
        else:
            print("\nInvalid choice! Arachnid takes advantage of your hesitation!")
            damage = random.randint(20, 30)
            player_health -= damage
            print(f"Arachnid attacks you for {damage} damage!")

        # Check if either combatant's health reaches 0
        if arachnid_health <= 0:
            print("\nYou have defeated Arachnid!")
            return "win"
        if player_health <= 0:
            print("\nYou have been defeated by Arachnid.")
            return "lose"

# Define a function for the final battle with Sentinel Prime (1 round)
def battle_sentinel(player):
    global player_health, sentinel_health
    
    print("\nNow you face **Sentinel Prime** in a final battle!")
    print(f"Sentinel Prime's Health: {sentinel_health} | Your Health: {player_health}")
    
    # Let the player choose an item from their inventory for the final battle
    print("\nChoose an item from your inventory to use in this final round:")
    for i, item in enumerate(player.inventory.items, 1):
        print(f"{i}. {item}")
    choice = int(input("\nEnter the number of the item you wish to use: "))
    
    if choice == 1:
        print("\nYou equip the Laser Sword and charge at Sentinel Prime!")
        damage = random.randint(20, 40)
        sentinel_health -= damage
        print(f"You hit Sentinel Prime for {damage} damage!")
    elif choice == 2:
        print("\nYou equip the Energy Shield to defend against Sentinel Prime's attack!")
        damage = random.randint(15, 25)
        player_health -= damage
        print(f"Sentinel Prime attacks you for {damage} damage!")
    elif choice == 3:
        print("\nYou use the Repair Kit to heal yourself!")
        heal = random.randint(20, 30)
        player_health += heal
        print(f"You heal for {heal} health!")
    elif choice == 4:
        print("\nYou use the Holo-map to confuse Sentinel Prime!")
        damage = random.randint(15, 30)
        sentinel_health -= damage
        print(f"Sentinel Prime is confused, and you deal {damage} damage!")
    elif choice == 5:
        print("\nYou use the Jet Pack to evade Sentinel Prime's attacks!")
        damage = random.randint(10, 20)
        sentinel_health -= damage
        print(f"You strike while dodging and deal {damage} damage to Sentinel Prime!")
    else:
        print("\nInvalid choice! Sentinel Prime takes advantage of your hesitation!")
        damage = random.randint(30, 50)
        player_health -= damage
        print(f"Sentinel Prime attacks you for {damage} damage!")
    round_counter = 1
    while player_health > 0 and sentinel_health > 0:
        print(f"Round {round_counter}")
    round_counter += 1

        # Let the player choose an item from their inventory for the final battle
    print("\nChoose an item from your inventory to use in this final round:")
    for i, item in enumerate(player_inventory.items, 1):
            print(f"{i}. {item}")
    choice = int(input("\nEnter the number of the item you wish to use: "))
        
    if choice == 1:
            print("\nYou equip the Laser Sword and charge at Sentinel Prime!")
            damage = random.randint(20, 40)
            sentinel_health -= damage
            print(f"You hit Sentinel Prime for {damage} damage!")
    elif choice == 2:
            print("\nYou equip the Energy Shield to defend against Sentinel Prime's attack!")
            damage = random.randint(15)
    
    # Check the health after the battle
    if sentinel_health <= 0 and player_health > 0:
        print("\nYou have defeated **Sentinel Prime**!")
        return "win"
    elif player_health <= 0:
        print("\nYou have been defeated by **Sentinel Prime**.")
        return "lose"
    else:
        print("\nThe battle is still ongoing. But it looks like you're both on the edge!")
        return "ongoing"

# Define a function to make the final choice (Kill or Spare Sentinel Prime)
def final_choice():
    choice = input("\n**Sentinel Prime** is at your mercy. What will you do?\nA) Kill Sentinel Prime and start the Decepticon Faction\nB) Spare Sentinel Prime and take him to trial for his crimes against Cybertron\nEnter A or B: ").lower()
    
    if choice == "a":
        print("\nYou have chosen to kill **Sentinel Prime**. With his death, you take control of the Decepticon Faction.")
        print("The war for Cybertron continues, but you will shape its future with an iron fist!")
    elif choice == "b":
        print("\nYou have chosen to spare **Sentinel Prime** and take him to trial.")
        print("Despite his actions, you believe in justice. You take him back to Iacon City for trial, hoping to restore balance to Cybertron.")
    else:
        print("\nInvalid choice! No action was taken.")
        
# Main event function
def main_event(player):
    global player_health, arachnid_health, sentinel_health
    
    # Start the battle with Arachnid
    arachnid_battle_result = battle_arachnid()
    
    if arachnid_battle_result == "win":
        print("\nYou have successfully defeated Arachnid! Now you face **Sentinel Prime**.")
        sentinel_battle_result = battle_sentinel(player)
        
        if sentinel_battle_result == "win":
            final_choice()
        elif sentinel_battle_result == "lose":
            print("\nYou were defeated by **Sentinel Prime**. The fate of Cybertron is uncertain.")
        else:
            print("\nThe battle with **Sentinel Prime** is still ongoing. Your fate rests on the edge of the blade!")
    else:
        print("\nYou were defeated by Arachnid, and now the fate of Cybertron is uncertain.")
        
# Call the main event function to start the game
# Ensure the player is initialized before calling main_event
player_name = input("Enter your player name: ").strip()
player = character_selection(player_name)
main_event(player)
def main_event():
    global player_health, arachnid_health, sentinel_health
    arachnid_battle_result = battle_arachnid()
    if player_health <= 0:
        print("\nYou were defeated by Arachnid, and now the fate of Cybertron is uncertain.")
    return