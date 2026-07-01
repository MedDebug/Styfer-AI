import json 
from voice_hub import ask,say,speak,get_float, get_int

def create_memory_file():
    user_details = {}
    username_validation = False
    age_validation = False
    
    while username_validation == False:                               #USERNAME
        username = ask("Please enter your username: ")
        if username.strip() == "":
            say("Please enter a valid username")
        else:
            user_details["username"] = username
            username_validation = True
    
    while age_validation == False:      
        age = get_int("Please enter your age: ")
        user_details["age"] = age
        age_validation = True
       
    current_project = ask("Please enter the current project you are working on: ")                                    #CURRENT PROJECT
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
        say(f"{key.replace('_', ' ').capitalize()}: {value}")
        
    return memory
        
def delete_memory():                                                   #DELETES SOME ENTRY
    removal = ask("What would you like to delete: ").lower()
    removal = removal.replace(" ","_")
    if removal == "username":
        say("This field cannot be deleted please choose another field")
    elif removal == "age":
        say("This field cannot be deleted please choose another field")
    else:
        with open("memory.json", "r") as read_data:
            memory = json.load(read_data)
            
        if removal in memory:
            del memory[removal]    
            with open("memory.json", "w") as deleted_data:
                json.dump(memory,deleted_data)
            say("Memory entry deleted successfully")
        else:
            say("That entry does not exist, please create one")
            
def change_user_details():                                                          #CHANGES SOME ENTRY
    change = ask("What would you like to change: ").lower()
    change = change.replace(" ","_")
    with open("memory.json", "r") as read_data:
        memory = json.load(read_data)
        
    if change in memory:
        new = ask("Please enter new data: ")
        memory[change] = new
        with open("memory.json", "w") as deleted_data:
            json.dump(memory,deleted_data)
        say("Memory entry changed successfully")
    else:
        say("That entry does not exist, please create one")       
     
def add_memory_entry():
    key = ask("What is the name of the field: ")
    key = key.lower()
    key = key.replace(" ", "_")
    value = ask("What is the value of this field: ")
    with open("memory.json", "r") as new_data:
        memory = json.load(new_data)
    if key in memory.keys():
        say("This key already exists, please pick option 4 to change the value")
    else:
        memory[key] = value
        with open("memory.json", "w") as new_data:
            json.dump(memory,new_data)
        say("Memory entry added successfully")

