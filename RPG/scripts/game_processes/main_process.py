import pygame

pygame.init()


def main_process(game):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    game.player.hp -= 1
            if event.type == pygame.QUIT:
                game.terminate()
            game.player.handle_event(event)
        game.player.move()
        # game.camera.update(game.player)
        # for sprite in game.all_sprites:
        #     if sprite not in game.gui_group:
        #         game.camera.apply(sprite)
        game.all_sprites.update()
        game.screen.fill((pygame.Color('black')))
        game.all_sprites.draw(game.screen)
        game.clock.tick(game.FPS)
        if game.count < game.FPS:
            game.count += 1
        else:
            game.count = 0
        pygame.display.flip()
