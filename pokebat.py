import json
import time
import random

letter_delay = 0.1
message_delay = 0.5

def type_message(message):
    for char in message:
        print(char, end="")
        time.sleep(letter_delay)
    print()
    time.sleep(message_delay)

class PokeBat:
    def __init__(self, id):
        self.id = id