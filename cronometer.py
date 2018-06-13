class Cronometer(object):
    def __init__(self):
        self.time = 0

    def time_simulation(self):
        return self.time

    def iterator(self, time):
        self.time += time

    def set_time(self, time):
        self.time = time