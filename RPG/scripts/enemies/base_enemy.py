import pygame
from scripts.game_objects.game_object import GameObject
from scripts.consts import TILE_SIZE
from scripts.enemies.hp_bar_npc import HealthBarNPC


class BaseEnemy(GameObject):
    def __init__(self, game, image, x, y, max_hp, damage, name):
        super().__init__(game, image,
                         x, y, game.all_sprites, game.enemy_group)
        self.max_hp = max_hp
        self.hp = max_hp
        self.damage = damage
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.angered = False
        self.last_attack_time = False
        self.name = name
        self.hp_bar = HealthBarNPC(game, self)
        self.first_time = True

    def update(self):
        if not self.first_time:
            if self.hp <= 0:
                self.die()
                for quest in self.game.player.quests:
                    if quest.enemy == self.name:
                        quest.left -= 1
                        quest.update()
                        self.game.journal_group.update()

            if self.check_player_around(TILE_SIZE + 8, 4):
                self.attack()
            elif self.check_player_around(TILE_SIZE * 6, TILE_SIZE * 3) and not self.angered:
                self.angered = True
            else:
                if self.angered:
                    self.move()
        else:
            self.first_time = False

    def check_player_around(self, rect_size, delta):
        check_sprite = pygame.sprite.Sprite()
        check_sprite.rect = pygame.Rect((0, 0), (rect_size, rect_size))
        check_sprite.rect.x = self.rect.x - delta
        check_sprite.rect.y = self.rect.y - delta
        return pygame.sprite.collide_rect(check_sprite, self.game.player)

    def die(self):
        for group in self.game.groups:
            if self in group:
                group.remove(self)
        self.game.all_sprites.remove(self.hp_bar)

    def move(self):
        if self.game.player.x > self.x:
            self.x += self.speed / self.game.FPS
        elif self.game.player.x < self.x:
            self.x -= self.speed / self.game.FPS

        if self.game.player.y > self.y:
            self.y += self.speed / self.game.FPS
        elif self.game.player.y < self.y:
            self.y -= self.speed / self.game.FPS

    def attack(self):
        cur_time = pygame.time.get_ticks()
        if cur_time - self.last_attack_time >= 10 ** 3:
            self.game.player.take_damage(self.damage)
            self.last_attack_time = cur_time
