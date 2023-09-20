import pygame, os
from enemy import Enemy

images = []
for x in range(1,4):
    images.append(
        pygame.transform.scale(pygame.image.load(os.path.join("jpg/SLIMES/SLIME6", "TD_slimebialy_" + str(x) + ".png")),
                               (96, 96)))

class Slime_6(Enemy):
    def __init__(self):
        super().__init__()
        self.money = 150
        self.images = images[:]
        self.max_health = 90
        self.health = self.max_health
