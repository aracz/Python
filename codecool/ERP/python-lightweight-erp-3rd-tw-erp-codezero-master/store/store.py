# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


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
    inputs = ui.get_inputs("\nPlease enter a number: ", "", "int")
    option = inputs[0]
    global store_table
    if option == "1":
        show_table(store_table)
    elif option == "2":
        store_table = add(store_table)
    elif option == "3":
        store_table = remove(store_table, "")
    elif option == "4":
        store_table = update(store_table)
    elif option == "5":
        get_counts_by_manufacturers(store_table)
    elif option == "6":
        get_average_by_manufacturer(store_table, "Ensemble Studios")
    elif option == "0":
        return option
    elif int(option) > 6:
        ui.print_error_message('There is no such option')
    else:
        raise KeyError("There is no such option.")
    return option


def start_module():
    global store_table
    store_table = data_manager.get_table_from_file("store/games.csv")
    menu = """
(1) Show Store table
(2) Add to table
(3) Remove from table
(4) Update
(5) Count by manufacturer
(6) Get average by manufacturer"""
    ui.print_menu('\n***STORE MENU***', menu, '(0) Back to Main menu')
    while choose() != '0':
        ui.print_menu('\n***STORE MENU***', menu, '(0) Back to Main menu')
    data_manager.write_table_to_file('store/storeout.txt', store_table)


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ['ID', 'Title', 'Manufacturer', 'Price', 'Stock']
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    word_list = ["Title ", "Manufacturer ", "Price ", "Count "]
    type_list = ["str", "str", "int", "int"]
    new_item = [common.generate_random(table)]
    for item in range(len(word_list)):
        new_item.append(ui.get_inputs(word_list[item], "Add new items", type_list[item]))
    table.append(new_item)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_):
    word_list = "Enter ID of the game you want to remove: "
    type_list = "str"
    show_table(table)
    id_ = ui.get_inputs(word_list, "", type_list)
    if id_ not in [item[0] for item in table]:
        ui.print_error_message('There is no item with this ID')
        table = remove(table, '')
    else:
        for each in table:
            if id_ == each[0]:
                table.remove(each)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_=""):
    word_list1 = "Enter ID of the game you want to update: "
    word_list2 = ["New Title: ", "New Manufacturer: ", "New Price: ", "New Stock Count: "]
    type_list = ["str", "str", "int", "int"]
    show_table(table)
    id_ = ui.get_inputs(word_list1, '', 'str')
    for each in range(len(table)):
        if table[each][0] == id_:
            for item in range(len(word_list2)):
                table[each][item + 1] = ui.get_inputs(word_list2[item], 'Type in the new values', type_list[item])
    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    games = {}
    for each in table:
        if each[2] in games.keys():
            games[each[2]] += 1
        else:
            games[each[2]] = 1
    ui.print_result(games, "How many different kinds of games are available of each manufacturer?")
    return games

# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number


def get_average_by_manufacturer(table, manufacturer):
    games = {}
    for each in table:
        if each[2] in games:
            games[each[2]].append(int(each[4]))
        else:
            games[each[2]] = [int(each[4])]
    for key in games:
        if key == manufacturer:
            avg = sum_list(games[key]) / len(games[key])
    ui.print_result(avg, 'What is the average amount of games in stock of Ensemble Studios?')
    return avg


def sum_list(a_list):  # list is passed to the function
    summ = 0
    for n in a_list:
        summ += n
    return summ
