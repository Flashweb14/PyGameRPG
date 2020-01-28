import pygame
from RPG.scripts.gui.button import Button
from RPG.scripts.game_processes.main_process import main_process
from RPG.scripts.consts import LEVEL

pygame.init()

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)


def main_menu_process(game):
    is_running = True
    new_game_btn = Button(game, 708, 200, 'new_game', game.main_menu_group)
    exit_btn = Button(game, 708, 488, 'exit', game.main_menu_group)

    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    if new_game_btn.rect.collidepoint(event.pos):
                        new_game_btn.on_click()
                        is_running = False
                        pygame.mouse.set_visible(False)
                        game.start_new_game(LEVEL)
                        main_process(game)
                    if exit_btn.rect.collidepoint(event.pos):
                        exit_btn.on_click()
                        game.terminate()
        screen.fill((48, 52, 109))
        game.main_menu_group.draw(game.screen)
        pygame.display.flip()
