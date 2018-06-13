from cronometer import Cronometer

class Server(object):
    def __init__(self, mu):
        self.mu = mu
        self.status = 0
        self.cronometer = Cronometer()
        self.tn = self.mu / 60
        self.client = None

    def request_status(self):
        return self.status

    def time_arrival_client(self):
        return self.cronometer.time_simulation()

    def time_next_client(self):
        return self.tn

    def request_client(self, request):
        if request != None:
            self.client = request
            self.status = 1
            self.cronometer.set_time(1)
        else:
            self.status = 0

    def dispatch(self, client):
        self.client = None
        self.status = 0
        self.request_client(client)