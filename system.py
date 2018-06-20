from queuetp import QueueTP
from server import Server
from chronometer import Chronometer


class SystemQueue(object):
    def __init__(self, s, lmbda, mu, nq):
        self.nq = nq
        self.n = nq
        self.s = s
        self.ei = 0
        self.chronometer = Chronometer()
        self.queue = QueueTP(lmbda, nq, self.chronometer)
        self.servers = Server(mu, self.queue, self.chronometer, self.n)
        # for i in range(0, s):
        #     self.servers.append(Server(mu))

    def iterator(self):
        time_next_client_server = self.servers.get_time_next_client()
        time_next_client_queue = self.queue.get_time_next_client()

        self.chronometer.iterator(min(time_next_client_queue, time_next_client_server))
        self.servers.iterator(self.chronometer.time_simulation(), self.n)
        self.queue.iterator(self.chronometer.time_simulation())

        if self.queue.quantity_client() >= 1:
            self.n = self.queue.quantity_client() + self.s
        else:
            # for s in self.servers:
            #     self.ei += s.request_status()
            self.n = self.queue.quantity_client() + self.servers.request_status()

    def display(self):
        print "Sistema de colas \n"
        print "Cant. cliente en el sist.: " + str(self.n)
        self.chronometer.display()
        self.queue.display()
        self.servers.display()
        print "---------------------------------\n"

    def get_status(self):
        return self.n, self.queue.quantity_client(), self.queue.get_lambda(), self.servers.status, \
               self.servers, self.servers.get_mu()

    def set_status(self):
        pass