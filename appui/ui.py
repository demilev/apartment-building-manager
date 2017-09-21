import easygui as gui


def fileChoiceMenu():
    msg = "Здравейте, г-н домоуправител.\nЗа да стартирате приложението, моля изберете db файл."
    filename = ""
    if gui.ccbox(msg, "Household Manager", ["Избери файл", "Изход"]):
        filename = gui.fileopenbox("Изберете db файл-а", "Избор на файл")
    return filename


def mainMenu():
    options = ['домакинства', 'разходи', 'таски', 'отчет']
    choice = gui.buttonbox('Household Manager главно меню.', 'Начало', options)
    return choice


def householdsMenu():
    options = ['добави домакинство', 'премахни домакинство', 'покажи всички']
    choice = gui.buttonbox('Изберете опция.', 'Домакинства', options)
    return choice


def addHouseholdMenu():
    fieldValues = gui.multenterbox(
        "Въведете данните на домакинството", "Добавяне на домакинство", ["име", "апартамент"])
    return fieldValues


def removeHouseholdMenu():
    fieldValues = gui.multenterbox(
        "Въведете данните на домакинството", "Премахване на домакинство", ["име", "апартамент"])
    return fieldValues


def showAllHouseholdsMenu(householdsInfo):
    gui.msgbox(householdsInfo, "Всички домакинства")


def expendituresMenu():
    options = ['добави разход', 'покажи разходи']
    choice = gui.buttonbox('Изберете опция.', 'Разходи', options)
    return choice


def addExpenditureMenu():
    fieldValues = gui.multenterbox("Въведете информация за разхода", "Добавяне на разход", [
                                   "сума", "обосновка", "година", "месец"])
    return fieldValues


def showExpendituresMenu():
    year = gui.enterbox("Въведете година: ", "Разходи")
    return year


def printExpendituresMenu(expendituresInfo, year):
    gui.msgbox(expendituresInfo, "Разходи за {}г".format(year))


def taxesMenu():
    options = ['плати такса', 'покажи неплатени такси']
    choice = gui.buttonbox('Изберете опция.', 'Такси', options)
    return choice


def reportMenu():
    year = gui.enterbox("Въведете година: ", "Отчет")
    return year


def printReportMenu(report, year):
    gui.msgbox(report, "Отчет за {}г".format(year))


# if mainMenu() == 'таски':
#   print(taxesMenu())
printReportMenu("блабла", reportMenu())
# print(removeHouseholdMenu())
