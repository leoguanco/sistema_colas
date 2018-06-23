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
            self.len = self.get_expectation(self.n)
        else:
            self.len = self.get_expectation(self.n)

    def get_client_quantity_system(self):
        return self.len

    # LQ
    def set_client_quantity_queue(self):
        if self.s > 1:
            self.lq = self.get_expectation(self.nq)
        else:
            self.lq = self.get_expectation(self.nq)

    def get_client_quantity_queue(self):
        return self.lq

    # E
    def get_expectation(self, n):
        expectation_summation = 0
        for x in range(0, n):
            expectation_summation += self.lbmda * self.probability_n(x)
        return expectation_summation

    # Pn
    def probability_n(self, n):
        p0 = 1 / (1 + self.cn(n))
        cn = self.get_intensity_traffic ** n
        pn = cn * p0
        return pn

    # Cn
    def cn(self, n):
        cn_summation = 0
        for x in range(0, n):
            cn_summation += self.get_intensity_traffic()**x
        return cn_summation

    # W
    def set_time_average_client_system(self):
        if self.s > 1:
            self.w = self.get_client_quantity_system() / self.lbmda
        else:
            self.w = self.get_client_quantity_system() / self.lbmda

    def get_time_average_client_system(self):
        return self.w

    # Wq
    def set_time_average_client_queue(self):
        if self.s > 1:
            self.wq = self.get_client_quantity_queue() / self.lbmda
        else:
            self.wq = self.get_client_quantity_queue() / self.lbmda

    def get_time_average_client_queue(self):
        return self.wq

    # ws
    def set_time_average_service_system(self):
        self.ws = 1 / self.mu

    def get_time_average_service_system(self):
        return self.ws
