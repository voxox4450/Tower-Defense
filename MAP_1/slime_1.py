import pygame, os
from enemy import Enemy

images = []
for x in range(3):
    images.append(
        pygame.transform.scale(pygame.image.load(os.path.join("jpg/SLIMES/SLIME1", "TD_slime1_f" + str(x) + ".png")),
                               (96, 96)))

class Slime_1(Enemy):
    def __init__(self):
        super().__init__()
        self.money = 20
        self.images = images[:]
        self.max_health = 10
        self.health = self.max_health
