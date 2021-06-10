from player import Player
import config as config
from game_state import GameState
import math
import pygame
import json
import time as t
from os import path
import sys
import random

map_tile_image = {
    'B1': pygame.transform.scale(pygame.image.load('../imgs/bush1.png'), (config.SCALE, config.SCALE)),
    'B2': pygame.transform.scale(pygame.image.load('../imgs/bush2.png'), (config.SCALE, config.SCALE)),
    'B3': pygame.transform.scale(pygame.image.load('../imgs/bush3.png'), (config.SCALE, config.SCALE)),
    'BR1': pygame.transform.scale(pygame.image.load('../imgs/bridge1.png'), (config.SCALE, config.SCALE)),
    'BR2': pygame.transform.scale(pygame.image.load('../imgs/bridge2.png'), (config.SCALE, config.SCALE)),
    'BR3': pygame.transform.scale(pygame.image.load('../imgs/bridge3.png'), (config.SCALE, config.SCALE)),
    
    'G': pygame.transform.scale(pygame.image.load('../imgs/grass13.png'), (config.SCALE, config.SCALE)),
    
    'G1': pygame.transform.scale(pygame.image.load('../imgs/grass1.png'), (config.SCALE, config.SCALE)),
    'G2': pygame.transform.scale(pygame.image.load('../imgs/grass2.png'), (config.SCALE, config.SCALE)),
    'G3': pygame.transform.scale(pygame.image.load('../imgs/grass2.png'), (config.SCALE, config.SCALE)),
    
    'P4': pygame.transform.scale(pygame.image.load('../imgs/pond4.png'), (config.SCALE, config.SCALE)),
    'P5': pygame.transform.scale(pygame.image.load('../imgs/pond5.png'), (config.SCALE, config.SCALE)),
    'P6': pygame.transform.scale(pygame.image.load('../imgs/pond6.png'), (config.SCALE, config.SCALE)),
    'P7': pygame.transform.scale(pygame.image.load('../imgs/pond7.png'), (config.SCALE, config.SCALE)),
    'P10': pygame.transform.scale(pygame.image.load('../imgs/pond10.png'), (config.SCALE, config.SCALE)),
    'P11': pygame.transform.scale(pygame.image.load('../imgs/pond11.png'), (config.SCALE, config.SCALE)),
    'P12': pygame.transform.scale(pygame.image.load('../imgs/pond12.png'), (config.SCALE, config.SCALE)),
    
    'T': pygame.transform.scale(pygame.image.load('../imgs/tree.png'), (config.SCALE, config.SCALE)),
    'W': pygame.transform.scale(pygame.image.load('../imgs/water.png'), (config.SCALE, config.SCALE)),
}

