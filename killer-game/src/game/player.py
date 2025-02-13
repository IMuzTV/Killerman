class Player:
    def __init__(self, name, health=100, score=0):
        self.name = name
        self.health = health
        self.score = score

    def move(self, direction):
        print(f"{self.name} moves {direction}.")

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.type}!")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage and now has {self.health} health.")