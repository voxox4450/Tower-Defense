import pygame


class Button:
    def __init__(self, x, y, image, scale, name=None, cost=None):
        self.x = x
        self.y = y
        self.name = name
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.cost = cost

    def draw(self, surface):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

    def click(self, x1, y1):
        if self.x <= x1 <= self.x + self.width:
            if self.y <= y1 <= self.y + self.height:
                return True
        return False


class ButtonGame:
    def __init__(self, interface, image, name=None):
        self.name = name
        self.image = image
        self.x = 0
        self.y = 0
        self.interface = interface
        self.width = image.get_width()
        self.height = image.get_height()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def click(self, x1, y1):
        if self.x <= x1 <= self.x + self.width:
            if self.y <= y1 <= self.y + self.height:
                return True
        return False

    def update(self, name):
        if name == "upgrade":
            self.x = self.interface.x-90
            self.y = self.interface.y-100
        if name == "sell":
            self.x = self.interface.x+40
            self.y = self.interface.y-100


class ButtonPP:
    def __init__(self, x, y, on, off):
        self.x = x
        self.y = y
        self.on = on
        self.off = off
        self.img = on
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.paused = True

    def draw(self, surface):
        if self.paused:
            surface.blit(self.on, (self.x, self.y))
        else:
            surface.blit(self.off, (self.x, self.y))

    def click(self, x1, y1):
        if self.x <= x1 <= self.x + self.width:
            if self.y <= y1 <= self.y + self.height:
                return True
        return False


class Text:
    def __init__(self, text, text_color, cx, cy, font_size=40, font_family=None):
        self.text = str(text)
        self.text_color = text_color
        self.font_family = font_family
        self.font_size = font_size
        self.cx = cx
        self.cy = cy
        self.font = pygame.font.SysFont(self.font_family, self.font_size)

    def draw(self, surface):
        self.update()
        surface.blit(self.image, self.rect)

    def update(self):
        self.image = self.font.render(self.text, True, self.text_color)
        self.rect = self.image.get_rect()
        self.rect.center = self.cx, self.cy
