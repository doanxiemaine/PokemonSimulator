import json
from pokemon import Pokemon

class Combat:
    def __init__(self, id):
        self.id = id
        self.turn = -1
        self.ready = False
        self.player1 = {}
        self.player2 = {}
        self.winner = -1
        self.dmg = [0,0]

    def get_turn(self):
        return self.turn

    def get_pokemon(self, player):
        with open('trainer_data.json', 'r') as read_file:
            data = json.loads(read_file.read())
        if player == 0:
            data2 = data[0]
            name = data2['collection']['name']
            level = data2['collection']['level']
            with open('pokemon_data.json', 'r') as read_file:
                data2 = json.loads(read_file.read())
            for i in data2:
                if i['name'] == name:
                    pokemon = Pokemon(i, level)
            self.player1['name'] = pokemon.name
            self.player1['stats'] = pokemon.stats
            self.player1['type_defenses'] = pokemon.type_defenses
            self.player1['moves'] = pokemon.moves
        else:
            data2 = data[1]
            name = data2['collection']['name']
            level = data2['collection']['level']
            with open('pokemon_data.json', 'r') as read_file:
                data2 = json.loads(read_file.read())
            for i in data2:
                if i['name'] == name:
                    pokemon = Pokemon(i, level)
            self.player2['name'] = pokemon.name
            self.player2['stats'] = pokemon.stats
            self.player2['type_defenses'] = pokemon.type_defenses
            self.player2['moves'] = pokemon.moves
            self.turn = 0

    def connected(self):
        return self.ready

    def get_data(self, pokemon):
        self.data['name'] = pokemon.name
        self.data['stats'] = pokemon.stats
        self.data['type_defenses'] = pokemon.type_defenses
        self.data['moves'] = pokemon.moves
        return self.data


    def get_move(self, player):
        if player == 0:
            moves = self.player1['moves']
        else:
            moves = self.player2['moves']
        for move in moves:
            move_details = moves[move]
            print(move, ':', move_details)

    def play(self, player, player_move):
        if player == 0:
            moves = self.player1['moves']
        else:
            moves = self.player2['moves']
        for move in moves:
            move_details = moves[move]
            if player_move == move:
                self.deal_damage(player, move_details)

    def deal_damage(self, p, move_details):
        type = move_details['type']
        type2 = type.lower()
        if p == 0:
            if type2 == 'normal':
                dmg = self.player1['stats']['attack']
                defense = self.player2['stats']['defense']
                self.player2['stats']['hp'] = self.player2['stats']['hp'] - (dmg - defense)
                self.dmg[0] = dmg - defense
            else:
                for i in self.player2['type_defenses']:
                    if type2 == i:
                        dmg = self.player1['stats']['attack'] * self.player2['type_defense'][i]
                        defense = self.player2['stats']['defense']
                        total = dmg - defense
                        if total <= 0:
                            total = 0
                        self.player2['hp'] = self.player2['stats']['hp'] - total
                        self.dmg[0] = totala
            self.turn = 1


        else:
            if type2 == 'normal':
                dmg = self.player2['stats']['attack']
                defense = self.player1['stats']['defense']
                self.player1['stats']['hp'] = self.player1['stats']['hp'] - (dmg - defense)
                self.dmg[1] = dmg - defense
            else:
                for i in self.player1['type_defenses']:
                    if type2 == i:
                        dmg = self.player2['stats']['attack'] * self.player1['type_defense'][i]
                        defense = self.player2['stats']['defense']
                        total = dmg - defense
                        if total <= 0:
                            total = 0
                        self.player1['stats']['hp'] = self.player1['stats']['hp'] - total
                        self.dmg[1] = total
            self.turn = 0

    def check_winner(self):
        if self.player1['stats']['hp'] <= 0:
            self.winner = 1
        elif self.player2['stats']['hp'] <= 0:
            self.winner = 0

    def get_result(self):
        return self.winner

    def surrender(self, player):
        if player == 0:
            self.winner = 1
        else:
            self.winner = 0


