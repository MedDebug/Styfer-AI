import os
condition = True
os.chdir(r"C:\Users\Medhansh\Desktop")
while condition == True:
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

    answer = int(input("What would you like to do? (Type a number from the above): "))
        
    if answer == 1:
        for folder in os.listdir():
            if os.path.isdir(folder):
                print(folder)
    elif answer == 2:
        for file in os.listdir():
            if os.path.isfile(file):
                print(file)
    elif answer == 3:
        folder_input = input("Please enter the name of folder: ")
        if os.path.isdir(folder_input):
            print("Folder already exists")
        else:
            os.mkdir(folder_input)
            print("Folder created")
    elif answer == 4:
        file_input = input("Please enter name of file you wish to delete: ")
        if os.path.isfile(file_input):
            os.remove(file_input)
            print("File deleted")
        else:
            print("This file does not exist")
    elif answer == 5:
        directory_input = input("Please enter the full directory you want to change: ")
        if os.path.isdir(directory_input):
            os.chdir(directory_input)
            print("Directory changed")
        else:
            print("This directory does not exist")
    elif answer == 6:
        print("Folder or file?")
        rename_input = input().lower()
        if rename_input == "folder":
            old_name = input("Please enter old name: ")
            new_name = input("Please enter new name: ")
            if os.path.isdir(old_name):
                os.rename(old_name,new_name)
                print("Directory renamed successfully")
            else:
                print("This folder does not exist")
        elif rename_input == "file":
            old_name = input("Please enter old name: ")
            new_name = input("Please enter new name: ")
            if os.path.isfile(old_name):
                os.rename(old_name,new_name)
                print("File renamed successfully")
            else:
                print("This file does not exist")
        else:
            print("Please enter either folder or file")
    elif answer == 7:
        print("Thank you for using the Styfer File Manager!")
        condition = False
    
    

    
