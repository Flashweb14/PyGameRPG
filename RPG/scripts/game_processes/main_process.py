import pygame

pygame.init()


def main_process(game):
    while True:
        while game.game_menu_opened:
            for event in pygame.event.get():
                game.game_menu.handle_event(event)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    game.game_menu_opened = True
            if event.type == pygame.QUIT:
                game.terminate()
            game.player.handle_event(event)
            if game.inventory:
                game.inventory.handle_event(event)
            for quest_gui in game.quest_gui_group:
                quest_gui.handle_event(event)
            for error in game.errors_group:
                error.handle_event(event)
        if game.inventory_opened or game.quest_gui_group or game.errors_group or game.game_menu_opened:
            pygame.mouse.set_visible(True)
        game.player.move()
        game.all_sprites.update()
        game.screen.fill((pygame.Color('grey')))
        game.camera.update(game.player)
        for sprite in game.all_sprites:
            if sprite not in game.gui_group:
                game.camera.apply(sprite)
        for sprite in game.background_group:
            game.camera.apply(sprite)
        for sprite in game.stopped_arrows_group:
            game.camera.apply(sprite)
        game.background_group.draw(game.screen)
        game.stopped_arrows_group.draw(game.screen)
        game.all_sprites.draw(game.screen)
        game.errors_group.draw(game.screen)
        game.errors_group.update()
        game.player_group.draw(game.screen)
        if game.inventory_opened:
            game.gui_group.draw(game.screen)
        if game.journal_opened:
            game.journal_group.draw(game.screen)
        game.quest_gui_group.draw(game.screen)
        if game.game_menu_opened:
            game.game_menu_group.draw(game.screen)
        game.clock.tick(game.FPS)
        if game.count < game.FPS:
            game.count += 1
        else:
            game.count = 0
        pygame.display.flip()
