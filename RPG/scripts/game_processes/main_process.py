from RPG.scripts.utilities import load_image
import pygame

pygame.init()


def main_process(game):
    while True:
        game.camera.update(game.player)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    game.player.hp -= 1
            if event.type == pygame.QUIT:
                game.terminate()
            game.player_group.update(event)
        if game.player.motion:
            for direction in game.player.motion:
                if game.player.motion.index(direction) == 0:
                    if game.player.animation % 7 == 0:
                        game.player.image = game.player.animation_dict[game.player.motion[0]][game.player.animation % 2]
                else:
                    if game.player.animation % 15 == 0:
                        game.player.image = game.player.animation_dict[game.player.motion[0]][game.player.animation % 2]
                game.player.animation += 1
                game.player.rect.x += game.player.speed_dict[direction][0]
                game.player.rect.y += game.player.speed_dict[direction][1]
                if pygame.sprite.spritecollideany(game.player, game.walls_group):
                    game.player.rect.x -= game.player.speed_dict[direction][0]
                    game.player.rect.y -= game.player.speed_dict[direction][1]
        for sprite in game.all_sprites:
            if sprite not in game.gui_group:
                game.camera.apply(sprite)

        game.hp_bar.image = load_image('resources/sprites/gui/hp_bar/hp_bar_{}.png'.format(game.player.hp))

        game.all_sprites.draw(game.screen)
        game.clock.tick(game.FPS)
        pygame.display.flip()
