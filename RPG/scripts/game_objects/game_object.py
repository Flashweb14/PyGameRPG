import pygame
from scripts.consts import TILE_SIZE

pygame.init()


class GameObject(pygame.sprite.Sprite):
    def __init__(self, game, image, x, y, *groups):
        super().__init__(*groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE

    def handle_event(self, event):
        pass
