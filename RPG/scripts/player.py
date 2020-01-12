import pygame
from RPG.scripts.consts import TILE_SIZE, PLAYER_FRONT_IMAGE, PLAYER_FRONT_1_IMAGE, PLAYER_FRONT_2_IMAGE, \
    PLAYER_BACK_IMAGE, PLAYER_BACK_1_IMAGE, PLAYER_BACK_2_IMAGE, PLAYER_RIGHT_IMAGE, PLAYER_RIGHT_1_IMAGE, \
    PLAYER_RIGHT_2_IMAGE, PLAYER_LEFT_IMAGE, PLAYER_LEFT_1_IMAGE, PLAYER_LEFT_2_IMAGE, PLAYER_FRONT_SWORD, \
    PLAYER_BACK_SWORD, PLAYER_RIGHT_SWORD, PLAYER_LEFT_SWORD
from RPG.scripts.game_object import GameObject

pygame.init()


class Player(GameObject):
    def __init__(self, game, x, y):
        super().__init__(game, PLAYER_FRONT_IMAGE, x, y, game.player_group, game.all_sprites)
        self.rect = pygame.Rect(((1, 1), (63, 63)))
        self.rect.x = TILE_SIZE * x
        self.rect.y = TILE_SIZE * y

        self.motion = []
        self.speed = 4
        self.motion_dict = {pygame.K_w: 'up', pygame.K_s: 'down',
                            pygame.K_d: 'right', pygame.K_a: 'left'}
        self.speed_dict = {'up': (0, -self.speed), 'down': (0, self.speed),
                           'right': (self.speed, 0), 'left': (-self.speed, 0)}
        self.animation_dict = {'up': (PLAYER_BACK_1_IMAGE, PLAYER_BACK_2_IMAGE, PLAYER_BACK_IMAGE),
                               'down': (PLAYER_FRONT_1_IMAGE, PLAYER_FRONT_2_IMAGE, PLAYER_FRONT_IMAGE),
                               'right': (PLAYER_RIGHT_1_IMAGE, PLAYER_RIGHT_2_IMAGE, PLAYER_RIGHT_IMAGE),
                               'left': (PLAYER_LEFT_1_IMAGE, PLAYER_LEFT_2_IMAGE, PLAYER_LEFT_IMAGE)}
        self.animation_dict_sword = {'up': PLAYER_BACK_SWORD, 'down': PLAYER_FRONT_SWORD,
                                     'right': PLAYER_RIGHT_SWORD, 'left': PLAYER_LEFT_SWORD}
        self.animation = 0
        self.direction = 'down'

        self.max_hp = 10
        self.hp = 10

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.motion:
                    self.image = self.animation_dict_sword[self.motion[0]]
                    self.attack(self.speed_dict[self.motion[0]])
                else:
                    self.image = self.animation_dict_sword[self.direction]
                    self.attack(self.speed_dict[self.direction])
            if event.key in self.motion_dict:
                self.direction = self.motion_dict[event.key]
                if not self.motion:
                    if self.image != self.animation_dict[self.direction][2]:
                        self.image = self.animation_dict[self.direction][2]
                    else:
                        count = self.game.count
                        self.image = self.animation_dict[self.direction][self.animation % 2]
                        if self.game.count == count + 1:
                            self.image = self.animation_dict[self.direction][2]
                self.motion.append(self.direction)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                if self.motion:
                    self.image = self.animation_dict[self.motion[0]][2]
                else:
                    self.image = self.animation_dict[self.direction][2]
            if event.key in self.motion_dict:
                self.direction = self.motion_dict[event.key]
                self.motion.remove(self.direction)
                if self.motion:
                    self.image = self.animation_dict[self.motion[0]][2]
                else:
                    self.image = self.animation_dict[self.direction][2]

    def update(self, *event):
        for sprite in self.game.harm_sprites:
            if pygame.sprite.collide_rect(self, sprite):
                self.hp -= sprite.damage / self.game.FPS
        if self.hp <= 0:
            self.game.terminate()

    def move(self):
        if self.motion:
            for direction in self.game.player.motion:
                if self.motion.index(direction) == 0:
                    if self.animation % 7 == 0:
                        self.image = self.game.player.animation_dict[self.motion[0]][self.animation % 2]
                else:
                    if self.game.player.animation % 15 == 0:
                        self.image = self.animation_dict[self.motion[0]][self.animation % 2]
                self.animation += 1
                self.rect.x += self.speed_dict[direction][0]
                self.rect.y += self.speed_dict[direction][1]
                if (pygame.sprite.spritecollideany(self, self.game.walls_group) or
                        pygame.sprite.spritecollideany(self, self.game.enemy_group)):
                    self.rect.x -= self.speed_dict[direction][0]
                    self.rect.y -= self.speed_dict[direction][1]

    def attack(self, speed):
        check_sprite = pygame.sprite.Sprite()
        check_sprite.rect = pygame.Rect((0, 0), (TILE_SIZE, TILE_SIZE))
        check_sprite.rect.x = self.rect.x + speed[0] * 2
        check_sprite.rect.y = self.rect.y + speed[1] * 2
        for enemy in self.game.enemy_group:
            if pygame.sprite.collide_rect(check_sprite, enemy):
                enemy.hp -= 1
                print(enemy.hp)
