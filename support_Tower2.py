import math
import os
import pygame
from support_Tower1 import Support_Range_Tower


class Support_DMG_Tower(Support_Range_Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.range = 50
        self.name = 'support2'
        self.original_damage = 1
        self.effect = [1, 2, 3]
        self.price = [700, 1000, "MAX"]
        self._interface(self.price)
        self.level = 1
        self.effected = []
        self.iteration = 0


    def support(self, towers):
        for tower in towers:
            x, y = tower.x, tower.y
            dis = math.sqrt((self.x - x)**2 + (self.y-y)**2)
            if dis <= self.range + tower.width / 2:
                self.effected.append(tower)

        for tower in self.effected:
            tower.damage = tower.original_damage + self.effect[self.level - 1]

    def draw(self, surface):
        super().draw_radius(surface)

        support_tower_dmg = []
        for y in range(1, 5):
            support_tower_dmg.append(
                pygame.transform.scale(pygame.image.load(
                    os.path.join("jpg/support_Towers/Buffer", f'TD_buffer{self.level}_{y}.png')),
                    (64, 64)))
        self.tower_images = support_tower_dmg[:]

        self.iteration += 1
        if self.iteration >= len(self.tower_images)*10:
            self.iteration = 0

        dmg_tower = self.tower_images[self.iteration//10]
        surface.blit(dmg_tower, (self.x - (dmg_tower.get_width() / 2),(self.y - dmg_tower.get_height()+10)))

        if self.selected:
            self.interface.draw(surface)
