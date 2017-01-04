# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made

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
    global sell_table
    if option == "1":
        show_table(sell_table)
    elif option == "2":
        sell_table = add(sell_table)
    elif option == "3":
        sell_table = remove(sell_table, "")
    elif option == "4":
        sell_table = update(sell_table)
    elif option == "5":
        get_lowest_price_item_id(sell_table)
    elif option == "6":
        get_items_sold_between(sell_table, 2, 12, 2016, 7, 6, 2016)
    elif option == "0":
        return option
    elif int(option) > 6:
        ui.print_error_message('There is no such option')
    else:
        raise KeyError("There is no such option.")
    return option


def start_module():
    global sell_table
    sell_table = data_manager.get_table_from_file("selling/sellings.csv")
    menu = """
(1) Show Selling table
(2) Add to table
(3) Remove from table
(4) Update
(5) Get lowest price
(6) Get items sold between given dates"""
    ui.print_menu('\n***SELLING MENU***', menu, '(0) Back to Main menu')
    while choose() != '0':
        ui.print_menu('\n***SELLING MENU***', menu, '(0) Back to Main menu')
    data_manager.write_table_to_file('selling/sellout.txt', sell_table)


# print the default table of records from the file
#
# @table: list of lists
def show_table(table):
    title_list = ['ID', 'Title', 'Price', 'Month', 'Day', 'Year']
    ui.print_table(table, title_list)


# Ask a new record as an input from the user than add it to @table, than return @table
#
# @table: list of lists
def add(table):
    word_list = ["Title: ", "Price: ", "Month: ", "Day: ", "Year: "]
    type_list = ["str", "int", "int", "int", "int"]
    new_item = [common.generate_random(table)]
    for item in range(len(word_list)):
        new_item.append(ui.get_inputs(word_list[item], "", type_list[item]))
    table.append(new_item)
    return table


# Remove the record having the id @id_ from the @list, than return @table
#
# @table: list of lists
# @id_: string
def remove(table, id_=""):
    word_list = "Enter ID of the game you want to remove: "
    type_list = "str"
    show_table(table)
    id_ = ui.get_inputs(word_list, "", type_list)
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
def update(table, id_=""):
    word_list1 = "Enter ID of the game you want to update: "
    word_list2 = ["New Title: ", "New Price: ", "New Month: ", "New Day: ", "New Year: "]
    type_list = ["str", "int", "int", "int", "int"]
    show_table(table)
    id_ = ui.get_inputs(word_list1, '', 'str')
    for line in range(len(table)):
        if table[line][0] == id_:
            for item in range(len(word_list2)):
                table[line][item + 1] = ui.get_inputs(word_list2[item], '', type_list[item])
    return table


# special functions:
# ------------------

# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order


def get_lowest_price_item_id(table):
    lowest = 10000
    lowest_ID = ["2"]
    for line in table:
        if int(line[2]) < lowest:
            lowest = int(line[2])
            lowest_ID.pop()
            lowest_ID.append(line[0])
        if int(line[2]) == lowest and line[0] != lowest_ID[0]:
            lowest_ID.append(line[0])
    result = max(lowest_ID)
    ui.print_result(result, 'What is the id of the item that sold for the lowest price ?')
    return result


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    filtered = []
    from_date = int(year_from) * 365 + int(month_from) * 31 + int(day_from)
    to_date = int(year_to) * 365 + int(month_to) * 31 + int(day_to)

    for line in table:
        date_sum = int(line[5]) * 365 + int(line[3]) * 31 + int(line[4])
        if date_sum > from_date and date_sum < to_date:
            filtered.append(line)

    for line in filtered:
        line[2] = int(line[2])
        line[3] = int(line[3])
        line[4] = int(line[4])
        line[5] = int(line[5])

    ui.print_result(filtered, 'Which items are sold between 9.12.2015,- 12.30.2015')
    return filtered
