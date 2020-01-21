from RPG.scripts.enemies.base_enemy import BaseEnemy
from RPG.scripts.consts import RED_SLIME_1, RED_SLIME_2, RED_SLIME_3
from RPG.scripts.enemies.hp_bar_npc import HealthBarNPC


class RedSlime(BaseEnemy):
    def __init__(self, game, x, y, name):
        super().__init__(game, RED_SLIME_1, x, y, 56, 20, name)
        self.animation_list = [RED_SLIME_1, RED_SLIME_2, RED_SLIME_3]
        self.speed = 60
        self.hp_bar = HealthBarNPC(game, self)
        self.name = 'Red Slime'

    def update(self):
        if self.game.count % 10 == 0:
            if self.animation_list.index(self.image) < 2:
                self.image = self.animation_list[self.animation_list.index(self.image) + 1]
            else:
                self.image = self.animation_list[0]
        super().update()
