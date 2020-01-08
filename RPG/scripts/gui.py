from RPG.scripts.game_object import GameObject
from RPG.scripts.consts import HP_BAR_FULL, TILE_SIZE
from RPG.scripts.utilities import load_image


class HealthBar(GameObject):
    def __init__(self, game, x, y):
        super().__init__(game, HP_BAR_FULL, x, y, game.gui_group, game.all_sprites)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        self.image = load_image('resources/sprites/gui/hp_bar/hp_bar_{}.png'.format(int(self.game.player.hp)))
