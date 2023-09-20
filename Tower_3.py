import pygame, os, math, time
from Tower_1 import Tower1Long
from interface import Interface

tower_images = []
shooter_images = []
for x in range(3):
    tower_images.append(
        pygame.transform.scale(pygame.image.load(
            os.path.join("jpg\Tower_1", f'TD_platforma_{x}.png')),
            (64, 64)))
for x in range(1, 7):
    shooter_images.append(
        pygame.transform.scale(pygame.image.load(
            os.path.join("jpg\Tower_3", f"TD_Bogdanogien_{x}.png")),
            (96, 96)))

class Tower3Medium(Tower1Long):
    def __init__(self,x ,y):
        super().__init__(x, y)
        self.range = 110
        self.original_range = self.range
        self.original_damage = self.damage
        self.damage = 2.5
        self.tower_images = tower_images[:]
        self.shooter_images = shooter_images[:]
        self.name = 'medium'
        self.price = [300, 500, "MAX"]
        self._interface(self.price)

    def upgrade(self):
        if self.level < len(self.tower_images):
            self.damage += 0.5
            self.level += 1
            self.range += 10