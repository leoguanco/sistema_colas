from prettytable import PrettyTable

class Chronometer(object):
    def __init__(self):
        self.time = 0

    def time_simulation(self):
        return self.time

    def iterator(self, time):
        self.time += time

    def display(self):
        table = PrettyTable()
        table.field_names = ["Tiempo transcurrido"]
        table.add_row([self.time])
        print table
        # print "Tiempo transcurrido: " + str(self.time) + "\n"
