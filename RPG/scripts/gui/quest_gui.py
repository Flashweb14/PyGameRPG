import pygame
from RPG.scripts.game_object import GameObject
from RPG.scripts.consts import QUEST_GUI
from RPG.scripts.gui.button import Button


class QuestGui(GameObject):
    def __init__(self, game, npc, reward):
        super().__init__(game, QUEST_GUI, 870, 200, game.quest_gui_group)
        self.rect.x = 870
        self.rect.y = 200
        self.npc = npc
        self.reward = reward
        self.accept_btn = Button(game, self.rect.x + 70, self.rect.y + 490, 'accept', game.quest_gui_group)
        self.reject_btn = Button(game, self.rect.x + 260, self.rect.y + 490, 'reject', game.quest_gui_group)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                if self.accept_btn.rect.collidepoint(event.pos):
                    self.accept_btn.on_click()
                if self.reject_btn.rect.collidepoint(event.pos):
                    for sprite in self.game.quest_gui_group:
                        self.game.quest_gui_group.remove(sprite)
