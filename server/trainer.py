from pokemon import Pokemon
import json
import random
pokemon_data_json = open('pokemon_data.json', 'r')
pokemon_data = json.load(pokemon_data_json)
pokemon_data_json.close()

class Trainer:
    def __init__(self, addr, name):
        self.name = name
        self.collection = []
        self.party = []
        self.new_pokemon = False
        self.ip = addr
        self.pos = []

    def generate_pokemon(self, choice):
        options = {
            '1': 'Bulbasaur',
            '2': 'Charmander',
            '3': 'Squirtle',
        }
        
        for pokemon in pokemon_data:
            if pokemon['name'] == options.get(choice):
                
                self.party.append(Pokemon(pokemon, 1))
    
    def get_name(self):
        return self.name
    
    def get_pos(self):
        return self.pos
    
    def set_pos(self, pos):
        self.pos = pos
    
    def get_collection(self):
        return self.collection
    
    def add_pokemon_to_collection(self, pokemon):
        self.collection.append(pokemon)
    
    def remove_pokemon_from_collection(self, pokemon):
        self.collection.pop(pokemon)
    
    def get_party(self):
        return self.party
    
    def get_random_pokemon(self):
        level = random.randint(1, 100)
        self.collection.insert(0, Pokemon(pokemon_data[random.randint(0,len(pokemon_data))], level)) 
        self.new_pokemon = True
    
    def check_new_pokemon(self):
        return self.new_pokemon
    
    def get_new_pokemon_info(self):
        new = self.collection[0]
        self.new_pokemon = not self.new_pokemon
        return {'name': new.name, 'level': new.level}

    def to_json(self):
        return json.dumps(self.__dict__)
    
    def disconnect(self):
        pass
