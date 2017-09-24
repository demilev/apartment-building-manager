from appui.ui import *
from household_manager.expenditure import Expenditure
from household_persistence.persistence import *
import sys


def householdsCycle(manager, householdsFileDB, expendituresFileDB):
    householdsMenuChoice = householdsMenu()
    if householdsMenuChoice == 'добави домакинство':
        householdInfo = addHouseholdMenu()
        if householdInfo and householdInfo[0] and householdInfo[1]:
            household = Household(householdInfo[0], householdInfo[1])
            manager.addHousehold(household)
            saveHouseholds(manager, householdsFileDB)
    elif householdsMenuChoice == 'премахни домакинство':
        household = removeHouseholdMenu(manager.getHouseholdsInChooseFormat())
        if household:
            manager.removeHousehold(household.split(',')[1])
            saveHouseholds(manager, householdsFileDB)
    elif householdsMenuChoice == 'покажи всички':
        showAllHouseholdsMenu(manager.getHouseholdsInPrintFormat())


def expendituresCycle(manager, householdsFileDB, expendituresFileDB):
    expendituresMenuChoice = expendituresMenu()
    if expendituresMenuChoice == 'добави разход':
        expenditureInfo = addExpenditureMenu()
        if expenditureInfo and expenditureInfo[0] and expenditureInfo[1] and expenditureInfo[2] and expenditureInfo[3]:
            manager.payExpenditure(Expenditure(
                expenditureInfo[0], expenditureInfo[1], expenditureInfo[2], expenditureInfo[3]))
            saveExpenditures(manager, expendituresFileDB)
    elif expendituresMenuChoice == 'покажи разходи':
        year = showExpendituresMenu()
        if year:
            expenditures = manager.getExpendituresForYear(year)
            outputFormat = "\n".join([e.toString() for e in expenditures])
            printExpendituresMenu(outputFormat, year)


def taxesCycle(manager, householdsFileDB, expendituresFileDB):
    taxesMenuChoice = taxesMenu()
    if taxesMenuChoice == 'плати такса':
        household = chooseHouseholdToPayMenu(
            manager.getHouseholdsInChooseFormat())
        if household:
            taxInfo = payHouseholdTaxMeny(household)
            if taxInfo and taxInfo[0] and taxInfo[1]:
                manager.payTaxes(household.split(
                    ',')[1], taxInfo[0], taxInfo[1])
                saveHouseholds(manager, householdsFileDB)
    elif taxesMenuChoice == 'покажи неплатени такси':
        option = unpaidTaxesMenu()
        if option == 'на домакинство':
            household = chooseHouseholdToShowMenu(
                manager.getHouseholdsInChooseFormat())
            if household:
                unpaidTaxes = manager.getUnpaidTaxesForHousehold(
                    household.split(',')[1])
                unpaidTaxesInfo = ', '.join(unpaidTaxes)
                showUnpaidTaxesForHouseholdMenu(
                    household, unpaidTaxesInfo)
        elif option == 'за година':
            year = chooseYearForUnpaidTaxesMenu()
            if year:
                unpaidTaxes = manager.getUnpaidTaxesForYear(year)
                unpaidTaxesInfo = ""
                for household, unpaid in unpaidTaxes.items():
                    unpaidTaxesInfo += "{}: {}\n".format(
                        household, ', '.join(unpaid))
                showUnpaidTaxesForYearMenu(
                    year, unpaidTaxesInfo)


def reportCycle(manager, householdsFileDB, expendituresFileDB):
    reportMenuChoice = reportMenu()
    if reportMenuChoice == 'баланс':
        balanceMenu(manager.balance)
    elif reportMenuChoice == 'отчет за година':
        year = reportYearMenu()
        if year:
            printReportMenu(manager.getReportForYear(year), year)


cycles = {'домакинства': householdsCycle,
          'разходи': expendituresCycle,
          'такси': taxesCycle,
          'отчет': reportCycle}


def startApp(dbfiles):
    householdsFileDB, expendituresFileDB = readDbFiles(dbfiles) 
    manager = loadManager(householdsFileDB)
    loadExpenditures(manager, expendituresFileDB)
    return (manager, householdsFileDB, expendituresFileDB)

def readDbFiles(dbfiles):
    with open(dbfiles) as f:
        files = [x.strip('\n') for x in f.readlines()]
    return files[0], files[1]

def mainAppCycle(manager, householdsFileDB, expendituresFileDB):
    mainMenuChoice = mainMenu()
    while mainMenuChoice and mainMenuChoice != 'изход':
        cycles[mainMenuChoice](manager, householdsFileDB, expendituresFileDB)
        mainMenuChoice = mainMenu()
    exitApp(manager, householdsFileDB, expendituresFileDB)


def exitApp(manager, householdsFileDB, expendituresFileDB):
    saveHouseholds(manager, householdsFileDB)
    saveExpenditures(manager, expendituresFileDB)


def main(dbfiles):
    manager, householdsFileDB, expendituresFileDB = startApp(dbfiles)
    mainAppCycle(manager, householdsFileDB, expendituresFileDB)
