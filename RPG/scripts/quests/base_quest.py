from RPG.scripts.consts import TILE_SIZE


class BaseQuest:
    def __init__(self, game, title, description, reward):
        self.reward = reward
        self.description = description
        self.title = title
        self.game = game

    def done(self):
        if not self.game.inventory.add_item(self.reward):
            self.reward.x = self.game.player.rect.x - TILE_SIZE
            self.reward.y = self.game.player.rect.y
