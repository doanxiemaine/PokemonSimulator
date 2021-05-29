from game_state import GameState
import pygame
import config
from pokecat import PokeCat
pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

pygame.display.set_caption('Pokémon')

clock = pygame.time.Clock()
game = PokeCat(screen)
game.set_up()

while game.game_state == GameState.RUNNING:
    clock.tick(15)
    game.update()
    pygame.display.flip()