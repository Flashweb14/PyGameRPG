from RPG.scripts.game_object import GameObject
from RPG.scripts.consts import USE_BUTTON, DROP_BUTTON, TILE_SIZE


class Button(GameObject):
    def __init__(self, game, inventory,  x, y, type):
        btns_dict = {'use': USE_BUTTON, 'drop': DROP_BUTTON}
        super().__init__(game, btns_dict[type], 0, 0, game.gui_group)
        self.inventory = inventory
        self.rect.x = self.inventory.rect.x + x
        self.rect.y = self.inventory.rect.y + y

    def on_click(self):
        print('click')