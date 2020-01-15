import pygame
from RPG.scripts.game_object import GameObject
from RPG.scripts.consts import INVENTORY_CELL_IMAGE, INVENTORY_SELECTED_CELL_IMAGE, INVENTORY_CELL_IMAGE_1, INVENTORY_SELECTED_CELL_IMAGE_1


class Cell(GameObject):
    def __init__(self, game, inventory,  x, y):
        super().__init__(game, INVENTORY_CELL_IMAGE, 0, 0, game.gui_group, game.inventory_cell_group)
        self.image = INVENTORY_CELL_IMAGE
        self.inventory = inventory
        self.rect.x = self.inventory.rect.x + x
        self.rect.y = self.inventory.rect.y + y
        self.selected = False
        self.item = None

    def update(self):
        if not self.item:
            if self.selected:
                self.image = INVENTORY_SELECTED_CELL_IMAGE
            else:
                self.image = INVENTORY_CELL_IMAGE
        else:
            if self.selected:
                self.image = INVENTORY_SELECTED_CELL_IMAGE_1
            else:
                self.image = INVENTORY_CELL_IMAGE_1
            self.image.blit(pygame.transform.scale(self.item.image, (80, 80)), (0, 0))
