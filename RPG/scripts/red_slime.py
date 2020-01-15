import pygame
from RPG.scripts.base_enemy import BaseEnemy
from RPG.scripts.utilities import load_image
from RPG.scripts.consts import RED_SLIME_1, RED_SLIME_2, RED_SLIME_3, TILE_SIZE
from RPG.scripts.hp_bar_npc import HealthBarNPC


class RedSlime(BaseEnemy):
    def __init__(self, game, x, y):
        super().__init__(game, RED_SLIME_1, x, y, 5, 1)
        self.animation_list = [RED_SLIME_1, RED_SLIME_2, RED_SLIME_3]
        self.speed = 60
        self.hp_bar = HealthBarNPC(game, self)

    def update(self):
        if self.game.count % 10 == 0:
            if self.animation_list.index(self.image) < 2:
                self.image = self.animation_list[self.animation_list.index(self.image) + 1]
            else:
                self.image = self.animation_list[0]
        super().update()

# TODO Пофиксить баг с хп баром
