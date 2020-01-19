import pygame
from RPG.scripts.game_object import GameObject
from RPG.scripts.consts import OVERWEIGHT_ERROR, TILE_SIZE, ERROR_CLOSE


class Error(GameObject):
    def __init__(self, game, type):
        errors_dict = {'overweight': OVERWEIGHT_ERROR}
        super().__init__(game, errors_dict[type], 1350 / TILE_SIZE, 10 / TILE_SIZE, game.errors_group)
        self.appear_time = pygame.time.get_ticks()
        self.close_btn = GameObject(game, ERROR_CLOSE, self.x + 475, 0, game.errors_group)
        self.close_btn.rect.x = self.x + 475
        self.close_btn.rect.y = self.y

    def update(self):
        if pygame.time.get_ticks() - self.appear_time >= 10 ** 4:
            self.game.errors_group.remove(self)
            self.game.has_error = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                if self.close_btn.rect.collidepoint(event.pos):
                    self.game.errors_group.remove(self)
                    self.game.has_error = False
