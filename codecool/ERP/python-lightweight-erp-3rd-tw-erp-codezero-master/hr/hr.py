# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


# importing everything you need
import os
import sys
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
    global hr_table
    if option == "1":
        show_table(hr_table)
    elif option == "2":
        hr_table = add(hr_table)
    elif option == "3":
        hr_table = remove(hr_table)
    elif option == "4":
        hr_tabel = update(hr_table)
    elif option == "5":
        get_oldest_person(hr_table)
    elif option == "6":
        get_persons_closest_to_average(hr_table)
    elif option == "0":
        return option
    elif int(option) > 6:
        ui.print_error_message('There is no such option')
    else:
        raise KeyError("There is no such option.")
    return option


def start_module():
    global hr_table
    hr_table = data_manager.get_table_from_file('hr/persons.csv')
    menu = """
(1) Show HR table
(2) Add to table
(3) Remove from table
(4) Update
(5) Get oldest person's name
(6) Closest person to average"""
    ui.print_menu('\n***HR MENU***', menu, '(0) Back to Main menu')
    while choose() != '0':
        ui.print_menu('\n***HR MENU***', menu, '(0) Back to Main menu')
    data_manager.write_table_to_file('hr/hrout.txt', hr_table)


# print the default table of records from the file
#
# @table: list of lists


def show_table(table):
    title_list = ['ID', 'Name', 'Year']
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    word_list = ["Name: ", "Birth year: "]
    type_list = ["str", "int"]
    new_item = [common.generate_random(table)]
    for item in range(len(word_list)):
        new_item.append(ui.get_inputs(word_list[item], "Add new person", type_list[item]))
    table.append(new_item)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_=''):
    word_list = 'Enter ID of the person you want to remove: '
    word_type = 'str'
    show_table(table)
    id_ = ui.get_inputs(word_list, "", word_type)
    if id_ not in [item[0] for item in table]:
        ui.print_error_message('There is no person with this ID')
        table = remove(table, '')
    else:
        for line in table:
            if id_ == line[0]:
                table.remove(line)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_=''):
    show_table(table)
    id_ = ui.get_inputs("Enter ID of the person you want to update: ", '', 'str')
    for line in range(len(table)):
        if table[line][0] == id_:
            word_list = ['Name: ', 'Year: ']
            word_type = ['str', 'int']
            for item in range(len(word_list)):
                table[line][item + 1] = ui.get_inputs(word_list[item], 'type in the new values', word_type[item])
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    oldest = []
    old_int = min(table, key=lambda x: int(x[2]))[2]
    for item in table:
        if item[2] == old_int:
            oldest.append(item[1])
    ui.print_result(oldest, 'Who is the oldest person?')
    return oldest


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)


def get_persons_closest_to_average(table):
    sum_years = sum_year([item[2] for item in table])
    avg = sum_years / len(table)
    min_value = min([abs(int(item[2]), avg) for item in table])
    averagest = [item[1] for item in table if abs(int(item[2]), avg) == min_value]
    ui.print_result(averagest, 'Who is the closest to the average age?')
    return averagest


def abs(int1, int2):
    if int1 - int2 < 0:
        return int2 - int1
    else:
        return int1 - int2


def sum_year(array):
    summary = 0
    for item in array:
        summary += int(item)
    return summary
