import pygame
from RPG.scripts.base_enemy import BaseEnemy
from RPG.scripts.utilities import load_image
from RPG.scripts.consts import RED_SLIME_1, RED_SLIME_2, RED_SLIME_3, TILE_SIZE


class RedSlime(BaseEnemy):
    def __init__(self, game, x, y):
        super().__init__(game, RED_SLIME_1, x, y, 5, 1)
        self.animation_list = [RED_SLIME_1, RED_SLIME_2, RED_SLIME_3]

    def update(self):
        if self.game.count % 10 == 0:
            if self.animation_list.index(self.image) < 2:
                self.image = self.animation_list[self.animation_list.index(self.image) + 1]
            else:
                self.image = self.animation_list[0]
        super().update()

        if self.hp <= 0:
            self.die()

        check_sprite = pygame.sprite.Sprite()
        check_sprite.rect = pygame.Rect(
            ((0, 0), (TILE_SIZE + self.game.player.speed * 4, TILE_SIZE + self.game.player.speed * 4)))
        check_sprite.rect.x = self.rect.x - self.game.player.speed * 2
        check_sprite.rect.y = self.rect.y - self.game.player.speed * 2
        if pygame.sprite.collide_rect(check_sprite, self.game.player):
            self.game.player.hp -= self.damage / self.game.FPS

    def die(self):
        for group in self.game.groups:
            if self in group:
                group.remove(self)
