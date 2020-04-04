import pygame
from random import randint
from scripts.game_objects.game_object import GameObject
from scripts.consts import ARROW_IMAGE_LEFT, ARROW_IMAGE_RIGHT, ARROW_IMAGE_DOWN, ARROW_IMAGE_UP, TILE_SIZE


class Arrow(GameObject):
    def __init__(self, game, direction):
        self.direction_dict = {'left': ARROW_IMAGE_LEFT, 'right': ARROW_IMAGE_RIGHT,
                               'up': ARROW_IMAGE_UP, 'down': ARROW_IMAGE_DOWN}
        if direction == 'right' or direction == 'down':
            x = (game.player.x + TILE_SIZE // 2 - 6) / TILE_SIZE
            y = (game.player.y + TILE_SIZE // 2 - 6) / TILE_SIZE
        elif direction == 'left':
            x = (game.player.x + TILE_SIZE // 2 - 60) / TILE_SIZE
            y = (game.player.y + TILE_SIZE // 2 - 5) / TILE_SIZE
        else:
            x = (game.player.x + TILE_SIZE // 2 - 6) / TILE_SIZE
            y = (game.player.y + TILE_SIZE // 2 - 60) / TILE_SIZE
        super().__init__(game, self.direction_dict[direction], x, y, game.all_sprites)
        self.speed = 10
        self.direction = direction
        self.stopped = False
        self.first_time = True

    def update(self, *args):
        if not self.first_time:
            if pygame.sprite.spritecollideany(self, self.game.npc_group):
                self.game.all_sprites.remove(self)
            if pygame.sprite.spritecollideany(self, self.game.walls_group):
                chance = randint(1, 101)
                if chance in range(1, 21):
                    self.stopped = True
                    self.game.stopped_arrows_group.add(self)
                    self.game.all_sprites.remove(self)
                else:
                    self.game.all_sprites.remove(self)
            if not self.stopped:
                self.x += self.game.player.speed_dict[self.direction][0] * 5 // self.game.FPS
                self.y += self.game.player.speed_dict[self.direction][1] * 5 // self.game.FPS
            for enemy in self.game.enemy_group:
                if pygame.sprite.collide_rect(self, enemy):
                    enemy.hp -= self.game.player.bow_damage
                    self.game.all_sprites.remove(self)
                    if not enemy.angered:
                        enemy.angered = True
        else:
            self.first_time = False
