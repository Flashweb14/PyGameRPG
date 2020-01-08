import sys
import pygame
from RPG.scripts.tile import Tile
from RPG.scripts.player import Player
from RPG.scripts.camera import Camera
from RPG.scripts.gui import HealthBar

pygame.init()


class Game:
    def __init__(self):
        self.size = self.width, self.height = 640, 640
        self.screen = pygame.display.set_mode(self.size)
        self.FPS = 60
        self.clock = pygame.time.Clock()

        self.player = None
        self.camera = Camera(self)

        self.all_sprites = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.walls_group = pygame.sprite.Group()
        self.background_group = pygame.sprite.Group()
        self.gui_group = pygame.sprite.Group()

        self.hp_bar = None

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
        self.player = Player(*player)
        Tile(*tree)
        self.hp_bar = HealthBar(self, 5, 10)

    def start_new_game(self, level):
        self.generate_level(level)
