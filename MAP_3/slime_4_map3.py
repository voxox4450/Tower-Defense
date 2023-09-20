import pygame, os
from enemy import Enemy

images = []
for x in range(1,4):
    images.append(
        pygame.transform.scale(pygame.image.load(os.path.join("jpg/SLIMES/SLIME4", "TD_slimeczarny_" + str(x) + ".png")),
                               (96, 96)))
class Slime_4_map_3(Enemy):
    def __init__(self):
        super().__init__()
        self.path =[(-10, 447), (11, 451), (197, 446), (200, 280), (430, 270), (450, 445), (769, 446), (778, 772), (1050, 766), (1060, 414), (1286, 411), (1310, 411)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_pos = 0
        self.images = images[:]
        self.max_health = 25
        self.money = 60
        self.health = self.max_health

    def draw(self, surface):
        self.img = self.images[self.animation_count // 5]
        modified_x1 = self.x - 40
        modified_y1 = self.y - 35
        surface.blit(self.img, (modified_x1, modified_y1))
        self.health_bar(surface)

    def health_bar(self, surface):
        length = 50
        moveBy = length / self.max_health
        health_bar = moveBy * self.health
        pygame.draw.rect(surface, (255, 0, 0), (self.x - 15, self.y - 25, length, 12), 0)
        pygame.draw.rect(surface, (0, 0, 255), (self.x - 15, self.y - 25, health_bar, 12), 0)
