# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this module by a module menu like the main menu
# user need to go back to the main menu from here
# we need to reach the default and the special functions of this module from the module menu
#

def choose():
    inputs = ui.get_inputs("\nPlease enter a number: ", "", 'int')
    option = inputs[0][0]
    global acc_table
    if option == "1":
        show_table(acc_table)
    elif option == "2":
        acc_table = add(acc_table)
    elif option == "3":
        remove(acc_table)
    elif option == "4":
        acc_tabel = update(acc_table)
    elif option == "5":
        which_year_max(acc_table)
    elif option == "6":
        year=ui.get_inputs('Year: ','Type','str')
        avg_amount(acc_table,int(year))
    elif option == "0":
        return option
    elif int(option) > 6:
        ui.print_error_message('There is no such option')
    else:
        raise KeyError("There is no such option.")
    return option

def start_module():
    global acc_table
    acc_table = data_manager.get_table_from_file('accounting/items.csv')
    menu = """
(1) Show Accounting table
(2) Add to table
(3) Remove from table
(4) Update
(5) Get highest profit
(6) Get average profit"""
    ui.print_menu('\n***ACCOUNTING MENU***', menu, '(0) Back to Main menu')
    while choose() != '0':
        ui.print_menu('\n***ACCOUNTING MENU***', menu, '(0) Back to Main menu')
    data_manager.write_table_to_file('accounting/accounting.txt', acc_table)


# print the default table of records from the file
#
# @table: list of lists


def show_table(table):
    title_list = ["ID", "Month ", "Day ", "Year ", "Type ", "Amount "]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
# @table: list of lists
def add(table):
    word_list = ["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "]
    type_list = ["str", "str", "str", "str", "int"]
    new_item = [common.generate_random(table)]
    for item in range(len(word_list)):
        new_item.append(ui.get_inputs(word_list[item], "", type_list[item]))
    table.append(new_item)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_=''):
    word_list = 'Enter ID of the item you want to remove: '
    word_type = 'str'
    show_table(table)
    id_ = ui.get_inputs(word_list, "", word_type)
    if id_ not in [item[0] for item in table]:
        ui.print_error_message('There is no item with this ID')
        remove(table, '')
    else:
        for line in table:
            if id_ == line[0]:
                return table.remove(line)


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_=''):
    show_table(table)
    id_ = ui.get_inputs("Enter ID of the item you want to update: ", '', 'str')
    for line in range(len(table)):
        if table[line][0] == id_:
            word_list = ["Month: ", "Day: ", "Year: ", "Type: ", "Amount: "]
            word_type = ["str", "str", "str", "str", "int"]
            for item in range(len(word_list)):
                table[line][item + 1] = ui.get_inputs(word_list[item], '', word_type[item])
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    years=[]
    for item in table:
        if item[3] not in years:
            years.append(item[3])
    highest=[0,0]
    for year in years:
        sum_profits = 0
        for item in range(len(table)):
            if table[item][3] == year:
                if table[item][4] == "in":
                    sum_profits += int(table[item][5])
                else:
                    sum_profits -= int(table[item][5])
        if highest[0]<sum_profits:
            highest[0]=sum_profits
            highest[1]=year
    ui.print_result(highest[1],'Which year has the highest profit? ')
    return int(highest[1])


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year=0):
    sum_profits = 0
    count=0
    for item in range(len(table)):
        if int(table[item][3]) == year:
            count+=1
            if table[item][4] == "in":
                sum_profits += int(table[item][5])
            elif table[item][4] == "out":
                sum_profits -= int(table[item][5])
    avg = sum_profits / count
    ui.print_result(avg,'What is the average (per item) profit in a given year?')
    return avg
