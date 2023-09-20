import pygame, os
from interface import Interface

upgrade_img = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu3_upgrade.png")), (60, 60))
sell_img = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu3_destroy.png")), (60, 60))


class Tower:
    def __init__(self, x, y):
        self.range = None
        self.x = x
        self.y = y
        self.sell_price = [200, 400, 500]
        self.price = [200, 300, "MAX"]
        self.level = 1
        self.selected = False
        self.menu = None
        self.shooter_images = []
        self.damage = 1
        self.height = self.width = 96
        self.tower_images = []
        self.name_click = None


    def draw(self, surface):
        images = self.tower_images[self.level-1]
        surface.blit(images, (self.x-images.get_width()//2, self.y-images.get_height()//2))
        if self.selected:
            self.interface.draw(surface)

    def draw_radius(self, surface):
        # draw range circle
        if self.selected:
            circle_surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(circle_surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            surface.blit(circle_surface, (self.x - self.range, self.y - self.range))
        else:
            self.name_click = None

    def click(self, x1, y1):
        images = self.tower_images[self.level-1]
        if self.x - images.get_width()//2 <= x1 <= self.x - images.get_width()//2 + self.width:
            if self.y - images.get_height()//2 <= y1 <= self.y + self.height - images.get_height()//2:
                return True
        return False

    def upgrade(self):
        if self.level < len(self.tower_images):
            self.level += 1
            self.damage += 1

    def _interface(self, price):
        self.interface = Interface(self, self.x, self.y, price)
        self.interface.add_button(upgrade_img, "upgrade")
        self.interface.add_button(sell_img, "sell")

    def move(self, x, y):
        self.x = x
        self.y = y
        self.interface.x = x
        self.interface.y = y
        self.interface.update()
