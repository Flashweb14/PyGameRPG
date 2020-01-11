import pygame
from RPG.scripts.game_object import GameObject
from RPG.scripts.utilities import load_image


class BaseEnemy(GameObject):
    def __init__(self, game, image, x, y, hp, damage):
        super().__init__(game, image,
                         x, y, game.all_sprites, game.enemy_group)
        self.hp = hp
        self.damage = damage
