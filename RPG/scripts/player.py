import pygame
from RPG.scripts.consts import TILE_SIZE, PLAYER_FRONT_IMAGE, PLAYER_FRONT_1_IMAGE, PLAYER_FRONT_2_IMAGE, \
    PLAYER_BACK_IMAGE, PLAYER_BACK_1_IMAGE, PLAYER_BACK_2_IMAGE, PLAYER_RIGHT_IMAGE, PLAYER_RIGHT_1_IMAGE, \
    PLAYER_RIGHT_2_IMAGE, PLAYER_LEFT_IMAGE, PLAYER_LEFT_1_IMAGE, PLAYER_LEFT_2_IMAGE, PLAYER_FRONT_SWORD, \
    PLAYER_BACK_SWORD, PLAYER_RIGHT_SWORD, PLAYER_LEFT_SWORD
from RPG.scripts.game_object import GameObject
from RPG.scripts.arrow import Arrow

pygame.init()


class Player(GameObject):
    def __init__(self, game, x, y):
        super().__init__(game, PLAYER_FRONT_IMAGE, x, y, game.player_group, game.all_sprites)
        self.rect = pygame.Rect(((2, 2), (62, 62)))
        #self.rect.x = TILE_SIZE * x
        #dself.rect.y = TILE_SIZE * y

        self.motion = []
        self.speed = 240
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

        self.x = self.game.width // 2 - self.rect.w // 2
        self.y = self.game.height // 2 - self.rect.h // 2

        self.last_shot_time = None

        self.inventory = []
        self.first_time = True

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.motion:
                    self.image = self.animation_dict_sword[self.motion[0]]
                    self.attack(self.speed_dict[self.motion[0]])
                else:
                    self.image = self.animation_dict_sword[self.direction]
                    self.attack(self.speed_dict[self.direction])
            if event.key == pygame.K_e:
                if not self.last_shot_time or pygame.time.get_ticks() - self.last_shot_time >= 3 * 10**2:
                    self.shoot()
                    self.last_shot_time = pygame.time.get_ticks()
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
            if event.key == pygame.K_i:
                if self.game.inventory_opened:
                    self.game.inventory_opened = False
                else:
                    self.game.inventory_opened = True
            if event.key in self.motion_dict:
                self.direction = self.motion_dict[event.key]
                self.motion.remove(self.direction)
                if self.motion:
                    self.image = self.animation_dict[self.motion[0]][2]
                else:
                    self.image = self.animation_dict[self.direction][2]

    def update(self, *event):
        if not self.first_time:
            for sprite in self.game.harm_sprites:
                if pygame.sprite.collide_rect(self, sprite):
                    self.hp -= sprite.damage / self.game.FPS
            if self.hp <= 0:
                self.game.terminate()
            for obj in self.game.pickable_objects:
                if pygame.sprite.collide_rect(self, obj):
                    self.inventory.append(obj)
                    self.game.all_sprites.remove(obj)
                    self.game.pickable_objects.remove(obj)
                    self.game.inventory.add_item(obj)
        else:
            self.first_time = False

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
                self.x += self.speed_dict[direction][0] / self.game.FPS
                self.y += self.speed_dict[direction][1] / self.game.FPS
                check_sprite = pygame.sprite.Sprite()
                check_sprite.rect = pygame.Rect((2, 2), (TILE_SIZE - 2, TILE_SIZE - 2))
                check_sprite.rect.x = self.rect.x + int(self.speed_dict[direction][0] / self.game.FPS)
                check_sprite.rect.y = self.rect.y + int(self.speed_dict[direction][1] / self.game.FPS)
                if (pygame.sprite.spritecollideany(check_sprite, self.game.walls_group) or
                        pygame.sprite.spritecollideany(check_sprite, self.game.enemy_group)):
                    self.x -= self.speed_dict[direction][0] / self.game.FPS
                    self.y -= self.speed_dict[direction][1] / self.game.FPS

    def attack(self, speed):
        check_sprite = pygame.sprite.Sprite()
        check_sprite.rect = pygame.Rect((0, 0), (TILE_SIZE, TILE_SIZE))
        check_sprite.rect.x = self.rect.x + speed[0] / 36
        check_sprite.rect.y = self.rect.y + speed[1] / 36
        for enemy in self.game.enemy_group:
            if pygame.sprite.collide_rect(check_sprite, enemy):
                enemy.hp -= 1

    def shoot(self):
        if self.motion:
            Arrow(self.game, self.motion[0])
        else:
            Arrow(self.game, self.direction)
