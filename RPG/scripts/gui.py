from RPG.scripts.game_object import GameObject
from RPG.scripts.consts import HP_BAR_0, HP_BAR_1
from RPG.scripts.utilities import load_image
import pygame


class HealthBar(GameObject):
    def __init__(self, game, x, y):
        super().__init__(game, HP_BAR_1, x, y, game.gui_group, game.all_sprites)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        pygame.draw.rect(self.image, (0, 0, 0, 0), (36, 8, 140, 20))
        if self.game.player.hp >= 1:
            pygame.draw.rect(self.image, (239, 39, 39),
                             (36, 8, 140 // self.game.player.max_hp * (self.game.player.hp - 1), 16))
            pygame.draw.rect(self.image, (138, 22, 22),
                             (36, 24, 140 // self.game.player.max_hp * (self.game.player.hp - 1), 4))
        else:
            self.image = HP_BAR_0
