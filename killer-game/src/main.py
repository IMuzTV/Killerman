import pygame
from game.player import Player
from game.enemy import Enemy
from game.level import Level

# Initialize the game
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Killer Game")

# Game variables
running = True
clock = pygame.time.Clock()

# Initialize game components
player = Player(name="Hero", health=100, score=0)
level = Level(level_number=1)

def game_loop():
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Game logic
        player.move()
        level.load_level()

        # Drawing
        screen.fill((0, 0, 0))  # Clear the screen with black
        # Here you would draw the player, enemies, and other game elements

        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 frames per second

# Start the game loop
game_loop()

# Clean up
pygame.quit()