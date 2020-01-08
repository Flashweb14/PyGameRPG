from RPG.scripts.game_object import GameObject


class Fire(GameObject):
    def __init__(self, game, x, y):
        super().__init__(game, FIRE_IMAGE_1, x, y, game.all_sprites)