import easygui as gui


def householdsFileChoiceMenu():
    msg = "Здравейте, г-н домоуправител.\nЗа да стартирате приложението, моля изберете db файл за домакинствата."
    filename = ""
    if gui.ccbox(msg, "Household Manager", ["Избери файл", "Изход"]):
        filename = gui.fileopenbox("Изберете db файл-а", "Избор на файл")
    return filename


def expendituresFileChoiceMenu():
    msg = "А сега, моля изберете db файл за разходите."
    filename = ""
    if gui.ccbox(msg, "Household Manager", ["Избери файл", "Изход"]):
        filename = gui.fileopenbox("Изберете db файл-а", "Избор на файл")
    return filename


def mainMenu():
    options = ['домакинства', 'разходи', 'такси', 'отчет', 'изход']
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


def removeHouseholdMenu(choices):
    choice = gui.choicebox("Изберете домакинството",
                           "Премахване на домакинство", choices)
    return choice


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


def chooseHouseholdToPayMenu(choices):
    choice = gui.choicebox("Изберете домакинството",
                           "Плащане на такса", choices)
    return choice


def payHouseholdTaxMeny(household):
    fieldValues = gui.multenterbox("Плащане на таксата на домакинство: {}".format(
        household), "Плащане на такса", ["Брой месеци", "Сума на месец"])
    return fieldValues


def unpaidTaxesMenu():
    options = ['на домакинство', 'за година']
    return gui.buttonbox('Неплатени такси: ', 'Неплатени такси', options)


def chooseHouseholdToShowMenu(choices):
    return gui.choicebox("Изберете домакинството",
                         "Неплатени такси", choices)


def showUnpaidTaxesForHouseholdMenu(household, unpaidTaxes):
    gui.msgbox("Неплатени такси на домакинство {}:\n{}".format(
        household, unpaidTaxes))


def chooseYearForUnpaidTaxesMenu():
    return gui.enterbox("Въведете година: ", "Неплатени такси")


def showUnpaidTaxesForYearMenu(year, unpaidTaxes):
    gui.msgbox("Неплатени такси за {}г:\n{}".format(year, unpaidTaxes))


def reportMenu():
    options = ['баланс', 'отчет за година']
    return gui.buttonbox('Изберете опция', 'Отчет', options)


def reportYearMenu():
    year = gui.enterbox("Въведете година: ", "Отчет")
    return year


def printReportMenu(report, year):
    gui.msgbox(report, "Отчет за {}г".format(year))


def balanceMenu(balance):
    gui.msgbox("Балансът е {}лв".format(balance), "Баланс")
