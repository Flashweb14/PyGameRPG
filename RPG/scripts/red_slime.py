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
        self.angered = False
        self.x = self.rect.x
        self.y = self.rect.y

    def update(self):
        if self.game.count % 10 == 0:
            if self.animation_list.index(self.image) < 2:
                self.image = self.animation_list[self.animation_list.index(self.image) + 1]
            else:
                self.image = self.animation_list[0]
        super().update()

        if self.hp <= 0:
            self.die()

        if self.check_player_around(TILE_SIZE + 8, 4):
            print('attack')
            # TODO Attack
        elif self.check_player_around(TILE_SIZE * 8, TILE_SIZE * 4) and not self.angered:
            self.angered = True
        else:
            if self.angered:
                self.move()

    def die(self):
        for group in self.game.groups:
            if self in group:
                group.remove(self)
        self.game.all_sprites.remove(self.hp_bar)

    def check_player_around(self, rect_size, delta):
        check_sprite = pygame.sprite.Sprite()
        check_sprite.rect = pygame.Rect((0, 0), (rect_size, rect_size))
        check_sprite.rect.x = self.rect.x - delta
        check_sprite.rect.y = self.rect.y - delta
        return pygame.sprite.collide_rect(check_sprite, self.game.player)

    def move(self):
        if self.game.player.rect.x > self.rect.x:
            self.x += self.speed / self.game.FPS
        elif self.game.player.rect.x < self.rect.x:
            self.x -= self.speed / self.game.FPS
        self.rect.x = int(self.x)

        if self.game.player.rect.y > self.rect.y:
            self.y += self.speed / self.game.FPS
        elif self.game.player.rect.y < self.rect.y:
            self.y -= self.speed / self.game.FPS
        self.rect.y = int(self.y)

    def attack(self):
        pass
