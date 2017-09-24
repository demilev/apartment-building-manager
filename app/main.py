from appui.ui import *
from household_manager.manager import HouseholdManager
from household_persistence.persistence import *


def householdsCycle(manager, fileDB):
    householdsMenuChoice = householdsMenu()
    if householdsMenuChoice == 'добави домакинство':
        householdInfo = addHouseholdMenu()
        household = Household(householdInfo[0], householdInfo[1])
        manager.addHousehold(household)
        saveHouseholds(manager, fileDB)
    elif householdsMenuChoice == 'премахни домакинство':
        household = removeHouseholdMenu(manager.getHouseholdsInChooseFormat())
        manager.removeHousehold(household.split(',')[1])
        saveHouseholds(manager, fileDB)
    elif householdsMenuChoice == 'покажи всички':
        showAllHouseholdsMenu(manager.getHouseholdsInPrintFormat())


def expendituresCycle(manager, fileDB):
    a = ''


def taxesCycle(manager, fileDB):
    a = ""


def reportCycle(manager, fileDB):
    a = ""


menus = {'домакинства': householdsCycle,
         'разходи': expendituresCycle,
         'такси': taxesCycle,
         'отчет': reportCycle}


def startApp():
    fileDB = fileChoiceMenu()
    manager = loadHouseholds(fileDB)
    return (manager, fileDB)


def mainAppCycle(manager, fileDB):
    mainMenuChoice = mainMenu()
    while mainMenuChoice and mainMenuChoice != 'изход':
        menus[mainMenuChoice](manager, fileDB)
        mainMenuChoice = mainMenu()
    exitApp(manager, fileDB)


def exitApp(manager, fileDB):
    saveHouseholds(manager, fileDB)


manager, fileDB = startApp()
mainAppCycle(manager, fileDB)
