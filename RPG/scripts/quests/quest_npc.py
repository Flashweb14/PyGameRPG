from scripts.game_objects.game_object import GameObject
from scripts.gui.quest_gui import QuestGui


class QuestNPC(GameObject):
    def __init__(self, game, image, quest, x, y):
        super().__init__(game, image, x, y, game.npc_group, game.all_sprites)
        self.quest = quest

    def give_quest(self):
        if self.quest:
            QuestGui(self.game, self.quest, self)
