import pygame
from RPG.scripts.consts import INVENTORY_IMAGE, INVENTORY_CELL_IMAGE, INVENTORY_SELECTED_CELL_IMAGE
from RPG.scripts.game_object import GameObject
from RPG.scripts.gui.inventory.cell import Cell
from RPG.scripts.gui.inventory.button import Button


class Inventory(GameObject):
    def __init__(self, game):
        super().__init__(game, INVENTORY_IMAGE, 0, 0, game.gui_group)
        self.rect.x = 1350
        self.rect.y = 200
        self.cells = []
        for i in range(45, 281, 95):
            for j in range(45, 376, 95):
                self.cells.append(Cell(self.game, self, j, i))
        self.drop_btn = Button(game, self, 310, 465, 'drop')
        self.use_btn = Button(game, self, 310, 395, 'use')
        self.selected_cell = None

    def update(self):
        self.game.inventory_cell_group.draw(self.image)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                for cell in self.cells:
                    if cell.rect.collidepoint(event.pos):
                        if cell.item:
                            for i in range(len(self.cells)):
                                if self.cells[i].selected:
                                    self.cells[i].selected = False
                            cell.selected = True
                            self.selected_cell = cell
                        self.game.inventory_cell_group.update()
            if self.drop_btn.rect.collidepoint(event.pos):
                self.drop_item()
            if self.use_btn.rect.collidepoint(event.pos):
                if self.selected_cell:
                    self.selected_cell.item.use()
                    for i in range(len(self.cells)):
                        if self.cells[i] == self.selected_cell:
                            self.cells[i].item = None
                            self.cells[i].selected = False
                            self.selected_cell = None
                    self.game.inventory_cell_group.update()

    def add_item(self, obj):
        for cell in self.cells:
            if not cell.item:
                cell.item = obj
                break
        self.game.inventory_cell_group.update()

    def drop_item(self):
        self.game.all_sprites.add(self.selected_cell.item)
        self.game.pickable_objects.add(self.selected_cell.item)
        for i in range(len(self.cells)):
            if self.cells[i] == self.selected_cell:
                self.cells[i].item = None
        # self.game.inventory.remove(self.game.inventory.index(self.selected_cell.item))
        speed = self.game.player.speed_dict[self.game.player.direction]
        #self.selected_cell.item.x = self.game.player.x + speed[0]
        #self.selected_cell.item.y = self.game.player.y + speed[1]
        self.selected_cell.item = None




