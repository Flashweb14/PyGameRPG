import pygame
from RPG.scripts.game_object import GameObject
from RPG.scripts.consts import INVENTORY_CELL_IMAGE, INVENTORY_SELECTED_CELL_IMAGE, INVENTORY_CELL_IMAGE_1, \
    INVENTORY_SELECTED_CELL_IMAGE_1, INVENTORY_ARMOR_IMAGE, INVENTORY_SWORD_IMAGE, INVENTORY_BOW_IMAGE, \
    INVENTORY_RING_IMAGE
from RPG.scripts.utilities import load_image


class Cell(GameObject):
    def __init__(self, game, inventory, type, x, y):
        super().__init__(game, INVENTORY_CELL_IMAGE, 0, 0, game.gui_group, game.inventory_cell_group)
        self.image = INVENTORY_CELL_IMAGE
        self.inventory = inventory
        self.rect.x = self.inventory.rect.x + x
        self.rect.y = self.inventory.rect.y + y
        self.selected = False
        self.item = None
        self.type = type
        self.slots_dict = {'sword': INVENTORY_SWORD_IMAGE, 'bow': INVENTORY_BOW_IMAGE, 'armor': INVENTORY_ARMOR_IMAGE,
                           'ring': INVENTORY_RING_IMAGE}

    def update(self):
        if not self.item:
            if self.type == 'cell':
                self.image = INVENTORY_CELL_IMAGE
            else:
                self.image = self.slots_dict[self.type]
        else:
            if self.selected:
                self.image = load_image('resources/sprites/gui/inventory/cell_selected.png')
            else:
                self.image = load_image('resources/sprites/gui/inventory/cell.png')
            self.image.blit(
                pygame.transform.scale(self.item.image, (int(self.item.rect.w * 1.25), int(self.item.rect.h * 1.25))),
                (((90 - self.item.rect.w * 1.25) // 2), ((90 - self.item.rect.h * 1.25) // 2)))
