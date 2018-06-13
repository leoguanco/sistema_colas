from cronometer import Cronometer
from client import Client

class Queue(object):
    def __init__(self, lmbda, nq):
        self.lmbda = lmbda
        self.nq = nq
        self.clients = []
        self.cronometer = Cronometer()
        self.tn = self.lmbda / 60

        if(self.nq > 0):
            for i in range(0, nq):
                self.receive()

    def quantity_client(self):
        return self.nq

    def time_arrival_client(self):
        return self.cronometer.time_simulation()

    def time_next_client(self):
        return self.tn

    def dispatch(self):
        self.clients.pop(0)

    def receive(self):
        self.clients.append(Client())