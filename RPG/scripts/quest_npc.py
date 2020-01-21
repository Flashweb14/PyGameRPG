from RPG.scripts.game_object import GameObject
from RPG.scripts.gui.quest_gui import QuestGui


class QuestNPC(GameObject):
    def __init__(self, game, image, x, y):
        super().__init__(game, image, x, y, game.npc_group, game.all_sprites)

    def give_quest(self):
        QuestGui(self.game, self, None)
        self.game.quest_gui_opened = True

