from scripts.game_objects.game_object import GameObject
from scripts.consts import IRON_SWORD, WOODEN_BOW


class Weapon(GameObject):
    def __init__(self, game, type, damage, x, y):
        weapon_dict = {'iron_sword': IRON_SWORD, 'wooden_bow': WOODEN_BOW}
        super().__init__(game, weapon_dict[type], x, y, game.pickable_objects, game.all_sprites)
        self.damage = damage
        self.type = type

    def use(self):
        if self.type == 'iron_sword':
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
        else:
            if self.game.inventory.bow_slot.item:
                if self.game.inventory.bow_slot.item == self:
                    self.game.inventory.add_item(self)
                    self.game.inventory.bow_slot.item = None
                    self.game.inventory.bow_slot.selected = False
                    self.game.player.bow_damage = 3
            else:
                self.game.inventory.bow_slot.item = self
                for cell in self.game.inventory.cells:
                    if cell.item == self:
                        cell.item = None
                        cell.selected = False
                self.game.all_sprites.remove(self)
                self.game.pickable_objects.remove(self)
                self.game.player.bow_damage = self.damage
