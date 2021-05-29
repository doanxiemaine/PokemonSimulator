import math
from game_state import GameState
import config
import pygame
from player import Player

class PokeCat:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.map = []
        self.camera =[0, 0]
    
    def set_up(self):
        player = Player(3, 3)
        self.player = player
        self.objects.append(player)
        print('do set up')
        self.game_state = GameState.RUNNING
        
        self.load_map('map1')

    def update(self):
        self.screen.fill(config.BLACK)
        print('update')

        self.handle_events()

        self.render_map(self.screen)

        for object in self.objects:
            object.render(self.screen, self.camera)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            
            #   handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_w: #  up
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_s: #  down
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_a: #  left
                    self.move_unit(self.player, [-1, 0])
                elif event.key == pygame.K_d: #  right
                    self.move_unit(self.player, [1, 0])
    
    def load_map(self, file_name):
        with open('maps/' + file_name + '.txt') as map_file:
            for line in map_file:
                tiles = []
                for teritory in line.split():
                    tiles.append(teritory)

                self.map.append(tiles)
            
            print(self.map)
    
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

map_tile_image = {
    'B1' : pygame.transform.scale(pygame.image.load('imgs/bush1.png'), (config.SCALE, config.SCALE)),
    'B2' : pygame.transform.scale(pygame.image.load('imgs/bush2.png'), (config.SCALE, config.SCALE)),
    'B3' : pygame.transform.scale(pygame.image.load('imgs/bush3.png'), (config.SCALE, config.SCALE)),
    'G1' : pygame.transform.scale(pygame.image.load('imgs/grass1.png'), (config.SCALE, config.SCALE)),
    'G2' : pygame.transform.scale(pygame.image.load('imgs/grass2.png'), (config.SCALE, config.SCALE)),
    'G3' : pygame.transform.scale(pygame.image.load('imgs/grass3.png'), (config.SCALE, config.SCALE)),
    'G4' : pygame.transform.scale(pygame.image.load('imgs/grass4.png'), (config.SCALE, config.SCALE)),
    'G5' : pygame.transform.scale(pygame.image.load('imgs/grass5.png'), (config.SCALE, config.SCALE)),
    'G6' : pygame.transform.scale(pygame.image.load('imgs/grass6.png'), (config.SCALE, config.SCALE)),
    'G7' : pygame.transform.scale(pygame.image.load('imgs/grass7.png'), (config.SCALE, config.SCALE)),
    'G8' : pygame.transform.scale(pygame.image.load('imgs/grass8.png'), (config.SCALE, config.SCALE)),
    'G9' : pygame.transform.scale(pygame.image.load('imgs/grass9.png'), (config.SCALE, config.SCALE)),
    'G10' : pygame.transform.scale(pygame.image.load('imgs/grass10.png'), (config.SCALE, config.SCALE)),
    'G11' : pygame.transform.scale(pygame.image.load('imgs/grass11.png'), (config.SCALE, config.SCALE)),
    'G12' : pygame.transform.scale(pygame.image.load('imgs/grass12.png'), (config.SCALE, config.SCALE)),
    'G13' : pygame.transform.scale(pygame.image.load('imgs/grass13.png'), (config.SCALE, config.SCALE)),
    'G14' : pygame.transform.scale(pygame.image.load('imgs/grass14.png'), (config.SCALE, config.SCALE)),
    'G15' : pygame.transform.scale(pygame.image.load('imgs/grass15.png'), (config.SCALE, config.SCALE)),
    'G16' : pygame.transform.scale(pygame.image.load('imgs/grass16.png'), (config.SCALE, config.SCALE)),
    'G17' : pygame.transform.scale(pygame.image.load('imgs/grass17.png'), (config.SCALE, config.SCALE)),
    'G18' : pygame.transform.scale(pygame.image.load('imgs/grass18.png'), (config.SCALE, config.SCALE)),
    'G19' : pygame.transform.scale(pygame.image.load('imgs/grass19.png'), (config.SCALE, config.SCALE)),
    'G20' : pygame.transform.scale(pygame.image.load('imgs/grass20.png'), (config.SCALE, config.SCALE)),
    'G21' : pygame.transform.scale(pygame.image.load('imgs/grass21.png'), (config.SCALE, config.SCALE)),
    'G22' : pygame.transform.scale(pygame.image.load('imgs/grass22.png'), (config.SCALE, config.SCALE)),
    'G23' : pygame.transform.scale(pygame.image.load('imgs/grass23.png'), (config.SCALE, config.SCALE)),
    'G24' : pygame.transform.scale(pygame.image.load('imgs/grass24.png'), (config.SCALE, config.SCALE)),
    'G25' : pygame.transform.scale(pygame.image.load('imgs/grass25.png'), (config.SCALE, config.SCALE)),
    'G26' : pygame.transform.scale(pygame.image.load('imgs/grass26.png'), (config.SCALE, config.SCALE)),
    'G27' : pygame.transform.scale(pygame.image.load('imgs/grass27.png'), (config.SCALE, config.SCALE)),
    'P1' : pygame.transform.scale(pygame.image.load('imgs/pond1.png'), (config.SCALE, config.SCALE)),
    'P2' : pygame.transform.scale(pygame.image.load('imgs/pond2.png'), (config.SCALE, config.SCALE)),
    'P3' : pygame.transform.scale(pygame.image.load('imgs/pond3.png'), (config.SCALE, config.SCALE)),
    'P4' : pygame.transform.scale(pygame.image.load('imgs/pond4.png'), (config.SCALE, config.SCALE)),
    'P5' : pygame.transform.scale(pygame.image.load('imgs/pond5.png'), (config.SCALE, config.SCALE)),
    'P6' : pygame.transform.scale(pygame.image.load('imgs/pond6.png'), (config.SCALE, config.SCALE)),
    'P7' : pygame.transform.scale(pygame.image.load('imgs/pond7.png'), (config.SCALE, config.SCALE)),
    'P8' : pygame.transform.scale(pygame.image.load('imgs/pond8.png'), (config.SCALE, config.SCALE)),
    'P9' : pygame.transform.scale(pygame.image.load('imgs/pond9.png'), (config.SCALE, config.SCALE)),
    'P10' : pygame.transform.scale(pygame.image.load('imgs/pond10.png'), (config.SCALE, config.SCALE)),
    'P11' : pygame.transform.scale(pygame.image.load('imgs/pond11.png'), (config.SCALE, config.SCALE)),
    'P12' : pygame.transform.scale(pygame.image.load('imgs/pond12.png'), (config.SCALE, config.SCALE)),
    'T1' : pygame.transform.scale(pygame.image.load('imgs/tree1.png'), (config.SCALE, config.SCALE)),
    'T2' : pygame.transform.scale(pygame.image.load('imgs/tree2.png'), (config.SCALE, config.SCALE)),
    'T3' : pygame.transform.scale(pygame.image.load('imgs/tree3.png'), (config.SCALE, config.SCALE)),
    'T4' : pygame.transform.scale(pygame.image.load('imgs/tree4.png'), (config.SCALE, config.SCALE)),
    'T5' : pygame.transform.scale(pygame.image.load('imgs/tree5.png'), (config.SCALE, config.SCALE)),
    'T6' : pygame.transform.scale(pygame.image.load('imgs/tree6.png'), (config.SCALE, config.SCALE)),
    'G' : pygame.transform.scale(pygame.image.load('imgs/ground.png'), (config.SCALE, config.SCALE)),
    'W' : pygame.transform.scale(pygame.image.load('imgs/water.png'), (config.SCALE, config.SCALE)),
}