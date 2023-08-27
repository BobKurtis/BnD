from Character.Player import Player
from sprites import *
from values.config import *
import sys
import CreateTilemap

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('OpenSans.ttf', 32)
        self.running = True

        # Character Sprites Files List
        character_file_list = ['images/Character Sprite Sheet Collection/Male/Male 09-1.png',
                               'images/Character Sprite Sheet Collection/Female/Female 02-1.png',
                               'images/Character Sprite Sheet Collection/Other/pipo-charachip_otaku01.png',
                               'images/Character Sprite Sheet Collection/Male/Male 14-1.png']
        terrain_file_list = ['img/terrain.png',
                             'images/tilesets/3.png',
                             'images/tilesets/1.png']
        self.terrain_spritesheet = []
        self.character_spritesheet = []
        # turn character spritesheet into a list
        for count, character in enumerate(character_file_list):
            self.character_spritesheet.append(Spritesheet(character))
        # turn terrain spritesheet into a list
        for count, terrain in enumerate(terrain_file_list):
            self.terrain_spritesheet.append(Spritesheet(terrain))
        # self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet = Spritesheet('img/enemy.png')
        self.attack_spritesheet = Spritesheet('img/attack.png')
        # self.intro_background = pygame.image.load('img/introbackground.png')
        self.intro_background = pygame.image.load('images/bnd background large.jpeg')
        self.go_background = pygame.image.load('img/gameover.png')

    # def createTilemap(self):
    #     for i, row in enumerate(tilemap):
    #         for j, column in enumerate(row):
    #             Ground(self, j, i)
    #             if column == "B":
    #                 Block(self, j, i)
    #             if column == "E":
    #                 Enemy(self, j, i)
    #             # if column == "S":
    #             #     StatusDisplay(self, j, i)

    def new(self, selected_player):
        # a new game starts
        self.playing = True
        # will contain all the sprites in the game Characters, walls everything
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.player = Player(self, 5, 12, [10, 8, 5], selected_player)

        self.tile_map_creator = CreateTilemap
        # self.createTilemap()
        # self.createTilemap = self.CreateTileMap.createTilemap(self)
        self.tile_map_creator.CreateTileMap.createTilemap(self)

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - TILE_SIZE)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + TILE_SIZE)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - TILE_SIZE, self.player.rect.y)
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + TILE_SIZE, self.player.rect.y)

    def update(self):
        # game loop updates
        # this will look into all the sprites in the group and find their update method and run it
        self.all_sprites.update()

    def draw(self):
        # game draw loop
        self.screen.fill(BLACK)
        # looks through all sprites in the group finds the image and the rect and draws them on the screen
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # game loop
        while self.playing:
            # listen to what's happening
            self.events()
            # react to what you heard
            self.update()
            # tell the screen to respond
            self.draw()

    def game_over(self):
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH / 2, WIN_HEIGHT / 2))

        restart_button = Button(10, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'Restart', 32)
        for sprite in self.all_sprites:  # go through all sprites and remove them
            sprite.kill()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
            self.screen.blit(self.go_background, (0, 0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def intro_screen(self):
        intro = True
        title = self.font.render('BnD', True, BLACK)
        title_rect = title.get_rect(x=self.screen.get_width() / 3, y=self.screen.get_width() / 3)
        self.character_select_id = 0
        character_selection_list = ['Alfred', 'Ravamora', 'Winston', 'Kyle']
        self.selected_character_name = character_selection_list[self.character_select_id]
        self.selected_character_display = self.font.render(("Playing As: " + self.selected_character_name), True, BLACK)
        self.selected_character_display_rect = self.selected_character_display.get_rect(x=self.screen.get_width() / 2,
                                                                                        y=self.screen.get_width() / 5)
        play_button = Button(10, 50, 100, 50, WHITE, BLACK, 'Play', 32)
        cycle_character_button = Button(10, 120, 300, 50, WHITE, BLACK, 'Toggle Character', 32)
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                # character_selected = 1
                g.new(self.character_select_id)
            if cycle_character_button.is_pressed(mouse_pos, mouse_pressed):
                # get the next character
                self.character_select_id += 1
                if self.character_select_id > len(character_selection_list) - 1:
                    # round-robin
                    self.character_select_id = 0
                    self.selected_character_name = character_selection_list[self.character_select_id]
                else:
                    self.selected_character_name = character_selection_list[self.character_select_id]

                # update the character display
                self.selected_character_display = self.font.render(("Playing As: " + self.selected_character_name),
                                                                   True, BLACK)

            self.screen.blit(self.intro_background, (0, 0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(cycle_character_button.image, cycle_character_button.rect)
            self.screen.blit(self.selected_character_display, self.selected_character_display_rect)
            self.clock.tick(FPS/6)
            pygame.display.update()


g = Game()
g.intro_screen()
# g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
