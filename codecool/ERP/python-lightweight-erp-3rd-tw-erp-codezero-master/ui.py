# This function needs to print outputs like this:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
#
# @table: list of lists - the table to print out
# @title_list: list of strings - the head of the table


def print_table(table, title_list):
    title_list_len = []
    for item in range(len(title_list)):
        title_list_len.append(len(title_list[item]))
        if len(max([line[item] for line in table], key=lambda x: len(x))) > title_list_len[item]:
            title_list_len[item] = len(max([line[item] for line in table], key=lambda x: len(x)))
    print('/' + '-' * (sum_title(title_list_len) + len(title_list) * 7 - 2) + '\\')
    for line in range(len(table)):
        if line == 0:
            for title in range(len(title_list)):
                print('|' + title_list[title].center(title_list_len[title] + 5) + "|", end="")
            print('\n', end="")
            print('-' * (sum_title(title_list_len) + len(title_list) * 7))
        else:
            for title in range(len(title_list)):
                print('|' + table[line][title].center(title_list_len[title] + 5) + "|", end="")
            print('\n', end="")
            if line != (len(table) - 1):
                print('-' * (sum_title(title_list_len) + len(title_list) * 7))
    print('\\' + '-' * (sum_title(title_list_len) + len(title_list) * 7 - 2) + '/')

# This function needs to print result of the special functions
#
# @result: string or list or dictionary - result of the special function
# @label: string - label of the result


def sum_title(array):
    sumof = 0
    for item in array:
        sumof += item
    return sumof


def print_result(result, label):
    print('\n' + label)
    if type(result) == type(dict()):
        for keys, values in result.items():
            print(keys + ": " + str(values))
        print('\n', end="")
    elif type(result) == float:
        print(result)
        print('\n', end="")
    elif type(result) == type(str()):
        print(result)
        print('\n', end="")
    elif type(result) == type(list()):
        for item in result:
            print(item)
        print('\n', end="")


# This function needs to generate outputs like this:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# @title: string - title of the menu
# @list_options: list of strings - the options in the menu
# @exit_message: string - the last option with (0) (example: "Back to main menu")
def print_menu(title, list_options, exit_message):
    print(title)
    print(list_options)
    print(exit_message)

# This function gets a list of inputs from the user by the terminal
#
# @list_labels: list of strings - the labels of the inputs
# @title: string - title of the "input section"
# @inputs: list of string - list of the received values from the user


def get_inputs(list_labels, title, types):
    inputs = input(list_labels)
    if types == 'int':
        if inputs.isdigit() == False:
            print_error_message('Invalid type')
            inputs = get_inputs(list_labels, title, types)
    return inputs

# This function needs to print an error message. (example: Error: @message)
#
# @message: string - the error message


def print_error_message(message):
    print(message)
