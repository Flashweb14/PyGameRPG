import pygame
from RPG.scripts.game_objects.game_object import GameObject
from RPG.scripts.consts import HP_BAR_NPC


class HealthBarNPC(GameObject):
    def __init__(self, game, npc):
        super().__init__(game, HP_BAR_NPC, npc.rect.x, npc.rect.y - 20, game.all_sprites)
        self.npc = npc

    def update(self):
        self.x = self.npc.x
        self.y = self.npc.y - 15
        pygame.draw.rect(self.image, (0, 0, 0, 0), (4, 4, 56, 8))
        pygame.draw.rect(self.image, (0, 255, 33), (4, 4, 56 // self.npc.max_hp * self.npc.hp, 8))
