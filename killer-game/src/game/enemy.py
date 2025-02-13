class Enemy:
    def __init__(self, enemy_type, health, damage):
        self.type = enemy_type
        self.health = health
        self.damage = damage

    def spawn(self):
        print(f"{self.type} has spawned with {self.health} health and {self.damage} damage.")

    def attack(self):
        print(f"{self.type} attacks dealing {self.damage} damage.")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.type} takes {amount} damage and has {self.health} health left.")
        if self.health <= 0:
            print(f"{self.type} has been defeated.")