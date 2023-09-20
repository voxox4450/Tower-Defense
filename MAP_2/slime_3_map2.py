import pygame, os
from enemy import Enemy

images = []
for x in range(1, 4):
    images.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("jpg/SLIMES/SLIME3", "TD_slimezielony_" + str(x) + ".png")),
            (96, 96)))
class Slime_3_map_2(Enemy):
    def __init__(self):
        super().__init__()
        self.path = [(-10, 535), (17, 535), (672, 525), (696, 601), (770, 616), (788, 693), (899, 688), (935, 618), (1002, 598), (1036, 524), (1099, 491), (1076, 371), (1010, 341), (994, 274), (930, 267), (913, 193), (803, 189), (764, 243), (730, 282), (684, 291), (661, 357), (0, 356), (-19, 358)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_pos = 0
        self.money = 50
        self.images = images[:]
        self.max_health = 20
        self.health = self.max_health

    def draw(self, surface):
        self.img = self.images[self.animation_count // 5]
        modified_x = self.x - 35
        modified_y = self.y - 50
        surface.blit(self.img, (modified_x, modified_y))
        self.health_bar(surface)

    def health_bar(self, surface):
        length = 50
        moveBy = length / self.max_health
        health_bar = moveBy * self.health
        pygame.draw.rect(surface, (255, 0, 0), (self.x - 10, self.y - 40, length, 12), 0)
        pygame.draw.rect(surface, (0, 0, 255), (self.x - 10, self.y - 40, health_bar, 12), 0)
