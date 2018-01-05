from datetime import datetime


class Household:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.monthly_payments = dict()
        self.__initializeEmptyYear(datetime.now().year)

    def makePayment(self, year, month, money):
        if year not in self.monthly_payments:
            self.__initializeEmptyYear(year)
        self.monthly_payments[year][month] += int(money)

    def getLastPayedYear(self):
        return min([int(y) for y in self.monthly_payments.keys() if self.__hasUnpaidMonth(y)])

    def getLastPayedMonth(self):
        lastPayedYear = self.getLastPayedYear()
        for month in range(1, 13):
            if self.monthly_payments[lastPayedYear][month] == 0:
                return month - 1
        return 12

    def getUnpaidTaxes(self):
        result = []
        for year in self.monthly_payments.keys():
            result += self.getUnpaidTaxesForYear(year)
        return result

    def getUnpaidTaxesForYear(self, year):
        result = []
        year = int(year)
        if year in self.monthly_payments:
            for i in range(1, 13):
                if self.monthly_payments[year][i] == 0:
                    result.append("{}.{}".format(i, year))
        return result

    def toString(self):
        return "{},{}".format(self.name, self.number)

    def toOutputFormat(self):
        result = self.name + "-" + str(self.number) + "-"
        for year in self.monthly_payments:
            result += (str(year) + ":")
            for month in self.monthly_payments[year]:
                result += (str(self.monthly_payments[year][month]) + ",")
            result = result[:-1]
            result += "-"
        return result[:-1]

    def getReportMessageForYear(self, year):
        year = int(year)
        household = self.toString()
        payments = ""
        if year in self.monthly_payments:
            for i in range(1, 12):
                payments += self.__format(self.monthly_payments[year][i])
            payments += str(self.monthly_payments[year][12])
            return household + " " * (16 - len(household)) + payments + "\n"
        return household + "\n"

    def __hasUnpaidMonth(self, year):
        for month in range(1, 13):
            if self.monthly_payments[year][month] == 0:
                return True
        return False

    def __initializeEmptyYear(self, year):
        self.monthly_payments[year] = {}
        for month in range(1, 13):
            self.monthly_payments[year][month] = 0

    def __format(self, payment):
        if len(str(payment)) == 1:
            return "{}    ".format(str(payment))
        return "{}   ".format(str(payment))
