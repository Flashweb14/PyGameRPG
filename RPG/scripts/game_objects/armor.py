from scripts.game_objects.game_object import GameObject
from scripts.consts import IRON_CHEST


class Armor(GameObject):
    def __init__(self, game, armor, x, y):
        super().__init__(game, IRON_CHEST, x, y, game.pickable_objects, game.all_sprites)
        self.armor = armor

    def use(self):
        if self.game.inventory.armor_slot.item:
            if self.game.inventory.armor_slot.item == self:
                self.game.inventory.add_item(self)
                self.game.inventory.armor_slot.item = None
                self.game.inventory.armor_slot.selected = False
                self.game.player.armor -= self.armor
        else:
            self.game.inventory.armor_slot.item = self
            for cell in self.game.inventory.cells:
                if cell.item == self:
                    cell.item = None
                    cell.selected = False
            self.game.all_sprites.remove(self)
            self.game.pickable_objects.remove(self)
            self.game.player.armor += self.armor
