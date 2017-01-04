# Do not modify this file
# run the program (the ERP software) by this file from the terminal from thd root directory of this project


import sys
import os
import ui  # User Interface
from importlib.machinery import SourceFileLoader
main_path = os.path.dirname(os.path.abspath(__file__))
# Store module
print(main_path)
store = SourceFileLoader("store", main_path + "/store/store.py").load_module()
# Human Resources module
hr = SourceFileLoader("hr", main_path + "/hr/hr.py").load_module()
# Tool manager module
tool_manager = SourceFileLoader("tool_manager", main_path + "/tool_manager/tool_manager.py").load_module()
# Accounting module
accounting = SourceFileLoader("accounting", main_path + "/accounting/accounting.py").load_module()
# Selling module
selling = SourceFileLoader("selling", main_path + "/selling/selling.py").load_module()
# Customer Relationship Management (CRM) module
crm = SourceFileLoader("crm", main_path + "/crm/crm.py").load_module()


def choose():
    inputs = ui.get_inputs("Please enter a number: ", "Main Menu:", 'str')
    option = inputs[0]
    if option == "1":
        store.start_module()
    elif option == "2":
        hr.start_module()
    elif option == "3":
        tool_manager.start_module()
    elif option == "4":
        accounting.start_module()
    elif option == "5":
        selling.start_module()
    elif option == "6":
        crm.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = """
(1) Store manager
(2) Human resources manager
(3) Tool manager
(4) Accounting manager
(5) Selling manager
(6) Customer Relationship Management (CRM)"""

    ui.print_menu("\n***MAIN MENU***", options, "(0) Exit program\n")


def main():
    while True:
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(err)


if __name__ == '__main__':
    main()
