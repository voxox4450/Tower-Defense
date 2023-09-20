import pygame, os
from Tower_1 import Tower1Long

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
            os.path.join("jpg\Tower_2", f"TD_BogdanBombiarz_{x}.png")),
            (96, 96)))

class Tower2Short(Tower1Long):
    def __init__(self,x ,y):
        super().__init__(x, y)
        self.range = 100
        self.damage = 5
        self.original_range = self.range
        self.original_damage = self.damage
        self.name = 'short'
        self.tower_images = tower_images[:]
        self.shooter_images = shooter_images[:]
        self.price = [500, 600, "MAX"]
        self._interface(self.price)
