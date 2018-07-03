from prettytable import PrettyTable
import math


class Statistics(object):

    def __init__(self, lbmda, mu, s, n, nq):
        self.lbmda = lbmda
        if s > 1:
            if 1 <= n <= s:
                self.mu = n * mu
                print "if"
            elif n >= s + 1:
                print "elif"
                self.mu = s * mu
            else:
                self.mu = mu
        else:
            self.mu = mu
        self.s = s
        self.n = n
        self.nq = nq
        self.p = float(lbmda) / self.mu
        self.len = 0
        self.lq = 0
        self.w = 0
        self.wq = 0
        self.ws = 0

    # p
    def set_intensity_traffic(self):
        self.p = float(self.lbmda) / self.mu

    def get_intensity_traffic(self):
        return self.p

    # L
    def set_client_quantity_system(self):
        if self.s > 1:
            # MMS
            numerator = self.lbmda ** (self.s + 1)
            denominator = math.factorial(self.s - 1) * (self.mu ** (self.s - 1)) * ((self.s * self.mu - self.lbmda)**2)
            p0 = self.get_p0(self.n)
            self.len = (float(numerator) / denominator) * p0 + (float(self.lbmda) / self.mu)
        else:
            # MM1
            self.len = self.get_expectation(self.n)

    def get_client_quantity_system(self):
        return self.len

    # LQ
    def set_client_quantity_queue(self):
        if self.s > 1:
            # MMS
            if self.n <= self.s:
                self.lq = 0
            else:
                for n in range(self.s, self.n):
                    self.lq += (n - self.s) * self.probability_n(n)
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
        p0 = 0
        cn = 0
        for x in range(1, n + 1):
            cn += self.cn(n)
        p0 = 1.0 / (1 + cn)
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
            if n > 0:
                # MMS
                if 1 <= n <= self.s:
                    cn_summation += (1.0 / math.factorial(n)) * ((float(self.lbmda) / self.mu) ** n)
                elif n >= self.s + 1:
                    cn_summation += (1.0 / (math.factorial(self.s) * (self.s ** (n - self.s)))) * (
                                (float(self.lbmda) / self.mu) ** n)
        else:
            cn_summation = self.get_intensity_traffic() ** n
        return cn_summation

    # W
    def set_time_average_client_system(self):
        if self.s > 1:
            # MMS
            numerator = self.lbmda ** self.s
            denominator = math.factorial(self.s - 1) * (self.mu ** (self.s - 1)) * ((self.s * self.mu - self.lbmda)**2)
            p0 = self.get_p0(self.n)
            self.w = (float(numerator) / denominator) * p0 + (1.0 / self.mu)
        else:
            # MM1
            self.w = float(self.get_client_quantity_system()) / self.lbmda

    def get_time_average_client_system(self):
        return self.w

    # Wq
    def set_time_average_client_queue(self):
        if self.s > 1:
            # MMS
            numerator = self.lbmda ** self.s
            denominator = math.factorial(self.s - 1) * (self.mu ** (self.s - 1)) * ((self.s * self.mu - self.lbmda)**2)
            p0 = self.get_p0(self.nq)
            self.wq = (float(numerator) / denominator) * p0
        else:
            # MM1
            self.wq = float(self.get_client_quantity_queue()) / self.lbmda

    def get_time_average_client_queue(self):
        return self.wq

    # ws
    def set_time_average_service_system(self):
        self.ws = 1.0 / self.mu

    def get_time_average_service_system(self):
        return self.ws

    def display(self):
        table = PrettyTable()
        table.field_names = ["L", "Lq", "W", "Wq"]
        table.add_row([self.len, self.lq, self.w, self.wq])
        print table
        # print "L: " + str(self.len) + "Lq: " + str(self.lq) + "W: " + str(self.w) + "Wq: " + str(self.wq) + "\n"

    def update(self, lbmda, mu, s, n, nq):
        # update var
        self.lbmda = lbmda
        if s > 1:
            if 1 <= n <= s:
                self.mu = n * mu
            elif n >= s + 1:
                self.mu = s * mu
        else:
            self.mu = mu
        self.s = s
        self.n = n
        self.nq = nq

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

