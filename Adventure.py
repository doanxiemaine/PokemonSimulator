import pygame
import json
import random
from camera import Camera
vec = pygame.math.Vector2

class Player():
    def __init__(self, color):
        self.x = random.randint(0, 4950)
        self.y = random.randint(0, 4950)
        self.width = 50
        self.height = 50
        self.color = color
        self.rect = (self.x, self.y, self.width, self.height)
        self.speed = 1
        self.offset = vec(0, 0)
        self.offset_float = vec(0, 0)
        self.DISPLAY_W, self.DISPLAY_H = 375, 275

    def draw(self, screen):
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
        self.rect = (self.x - self.offset.x, self.y - self.offset.y, self.width, self.height)

    def boundaries(self):
        if self.x < 0:
            self.x = 0
        elif self.x > 4950:
            self.x = 4950
        elif self.y < 0:
            self.y = 0
        elif self.y > 4950:
            self.y = 4950
            
    def scroll(self):
        self.offset_float.x += (self.x - self.offset_float.x - self.DISPLAY_W)
        self.offset_float.y += (self.y - self.offset_float.y - self.DISPLAY_H)
        self.offset.x, self.offset.y = int(self.offset_float.x), int(self.offset_float.y)

    def other_scroll(self, offset_x, offset_y):
        self.rect = (self.x - offset_x, self.y - offset_y, self.width, self.height)

class Pokemon:
    def __init__(self):
        self.x = random.randint(0, 4970)
        self.y = random.randint(0, 4970)
        self.width = 30
        self.height = 30
        self.color = (0, 0, 0)
        self.rect = (self.x, self.y, self.width, self.height)
        self.attributes = {}

        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def scroll(self, offset_x, offset_y):
        self.rect = (self.x - offset_x, self.y - offset_y, self.width, self.height)

    def set_attributes(self):
        with open('pokemon_data.json', 'r') as read_file:
            data = json.loads(read_file.read())
        self.attributes = random.choice(data)

class Adventure:
    def __init__(self, screen):
        self.pokemon_list = []
        self.spawn_timer = 0
        self.despawn_timer = 300000
        self.player = Player((255, 0, 0))
        self.screen = screen
        self.pokemon_name = ""

    def spawn_poke(self):
        self.now = pygame.time.get_ticks()
        if self.now - self.spawn_timer > 1200:
            self.spawn_timer = self.now
            self.pokemon = Pokemon()
            self.pokemon.set_attributes()
            self.pokemon_list.append(self.pokemon)
        self.despawn_poke()
        self.capture()
        self.capture_screen()

    def despawn_poke(self):
        if self.now - self.despawn_timer > 1200:
                self.pokemon_list.pop(0)
                self.despawn_timer = self.now

    def capture(self):
        for pokemon in self.pokemon_list:
            if self.player.y < (pokemon.y + pokemon.height) and self.player.y > pokemon.y and (self.player.x + self.player.width) > pokemon.x and (self.player.x + self.player.width) < (pokemon.x + pokemon.width):
                self.pokemon_name = pokemon.attributes['name']
                self.pokemon_list.pop(self.pokemon_list.index(pokemon))
            elif (self.player.y + self.player.height) > pokemon.y and (self.player.y + self.player.height) < (pokemon.y + pokemon.height) and (self.player.x + self.player.width) > pokemon.x and (self.player.x + self.player.width) < (pokemon.x + pokemon.width):
                self.pokemon_name = pokemon.attributes['name']
                self.pokemon_list.pop(self.pokemon_list.index(pokemon))
            elif (self.player.y + self.player.height) > pokemon.y and (self.player.y + self.player.height) < (pokemon.y + pokemon.height) and self.player.x  > pokemon.x and self.player.x < (pokemon.x + pokemon.width):
                self.pokemon_name = pokemon.attributes['name']
                self.pokemon_list.pop(self.pokemon_list.index(pokemon))
            elif self.player.y > pokemon.y and self.player.y < (pokemon.y + pokemon.height) and self.player.x  > pokemon.x and self.player.x < (pokemon.x + pokemon.width):
                self.pokemon_name = pokemon.attributes['name']
                self.pokemon_list.pop(self.pokemon_list.index(pokemon))


    def capture_screen(self):
        font = pygame.font.SysFont("comicsansms", 20)
        text = font.render(self.pokemon_name, 1, (0, 0, 0))
        self.screen.blit(text, (10, 10))



