from pokemon import Pokemon
import json
pokemon_data_json = open('pokemon_data.json', 'r')
pokemon_data = json.load(pokemon_data_json)
pokemon_data_json.close()

class Trainer:
    def __init__(self):
        self.name = input("How should other trainers call you? (name) ")
        self.collection = []
        self.party = []
        initial_pokemon_choice = input("Please choose your starting pokemon. You can choose one of the following:\n1. Bulbasaur\n2. Charmander\n3. Squirtle\nType in your choice index: (pokemon index) ")
        while initial_pokemon_choice != '1' and initial_pokemon_choice != '2' and initial_pokemon_choice != '3':
            initial_pokemon_choice = input("Please type in the index of your pokemon choice: (pokemon index) ")

        self.collection.append(self.generate_pokemon(initial_pokemon_choice))
        self.party.append(self.collection[0])

    def generate_pokemon(self, poke_choice):
        choice = {
            '1': 'Bulbasaur',
            '2': 'Charmander',
            '3': 'Squirtle',
        }
        for pokemon in pokemon_data:
            if pokemon['name'] == choice.get(poke_choice):
                return json.loads(Pokemon(pokemon, 1).to_json())

testing = Trainer()
trainer_data_json = open('trainer_data.json', 'w')
json.dump(testing.__dict__, trainer_data_json)
trainer_data_json.close()