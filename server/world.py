import json
import random
from pokemon import Pokemon
import time as t

class World:
    
    pokemon_data_json = open('pokemon_data.json', 'r')
    pokemon_data = json.load(pokemon_data_json)
    pokemon_data_json.close()

    def __init__(self):
        self.map = []
        self.trainers = []
        self.wild_pokemons_pos = []
        self.load_map()
        self.timer = t.perf_counter()
        self.disappear = self.timer
            
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

    
    def get_trainers_pos(self, requester):
        trainers_pos = []
        for trainer in self.trainers:
            if trainer == requester:
                continue
            trainers_pos.append(trainer.get_pos())
        return trainers_pos
    
    def udate_trainers_pos(self, pos):
        self.trainers_pos = pos

    def seek_bush(self):
        bush = []
        flag = False
        while not flag:
            print(len(self.map))
            print(len(self.map[0]))

            x = random.randint(0, len(self.map[0])-1)
            y = random.randint(0, len(self.map)-1)
            if self.map[y][x] == 'B1' or self.map[y][x] == 'B2' or self.map[y][x] == 'B3':
                flag = True            
        bush.append(x)
        bush.append(y)
        return bush
    
    def spawn_wild_pokemons_pos(self):
        count = 1
        batch = []
        if len(self.wild_pokemons_pos) == 0:
            while count < 50:
                bush = self.seek_bush()
                batch.append(bush)
                count += 1
            self.wild_pokemons_pos.append(batch)
        else:
            if t.perf_counter() - self.timer < 60.0:
                pass
            else:
                self.timer = t.perf_counter()
                while count < 20:
                    bush = self.seek_bush()
                    
                    for previous in self.wild_pokemons_pos:
                        if len(previous) == 0:
                            self.wild_pokemons_pos.remove(previous)
                        else:
                            if t.perf_counter() - self.disappear > 900.0:
                                self.wild_pokemons_pos.remove(previous)
                                self.disappear += 60.0
                        if bush not in previous:
                            batch.append(bush)
                            count += 1
            self.wild_pokemons_pos.append(batch)
        
    def get_wild_pokemons_pos(self):
        return self.wild_pokemons_pos
    
    def check_exist_pokemon(self, trainer, pos):
        exist = False
        for batch in self.wild_pokemons_pos:
            if pos in batch:
                batch.remove(pos)
                trainer.get_random_pokemon()
                exist = True
                break
        
