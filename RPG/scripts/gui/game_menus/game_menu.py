import pygame
from RPG.scripts.gui.button import Button
from RPG.scripts.game_processes.main_menu_process import main_menu_process


class GameMenu:
    def __init__(self, game):
        self.game = game
        self.continue_btn = Button(game, 708, 200, 'continue', game.game_menu_group)
        self.main_menu_btn = Button(game, 708, 488, 'main_menu', game.game_menu_group)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                if self.continue_btn.rect.collidepoint(event.pos):
                    self.continue_btn.on_click()
                    self.game.game_menu_opened = False
                    pygame.mouse.set_visible(False)
                if self.main_menu_btn.rect.collidepoint(event.pos):
                    self.main_menu_btn.on_click()
                    main_menu_process(self.game)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                self.game.game_menu_opened = False
