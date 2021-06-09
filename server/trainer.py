from pokemon import Pokemon
import json
pokemon_data_json = open('pokemon_data.json', 'r')
pokemon_data = json.load(pokemon_data_json)
pokemon_data_json.close()

class Trainer:
    def __init__(self, addr, name):
        self.name = name
        self.collection = []
        self.party = []
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
    
    def add_pokemon_to_party(self, pokemon):
        self.party.append(pokemon)
    
    def remove_pokemon_from_party(self, pokemon):
        self.party.pop(pokemon)
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    def disconnect(self):
        pass
