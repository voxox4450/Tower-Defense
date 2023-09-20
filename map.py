import time
import random


class Map:
    def __init__(self, Menu, towers, support, enemies, HUD, map_number, money_map, wave_map):
        self.towers = towers
        self.support = support
        self.enemies = enemies
        self.hud = HUD
        self.map_number = map_number
        self.money_map = money_map
        self.wave_map = wave_map
        self.menu = Menu

    def game(self):
        if not self.menu.pause:
            to_del = []

            for tower in self.towers:
                tower.draw(self.menu.screen)
                if self.map_number == 1:
                    self.menu.money += tower.attack(self.enemies)
                if self.map_number == 2:
                    self.menu.money_map2 += tower.attack(self.enemies)
                if self.map_number == 3:
                    self.menu.money_map3 += tower.attack(self.enemies)

            for tower in self.support:
                tower.draw(self.menu.screen)
                tower.support(self.towers)

            if time.time() - self.menu.timer >= random.randrange(1, 4)/2:
                self.menu.timer = time.time()
                self.menu.gen(self.enemies, self.map_number, self.wave_map)

            for enemy in self.enemies:
                enemy.draw(self.menu.screen)
                enemy.move()
                if enemy.x < -20 or enemy.y > 910 or enemy.x > 1315:
                    to_del.append(enemy)

            for delete in to_del:
                self.menu.lives -= 1
                self.enemies.remove(delete)

        if self.menu.pause:
            for tower in self.towers:
                tower.draw(self.menu.screen)

            for tower in self.support:
                tower.draw(self.menu.screen)
                tower.support(self.towers)

            for enemy in self.enemies:
                enemy.draw(self.menu.screen)

        self.menu.draw_lives()
        self.menu.draw_currency(self.money_map)
        if self.menu.object:
            self.menu.object.draw(self.menu.screen)

        self.menu.draw_wave()
