import os
def search_file():
    search = input("Do you want to search for a file or a folder? : ").lower()
    found = False
    if search == "file":
        file_name = input("Please enter the name of the file: ")
        for root,dirs,files in os.walk("C:\\Users\\Medhansh\\Desktop"):
            if file_name in files:
                print("File found successfully")
                print("File location: ", os.path.join(root,file_name))
                found = True
                break
        if found == False:
            print("File not found")
    elif search == "folder":
        folder_name = input("Please enter the name of the folder: ")
        for root,dirs,files in os.walk("C:\\Users\\Medhansh\\Desktop"):
            if folder_name in dirs:
                print("Directory found successfully")
                print("File location: ", os.path.join(root,folder_name))
                found = True
                break
        if found == False:
            print("Directory not found")
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

