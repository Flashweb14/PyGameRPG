from RPG.scripts.game_objects.game_object import GameObject
from RPG.scripts.consts import CHEST_CLOSED, CHEST_OPENED


class Chest(GameObject):
    def __init__(self, game, item, x, y):
        super().__init__(game, CHEST_CLOSED, x, y, game.chests_group, game.walls_group, game.all_sprites)
        self.is_opened = False
        self.item = item
        for group in self.item.groups():
            group.remove(self.item)

    def open(self):
        if self.item:
            self.item.x = self.x
            self.item.y = self.y + 80
            self.game.all_sprites.add(self.item)
            self.game.pickable_objects.add(self.item)
            self.item = None
        self.image = CHEST_OPENED
        self.is_opened = True

    def close(self):
        self.image = CHEST_CLOSED
        self.is_opened = False
