from game import PokeCat
import pygame
import config as config
from game_state import GameState
from network import Network
import time as t

n = Network('test')

world = PokeCat(n)

while world.game_state == GameState.RUNNING:
    world.set_up()
    world.run()    