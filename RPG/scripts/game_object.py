import pygame
from RPG.scripts.utilities import load_image
from RPG.scripts.consts import TILE_SIZE

pygame.init()


class GameObject(pygame.sprite.Sprite):
    def __init__(self, game, image, x, y, *groups):
        super().__init__(*groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


