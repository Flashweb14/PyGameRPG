import pygame
from RPG.scripts.consts import INVENTORY_IMAGE, INVENTORY_CELL_IMAGE, INVENTORY_SELECTED_CELL_IMAGE
from RPG.scripts.game_object import GameObject
from RPG.scripts.gui.inventory.cell import Cell


class Inventory(GameObject):
    def __init__(self, game):
        super().__init__(game, INVENTORY_IMAGE, 0, 0, game.gui_group)
        self.rect.x = 1350
        self.rect.y = 200
        self.cells = []
        for i in range(45, 281, 95):
            for j in range(45, 376, 95):
                self.cells.append(Cell(self.game, self, j, i))

    def update(self):
        self.game.inventory_cell_group.draw(self.image)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                for cell in self.cells:
                    if cell.rect.collidepoint(event.pos):
                        for i in range(len(self.cells)):
                            if self.cells[i].selected:
                                self.cells[i].selected = False
                        cell.selected = True
                        self.game.inventory_cell_group.update()

    def add_item(self, obj):
        for cell in self.cells:
            if not cell.item:
                cell.item = obj
                break
        self.game.inventory_cell_group.update()




