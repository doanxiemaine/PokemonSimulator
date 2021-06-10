from game import PokeCat
import pygame
import config as config
from game_state import GameState
from network import Network
import time as t

class MainMenu:
    BG = (255,255,255)
    
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.name = ""
        self.name_font = pygame.font.SysFont("comicsans", 80)
        self.title_font = pygame.font.SysFont("comicsans", 120)
        self.enter_font = pygame.font.SysFont("comicsans", 60) 
        self.waiting = False
    
    def draw(self):
        self.win.fill(self.BG)
        title = self.title_font.render("Pokemon Simulator", 1, (0,0,0))
        self.win.blit(title, (self.WIDTH/2 - title.get_width()/2, 50))

        name = self.name_font.render("Type a Name: " + self.name, 1, (0,0,0))
        self.win.blit(name, (100, 400))

        pygame.display.update()
    
    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(config.FPS)
            self.draw()
            if self.waiting:
                run = False
                pygame.quit()
                print("IM HERE")
                world = PokeCat(self.n)

                while world.game_state == GameState.RUNNING:
                    world.set_up()
                    world.run()    
                """response = self.n.send({-1:[]})
                if response == '-1':
                    print (response)
                    run = False
                    g = Game(self.win, self.n)

                    for player in response:
                        p = Player(player)
                        g.add_player(p)
                    g.run()"""

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if len(self.name) > 1:
                            self.n = Network(self.name)
                            if self.n.get_flag() == -1:
                                self.n.client.close()
                                self.name = ""
                            if self.n.flag == 1:
                                self.waiting = True
                    else:
                        # gets the key name
                        key_name = pygame.key.name(event.key)

                        # converts to uppercase the key name
                        key_name = key_name.lower()
                        self.type(key_name)

    def type(self, char):
        if char == "backspace":
            if len(self.name) > 0:
                self.name = self.name[:-1]
        elif char == "space":
            self.name += " "
        elif len(char) == 1:
            self.name += char
"""n = Network('test')

world = PokeCat(n)

while world.game_state == GameState.RUNNING:
    world.set_up()
    world.run()   """ 

if __name__ == "__main__":
    pygame.font.init()
    main = MainMenu()
    main.run()