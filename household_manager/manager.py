import apartment_building.py

class HouseholdManager:

	def __init__(self, startingBalance):
		self.apartments = dict()
		self.balance = startingBalance
		self.expenditures = list()

	def addHousehold(self, household):
		self.apartments[household.name] = household

	def addExpenditure(self, expenditure):
		self.expenditures.append(expenditure)
		self.balance -= expenditure.cost

	def payTax(self, householdName, year, month, money):
		self.apartments[householdName].makePayment(year, month, money)
		self.balance += money

