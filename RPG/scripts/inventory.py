import pygame
from RPG.scripts.consts import INVENTORY_IMAGE
from RPG.scripts.game_object import GameObject


class Inventory(GameObject):
    def __init__(self, game):
        super().__init__(game, INVENTORY_IMAGE, 0, 0, game.gui_group)
        self.rect.x = 1350
        self.rect.y = 200
