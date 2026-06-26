from file_menu import file_menu
import os
from file_manager import list_folders, list_files, create_folder, delete_file, change_directory, rename_file_or_directory, search_file
def run_file_manager():
    os.chdir(r"C:\Users\Medhansh\Desktop")
    file_menu()
    while True:
        try:
            print()
            answer = int(input("Please enter a number: "))
        except ValueError:
            print("Please enter a valid number between 1 and 7 (inclusive) ")
            continue
        if answer == 1:
            list_folders()
        elif answer == 2:
            list_files()
        elif answer == 3:
            create_folder()
        elif answer == 4:
            delete_file()
        elif answer == 5:
            change_directory()
        elif answer == 6:
            rename_file_or_directory()
        elif answer == 7:
            search_file()
        elif answer == 8:
            print("Thank you for using the Styfer File Manager!")
            break
        else:
            print("Please enter a number between 1 and 7 (inclusive) ")

#MAIN LOOP FOR FILE MANAGER