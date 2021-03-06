import pygame
from scripts.game_objects.game_object import GameObject
from scripts.consts import QUEST_GUI, QUEST_DESCRIPTION_FONT
from scripts.gui.button import Button
from scripts.utilities import load_image


class QuestGui(GameObject):
    def __init__(self, game, quest, npc):
        super().__init__(game, load_image('resources/sprites/gui/quest/quest_gui.png'), 870, 200, game.quest_gui_group)
        self.rect.x = 870
        self.rect.y = 200
        self.quest = quest
        self.npc = npc
        self.accept_btn = Button(game, self.rect.x + 70, self.rect.y + 490, 'accept', game.quest_gui_group)
        self.reject_btn = Button(game, self.rect.x + 260, self.rect.y + 490, 'reject', game.quest_gui_group)
        description_y = 50
        for string in quest.description:
            string_rendered = QUEST_DESCRIPTION_FONT.render(string, 0, pygame.Color('white'))
            string_rect = string_rendered.get_rect()
            string_rect.x = 55
            string_rect.y = description_y
            self.image.blit(string_rendered, string_rect)
            description_y += 40
        self.quest.reward.rect.x = 180 + (105 - self.quest.reward.rect.w) // 2
        self.quest.reward.rect.y = 370 + (105 - self.quest.reward.rect.h) // 2
        self.image.blit(self.quest.reward.image, self.quest.reward.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                if self.accept_btn.rect.collidepoint(event.pos):
                    self.accept_btn.on_click()
                    if self.quest not in self.game.player.quests:
                        self.game.player.quests.append(self.quest)
                        self.game.journal.update()
                        for sprite in self.game.quest_gui_group:
                            self.game.quest_gui_group.remove(sprite)
                        self.npc.quest = None
                        pygame.mouse.set_visible(False)
                if self.reject_btn.rect.collidepoint(event.pos):
                    self.reject_btn.on_click()
                    for sprite in self.game.quest_gui_group:
                        self.game.quest_gui_group.remove(sprite)
                    pygame.mouse.set_visible(False)
