from datetime import datetime
class Household:
	def __init__(self, name, number):
		self.name = name
		self.number = number
		self.monthly_payments = dict()
		self.__initializeEmptyYear(datetime.now().year)

	def makePayment(self, year, month, money):
		if not year in self.monthly_payments:
			self.__initializeEmptyYear(year)
		self.monthly_payments[year][month] += money

	def printPayments(self, year):
		print("Payments of household: {}, appnumber: {}".format(self.name, self.number))
		for key,value in self.monthly_payments[year].items():
			print(key)
			print(value)
		print("---------------------------------------------------------------")
	
	def toOutputFormat(self):
		result = self.name + "-" + str(self.number) + "-"
		for year in self.monthly_payments:
			result += (str(year) + ":")
			for month in self.monthly_payments[year]:
				result += (str(self.monthly_payments[year][month]) + ",")
			result = result[:-1]
			result += "-"	
		return result[:-1]

	def __initializeEmptyYear(self, year):
		self.monthly_payments[year] = {}
		for month in range(1,13):
			self.monthly_payments[year][month] = 0

h = Household('milevi',17)
h.makePayment(2017,1,10)
h.makePayment(2017,3,10)
h.makePayment(2017,5,10)
h.makePayment(2017,6,10)
h.makePayment(2016,12,10)
#h.printPayments(2016)

