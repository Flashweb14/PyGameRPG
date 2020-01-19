from RPG.scripts.game_object import GameObject
from RPG.scripts.consts import IRON_SWORD


class Weapon(GameObject):
    def __init__(self, game, damage, x, y):
        super().__init__(game, IRON_SWORD, x, y, game.pickable_objects, game.all_sprites)
        self.damage = damage

    def use(self):
        if self.game.inventory.sword_slot.item:
            if self.game.inventory.sword_slot.item == self:
                self.game.inventory.add_item(self)
                self.game.inventory.sword_slot.item = None
                self.game.inventory.sword_slot.selected = False
                self.game.player.damage = 3
        else:
            self.game.inventory.sword_slot.item = self
            for cell in self.game.inventory.cells:
                if cell.item == self:
                    cell.item = None
                    cell.selected = False
            self.game.all_sprites.remove(self)
            self.game.pickable_objects.remove(self)
            self.game.player.damage = self.damage