from scripts.quests.base_quest import BaseQuest


class KillQuest(BaseQuest):
    def __init__(self, game, title, description, enemy, reward, amount):
        super().__init__(game, title, description, reward)
        self.enemy = enemy
        self.amount = amount
        self.left = amount

    def update(self):
        if self.left == 0:
            self.done()
            self.game.player.quests.remove(self)
