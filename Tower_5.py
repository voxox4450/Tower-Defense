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
            os.path.join("jpg\Tower_5", f"TD_Bogdanpierun_{x}.png")),
            (96, 96)))


class Tower5Money(Tower1Long):
    def __init__(self,x ,y):
        super().__init__(x, y)
        self.range = 150
        self.damage = 2
        self.i = 2
        self.name = 'money'
        self.original_range = self.range
        self.original_damage = self.damage
        self.tower_images = tower_images[:]
        self.shooter_images = shooter_images[:]
        self.price = [300, 500, "MAX"]
        self._interface(self.price)

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

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
            if dis < self.range:
                self.inRange = True
                enemy_closet.append(enemy)

        enemy_closet.sort(key=lambda x: x.x)
        if len(enemy_closet) > 0:
            first_enemy = enemy_closet[0]
            if self.iterator == 3:
                if first_enemy.hit(self.damage):
                    money = first_enemy.money * self.i
                    enemies.remove(first_enemy)
        return money

    def upgrade(self):
        if self.level < len(self.tower_images):
            self.damage += 0.5
            self.level += 1
            self.range += 20
            self.i += 1
