import sys
import pygame
from RPG.scripts.tile import Tile
from RPG.scripts.player import Player
from RPG.scripts.camera import Camera
from RPG.scripts.gui.health_bar import HealthBar
from RPG.scripts.fire import Fire
from RPG.scripts.red_slime import RedSlime
from RPG.scripts.gui.inventory.inventory import Inventory
from RPG.scripts.food import Food
from RPG.scripts.gui.arrows_ind import ArrowsIndicator
from RPG.scripts.gui.armor_ind import ArmorIndicator
from RPG.scripts.armor import Armor
from RPG.scripts.weapon import Weapon
from RPG.scripts.ring import Ring
from RPG.scripts.chest import Chest
from RPG.scripts.error import Error

pygame.init()


class Game:
    def __init__(self):
        self.size = self.width, self.height = 1920, 1080
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        self.FPS = 60
        self.clock = pygame.time.Clock()

        pygame.mouse.set_visible(False)

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
        self.stopped_arrows_group = pygame.sprite.Group()
        self.inventory_cell_group = pygame.sprite.Group()
        self.pickable_objects = pygame.sprite.Group()
        self.chests_group = pygame.sprite.Group()
        self.errors_group = pygame.sprite.Group()

        self.groups = [self.all_sprites, self.player_group, self.walls_group, self.background_group,
                       self.gui_group, self.harm_sprites, self.enemy_group]

        self.hp_bar = None
        self.arrows_ind = None
        self.armor_ind = None

        self.count = 0

        self.inventory_opened = False
        self.has_error = False

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
        self.arrows_ind = ArrowsIndicator(self, 26, 140)
        self.armor_ind = ArmorIndicator(self, 5, 70)
        self.inventory = Inventory(self)
        Food(self, 'meat', 9, 9)
        Food(self, 'meat', 14, 10)
        Food(self, 'meat', 14, 10)
        Food(self, 'meat', 14, 10)
        Food(self, 'meat', 14, 10)
        Food(self, 'meat', 14, 10)
        Food(self, 'meat', 14, 10)
        Food(self, 'meat', 14, 10)
        Armor(self, 2, 16, 8)
        Weapon(self, 'iron_sword', 10, 18, 8)
        Weapon(self, 'wooden_bow', 7, 20, 8)
        Ring(self, 'golden_ring', 22, 8)
        Chest(self, Armor(self, 2, 16, 8), 24, 8)

    def start_new_game(self, level):
        self.generate_level(level)
