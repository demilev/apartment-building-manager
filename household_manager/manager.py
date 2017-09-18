from household_manager.household import Household 
from household_manager.expenditure import Expenditure

class HouseholdManager:

	def __init__(self, startingBalance):
		self.households = dict()
		self.balance = startingBalance
		self.expenditures = list()

	def addHousehold(self, household):
		self.households[household.name] = household

	def addExpenditure(self, expenditure):
		self.expenditures.append(expenditure)
	
	def payExpenditure(self, expenditure):
		self.expenditures.append(expenditure)
		self.balance -= expenditure.cost

	def payTax(self, householdName, year, month, money):
		self.households[householdName].makePayment(year, month, money)
		self.balance += money

