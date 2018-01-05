class HouseholdManager:

    def __init__(self, startingBalance):
        self.households = dict()
        self.balance = startingBalance
        self.expenditures = list()

    def addHousehold(self, household):
        self.households[household.number] = household

    def removeHousehold(self, householdNumber):
        del self.households[householdNumber]

    def addExpenditure(self, expenditure):
        self.expenditures.append(expenditure)

    def payExpenditure(self, expenditure):
        self.expenditures.append(expenditure)
        self.balance -= int(expenditure.cost)

    def payTax(self, householdNumber, year, month, money):
        self.households[householdNumber].makePayment(year, month, money)
        self.balance += int(money)

    def payTaxes(self, householdNumber, months, money):
        lastPayedYear = self.households[householdNumber].getLastPayedYear()
        lastPayedMonth = self.households[householdNumber].getLastPayedMonth()
        for i in range(1, int(months) + 1):
            month = i + lastPayedMonth
            if month > 12:
                yearOffset = month // 12
                month %= 12
                self.payTax(householdNumber, lastPayedYear +
                            yearOffset, month, money)
            else:
                self.payTax(householdNumber, lastPayedYear, month, money)

    def getHouseholdsInChooseFormat(self):
        return [h.toString() for h in self.households.values()]

    def getHouseholdsInPrintFormat(self):
        return "\n".join(self.getHouseholdsInChooseFormat())

    def getExpendituresForYear(self, year):
        return [e for e in self.expenditures if e.year == year]

    def getReportForYear(self, year):
        result = " " * 29 + "Отчет за {}г".format(year) + " " * 29 + "\n" * 2
        result += "домакинствo     1    2    3    4    5    6    7    8    9    10   11   12\n"
        result += "-" * 73 + "\n"
        for household in self.households.values():
            result += household.getReportMessageForYear(year)
        return result

    def getUnpaidTaxesForHousehold(self, householdNumber):
        household = self.households[householdNumber]
        return household.getUnpaidTaxes()

    def getUnpaidTaxesForYear(self, year):
        result = {}
        for household in self.households.values():
            result[household.toString()] = household.getUnpaidTaxesForYear(year)
        return result
