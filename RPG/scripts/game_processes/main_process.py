import pygame

pygame.init()


def main_process(game):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    game.player.hp -= 1
                if event.key == pygame.K_ESCAPE:
                    game.terminate()
            if event.type == pygame.QUIT:
                game.terminate()
            game.player.handle_event(event)
            if game.inventory_opened:
                game.inventory.handle_event(event)
            if game.has_error:
                for error in game.errors_group:
                    error.handle_event(event)
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
        if game.has_error:
            game.errors_group.draw(game.screen)
            game.errors_group.update()
        if game.inventory_opened:
            game.gui_group.draw(game.screen)
        game.clock.tick(game.FPS)
        if game.count < game.FPS:
            game.count += 1
        else:
            game.count = 0
        pygame.display.flip()
