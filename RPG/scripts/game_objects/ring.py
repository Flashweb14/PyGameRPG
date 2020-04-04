from scripts.game_objects.game_object import GameObject
from scripts.consts import GOLDEN_RING


class Ring(GameObject):
    def __init__(self, game, type, x, y):
        rings_dict = {'golden_ring': GOLDEN_RING}
        super().__init__(game, rings_dict[type], x, y, game.pickable_objects, game.all_sprites)
        self.type = type

    def use(self):
        if self.game.inventory.ring_slot.item:
            if self.game.inventory.ring_slot.item == self:
                self.game.inventory.add_item(self)
                self.game.inventory.ring_slot.item = None
                self.game.inventory.ring_slot.selected = False
                self.give_effect()
        else:
            self.game.inventory.ring_slot.item = self
            for cell in self.game.inventory.cells:
                if cell.item == self:
                    cell.item = None
                    cell.selected = False
            self.game.all_sprites.remove(self)
            self.game.pickable_objects.remove(self)
            self.remove_effect()

    def give_effect(self):
        if self.type == 'golden_ring':
            self.game.player.crit_chance -= 20

    def remove_effect(self):
        if self.type == 'golden_ring':
            self.game.player.crit_chance += 20
