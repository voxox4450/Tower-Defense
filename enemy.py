import pygame, math


class Enemy:

    def __init__(self):
        self.width = 64
        self.height = 64
        self.animation_count = 0
        self.health = 0
        self.path = [(-19, 349), (5, 359), (590, 355), (585, 111), (365, 118), (351, 756), (90, 760), (80, 520), (800, 515), (805, 283), (950, 274), (955, 687), (531, 699), (526, 892), (520, 940)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.path_pos = 0
        self.dis = 0
        self.move_dis = 0
        self.images = []
        self.flipped = False
        self.max_health = 0

    def move(self):
        self.animation_count += 1
        if self.animation_count >= len(self.images)*5:
            self.animation_count = 0

        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (540, 930)
        else:
            x2, y2 = self.path[self.path_pos + 1]

        direction = ((x2 - x1)*2, (y2 - y1)*2)
        lenght = math.sqrt((direction[0])**2 + (direction[1])**2)
        direction = (direction[0]/lenght, direction[1]/lenght)

        if direction[0] < 0 and not(self.flipped):
            self.flipped = True
            for x, img in enumerate(self.images):
                self.images[x] = pygame.transform.flip(img, True, False)
        elif direction[0] > 0 and self.flipped:
            self.flipped = False
            for x, img in enumerate(self.images):
                self.images[x] = pygame.transform.flip(img, True, False)

        move_x, move_y = (self.x + direction[0], self.y + direction[1])
        self.dis += lenght
        self.x = move_x
        self.y = move_y

        #go to next point
        if direction[0] >= 0: # move right
            if direction[1] >= 0: # move down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1

            else: #move up
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1

        else: # move left
            if direction[1] >= 0: # move down
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1

            else: #move up
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1

    def health_bar(self, surface):
        length = 50
        hp = length / self.max_health
        health_bar = hp * self.health

        pygame.draw.rect(surface, (255, 0, 0), (self.x - 58, self.y - 30, length, 12), 0)
        pygame.draw.rect(surface, (0, 0, 255), (self.x - 58, self.y - 30, health_bar, 12), 0)

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            return True
        return False

    def draw(self, surface):
        self.img = self.images[self.animation_count//5]
        surface.blit(self.img, (self.x-80, self.y-45))
        self.health_bar(surface)
