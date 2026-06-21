import os

os.chdir(r"C:\Users\Medhansh\Desktop")
def list_folders():
    for folder in os.listdir():
        if os.path.isdir(folder):
            print(folder)
            
def list_files():
    for file in os.listdir():
        if os.path.isfile(file):
            print(file)
                
def create_folder():
    folder_input = input("Please enter the name of folder: ")
    if os.path.isdir(folder_input):
        print("Folder already exists")
    else:
        os.mkdir(folder_input)
        print("Folder created")
            
def delete_file():
    file_input = input("Please enter name of file you wish to delete: ")
    try:
        os.remove(file_input)
        print("File deleted successfully")
    except IsADirectoryError:
        print("Folder entered, expected file")
    except FileNotFoundError:
        print("This file does not exist")
            
def change_directory():
    directory_input = input("Please enter the full directory you want to change: ")
    if os.path.isdir(directory_input):
        os.chdir(directory_input)
        print("Directory successfully changed")
    else:
        print("Please enter a valid existing directory")
        
def rename_file_or_directory():
    rename_input = input("Folder or file? : ").lower()
    if rename_input == "folder":
        old_name_folder = input("Please enter old name: ")
        new_name_folder = input("Please enter new name: ")
        if os.path.isdir(old_name_folder):
            os.rename(old_name_folder,new_name_folder)
            print("Directory renamed successfully")
        else:
            print("This folder does not exist")
    elif rename_input == "file":
        old_name_file = input("Please enter old name: ")
        new_name_file = input("Please enter new name: ")
        if os.path.isfile(old_name_file):
            os.rename(old_name_file,new_name_file)
            print("File renamed successfully")
        else:
            print("This file does not exist")
    else:
        print("Please enter either folder or file")
                
def show_menu():      
    print("-------------------------------------------")
    print("------------Styfer File Manager------------")
    print("-------------------------------------------")
    print()
    print("Current Working Directory: ")
    print(os.getcwd())
    print()
    print("1 - List all folders")
    print("2 - List all files")
    print("3 - Create a folder")
    print("4 - Delete a file")
    print("5 - Change directory")
    print("6 - Rename a file/directory")
    print("7 - Exit")
    

while True:
    show_menu()

    try:
        answer = int(input())
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
        print("Thank you for using the Styfer File Manager!")
        break
    else:
        print("Please enter a number between 1 and 7 (inclusive) ")
    
    

    
