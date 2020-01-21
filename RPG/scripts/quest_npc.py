from RPG.scripts.game_object import GameObject


class QuestNPC(GameObject):
    def __init__(self, game, image, x, y):
        super().__init__(game, image, x, y, game.npc_group, game.all_sprites)

    def give_quest(self):
        print('quest')