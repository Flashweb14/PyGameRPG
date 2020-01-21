from RPG.scripts.game_objects.game_object import GameObject
from RPG.scripts.consts import USE_BUTTON, DROP_BUTTON, CLOSE_BUTTON, ACCEPT_BUTTON, REJECT_BUTTON


class Button(GameObject):
    def __init__(self, game, x, y, type, *groups):
        btns_dict = {'use': USE_BUTTON, 'drop': DROP_BUTTON, 'close': CLOSE_BUTTON, 'accept': ACCEPT_BUTTON,
                     'reject': REJECT_BUTTON}
        super().__init__(game, btns_dict[type], x, y, *groups)
        self.rect.x = x
        self.rect.y = y

    def on_click(self):
        print('click')
