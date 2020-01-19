from RPG.scripts.game_object import GameObject
from RPG.scripts.consts import FOOD_MEAT


class Food(GameObject):
    def __init__(self, game, type, x, y):
        food_dict = {'meat': (FOOD_MEAT, 2)}
        super().__init__(game, food_dict[type][0], x, y, game.pickable_objects, game.all_sprites)
        self.hp_increase = food_dict[type][1]

    def use(self):
        if self.game.player.hp + self.hp_increase <= self.game.player.max_hp:
            self.game.player.hp += self.hp_increase
        else:
            self.game.player.hp = self.game.player.max_hp
