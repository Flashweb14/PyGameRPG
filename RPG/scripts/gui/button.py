from RPG.scripts.game_objects.game_object import GameObject
from RPG.scripts.consts import USE_BUTTON, DROP_BUTTON, CLOSE_BUTTON, ACCEPT_BUTTON, REJECT_BUTTON, NEW_GAME_BTN, \
    EXIT_BTN, CONTINUE_BTN, MAIN_MENU_BTN
from RPG.scripts.consts import CLICK_SOUND


class Button(GameObject):
    def __init__(self, game, x, y, type, *groups):
        btns_dict = {'use': USE_BUTTON, 'drop': DROP_BUTTON, 'close': CLOSE_BUTTON, 'accept': ACCEPT_BUTTON,
                     'reject': REJECT_BUTTON, 'new_game': NEW_GAME_BTN, 'exit': EXIT_BTN, 'continue': CONTINUE_BTN,
                     'main_menu': MAIN_MENU_BTN}
        super().__init__(game, btns_dict[type], x, y, *groups)
        self.rect.x = x
        self.rect.y = y
        self.sound = CLICK_SOUND

    def on_click(self):
        self.sound.play()

