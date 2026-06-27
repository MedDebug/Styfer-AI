import json 

def create_memory_file():
    user_details = {}
    username_validation = False
    age_validation = False
    
    while username_validation == False:                               #USERNAME
        username = input("Please enter your username: ")
        if username.strip() == "":
            print("Please enter a valid username")
        else:
            user_details["username"] = username
            username_validation = True
    
    while age_validation == False:      
        try:                                                             #AGE
            age = int(input("Please enter your age: "))
            user_details["age"] = age
            age_validation = True
        except ValueError:
            print("Please enter a valid age")
            continue
       
    current_project = input("Please enter the current project you are working on: ")                                    #CURRENT PROJECT
    current_project = current_project.lower()
    current_project = current_project.replace(" ", "_")
    user_details["current_project"] = current_project
      
    with open("memory.json","w") as user_data:
        json.dump(user_details,user_data)
        
    return user_details
        
def load_memory():                                                  #LOADS LAST SAVED MEMORY
    with open("memory.json", "r") as starter_data:
        memory = json.load(starter_data)
    for key,value in memory.items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")
        
    return memory
        
def delete_memory():                                                   #DELETES SOME ENTRY
    removal = input("What would you like to delete: ").lower()
    removal = removal.replace(" ","_")
    if removal == "username":
        print("This field cannot be deleted please choose another field")
    elif removal == "age":
        print("This field cannot be deleted please choose another field")
    else:
        with open("memory.json", "r") as read_data:
            memory = json.load(read_data)
            
        if removal in memory:
            del memory[removal]    
            with open("memory.json", "w") as deleted_data:
                json.dump(memory,deleted_data)
            print("Memory entry deleted successfully")
        else:
            print("That entry does not exist, please create one")
            
def change_user_details():                                                          #CHANGES SOME ENTRY
    change = input("What would you like to change: ").lower()
    change = change.replace(" ","_")
    with open("memory.json", "r") as read_data:
        memory = json.load(read_data)
        
    if change in memory:
        new = input("Please enter new data: ")
        memory[change] = new
        with open("memory.json", "w") as deleted_data:
            json.dump(memory,deleted_data)
        print("Memory entry changed successfully")
    else:
        print("That entry does not exist, please create one")       
     
def add_memory_entry():
    key = input("What is the name of the field: ")
    key = key.lower()
    key = key.replace(" ", "_")
    value = input("What is the value of this field: ")
    with open("memory.json", "r") as new_data:
        memory = json.load(new_data)
    if key in memory.keys():
        print("This key already exists, please pick option 4 to change the value")
    else:
        memory[key] = value
        with open("memory.json", "w") as new_data:
            json.dump(memory,new_data)
        print("Memory entry added successfully")

