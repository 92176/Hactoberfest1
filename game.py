import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 10

    def attack(self, enemy):
        damage = random.randint(0, self.strength)
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} and deals {damage} damage.")

    def heal(self):
        heal_amount = random.randint(1, 10)
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} health.")

    def print_status(self):
        print(f"{self.name} - Health: {self.health}, Strength: {self.strength}")


class Enemy:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, player):
        damage = random.randint(0, self.strength)
        player.health -= damage
        print(f"{self.name} attacks {player.name} and deals {damage} damage.")

    def print_status(self):
        print(f"{self.name} - Health: {self.health}, Strength: {self.strength}")


def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    enemy = Enemy("Goblin", 50, 5)

    while player.health > 0 and enemy.health > 0:
        print("\n--- Player's Turn ---")
        player.print_status()
        enemy.print_status()
        action = input("Enter 'attack' to attack or 'heal' to heal: ")

        if action.lower() == "attack":
            player.attack(enemy)
        elif action.lower() == "heal":
            player.heal()
        else:
            print("Invalid action. Try again.")

        if enemy.health > 0:
            print("\n--- Enemy's Turn ---")
            enemy.attack(player)

    if player.health > 0:
        print("You defeated the enemy. Congratulations!")
    else:
        print("You were defeated. Try again.")

if __name__ == "__main__":
    main()
