class Stadistic(object):
    def __init__(self, lbmda, mu, s, n, nq):
        self.lbmda = lbmda
        self.mu = mu
        self.s = s
        self.n = n
        self.nq = nq
        self.p = 0
        self.l = 0
        self.lq = 0

    def set_intensity_trafic(self):
        self.p = self.lbmda / self.mu

    def get_intensity_trafic(self):
        return self.p

    def set_client_quantity_system(self):
        self.l = self.expectation(self.n)

    def get_client_quantity_system(self):
        return self.l

    def set_client_quantity_queue(self):
        self.lq = self.expectation(self.nq)

    def get_client_quantity_queue(self):
        return self.lq

    def expectation(self, n):
        expectation_summation = 0
        for x in range(0, n):
            expectation_summation += self.lbmda * self.probability_n(x)
        return expectation_summation

    def probability_n(self, n):
        p0 = 1 / (1 + self.cn(n))
        cn = self.p ** n
        pn = cn * p0
        return pn


    def cn(self, n):
        cn_summation = 0
        for x in range(0, n):
            cn_summation += self.p**x
        return cn_summation