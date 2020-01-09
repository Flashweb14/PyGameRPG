import pygame
from RPG.scripts.utilities import load_image

pygame.init()

TILE_SIZE = tile_height = 64
TILE_IMAGES = {'wall': load_image('resources/sprites/map/wall.png'),
               'empty': load_image('resources/sprites/map/grass.png'),
               'tree': load_image('resources/sprites/map/tree.png')}

PLAYER_FRONT_IMAGE = load_image('resources/sprites/player/player_front.png')
PLAYER_FRONT_1_IMAGE = load_image('resources/sprites/player/player_front_1.png')
PLAYER_FRONT_2_IMAGE = load_image('resources/sprites/player/player_front_2.png')

PLAYER_BACK_IMAGE = load_image('resources/sprites/player/player_back.png')
PLAYER_BACK_1_IMAGE = load_image('resources/sprites/player/player_back_1.png')
PLAYER_BACK_2_IMAGE = load_image('resources/sprites/player/player_back_2.png')

PLAYER_RIGHT_IMAGE = load_image('resources/sprites/player/player_right.png')
PLAYER_RIGHT_1_IMAGE = load_image('resources/sprites/player/player_right_1.png')
PLAYER_RIGHT_2_IMAGE = load_image('resources/sprites/player/player_right_2.png')

PLAYER_LEFT_IMAGE = pygame.transform.flip(PLAYER_RIGHT_IMAGE, True, False)
PLAYER_LEFT_1_IMAGE = pygame.transform.flip(PLAYER_RIGHT_1_IMAGE, True, False)
PLAYER_LEFT_2_IMAGE = pygame.transform.flip(PLAYER_RIGHT_2_IMAGE, True, False)

PLAYER_FRONT_SWORD = load_image('resources/sprites/player/sword/player_front_sword.png')
PLAYER_BACK_SWORD = load_image('resources/sprites/player/sword/player_back_sword.png')
PLAYER_RIGHT_SWORD = load_image('resources/sprites/player/sword/player_right_sword.png')
PLAYER_LEFT_SWORD = pygame.transform.flip(PLAYER_RIGHT_SWORD, True, False)

HP_BAR_FULL = load_image('resources/sprites/gui/hp_bar/hp_bar_10.png')




