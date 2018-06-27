from queuetp import QueueTP
from server import Server
from chronometer import Chronometer
from prettytable import PrettyTable


class SystemQueue(object):
    def __init__(self, s, lmbda, mu, nq):
        self.lmbda = lmbda
        self.nq = nq
        self.n = nq
        self.mu = mu
        self.s = s
        self.ei = 0
        self.chronometer = Chronometer()
        self.queue = QueueTP(self.lmbda, self.nq, self.chronometer)
        self.servers = []
        for i in range(0, s):
            self.servers.append(Server(self.mu, self.queue, self.chronometer))

    def get_lmbda(self):
        return self.lmbda

    def get_s(self):
        return self.s

    def get_mu(self):
        return self.mu

    def get_nq(self):
        return self.nq

    def set_status(self, s, lmbda, mu, nq):
        self.queue.set_lambda(lmbda)
        self.queue.set_nq(nq)
        self.mu = mu
        self.lmbda = lmbda

        for i in range(0, s):
            self.servers.append(Server(self.mu, self.queue, self.chronometer))

        for s in self.servers:
            s.set_mu(mu)

    def iterator(self):
        time_next_event = []
        self.n = 0
        self.ei = 0

        for s in self.servers:
            time_next_event.append(s.get_time_next_client())

        time_next_event.append(self.queue.get_time_next_client())

        self.chronometer.iterator(min(time_next_event))
        self.queue.iterator(self.chronometer.time_simulation())

        for s in self.servers:
            s.iterator(self.chronometer.time_simulation(), self.n)

        if self.queue.quantity_client() >= 1:
            self.n = self.queue.quantity_client() + self.s
        else:
            for s in self.servers:
                self.ei += s.request_status()
            self.n = self.queue.quantity_client() + self.ei

    def display(self):
        table = PrettyTable()
        table.field_names = ["Cant. cliente en el sist."]
        table.add_row([self.n])
        print "Sistema de colas \n"
        print table
        self.chronometer.display()
        self.queue.display()

        for s in self.servers:
            s.display()

    def get_status(self):
        pass
        # return self.n, self.queue.quantity_client(), self.queue.get_lambda(), self.servers.status, \
        #        self.servers, self.servers.get_mu()