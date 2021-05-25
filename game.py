import pygame
from Adventure import Player
from camera import Camera

pygame.init()

game_State = ["menu", "adventure", "combat"]
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = Player(375, 275,50,50,(255,0,0))

run = True

pygame.display.set_caption("Pokemon game")

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 300
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
            return True
        else:
            return False

btns = [Button("Adventure", 250, 150, (34,139,34)), Button("Combat", 250, 350, (255,0,0))]

class Game():
    def __init__(self):
        self.state = game_State[0]

    def menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and btn.text == "Adventure":
                        self.state = game_State[1]
                    #if btn.click(pos) and btn.text == "Combat":
                        #self.state = game_State[2]
        for btn in btns:
            btn.draw(screen)
        pygame.display.update()
        screen.fill((211, 211, 211))


    def catch(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        screen.fill((211, 211, 211))
        player.draw(screen)
        #player.scroll()
        player.move()
        pygame.display.update()


    def combat(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

    def state_manager(self):
        if self.state == game_State[0]:
            self.menu()
        if self.state == game_State[1]:
            self.catch()


game = Game()
while run:
    game.state_manager()





