import pygame
from RPG.scripts.game_object import GameObject
from RPG.scripts.consts import OVERWEIGHT_ERROR, TILE_SIZE
from RPG.scripts.gui.button import Button


class Error(GameObject):
    def __init__(self, game, type):
        errors_dict = {'overweight': OVERWEIGHT_ERROR}
        super().__init__(game, errors_dict[type], 1350 / TILE_SIZE, 45 / TILE_SIZE, game.errors_group)
        self.rect.x = 1350
        self.rect.y = 45
        self.appear_time = pygame.time.get_ticks()
        self.close_btn = Button(game, self.x + 475, self.y, 'close')

    def update(self):
        if pygame.time.get_ticks() - self.appear_time >= 10 ** 4:
            self.game.errors_group.remove(self)
            self.game.gui_group.remove(self.close_btn)
            self.game.has_error = False
            pygame.mouse.set_visible(False)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                if self.close_btn.rect.collidepoint(event.pos):
                    self.game.errors_group.remove(self)
                    self.game.gui_group.remove(self.close_btn)
                    self.game.has_error = False
                    pygame.mouse.set_visible(False)
