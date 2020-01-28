import pygame
from RPG.scripts.utilities import load_image, load_level

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

ARROWS_INDICATOR = load_image('resources/sprites/gui/arrows_ind.png')
ARMOR_INDICATOR = load_image('resources/sprites/gui/armor_ind.png')

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

INVENTORY_ARMOR_IMAGE = load_image('resources/sprites/gui/inventory/cell_armor.png')
INVENTORY_SWORD_IMAGE = load_image('resources/sprites/gui/inventory/cell_sword.png')
INVENTORY_BOW_IMAGE = load_image('resources/sprites/gui/inventory/cell_bow.png')
INVENTORY_RING_IMAGE = load_image('resources/sprites/gui/inventory/cell_ring.png')

FOOD_MEAT = load_image('resources/sprites/game_objects/food/meat.png')

USE_BUTTON = load_image('resources/sprites/gui/inventory/use_btn.png')
DROP_BUTTON = load_image('resources/sprites/gui/inventory/drop_btn.png')

GAME_FONT = pygame.font.Font('resources/fonts/font.ttf', 35)
QUEST_DESCRIPTION_FONT = pygame.font.Font('resources/fonts/font.ttf', 25)

IRON_CHEST = load_image('resources/sprites/game_objects/armor/iron_chest.png')
IRON_SWORD = load_image('resources/sprites/game_objects/weapon/iron_sword.png')
WOODEN_BOW = load_image('resources/sprites/game_objects/weapon/wooden_bow.png')
GOLDEN_RING = load_image('resources/sprites/game_objects/rings/golden_ring.png')

CHEST_CLOSED = load_image('resources/sprites/game_objects/chest/chest_closed.png')
CHEST_OPENED = load_image('resources/sprites/game_objects/chest/chest_opened.png')
CHEST_GUI = load_image('resources/sprites/gui/chest_gui.png')

OVERWEIGHT_ERROR = load_image('resources/sprites/gui/full_error.png')
CLOSE_BUTTON = load_image('resources/sprites/gui/error_close.png')

RED_SHIRT_NPC = load_image('resources/sprites/npcs/redshirt/redshirt.png')

QUEST_GUI = load_image('resources/sprites/gui/quest/quest_gui.png')
QUEST_GUI_1 = load_image('resources/sprites/gui/quest/quest_gui.png')
ACCEPT_BUTTON = load_image('resources/sprites/gui/quest/accept_btn.png')
REJECT_BUTTON = load_image('resources/sprites/gui/quest/reject_btn.png')

NEW_GAME_BTN = load_image('resources/sprites/gui/menu/new_game_btn.png')
EXIT_BTN = load_image('resources/sprites/gui/menu/exit_btn.png')
CONTINUE_BTN = load_image('resources/sprites/gui/menu/continue_btn.png')
MAIN_MENU_BTN = load_image('resources/sprites/gui/menu/main_menu_btn.png')

LEVEL = load_level('resources/level_maps/level.txt')

