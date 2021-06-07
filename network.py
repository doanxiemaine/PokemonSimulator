import socket
import pickle
import jsonpickle
import json


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = socket.gethostname()
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(4096).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)

    def send_pokemon(self, data):
        try:
            self.client.send((json.dumps(data)).encode())
            return pickle.loads(self.client.recv(4096))
        except socket.error as e:
            print(e)

    def receive(self):
        return pickle.loads(self.client.recv(4096))