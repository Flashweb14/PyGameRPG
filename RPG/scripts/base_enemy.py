import pygame
from RPG.scripts.game_object import GameObject
from RPG.scripts.hp_bar_npc import HealthBarNPC


class BaseEnemy(GameObject):
    def __init__(self, game, image, x, y, max_hp, damage):
        super().__init__(game, image,
                         x, y, game.all_sprites, game.enemy_group)
        self.hp = 5
        self.max_hp = max_hp
        self.damage = damage
        self.max_hp = max_hp
        self.hp_bar = HealthBarNPC(game, self)
