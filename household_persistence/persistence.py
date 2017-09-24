from household_manager.household import Household
from household_manager.manager import HouseholdManager
from household_manager.expenditure import Expenditure


def loadManager(fileName):
    with open(fileName) as file:
        householdsInfo = [x.strip('\n') for x in file.readlines()]
    manager = HouseholdManager(int(householdsInfo[0]))
    for line in householdsInfo[1:]:
        householdInfo = line.split('-')
        household = Household(householdInfo[0], householdInfo[1])
        for payment in householdInfo[2:]:
            paymentInfo = payment.split(':')
            monthPayments = paymentInfo[1].split(',')
            month = 1
            for monthPayment in monthPayments:
                household.makePayment(
                    int(paymentInfo[0]), month, int(monthPayment))
                month += 1
        manager.addHousehold(household)
    return manager


def saveHouseholds(householdManager, fileName):
    file = open(fileName, 'w')
    file.write(str(householdManager.balance) + '\n')
    households = list(householdManager.households.values())
    for household in households:
        file.write(household.toOutputFormat() + '\n')
    file.close()


def loadExpenditures(householdManager, fileName):
    with open(fileName) as file:
        expendituresInfo = [x.strip('\n') for x in file.readlines()]
    for line in expendituresInfo:
        expenditureInfo = line.split('^')
        expenditure = Expenditure(
            expenditureInfo[0], expenditureInfo[1], expenditureInfo[2], expenditureInfo[3])
        householdManager.addExpenditure(expenditure)


def saveExpenditures(householdManager, fileName):
    file = open(fileName, 'w')
    for expenditure in householdManager.expenditures:
        file.write(expenditure.toPersistenceFormat())
