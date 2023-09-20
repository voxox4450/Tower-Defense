import pygame, os
from enemy import Enemy

images = []
for x in range(1,4):
    images.append(
        pygame.transform.scale(pygame.image.load(os.path.join("jpg/SLIMES/SLIME4", "TD_slimeczarny_" + str(x) + ".png")),
                               (96, 96)))

class Slime_4(Enemy):
    def __init__(self):
        super().__init__()
        self.money = 60
        self.images = images[:]
        self.max_health = 25
        self.health = self.max_health
