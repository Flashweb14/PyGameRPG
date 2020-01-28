import pygame
from RPG.scripts.gui.button import Button
from RPG.scripts.game_processes.main_menu_process import main_menu_process


class DeathMenu:
    def __init__(self, game):
        self.game = game
        self.main_menu_btn = Button(game, 708, 200, 'main_menu', game.death_menu_group)
        self.exit_btn = Button(game, 708, 488, 'exit', game.death_menu_group)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                if self.exit_btn.rect.collidepoint(event.pos):
                    self.game.terminate()
                if self.main_menu_btn.rect.collidepoint(event.pos):
                    main_menu_process(self.game)
