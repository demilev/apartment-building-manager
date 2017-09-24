class Expenditure:
    def __init__(self, cost, reason, year, month):
        self.cost = cost
        self.reason = reason
        self.year = year
        self.month = month

    def toString(self):
        return "Разход на стойност {}лв, с обосновка : {}, за {}.{}".format(self.cost, self.reason, self.month, self.year)

    def toPersistenceFormat(self):
        return "{}^{}^{}^{}\n".format(self.cost, self.reason, self.year, self.month)
