from memory_system.memory_menu import show_memory_menu
from memory_system.memory_manager import create_memory_file, delete_memory, change_user_details, load_memory, add_memory_entry
import os
def run_memory_manager():
    while True:
        if os.path.isfile("memory.json"):
            show_memory_menu()
        else:
            create_memory_file()
            show_memory_menu()
        try:
            answer = int(input("Please enter a number from 1 to 5 (inclusive): "))
        except ValueError:
            print("Please enter a number from 1 to 5 (inclusive)")
            continue
        if answer == 1:
            load_memory()
        elif answer == 2:
            add_memory_entry()
        elif answer == 3:
            delete_memory()
        elif answer == 4:
            change_user_details()
        elif answer == 5:
            print("Thank you for using Styfer AI Memory Manager")
            break
        else:
            print("Please enter a number from 1 to 5 (inclusive)")
        