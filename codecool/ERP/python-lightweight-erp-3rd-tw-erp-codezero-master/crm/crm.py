# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
    if option == "1":
        show_table(crm_table)
    elif option == "2":
        add(crm_table)
    elif option == "3":
        remove(crm_table, "")
    elif option == "4":
        update(crm_table, "")
    elif option == "5":
        get_longest_name_id(crm_table)
    elif option == "6":
        get_subscribed_emails(crm_table)
    elif option == "0":
        return option
    elif int(option) > 6:
        ui.print_error_message('There is no such option')
    else:
        raise KeyError("There is no such option.")
    return option


def start_module():
    global crm_table
    crm_table = data_manager.get_table_from_file("crm/customers.csv")
    menu = """
(1) Show CRM table
(2) Add to table
(3) Remove from table
(4) Update 
(5) Get ID of longest name
(6) Get subscribed emails"""
    ui.print_menu('\n***CRM MENU***', menu, '(0) Back to Main menu')
    while choose() != '0':
        ui.print_menu('\n***CRM MENU***', menu, '(0) Back to Main menu')
    data_manager.write_table_to_file('crm/crm.txt', crm_table)


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    word_list = ["ID ", "Name ", "Email ", "Subscribed(1:Y,0:N) "]
    ui.print_table(crm_table, word_list)

# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists


def add(table):
    word_list = ["Name: ", "Email: ", "Subscribed(1:Y,0:N): "]
    type_list = ["str", "str", "int"]
    new_item = [common.generate_random(table)]
    for item in range(len(word_list)):
        new_item.append(ui.get_inputs(word_list[item], "", type_list[item]))
    table.append(new_item)
    show_table(table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_=""):
    word_list = "Enter ID of the user you want to remove: "
    word_type = "str"
    show_table(table)
    id_ = ui.get_inputs(word_list, "", word_type)
    if id_ not in [item[0] for item in table]:
        ui.print_error_message("There is no person with his ID")
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
    id_ = ui.get_inputs("Enter ID of the person you want to update: ", "", "str")
    for line in range(len(table)):
        if table[line][0] == id_:
            word_list = ["Name: ", "Email: ", "Subscribed(1:Y,0:N): "]
            word_type = ["str", "str", "int"]
            for item in range(len(word_list)):
                table[line][item + 1] = ui.get_inputs(word_list[item], "", word_type[item])
    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of descending alphabetical order
def get_longest_name_id(table):
    longest_name_numb = len(max(table, key=lambda x: len(x[1]))[1])
    longest = []
    for item in table:
        if len(item[1]) == longest_name_numb:
            longest.append([item[0], item[1]])
    first = min(longest, key=lambda x: x[1])[0]
    ui.print_result(first, "What is the ID of the user with the longest name?")
    return first

# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")


def get_subscribed_emails(table):
    sub = []
    for line in table:
        if line[3] == "1":
            sub.extend([line[2] + ";" + line[1]])
    ui.print_result(sub, "Which customers have subscribed to the newsletter?")
    return sub
