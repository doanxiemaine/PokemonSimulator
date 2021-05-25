import pygame
from camera import Camera
vec = pygame.math.Vector2

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.speed = 1
        self.offset = vec(0, 0)
        self.offset_float = vec(0, 0)
        self.DISPLAY_W, self.DISPLAY_H = 375, 275

    def draw(self, screen,):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if keys[pygame.K_UP]:
            self.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.y += self.speed

        self.boundaries()
        self.update()


    def update(self):
        #self.x -= self.offset.x
        #self.y -= self.offset.y
        self.rect = (self.x , self.y, self.width, self.height)

    def boundaries(self):
        if self.x < 0:
            self.x = 0
        elif self.x > 9950:
            self.x = 9950
        elif self.y < 0:
            self.y = 0
        elif self.y > 9950:
            self.y = 9950
            
    #def scroll(self):
     #   self.offset_float.x += (self.x - self.offset_float.x - self.DISPLAY_W)
     #  self.offset_float.y += (self.y - self.offset_float.y - self.DISPLAY_H)
     #  self.offset.x, self.offset.y = int(self.offset_float.x), int(self.offset_float.y)

    
