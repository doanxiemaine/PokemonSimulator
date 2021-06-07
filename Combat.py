import json
from pokemon import Pokemon

class Combat:
    def __init__(self, id):
        self.id = id
        self.turn = -1
        self.name = ""
        self.level = 0
        self.dmg = 0
        self.defense = 0
        self.ready = False
        self.data = {}
        self.player1 = {}
        self.player2 = {}
        self.winner = -1

    def get_pokemon(self, player):
        with open('trainer_data.json', 'r') as read_file:
            data = json.loads(read_file.read())
        if player == 0:
            data2 = data[0]
        else:
            data2 = data[1]
        self.name = data2['collection']['name']
        self.level = data2['collection']['level']
        with open('pokemon_data.json', 'r') as read_file:
            data2 = json.loads(read_file.read())
        for i in data2:
            if i['name'] == self.name:
                self.pokemon = Pokemon(i, self.level)
        return self.pokemon

    def connected(self):
        return self.ready

    def get_data(self, pokemon):
        self.data['name'] = pokemon.name
        self.data['stats'] = pokemon.stats
        self.data['type_defenses'] = pokemon.type_defenses
        #self.data['turn'] = self.turn
        return self.data

    def player_data(self, player, data):
        if self.turn == -1:
            if player == 0:
                self.player1 = json.loads(data)
            else:
                self.player2 = json.loads(data)
            self.turn = 0
        else:
            if player == 0:
                self.player2 = json.loads(data)
            else:
                self.player1 = json.loads(data)

    def game_work(self):
        self.work = True

    def play(self, player, pokemon, player_move):
        for move in pokemon.moves:
            move_details = pokemon.moves[move]
            if player_move == move:
                self.deal_damage(player, move_details)

    def deal_damage(self, p, move_details):
        type = move_details['type']
        type.lower()
        if p == 0:
            if type == 'normal':
                self.dmg = move_details['power']
                self.defense = player2['stats']['defense']
                self.player2['stats']['hp'] = self.player2['stats']['hp'] - (self.dmg - self.defense)
            else:
                for i in self.player2['type_defenses']:
                    if type == i:
                        self.dmg = move_details['power'] * player2['type_defense'][i]
                        self.defense = self.player2['stats']['defense']
                        player2['hp'] = self.dmg - self.defense
            self.turn = 1


        else:
            if type == 'normal':
                self.dmg = move_details['power']
                self.defense = player1['stats']['defense']
                self.player1['stats']['hp'] = self.dmg - self.defense
            else:
                for i in self.player1['type_defenses']:
                    if type == i:
                        self.dmg = move_details['power'] * player2['type_defense'][i]
                        self.defense = player2['stats']['defense']
                        self.player1['stats']['hp'] = self.player1['stats']['hp'] - (self.dmg - self.defense)
            self.turn = 0

    def get_turn(self):
        return self.turn

    def get_result(self):
        if self.player1['stats']['hp'] <= 0:
            self.winner = 1
        elif self.player2['stats']['hp'] <= 0:
            self.winner = 0
        return self.winner

