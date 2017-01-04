# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


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
    inputs = ui.get_inputs("\nPlease enter a number: ", "", "")
    option = inputs[0]
    global store_table
    if option == "1":
        show_table(tool_table)
    elif option == "2":
        add(tool_table)
    elif option == "3":
        remove(tool_table, "")
    elif option == "4":
        update(tool_table, "")
    elif option == "5":
        get_available_tools(tool_table)
    elif option == "6":
        get_average_durability_by_manufacturers(tool_table)
    elif option == "0":
        return option
    elif int(option) > 6:
        ui.print_error_message('There is no such option')
    else:
        raise KeyError("There is no such option.")
    return option


def start_module():
    global tool_table
    tool_table = data_manager.get_table_from_file("tool_manager/tools.csv")
    menu = """ 
(1) Show Tool Manager table
(2) Add to table
(3) Remove from table
(4) Update
(5) Availability by tool
(6) Get average durability by manufacturer"""
    ui.print_menu('\n***TOOL MANAGER MENU***', menu, '(0) Back to Main menu')
    while choose() != '0':
        ui.print_menu('\n***TOOL MANAGER MENU***', menu, '(0) Back to Main menu')
    data_manager.write_table_to_file('tool_manager/tool_manager.txt', tool_table)


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ["ID", "Name", "Manufacturer", "PurchaseDate", "Durability"]
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    word_list = ["Name: ", "Manufacturer: ", "Purchase date: ", "Durability: "]
    type_list = ["str", "str", "int", "int"]
    new_item = [common.generate_random(table)]
    for item in range(len(word_list)):
        new_item.append(ui.get_inputs(
            word_list[item], "Enter ID of the tool you want to remove: ", type_list[item]))
    table.append(new_item)
    show_table(table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_=""):
    word_list = "Enter ID of the tool you want to remove: "
    word_type = "str"
    show_table(table)
    id_ = ui.get_inputs(word_list, "", word_type)
    if id_ not in [item[0] for item in table]:
        ui.print_error_message("There is no tool with his ID")
        remove(table, "")
    else:
        for line in table:
            if id_ == line[0]:
                table.remove(line)
    show_table(table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
#
# @table: list of lists
# @id_: string
def update(table, id_=""):
    show_table(table)
    id_ = ui.get_inputs("Enter ID of the tool you want to update: ", "", "str")
    for line in range(len(table)):
        if table[line][0] == id_:
            word_list = ["Name: ", "Manufacturer: ", "PurchaseDate: ", "Durability: "]
            word_type = ["str", "str", "int", "int"]
            for item in range(len(word_list)):
                table[line][item + 1] = ui.get_inputs(word_list[item], "Type in the new values", word_type[item])
    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
#
# @table: list of lists
def get_available_tools(table):
    available = []
    for line in table:
        if int(line[3]) + int(line[4]) > 2016:
            available.append(line)
    for line in available:
        line[3] = int(line[3])
        line[4] = int(line[4])
    ui.print_result(available, "List of available tools: ")
    return available

# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
#
# @table: list of lists


def get_average_durability_by_manufacturers(table):
    avg_durability = {}
    for line in table:
        if line[2] in avg_durability:
            avg_durability[line[2]].append(int(line[4]))
        else:
            avg_durability[line[2]] = [int(line[4])]
    for key in avg_durability:
        avg_durability[key] = sum_list(avg_durability[key]) / len(avg_durability[key])
    ui.print_result(avg_durability, "Average durability by manufacturer")
    return avg_durability


def sum_list(a_list):
    summ = 0
    for n in a_list:
        summ += n
    return summ
