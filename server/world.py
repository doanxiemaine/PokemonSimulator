import json
import random
from pokemon import Pokemon

class World:
    
    pokemon_data_json = open('pokemon_data.json', 'r')
    pokemon_data = json.load(pokemon_data_json)
    pokemon_data_json.close()

    def __init__(self):
        self.map = []
        self.trainers = []
        self.load_map()
            
    def get_map(self):
        return self.map

    def load_map(self):
        with open('../maps/map1.txt') as map_file:
            for line in map_file:
                tiles = []
                for teritory in line.split():
                    tiles.append(teritory)

                self.map.append(tiles)
    
    def seek_movable(self):
        movable = []
        flag = False
        while not flag:
            print(len(self.map))
            print(len(self.map[0]))

            x = random.randint(0, len(self.map[0])-1)
            y = random.randint(0, len(self.map)-1)
            if self.map[y][x] == 'T' or self.map[y][x] == 'W':
                continue
            flag = True
        movable.append(x)
        movable.append(y)
        return movable

    
    def spawn_trainer(self, trainer):
        tile = self.seek_movable()
        print(tile)
        trainer.pos = tile
        self.trainers.append(trainer)
        

    
    def check_move_possible(self, x, y):
        if self.map[y][x]['TYPE'] == 'TREE':
            return False
        return True

    def update_pos(self, trainer, x, y):        
        if self.check_move_possible(x, y):
            self.map[self.trainers_pos[trainer][1]][self.trainers_pos[trainer][0]]['TRAINERS'].pop(trainer)
            self.trainers_pos[trainer][0] = x
            self.trainers_pos[trainer][1] = y
            self.map[y][x]['TRAINERS'].append(trainer)

    
    def get_trainers_pos(self):
        trainers_pos = []
        for trainer in self.trainers:
            trainers_pos.append(trainer.get_pos())
        return trainers_pos
    
    def udate_trainers_pos(self, pos):
        self.trainers_pos = pos
