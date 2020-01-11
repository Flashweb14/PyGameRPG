import pygame
from RPG.scripts.game_object import GameObject
from RPG.scripts.consts import TILE_SIZE


class BaseEnemy(GameObject):
    def __init__(self, game, image, x, y, hp, damage):
        super().__init__(game, image,
                         x, y, game.all_sprites, game.enemy_group)
        self.hp = hp
        self.damage = damage

# TODO Полоску HP над врагами