class PokeCat:

    def __init__(self, connection=None):
        pygame.init()
        self.connection = connection
        self.screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption('Pokémon')
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(200, 100)
        self.load_map()
        self.game_state = GameState.RUNNING
        self.auto = False
        self.paused = False
        self.camera = [0, 0]
        self.poke_spawn = []
    
    def set_up(self):
        print('do set up')        
        current_trainer_pos = self.connection.send({3:[]})
        print(current_trainer_pos)
        self.player = Player(self, current_trainer_pos[0], current_trainer_pos[1])

    def load_map(self):
        game_folder = path.dirname(__file__)
        self.map = []
        #print(self.map)
        with open(path.join(game_folder, 'map1.txt')) as map_file:
            for line in map_file:
                tiles = []
                for teritory in line.split():
                    tiles.append(teritory)

                self.map.append(tiles)
    
    def run(self):
        # game loop - set self.playing = False to end the game
        self.game_state = GameState.RUNNING
        while self.game_state == GameState.RUNNING:
            self.dt = self.clock.tick(config.FPS) / 1000
            self.events()
            self.update()
            self.draw()
    
    def quit(self):
        self.game_state = GameState.ENDED
        pygame.quit()
        self.connection.send({5:[]})
        self.connection.client.close()
        sys.exit()
    
    def draw_text(self, text, font_name, size, color, x, y, align="center"):
        font = pygame.font.SysFont(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "nw":
            text_rect.topleft = (x, y)
        if align == "ne":
            text_rect.topright = (x, y)
        if align == "sw":
            text_rect.bottomleft = (x, y)
        if align == "se":
            text_rect.bottomright = (x, y)
        if align == "n":
            text_rect.midtop = (x, y)
        if align == "s":
            text_rect.midbottom = (x, y)
        if align == "e":
            text_rect.midright = (x, y)
        if align == "w":
            text_rect.midleft = (x, y)
        if align == "center":
            text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def update(self):
        # update portion of the game loop
        self.other_players_pos = self.connection.send({2:[]})
        self.poke_spawn = self.connection.send({6:[]})
        print(self.poke_spawn)
        if self.poke_spawn != []:
            self.paused = True
            text = f"New Pokemon: \nName: {self.poke_spawn['name']}\nLevel: {self.poke_spawn['level']}"
            self.draw_text(text, 'comicsans', 105, config.BLACK, config.SCREEN_WIDTH / 2, config.SCREEN_HEIGHT / 2)
            t.sleep(2)
            self.paused = False

        if self.auto:
            t.sleep(1)
            self.player.move([random.randint(-1, 2), random.randint(-1, 2)])

    def draw(self):
        self.screen.fill(config.BGCOLOR)
        self.render_map(self.screen)
        self.player.render(self.screen, self.camera)
        for pos in self.other_players_pos:
            print(pos)
            rect1 = pygame.Rect((pos[0] - self.camera[0])* config.SCALE, (pos[1] - self.camera[1]) * config.SCALE, config.SCALE, config.SCALE)
            image1 = pygame.image.load("../imgs/trainer1.png")
            image1 = pygame.transform.scale(image1, (config.SCALE, config.SCALE))
            print("IM HERE")
            self.screen.blit(image1, rect1)
        pygame.display.flip()
    
    def events(self):
        # catch all events here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_LEFT:
                    self.player.move([-1, 0])
                if event.key == pygame.K_RIGHT:
                    self.player.move([1, 0])
                if event.key == pygame.K_UP:
                    self.player.move([0, -1])
                if event.key == pygame.K_DOWN:
                    self.player.move([0, 1])
                if event.key == pygame.K_EQUALS:
                    self.auto = not self.auto
        self.connection.send({4:self.player.get_pos()})

    def render_map(self, screen):
        self.determine_camera()

        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect((x_pos - self.camera[0]) * config.SCALE, (y_pos - self.camera[1]) * config.SCALE, config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos += 1

            y_pos += 1            

    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) -1):
            return
        if new_position[1] < 0 or new_position[1] > (len(self.map) -1):
            return
        
        if self.map[new_position[1]][new_position[0]] == 'T':
            return
        
        if self.map[new_position[1]][new_position[0]] == 'W':
            return
        elif self.map[new_position[1]][new_position[0]] == 'P1':
            return
        elif self.map[new_position[1]][new_position[0]] == 'P2':
            return
        elif self.map[new_position[1]][new_position[0]] == 'P3':
            return
        elif self.map[new_position[1]][new_position[0]] == 'P4':
            return
        elif self.map[new_position[1]][new_position[0]] == 'P5':
            return
        elif self.map[new_position[1]][new_position[0]] == 'P6':
            return
        elif self.map[new_position[1]][new_position[0]] == 'P7':
            return
        elif self.map[new_position[1]][new_position[0]] == 'P8':
            return
        elif self.map[new_position[1]][new_position[0]] == 'P9':
            return
        elif self.map[new_position[1]][new_position[0]] == 'P10':
            return
        elif self.map[new_position[1]][new_position[0]] == 'P11':
            return
        elif self.map[new_position[1]][new_position[0]] == 'P12':
            return
        elif self.map[new_position[1]][new_position[0]] == 'T':
            return
        elif self.map[new_position[1]][new_position[0]] == 'T1':
            return
        elif self.map[new_position[1]][new_position[0]] == 'T2':
            return
        elif self.map[new_position[1]][new_position[0]] == 'T3':
            return
        elif self.map[new_position[1]][new_position[0]] == 'T4':
            return
        elif self.map[new_position[1]][new_position[0]] == 'T5':
            return
        elif self.map[new_position[1]][new_position[0]] == 'T6':
            return
        
        unit.update_position(new_position)
        
    def non_match_elements(self, list_a, list_b):
        non_match = []
        for i in list_a:
            if i not in list_b:
                non_match.append(i)
        return non_match

    def determine_camera(self):
        max_y_position = len(self.map) - config.SCREEN_HEIGHT / config.SCALE
        y_position = self.player.position[1] - math.ceil(round(config.SCREEN_HEIGHT / config.SCALE / 2))

        if y_position <= max_y_position and y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position

        max_x_position = len(self.map[0]) - config.SCREEN_WIDTH / config.SCALE
        x_position = self.player.position[0] - math.ceil(round(config.SCREEN_WIDTH / config.SCALE / 2))

        if x_position <= max_x_position and x_position >= 0:
            self.camera[0] = x_position
        elif x_position < 0:
            self.camera[0] = 0
        else:
            self.camera[0] = max_x_position