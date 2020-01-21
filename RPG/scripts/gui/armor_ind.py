import pygame
from RPG.scripts.game_objects.game_object import GameObject
from RPG.scripts.consts import ARMOR_INDICATOR, GAME_FONT


class ArmorIndicator(GameObject):
    def __init__(self, game, x, y):
        super().__init__(game, ARMOR_INDICATOR, x, y, game.gui_group, game.all_sprites)
        self.rect.x = x
        self.rect.y = y
        num = GAME_FONT.render(str(self.game.player.armor), 0, pygame.Color('black'))
        num_rect = num.get_rect()
        num_rect.x = 70
        num_rect.y = 10
        self.image.blit(num, num_rect)

    def update(self):
        pygame.draw.rect(self.image, (0, 0, 0, 0), (64, 0, 120, 64))
        num = GAME_FONT.render(str(self.game.player.armor), 0, pygame.Color('black'))
        num_rect = num.get_rect()
        num_rect.x = 70
        num_rect.y = 10
        self.image.blit(num, num_rect)
