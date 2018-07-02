from prettytable import PrettyTable
import math


class Statistics(object):

    def __init__(self, lbmda, mu, s, n, nq):
        self.lbmda = lbmda
        self.mu = mu
        self.s = s
        self.n = n
        self.nq = nq
        self.p = 0
        self.len = 0
        self.lq = 0
        self.w = 0
        self.wq = 0
        self.ws = 0

    # p
    def set_intensity_traffic(self):
        self.p = self.lbmda / self.mu

    def get_intensity_traffic(self):
        return self.p

    # L
    def set_client_quantity_system(self):
        if self.s > 1:
            # MMS
            numerator = self.lbmda ** (self.s + 1)
            denominator = math.factorial(self.s - 1) * (self.mu ** (self.s - 1)) * ((self.s * self.mu - self.lbmda)**2)
            p0 = self.get_p0(self.n)
            self.len = (numerator / denominator) * p0 + (self.lbmda / self.mu)
        else:
            # MM1
            self.len = self.get_expectation(self.n)

    def get_client_quantity_system(self):
        return self.len

    # LQ
    def set_client_quantity_queue(self):
        if self.s > 1:
            # MMS
            numerator = self.lbmda ** (self.s + 1)
            denominator = math.factorial(self.s - 1) * (self.mu ** (self.s-1)) * ((self.s * self.mu - self.lbmda)**2)
            p0 = self.get_p0(self.nq)
            self.lq = (numerator / denominator) * p0
        else:
            # MM1
            self.lq = self.get_expectation(self.nq)

    def get_client_quantity_queue(self):
        return self.lq

    # E
    def get_expectation(self, n):
        expectation_summation = 0
        for x in range(0, n):
            expectation_summation += self.lbmda * self.probability_n(x)
        return expectation_summation

    # P0
    def get_p0(self, n):
        if self.s > 1:
            # MMS
            first_summation_segment = 0
            for x in range(0, self.s):
                first_summation_segment += (1 / math.factorial(x)) * ((self.lbmda / self.mu) ** x)
            second_summation_segment = (math.factorial(self.s) * (self.mu ** 2) * (self.s * self.mu - self.lbmda))
            denominator = 1 + first_summation_segment + ((self.lbmda ** (self.s + 1)) / second_summation_segment)
            p0 = 1 / denominator
        else:
            # MM1
            p0 = 1 / (1 + self.cn(n))
        return p0

    # Pn
    def probability_n(self, n):
        p0 = self.get_p0(n)
        cn = self.get_intensity_traffic() ** n
        pn = cn * p0
        return pn

    # Cn
    def cn(self, n):
        cn_summation = 0
        if self.s > 1:
            # MMS
            for x in range(1, self.s):
                if x <= self.s:
                    cn_summation += (1/math.factorial(x)) * ((self.lbmda / self.mu) ** x)
                elif x >= self.s + 1:
                    cn_summation += (1/(math.factorial(self.s)*(self.s**(x-self.s)))) * ((self.lbmda / self.mu) ** x)
        else:
            for x in range(0, n):
                cn_summation += self.get_intensity_traffic()**x
        return cn_summation

    # W
    def set_time_average_client_system(self):
        if self.s > 1:
            # MMS
            numerator = self.lbmda ** self.s
            denominator = math.factorial(self.s - 1) * (self.mu ** (self.s - 1)) * ((self.s * self.mu - self.lbmda)**2)
            p0 = self.get_p0(self.n)
            self.w = (numerator / denominator) * p0 + (1 / self.mu)
        else:
            # MM1
            self.w = self.get_client_quantity_system() / self.lbmda

    def get_time_average_client_system(self):
        return self.w

    # Wq
    def set_time_average_client_queue(self):
        if self.s > 1:
            # MMS
            numerator = self.lbmda ** self.s
            denominator = math.factorial(self.s - 1) * (self.mu ** (self.s - 1)) * ((self.s * self.mu - self.lbmda)**2)
            p0 = self.get_p0(self.nq)
            self.wq = (numerator / denominator) * p0
        else:
            # MM1
            self.wq = self.get_client_quantity_queue() / self.lbmda

    def get_time_average_client_queue(self):
        return self.wq

    # ws
    def set_time_average_service_system(self):
        self.ws = 1 / self.mu

    def get_time_average_service_system(self):
        return self.ws

    def display(self):
        table = PrettyTable()
        table.field_names = ["L", "Lq", "W", "Wq"]
        table.add_row([self.len, self.lq, self.w, self.wq])
        print table
        # print "L: " + str(self.len) + "Lq: " + str(self.lq) + "W: " + str(self.w) + "Wq: " + str(self.wq) + "\n"

    def update(self):
        # Lq
        self.set_client_quantity_queue()
        # L
        self.set_client_quantity_system()
        # p
        self.set_intensity_traffic()
        # Wq
        self.set_time_average_client_queue()
        # W
        self.set_time_average_client_system()
        # ws
        self.set_time_average_service_system()

