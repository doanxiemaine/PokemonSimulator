import random
import json


class Pokemon:
    def __init__(self, pokemon, level):
        self.name = pokemon['name']
        self.type = pokemon['type']
        self.exp = pokemon['base_exp']
        self.exp_level_up = self.exp * 2
        self.type_defenses = pokemon['type_defenses']
        self.level = 1
        self.ev = random.randrange(50, 101, 1) / 100
        self.stats = pokemon['base_stats']
        self.future_moves = pokemon['moves']
        self.moves = {}
        self.initial_stats_setup(level - 1)

    def initial_stats_setup(self, levels_to_update):
        while levels_to_update:
            self.exp *= 2
            self.upgrade()
            #self.update_available_moves()
            levels_to_update -= 1
        self.update_available_moves()
        self.exp = random.randint(self.exp, self.exp_level_up)

    def upgrade(self):
        for stat in self.stats:
            if stat == 'speed':
                continue
            else:
                self.stats[stat] *= (1 + self.ev)
        self.update_available_moves()
        self.exp_level_up *= 2
        self.level += 1

    def level_up(self):
        if self.level <= 100:
            self.upgrade()
            print('Congratulation, your ' + self.name + ' have reached level ' + str(self.level) + '\n')

    def update_available_moves(self):
        moves_left = self.future_moves
        for move in self.future_moves:
            if self.level >= move['move_level_needed']:
                self.moves[move['move_name']] = {
                    'type': move['move_type'],
                    'category': move['move_category'],
                    'power': move['move_power'],
                }
                moves_left.remove(move)
            else:
                continue
        self.future_moves = moves_left

    def set_exp(self, exp_gained):
        self.exp += exp_gained
        if self.exp >= self.exp_level_up:
            self.level_up()
        else:
            print('You need ' + (self.exp_level_up - self.exp) + ' more XP to reach next level\n')

    def to_json(self):
        return json.dumps(self.__dict__)