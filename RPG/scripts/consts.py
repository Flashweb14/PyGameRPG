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

RED_SLIME_1 = load_image('resources/sprites/enemies/red_slime/red_slime_1.png')
RED_SLIME_2 = load_image('resources/sprites/enemies/red_slime/red_slime_2.png')
RED_SLIME_3 = load_image('resources/sprites/enemies/red_slime/red_slime_3.png')

HP_BAR_0 = load_image('resources/sprites/gui/hp_bar/hp_bar_0.png')
HP_BAR_1 = load_image('resources/sprites/gui/hp_bar/hp_bar_1.png')

HP_BAR_NPC = load_image('resources/sprites/gui/npc_hp_bar.png')

INVENTORY_IMAGE = load_image('resources/sprites/gui/inventory/inventory.png')

ARROW_IMAGE_LEFT = load_image('resources/sprites/game_objects/arrow/arrow_left.png')
ARROW_IMAGE_RIGHT = pygame.transform.flip(ARROW_IMAGE_LEFT, True, False)
ARROW_IMAGE_UP = load_image('resources/sprites/game_objects/arrow/arrow_up.png')
ARROW_IMAGE_DOWN = pygame.transform.flip(ARROW_IMAGE_UP, False, True)

INVENTORY_CELL_IMAGE = load_image('resources/sprites/gui/inventory/cell.png')
INVENTORY_SELECTED_CELL_IMAGE = load_image('resources/sprites/gui/inventory/cell_selected.png')
INVENTORY_CELL_IMAGE_1 = load_image('resources/sprites/gui/inventory/cell.png')
INVENTORY_SELECTED_CELL_IMAGE_1 = load_image('resources/sprites/gui/inventory/cell_selected.png')

FOOD_MEAT = load_image('resources/sprites/game_objects/food/meat.png')

USE_BUTTON = load_image('resources/sprites/gui/inventory/use_btn.png')
DROP_BUTTON = load_image('resources/sprites/gui/inventory/drop_btn.png')

