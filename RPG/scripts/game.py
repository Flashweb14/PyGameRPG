import sys
import pygame
from RPG.scripts.tile import Tile
from RPG.scripts.player import Player
from RPG.scripts.camera import Camera
from RPG.scripts.gui import HealthBar
from RPG.scripts.fire import Fire
from RPG.scripts.red_slime import RedSlime
from RPG.scripts.hp_bar_npc import HealthBarNPC
from RPG.scripts.inventory import Inventory

pygame.init()


class Game:
    def __init__(self):
        self.size = self.width, self.height = 1920, 1080
        self.screen = pygame.display.set_mode(self.size)
        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.player = None
        self.inventory = None
        self.camera = Camera(self)

        self.all_sprites = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.walls_group = pygame.sprite.Group()
        self.background_group = pygame.sprite.Group()
        self.gui_group = pygame.sprite.Group()
        self.harm_sprites = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()

        self.groups = [self.all_sprites, self.player_group, self.walls_group, self.background_group,
                       self.gui_group, self.harm_sprites, self.enemy_group]

        self.hp_bar = None

        self.count = 0

        self.inventory_opened = False


    @staticmethod
    def terminate():
        pygame.quit()
        sys.exit()

    def generate_level(self, level):
        player = None
        tree = None
        for y in range(len(level)):
            for x in range(len(level[y])):
                if level[y][x] == '.':
                    Tile(self, 'empty', x, y)
                elif level[y][x] == '#':
                    Tile(self, 'wall', x, y)
                elif level[y][x] == '@':
                    Tile(self, 'empty', x, y)
                    player = self, x, y
                elif level[y][x] == 'T':
                    Tile(self, 'empty', x, y)
                    tree = self, 'tree', x, y
        Fire(self, 3, 4)
        self.player = Player(*player)
        Tile(*tree)
        RedSlime(self, 5, 5)
        RedSlime(self, 10, 10)
        self.hp_bar = HealthBar(self, 5, 10)
        self.inventory = Inventory(self)

    def start_new_game(self, level):
        self.generate_level(level)
