import math
import os
import pygame
from tower import Tower


class Support_Range_Tower(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = self.height = 64
        self.range = 75
        self.name = 'support1'
        self.original_range = 1
        self.effect = [1, 1.3, 1.6]
        self.price = [900, 1100, "MAX"]
        self.archer_count = 0
        self._interface(self.price)
        self.level = 1
        self.effected = []
        self.iteration = 0

    def draw(self, surface):
        super().draw_radius(surface)
        support_action_range = []

        for y in range(1, 5):
            support_action_range.append(
                pygame.transform.scale(pygame.image.load(
                    os.path.join("jpg/support_Towers/Support", f'TD_support{self.level}_{y}.png')),
                    (64, 64)))
        self.tower_images = support_action_range[:]

        self.iteration += 1
        if self.iteration >= len(self.tower_images)*10:
            self.iteration = 0

        range_tower = self.tower_images[self.iteration//10]
        surface.blit(range_tower, (self.x - (range_tower.get_width() / 2), (self.y - range_tower.get_height()+10)))

        if self.selected:
            self.interface.draw(surface)

    def support(self, towers):
        for tower in towers:
            x, y = tower.x, tower.y
            dis = math.sqrt((self.x - x)**2 + (self.y-y)**2)
            if dis <= self.range + tower.width / 2:
                self.effected.append(tower)
        for tower in self.effected:
            tower.range = tower.original_range * self.effect[self.level - 1]
