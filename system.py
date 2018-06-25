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
        self.servers = []
        for i in range(0, s):
            self.servers.append(Server(mu, self.queue, self.chronometer, self.n))

    def iterator(self):
        time_next_event = []

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
        print "Sistema de colas \n"
        print "Cant. cliente en el sist.: " + str(self.n)
        self.chronometer.display()
        self.queue.display()

        for s in self.servers:
            s.display()

        print "---------------------------------\n"

    def get_status(self):
        pass
        # return self.n, self.queue.quantity_client(), self.queue.get_lambda(), self.servers.status, \
        #        self.servers, self.servers.get_mu()

    def set_status(self):
        pass