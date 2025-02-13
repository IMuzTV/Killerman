class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.enemies = []

    def load_level(self):
        # Logic to load the level, such as initializing enemies and setting up the environment
        print(f"Loading level {self.level_number}...")

    def reset_level(self):
        # Logic to reset the level, such as clearing enemies and resetting player position
        print(f"Resetting level {self.level_number}...")