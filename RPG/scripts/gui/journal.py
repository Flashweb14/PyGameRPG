import pygame
from RPG.scripts.consts import QUEST_DESCRIPTION_FONT


class Journal(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__(game.journal_group)
        self.game = game
        self.image = pygame.Surface((500, 500), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = 10
        self.y = 50
        self.rect.x = 5
        self.rect.y = 220

    def update(self):
        self.image.fill((0, 0, 0, 0))
        string_y = 0
        for quest in self.game.player.quests:
            string_rendered = QUEST_DESCRIPTION_FONT.render(quest.title, 1, pygame.Color(210, 125, 44))
            rect = string_rendered.get_rect()
            rect.x = 0
            rect.y = string_y
            string_y += 42
            self.image.blit(string_rendered, rect)

            string_rendered = QUEST_DESCRIPTION_FONT.render(quest.enemy + ' ' + str(quest.amount - quest.left) +
                                                            '/' + str(quest.amount), 1, pygame.Color('black'))
            rect = string_rendered.get_rect()
            rect.x = 15
            rect.y = string_y
            string_y += 45
            self.image.blit(string_rendered, rect)
