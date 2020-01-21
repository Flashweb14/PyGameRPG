from RPG.scripts.game_objects.game_object import GameObject
from RPG.scripts.utilities import load_image


class Fire(GameObject):
    def __init__(self, game, x, y):
        super().__init__(game, load_image('resources/sprites/game_objects/fire/fire_1.png'), x, y, game.all_sprites,
                         game.harm_sprites)
        self.damage = 10
        self.image_num = 0

    def update(self):
        if self.game.count % 10 == 0:
            self.image = load_image('resources/sprites/game_objects/fire/fire_{}.png'.format(self.image_num))
            if self.image_num >= 3:
                self.image_num = 0
            else:
                self.image_num += 1
