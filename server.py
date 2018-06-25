from prettytable import PrettyTable
import math


class Server(object):
    def __init__(self, mu, queue, chronometer, n):
        self.mu = mu
        self.chronometer = chronometer
        self.status = 0
        self.client = None
        self.time_arrival_client = 0
        self.time_next_client = self.mu * (math.e ** (-1 * self.mu * self.chronometer.time_simulation()))
        self.queue = queue
        self.ns = 0

    def get_mu(self):
        return self.mu

    def request_status(self):
        return self.status

    def get_time_arrival_client(self):
        return self.time_arrival_client

    def set_time_next_client(self, n):
        self.time_next_client = self.mu * (math.e ** (-1 * self.mu * self.chronometer.time_simulation())) + \
                                self.time_arrival_client

    def get_time_next_client(self):
        return self.time_next_client

    def request_client(self, n):
        request = self.queue.dispatch()
        if request is not None:
            self.client = request
            self.status = 1
            self.time_arrival_client = self.chronometer.time_simulation()
            self.set_time_next_client(n)
            self.ns += 1
        else:
            self.status = 0

    def dispatch(self, n):
        self.client = None
        self.status = 0
        self.request_client(n)

    def iterator(self, time, n):
        if self.status == 0:
            self.request_client(n)
        else:
            if time >= self.get_time_next_client():
                self.dispatch(n)

    def display(self):
        table = PrettyTable()
        table.field_names = ["mu", "Estado del servidor", "Tiempo llegada ultimo cliente", "Tiempo proximo cliente", "Clientes pasados por el servidor"]
        table.add_row([self.mu, self.request_status(), self.get_time_arrival_client(), self.get_time_next_client(), self.ns])
        print table
        # print "mu: " + str(self.mu) + " Estado del servidor: " + str(self.request_status()) + \
        #       " Tiempo llegada ultimo cliente: " + str(self.get_time_arrival_client()) + \
        #       " Tiempo proximo cliente: " + str(self.get_time_next_client()) + \
        #       " Clientes pasados por el servidor: " + str(self.ns) + "\n"
