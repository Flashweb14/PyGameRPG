from scripts.game_objects.game_object import GameObject
from scripts.consts import HP_BAR_0, HP_BAR_1
import pygame


class HealthBar(GameObject):
    def __init__(self, game, x, y):
        super().__init__(game, HP_BAR_1, x, y, game.gui_group, game.all_sprites)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        pygame.draw.rect(self.image, (0, 0, 0, 0), (54, 12, 210, 30))
        if self.game.player.hp > 0:
            pygame.draw.rect(self.image, (239, 39, 39),
                             (54, 12, 210 // self.game.player.max_hp * self.game.player.hp +
                              210 % self.game.player.max_hp, 24))
            pygame.draw.rect(self.image, (138, 22, 22),
                             (54, 36, 210 // self.game.player.max_hp * self.game.player.hp +
                              210 % self.game.player.max_hp, 6))
        else:
            self.image = HP_BAR_0
