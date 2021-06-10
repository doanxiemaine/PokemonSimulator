"""
MAIN THREAD
Handles all of the connections, creating new games and
requests from the client(s).
"""
import socket
import threading
import json
import random

from trainer import Trainer
from world import World

class Server():

    def __init__(self):
        self.connecting_trainers = []
        self.world = World()
        
        self.game_id = 0

    def player_thread(self, conn, trainer):
        self.world.spawn_trainer(trainer)
        print(trainer)
        while True:
            try:
                try:
                    data = conn.recv(2048)
                    data = json.loads(data.decode())
                    print("Incoming: ", data)
                except Exception as e:
                    break

                keys = [int(key) for key in data.keys()]
                send_msg = {key:[] for key in keys}
                last_board = None
                

                for key in keys:
                    if key == -1:  # get game, returns a list of players
                        send = self.world.get_map()
                        send_msg[-1] = send

                    if key == 1:  # get game, returns a list of players
                        send = trainer
                        send_msg[1] = send

                    if key == 2:  # get game, returns a list of players
                        send = self.world.get_trainers_pos(trainer)
                        send_msg[2] = send
                    
                    if key == 3:  # get game, returns a list of players
                        send = trainer.get_pos()
                        send_msg[3] = send
                    
                    if key == 4:  # get game, returns a list of players
                        print(data['4'][:3])
                        trainer.set_pos(data['4'][:3])
                        self.world.check_exist_pokemon(trainer, data['4'][:3])
                    
                    if key == 5:  # get game, returns a list of players
                        self.world.trainers.remove(trainer)
                    
                    if key == 6:
                        self.world.spawn_wild_pokemons_pos()
                        if trainer.check_new_pokemon():
                            send = trainer.get_new_pokemon_info()
                            send_msg[6] = send
                        else:
                            send_msg[6] = []
                        

                send_msg = json.dumps(send_msg)
                print(send_msg)
                conn.sendall(send_msg.encode() + ".".encode())

            except Exception as e:
                #print(f"[EXCEPTION] {trainer.name}:", e)
                break

    def authentication(self, conn, addr):
        """
        authentication here
        :param ip: str
        :return: None
        """
        accounts_json = open('accounts.json', 'r')
        accounts = json.load(accounts_json)
        accounts_json.close()
        try:
            data = conn.recv(1024)
            name = str(data.decode())
            if not name:
                raise Exception("No name received")
            if name not in accounts:
                conn.sendall(str.encode('-1')) # Response code for login failed
                
            else:
                conn.sendall(str.encode('1')) # Response Code for Connected Client

                #conn.sendall("1".encode())

                trainer = Trainer(addr, name)
                trainer.generate_pokemon(random.randint(1, 4))
                thread = threading.Thread(target=self.player_thread, args=(conn, trainer))
                thread.start()
        except Exception as e:
            print("[EXCEPTION]", e)
            conn.close()
    def connection_thread(self):
        server = "192.168.1.5"
        port = 5556

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((server, port))
        except socket.error as e:
            str(e)

        s.listen(1)
        print("Waiting for a connection, Server Started")

        while True:
            conn, addr = s.accept()
            print("[CONNECT] New connection!")

            self.authentication(conn, addr)


if __name__ == "__main__":
    s = Server()
    thread = threading.Thread(target=s.connection_thread)
    thread.start()
