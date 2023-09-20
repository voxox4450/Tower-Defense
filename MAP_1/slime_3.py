import pygame, os
from enemy import Enemy

images = []

for x in range(1, 4):
    images.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("jpg/SLIMES/SLIME3", "TD_slimezielony_" + str(x) + ".png")),
            (96, 96)))
class Slime_3(Enemy):
    def __init__(self):
        super().__init__()
        self.money = 50
        self.images = images[:]
        self.max_health = 20
        self.health = self.max_health
