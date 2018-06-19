from chronometer import Chronometer
from client import Client
import math

class QueueTP(object):
    def __init__(self, lmbda, nq, chronometer):
        self.lmbda = lmbda
        self.nq = nq
        self.clients = []
        self.time_arrival_client = 0
        self.time_next_client = self.lmbda * (math.e ** (-1*self.lmbda*self.nq))
        self.chronometer = chronometer

        if self.nq > 0:
            for i in range(0, nq):
                self.receive()

    def get_lambda(self):
        return self.lmbda

    def quantity_client(self):
        return self.nq

    def get_time_arrival_client(self):
        return self.time_arrival_client

    def set_time_next_client(self):
        self.time_next_client += self.lmbda * (math.e ** (-1*self.lmbda*(self.nq)))

    def get_time_next_client(self):
        return self.time_next_client

    def dispatch(self):
        if len(self.clients) > 0:
            client = self.clients.pop(0)
            self.nq = self.nq - 1
            return client
        else:
            return None

    def receive(self):
        self.clients.append(Client())
        self.nq = self.nq + 1
        self.time_arrival_client = self.chronometer.time_simulation()
        self.set_time_next_client()

    def iterator(self, time):
        if time >= self.get_time_next_client():
            self.receive()

    def display(self):
        print "lambda: " + str(self.lmbda) + " Cant. clientes en la cola: " + str(self.quantity_client()) + \
              " Tiempo llegada ultimo cliente: " + str(self.get_time_arrival_client()) + \
              " Tiempo proximo cliente: " + str(self.get_time_next_client()) + "\n"