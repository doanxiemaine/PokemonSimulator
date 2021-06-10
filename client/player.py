import pygame
import config as config

class Player:
    def __init__(self, game, x_position, y_position):
        print('player created')
        self.game = game
        self.position = [x_position, y_position]
        self.image = pygame.image.load("../imgs/trainer1.png")
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)
        
    def move(self, position_change):
        new_position = [self.position[0] + position_change[0], self.position[1] + position_change[1]]

        if new_position[0] < 0 or new_position[0] > (len(self.game.map[0]) -1):
            return
        if new_position[1] < 0 or new_position[1] > (len(self.game.map) -1):
            return
        
        if self.game.map[new_position[1]][new_position[0]] == 'T':
            return
        
        if self.game.map[new_position[1]][new_position[0]] == 'W':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'P1':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'P2':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'P3':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'P4':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'P5':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'P6':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'P7':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'P8':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'P9':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'P10':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'P11':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'P12':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'T':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'T1':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'T2':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'T3':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'T4':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'T5':
            return
        elif self.game.map[new_position[1]][new_position[0]] == 'T6':
            return
        
        self.position = new_position
    
    def update(self):
        print('player updated')
    
    def update_position(self, new_position):
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]
    
    def get_pos(self):
        return self.position
        
    def render(self, screen, camera):
        self.rect = pygame.Rect((self.position[0] - camera[0]) * config.SCALE, (self.position[1] - camera[1]) * config.SCALE, config.SCALE, config.SCALE)

        screen.blit(self.image, self.rect)