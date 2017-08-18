from datetime import datetime
class Household:
	def __init__(self, name):
		self.name = name
		self.monthly_payments = dict()
		self.__initializeEmptyYear(datetime.now().year)

	def makePayment(self, year, month, money):
		if not year in self.monthly_payments:
			self.__initializeEmptyYear(year)
		self.monthly_payments[year][month] += money

	def printPayments(self, year):
		for key,value in self.monthly_payments[year].items():
			print(key)
			print(value)
	def __initializeEmptyYear(self, year):
		self.monthly_payments[year] = {}
		for month in range(1,13):
			self.monthly_payments[year][month] = 0
h = Household('milevi')
h.makePayment(2017,1,10)
h.makePayment(2017,3,10)
h.makePayment(2017,5,10)
h.makePayment(2017,6,10)
h.makePayment(2016,12,10)
h.printPayments(2016)

