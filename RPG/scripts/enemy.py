import pygame
from RPG.scripts.game_object import GameObject
from RPG.scripts.utilities import load_image


class BaseEnemy(GameObject):
    def __init__(self, game, x, y, hp):
        super().__init__(game, load_image('resources/sprites/enemies/red_slime/red_slime_1.png'),
                         x, y, game.all_sprites, game.enemy_group, game.walls_group)
        self.hp = hp
