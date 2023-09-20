import pygame, os, math
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
            os.path.join("jpg\Tower_4", f"TD_Bogdanlod_{x}.png")),
            (96, 96)))


class Tower4Slow(Tower1Long):
    def __init__(self,x ,y):
        super().__init__(x, y)
        self.range = 300
        self.original_range = self.range
        self.original_damage = self.damage
        self.damage = 1
        self.name = 'slow'
        self.tower_images = tower_images[:]
        self.shooter_images = shooter_images[:]
        self.price = [600,700,"MAX"]
        self._interface(self.price)
        self.speed = -10

    def attack(self, enemies):
        if self.inRange and not self.moving:
            self.iterator += 1
            if self.iterator >= len(self.shooter_images) * 7:
                self.iterator = 0
        else:
            self.iterator = 0

        self.inRange = False
        money = 0
        enemy_closet = []
        for enemy in enemies:
            x, y = enemy.x, enemy.y

            dis = math.sqrt((self.x - x)**2 + (self.y-y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closet.append(enemy)

        enemy_closet.sort(key=lambda x: x.x)
        if len(enemy_closet) > 0:
            first_enemy = enemy_closet[0]
            if self.iterator == 3:
                if first_enemy.hit(self.damage):
                    money = first_enemy.money
                    enemies.remove(first_enemy)
        return money

    def upgrade(self):
        if self.level < len(self.tower_images):
            self.damage += 3
            self.level += 1
            self.range += 50
