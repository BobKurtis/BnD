import pygame
import random
import Character.PlayableCharacter as PlayableCharacter
import StatsDisplay
import values.PlayerOne

'''
TODO:
1. resize character
2. limit movement based on stats
    - limit move to no diagonals 
3. fill in background with map data
'''

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1920 - 192
SCREEN_HEIGHT = 1080 - 108


# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("images/missile.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("images/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()


class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Create the screen object
        # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Instantiate player.
        self.player = PlayableCharacter.Player((values.PlayerOne.HEALTH, values.PlayerOne.WISDOM, values.PlayerOne.STRESS))
        # Instantiate Stats Screen
        self.stats = StatsDisplay.Status()

        # Create groups to hold enemy sprites and all sprites
        # - enemies is used for collision detection and position updates
        # - all_sprites is used for rendering
        enemies = pygame.sprite.Group()
        clouds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player.status_display)

        self.game_tick()

        # Load and play background music
        # Sound source: http://ccmixter.org/files/Apoxode/59262
        # License: https://creativecommons.org/licenses/by/3.0/
        # pygame.mixer.music.load("music/Apoxode_-_Electric_1.mp3")
        # pygame.mixer.music.play(loops=-1)

    def game_tick(self):
        # Variable to keep the main loop running
        running = True

        # Set up the clock for a decent framerate
        clock = pygame.time.Clock()
        while running:
            # for loop through the event queue
            for event in pygame.event.get():
                # Check for KEYDOWN event
                if event.type == KEYDOWN:
                    # If the Esc key is pressed, then exit the main loop
                    if event.key == K_ESCAPE:
                        running = False
                # Check for QUIT event. If QUIT, then set running to false.
                elif event.type == QUIT:
                    running = False

            # Get the set of keys pressed and check for user input
            pressed_keys = pygame.key.get_pressed()

            # Update the player sprite based on user keypresses
            self.player.update(pressed_keys)

            # Fill the screen with sky blue
            self.screen.fill((135, 206, 250))

            # Draw all sprites
            for entity in self.all_sprites:
                self.screen.blit(entity.surf, entity.rect)

                # Check if any enemies have collided with the player
                # if pygame.sprite.spritecollideany(self.player, enemies):
                #     # If so, then remove the player and stop the loop
                #     player.kill()
                #     # Stop any moving sounds and play the collision sound
                #     # move_up_sound.stop()
                #     # move_down_sound.stop()
                #     collision_sound.play()
                #
                #     running = False

            # Update the display
            pygame.display.flip()

            # Ensure program maintains a rate of 30 frames per second
            clock.tick(60)

        # All done! Stop and quit the mixer.
        pygame.mixer.music.stop()
        pygame.mixer.quit()
Game()
