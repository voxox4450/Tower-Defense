import pygame, os
from button import Button
from button import ButtonGame

currency_img = pygame.transform.scale(pygame.image.load(os.path.join("jpg/SLIMES/LIVES", "TD_menu3_waluta.png")), (60, 60))
currency2_img = pygame.transform.scale(pygame.image.load(os.path.join("jpg/SLIMES/LIVES", "TD_menu3_waluta.png")), (24, 24))
sidebar_img = pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu_sidebar.png")), (135, 490))
sidebar_img_map3 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(os.path.join("jpg/interface", "TD_menu_sidebar.png")), (135, 490)), 90)


class Interface:
    def __init__(self, tower, x, y, price, cost=None):
        self.x = x
        self.y = y
        self.width = 64
        self.items = 0
        self.item_cost = price
        self.sell_price = [200, 400, 500]
        self.images = []
        self.buttons = []
        self.tower = tower
        self.cost = cost
        self.font_money = pygame.font.SysFont("Berlin Sans FB Demi", 28)

    def add_button(self, image, name):
        self.items += 1
        self.buttons.append(ButtonGame(self, image, name))

    def draw(self, surface):
        for item in self.buttons:
            item.draw(surface)
            if item.name == 'upgrade':
                text = self.font_money.render(str(self.tower.price[self.tower.level-1]), False, (0, 0, 0))
                surface.blit(text, (item.x, item.y + currency_img.get_height() + 50))
                surface.blit(currency_img, (item.x, item.y + currency_img.get_height()))
            if item.name == 'sell':
                text = self.font_money.render(str(self.tower.sell_price[self.tower.level-1]), False, (0, 0, 0))
                surface.blit(text, (item.x, item.y + currency_img.get_height() + 50))
                surface.blit(currency_img, (item.x, item.y + currency_img.get_height()))

    def buying(self):
        return self.item_cost[self.tower.level-1]

    def selling(self):
        return self.sell_price[self.tower.level-1]

    def get_clicked(self, x1, y1):
        for button in self.buttons:
            if button.click(x1, y1):
                return button.name
        return None

    def update(self):
        for button in self.buttons:
            button.update(button.name)


class Hud(Interface):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 64
        self.items = 0
        self.sell_price = [200, 400, 500]
        self.images = []
        self.buttons = []
        self.moving = False
        self.font_money = pygame.font.SysFont("Berlin Sans FB Demi", 28)

    def add_button(self, image, x, y,name, cost):
        self.items += 1
        self.cost = cost
        button_x = self.x - x
        button_y = self.y - y
        scale = 1.0
        self.buttons.append(Button(button_x, button_y, image, scale, name, cost))

    def get_item_cost(self, name):
        for button in self.buttons:
            if button.name == name:
                return button.cost
        return -1

    def draw(self, surface, W=None):
        if W == 3:
            surface.blit(sidebar_img_map3, (self.x-5, self.y))
            for item in self.buttons:
                item.draw(surface)
                text = self.font_money.render(str(item.cost), False, (255, 255, 255))
                surface.blit(text, (item.x+2, item.y + currency_img.get_height()))
                surface.blit(currency2_img, (item.x + 20, item.y + currency_img.get_height()+30))

        else:
            surface.blit(sidebar_img, (self.x-55, self.y-5))
            for item in self.buttons:
                item.draw(surface)
                text = self.font_money.render(str(item.cost), False, (255, 255, 255))
                surface.blit(text, (item.x - currency_img.get_width(), item.y + 10))
                surface.blit(currency2_img, (item.x - currency_img.get_width()+10, item.y+35))
