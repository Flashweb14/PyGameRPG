import pygame
from scripts.game_objects.game_object import GameObject
from scripts.consts import ARROWS_INDICATOR, GAME_FONT


class ArrowsIndicator(GameObject):
    def __init__(self, game, x, y):
        super().__init__(game, ARROWS_INDICATOR, x, y, game.gui_group, game.all_sprites)
        self.rect.x = x
        self.rect.y = y
        num = GAME_FONT.render(str(self.game.player.arrows_left), 0, pygame.Color('black'))
        num_rect = num.get_rect()
        num_rect.x = 50
        num_rect.y = 10
        self.image.blit(num, num_rect)

    def update(self):
        pygame.draw.rect(self.image, (0, 0, 0, 0), (50, 0, 120, 64))
        num = GAME_FONT.render(str(self.game.player.arrows_left), 0, pygame.Color('black'))
        num_rect = num.get_rect()
        num_rect.x = 50
        num_rect.y = 10
        self.image.blit(num, num_rect)
