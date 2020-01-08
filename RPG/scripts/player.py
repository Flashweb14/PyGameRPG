import pygame
from RPG.scripts.consts import TILE_SIZE, PLAYER_FRONT_IMAGE, PLAYER_FRONT_1_IMAGE, PLAYER_FRONT_2_IMAGE, \
    PLAYER_BACK_IMAGE, PLAYER_BACK_1_IMAGE, PLAYER_BACK_2_IMAGE, PLAYER_RIGHT_IMAGE, PLAYER_RIGHT_1_IMAGE, \
    PLAYER_RIGHT_2_IMAGE, PLAYER_LEFT_IMAGE, PLAYER_LEFT_1_IMAGE, PLAYER_LEFT_2_IMAGE
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
        self.animation = 0

        self.hp = 10

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in self.motion_dict:
                direction = self.motion_dict[event.key]
                if not self.motion:
                    if self.image != self.animation_dict[direction][2]:
                        self.image = self.animation_dict[direction][2]
                    else:
                        self.image = self.animation_dict[direction][self.animation % 2]
                self.motion.append(direction)
        elif event.type == pygame.KEYUP:
            if event.key in self.motion_dict:
                direction = self.motion_dict[event.key]
                self.motion.remove(direction)
                if self.motion:
                    self.image = self.animation_dict[self.motion[0]][2]
                else:
                    self.image = self.animation_dict[direction][2]

    def update(self, event):
        self.handle_event(event)
