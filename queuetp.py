from client import Client
from prettytable import PrettyTable
import numpy as np
import math


class QueueTP(object):
    def __init__(self, lmbda, nq, chronometer):
        self.lmbda = lmbda
        self.chronometer = chronometer
        self.nq = nq
        self.clients = []
        self.time_arrival_client = 0
        self.time_next_client = -1.0 * (math.log(1 - float(np.random.rand(1)[0]), math.e) / self.lmbda)

        if self.nq > 0:
            for i in range(0, nq):
                self.receive()

    def get_lambda(self):
        return self.lmbda

    def set_lambda(self, lmbda):
        self.lmbda = lmbda

    def set_nq(self, nq):
        if self.nq > 0:
            for i in range(0, nq):
                self.receive()

    def quantity_client(self):
        return len(self.clients)

    def get_time_arrival_client(self):
        return self.time_arrival_client

    def set_time_next_client(self):
        self.time_next_client = -1.0 * (math.log(1 - float(np.random.rand(1)[0]), math.e) / self.lmbda) + \
                                self.time_next_client

    def get_time_next_client(self):
        return self.time_next_client

    def dispatch(self):
        if len(self.clients) > 0:
            client = self.clients.pop(0)
            return client
        else:
            return None

    def receive(self):
        self.clients.append(Client())
        self.time_arrival_client = self.chronometer.time_simulation()
        self.set_time_next_client()

    def iterator(self, time):
        if time >= self.get_time_next_client():
            self.receive()

    def display(self):
        table = PrettyTable()
        table.field_names = ["lambda", "Cant. clientes en la cola", "Tiempo llegada ultimo cliente", "Tiempo proximo cliente"]
        table.add_row([self.lmbda, self.quantity_client(), self.get_time_arrival_client(), self.get_time_next_client()])
        print table