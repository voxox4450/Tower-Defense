import pygame, os
from enemy import Enemy

images = []
for x in range(1, 4):
    images.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("jpg/SLIMES/SLIME2", "TD_slimezolty_" + str(x) + ".png")),
            (96, 96)))
class Slime_2(Enemy):
    def __init__(self):
        super().__init__()
        self.money = 30
        self.images = images[:]
        self.max_health = 12
        self.health = self.max_health
