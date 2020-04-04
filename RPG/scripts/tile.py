import pygame
from scripts.consts import TILE_IMAGES
from scripts.game_objects.game_object import GameObject

pygame.init()


class Tile(GameObject):
    def __init__(self, game, tile_type, pos_x, pos_y):
        super().__init__(game, TILE_IMAGES[tile_type], pos_x, pos_y, game.all_sprites)
        if tile_type == 'wall' or tile_type == 'tree':
            self.game.walls_group.add(self)
        else:
            self.game.background_group.add(self)
            self.game.all_sprites.remove(self)
