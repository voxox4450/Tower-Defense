import pygame, os
from enemy import Enemy

images = []
for x in range(1,4):
    images.append(
        pygame.transform.scale(pygame.image.load(os.path.join("jpg/SLIMES/SLIME5", "TD_slimeniebieski_" + str(x) + ".png")),
                               (96, 96)))

class Slime_5(Enemy):
    def __init__(self):
        super().__init__()
        self.money = 100
        self.images = images[:]
        self.max_health = 60
        self.health = self.max_health
