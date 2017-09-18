from household_manager.household import Household 
from household_manager.manager import HouseholdManager

def loadHouseholds(fileName):
	with open(fileName) as file:
		householdsInfo = [x.strip('\n') for x in file.readlines()]
	manager = HouseholdManager(int(householdsInfo[0]))
	for line in householdsInfo[1:]:
		householdInfo = line.split('-')
		household = Household(householdInfo[0],householdInfo[1])
		for payment in householdInfo[2:]:
			paymentInfo = payment.split(':')
			monthPayments = paymentInfo[1].split(',')
			month = 1
			for monthPayment in monthPayments:
				household.makePayment(int(paymentInfo[0]), month, int(monthPayment))
				month+=1
		manager.addHousehold(household)
	return manager

def saveHouseholds(fileName, householdManager):
	file = open(fileName,'w')
	file.write(str(householdManager.balance) + '\n')
	households = list(householdManager.households.values())
	for household in households[:-1]:
		file.write(household.toOutputFormat() + '\n')
	file.write(households[-1].toOutputFormat())
	file.close()

m = loadHouseholds('households.txt')
saveHouseholds('output.txt',m)
