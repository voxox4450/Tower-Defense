import pygame, os, math
from tower import Tower

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
            os.path.join("jpg\Tower_1", f"TD_Bogdan_{x}.png")),
            (96, 96)))


class Tower1Long(Tower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.iterator = 0
        self.range = 150
        self.original_range = self.range
        self.original_damage = self.damage
        self.damage = 1
        self.inRange = False
        self.Left = True
        self.name = 'long'
        self.tower_images = tower_images[:]
        self.shooter_images = shooter_images[:]
        self.width = self.height = 96
        self.price = [250, 450, 'MAX']
        self.moving = False
        self._interface(self.price)

    def draw(self, surface):
        super().draw_radius(surface)
        super().draw(surface)

        archer = self.shooter_images[self.iterator//7]
        surface.blit(archer, (self.x - (archer.get_width() / 2),
                                  (self.y - archer.get_height()+10)))

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
            self.damage += 0.75
            self.level += 1
