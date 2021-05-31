import pygame
import random
from Adventure import *
from camera import Camera
from menu import Button

pygame.init()
WIDTH, HEIGHT = 800, 600
run = True

pygame.display.set_caption("Pokemon game")

class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.btns = [Button("Adventure", 250, 150, (34,139,34)), Button("Combat", 250, 350, (255,0,0))]
        self.game_State = ["menu", "adventure", "combat"]
        self.state = self.game_State[0]
        self.ad = Adventure(self.screen)

    def menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in self.btns:
                    if btn.click(pos) and btn.text == "Adventure":
                        self.state = self.game_State[1]
                    #if btn.click(pos) and btn.text == "Combat":
                        #self.state = self.game_State[2]
        for btn in self.btns:
            btn.draw(self.screen)
        pygame.display.update()
        self.screen.fill((211, 211, 211))


    def catch(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        self.screen.fill((211, 211, 211))
        self.ad.player.draw(self.screen)
        self.ad.spawn_poke()
        for pokemon in self.ad.pokemon_list:
            pokemon.draw(self.screen)
        self.ad.player.scroll()
        for pokemon in self.ad.pokemon_list:
            pokemon.scroll(self.ad.player.offset.x, self.ad.player.offset.y)
        self.ad.player.move()
        pygame.display.update()


    def combat(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

    def state_manager(self):
        if self.state == self.game_State[0]:
            self.menu()
        if self.state == self.game_State[1]:
            self.catch()
        #if self.state == self.game_State[2]:
         #   self.combat()

g = Game()
while True:
    g.state_manager()




